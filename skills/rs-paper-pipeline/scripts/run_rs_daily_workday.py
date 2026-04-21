#!/usr/bin/env python3
from __future__ import annotations

"""
工作日 09:05 自动执行：
1) 抓取并筛选“当天”遥感xAI论文，生成/更新单篇 issue
2) 生成当天日报 issue
3) 推送日报到 Feishu 私聊
"""

import os
import json
import time
import fcntl
import re
import subprocess
from datetime import datetime, timedelta

from clients.github_ops import daily_report_file_exists, get_today_digest_issue
from clients.notify_client import has_available_notify_channel, send_dingtalk_markdown, send_feishu_message
from pipeline_config import build_runtime_env, get_repo, load_config

CONFIG = load_config()
LOCK_FILE = CONFIG.memory_dir / "rs_daily_workday.lock"
STATE_DIR = CONFIG.pipeline_state_dir


def _env_with_proxy() -> dict:
    return build_runtime_env()


def check_github_connectivity() -> bool:
    cmd = [
        "curl", "-s", "-o", "/dev/null", "-w", "%{http_code}",
        f"https://api.github.com/repos/{CONFIG.github_repo}",
    ]
    try:
        out = subprocess.check_output(cmd, cwd=CONFIG.root_dir, env=_env_with_proxy(), timeout=20).decode().strip()
        return out == "200"
    except Exception:
        return False


def run(cmd: list[str], retries: int = 4):
    print("$", " ".join(cmd))
    env = _env_with_proxy()
    backoff = [2, 5, 10, 20]
    for i in range(retries):
        try:
            subprocess.run(cmd, cwd=CONFIG.root_dir, check=True, env=env)
            return
        except subprocess.CalledProcessError:
            if i == retries - 1:
                raise
            wait_s = backoff[min(i, len(backoff) - 1)]
            print(f"[retry] attempt={i+1}/{retries} failed, sleep={wait_s}s")
            time.sleep(wait_s)


def _get_repo():
    return get_repo(CONFIG)


def _write_state(date_str: str, step: str, status: str, extra: dict | None = None):
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    p = STATE_DIR / f"{date_str}.json"
    state = {
        "date": date_str,
        "step": step,
        "status": status,
        "updated_at": datetime.now().isoformat(timespec="seconds"),
    }
    if p.exists():
        try:
            old = json.loads(p.read_text(encoding="utf-8"))
            if isinstance(old, dict):
                state = {**old, **state}
        except Exception:
            pass
    if status != "failed":
        state.pop("reason", None)
        state.pop("failed_command", None)
    if extra:
        for key, value in extra.items():
            if value is None:
                state.pop(key, None)
            else:
                state[key] = value
    p.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8")


def _format_exc(exc: Exception) -> str:
    text = str(exc).strip()
    return text or exc.__class__.__name__


def _extract_digest_issue_numbers(body: str) -> list[int]:
    seen: set[int] = set()
    numbers: list[int] = []
    for match in re.finditer(r"github\.com/[^/]+/[^/]+/issues/(\d+)", body or ""):
        number = int(match.group(1))
        if number in seen:
            continue
        seen.add(number)
        numbers.append(number)
    return numbers


def _date_already_completed(date_str: str) -> tuple[bool, str]:
    repo = _get_repo()
    digest_issue = get_today_digest_issue(repo, date_str)
    if digest_issue is None:
        return False, "digest issue missing"

    if not daily_report_file_exists(repo, date_str):
        return False, "daily report file missing"

    linked_issue_numbers = _extract_digest_issue_numbers(digest_issue.body or "")
    if not linked_issue_numbers:
        return False, "digest issue has no linked paper issues"

    return True, f"digest=#{digest_issue.number} papers={len(linked_issue_numbers)}"


def _load_stats(stats_path: str) -> dict:
    try:
        with open(stats_path, "r", encoding="utf-8") as fh:
            data = json.load(fh)
        return data if isinstance(data, dict) else {}
    except Exception:
        return {}


def _short_title(title: str, limit: int = 88) -> str:
    text = " ".join((title or "").split())
    if len(text) <= limit:
        return text
    return text[: limit - 3].rstrip() + "..."


def _short_text(text: str, limit: int = 96) -> str:
    value = " ".join((text or "").split())
    if len(value) <= limit:
        return value
    return value[: limit - 3].rstrip() + "..."


def _clean_digest_title(text: str) -> str:
    value = " ".join((text or "").split())
    return re.sub(r"^\[\d{8}\]\s*", "", value)


def _strip_markdown(text: str) -> str:
    value = (text or "").strip()
    value = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", value)
    value = re.sub(r"`([^`]+)`", r"\1", value)
    value = re.sub(r"\*\*([^*]+)\*\*", r"\1", value)
    value = re.sub(r"\*([^*]+)\*", r"\1", value)
    return " ".join(value.split())


def _split_table_row(row: str) -> list[str]:
    stripped = row.strip().strip("|")
    return [cell.strip() for cell in stripped.split("|")]


def _extract_first_link(text: str) -> str:
    match = re.search(r"\[[^\]]+\]\(([^)]+)\)", text or "")
    return match.group(1).strip() if match else ""


def _extract_markdown_section(body: str, heading: str) -> list[str]:
    pattern = re.compile(
        rf"^##\s+{re.escape(heading)}\s*$([\s\S]*?)(?=^##\s+|\n---\n|\Z)",
        re.MULTILINE,
    )
    match = pattern.search(body or "")
    if not match:
        return []
    section = match.group(1).strip()
    lines: list[str] = []
    for raw_line in section.splitlines():
        line = raw_line.strip()
        if not line or not line.startswith("- "):
            continue
        lines.append(line[2:].strip())
    return lines


def _extract_digest_articles(body: str) -> list[dict[str, str]]:
    pattern = re.compile(
        r"^##\s+🗂\s*今日文章列表\s*$([\s\S]*?)(?=^##\s+|\n---\n|\Z)",
        re.MULTILINE,
    )
    match = pattern.search(body or "")
    if not match:
        return []

    lines = [
        line.strip()
        for line in match.group(1).splitlines()
        if line.strip().startswith("|")
    ]
    if len(lines) < 3:
        return []

    headers = [_strip_markdown(cell) for cell in _split_table_row(lines[0])]
    articles: list[dict[str, str]] = []
    for row in lines[2:]:
        cells = _split_table_row(row)
        if len(cells) < 4:
            continue
        item = {headers[i]: cells[i] if i < len(cells) else "" for i in range(len(headers))}
        title = _strip_markdown(item.get("标题") or item.get("Title") or cells[0])
        summary = _strip_markdown(
            item.get("一句话概括") or item.get("摘要") or item.get("Summary") or cells[-2]
        )
        institution = _strip_markdown(
            item.get("单位") or item.get("机构") or item.get("Institution") or item.get("Affiliation") or ""
        )
        issue_cell = item.get("Issue") or cells[-1]
        issue = _strip_markdown(issue_cell)
        issue_url = _extract_first_link(issue_cell)
        if not title:
            continue
        articles.append(
            {
                "title": title,
                "summary": summary,
                "institution": institution,
                "issue": issue,
                "issue_url": issue_url,
            }
        )
    return articles


def _build_daily_report_urls(date_str: str) -> tuple[str, str]:
    owner, repo = CONFIG.github_repo.split("/", 1)
    markdown_url = f"https://github.com/{CONFIG.github_repo}/blob/main/daily_reports/{date_str[:6]}/{date_str}.md"
    portal_url = f"https://{owner}.github.io/{repo}/"
    return markdown_url, portal_url


def _build_notify_message(date_str: str, stats_path: str, issue) -> tuple[str, str]:
    title = f"遥感AI日报 {date_str}"
    stats = _load_stats(stats_path)
    selected_items = stats.get("selected_items") or []
    selected_count = stats.get("llm_selected_count")
    candidate_count = stats.get("candidate_count")
    included_count = len(selected_items) if selected_items else selected_count
    existing_count = stats.get("existing_count")
    refresh_count = stats.get("refresh_count")
    todo_count = stats.get("todo_count")

    if not issue:
        lines = [
            f"## 🛰️ {title}",
            "",
            f"> 日期：{date_str}",
        ]
        if candidate_count is not None and selected_count is not None:
            lines.append(f"> 候选 **{candidate_count}** ｜ 筛中 **{selected_count}**")
        lines.extend(
            [
                "",
                "## 状态说明",
                "",
                "- 当天日报 issue 尚未生成，可能是未命中论文，或生成流程失败。",
                "- 可优先检查 `daily_digest_llm_upgrade.py` 与 `sync_daily_reports_to_repo.py` 日志。",
            ]
        )
        return title, "\n".join(lines)

    issue_body = issue.body or ""
    highlights = _extract_markdown_section(issue_body, "✨ 今日亮点")
    observations = _extract_markdown_section(issue_body, "🔎 观察")
    articles = _extract_digest_articles(issue_body)
    markdown_url, portal_url = _build_daily_report_urls(date_str)

    lines = [
        f"## 🛰️ {title}",
        "",
        f"> 日期：{date_str}",
        f"> 日报 Issue：[#{issue.number}]({issue.html_url})",
    ]
    if candidate_count is not None and selected_count is not None:
        stats_line = f"> 候选 **{candidate_count}** ｜ 筛中 **{selected_count}** ｜ 纳入 **{included_count}**"
        if existing_count is not None and refresh_count is not None and todo_count is not None:
            stats_line += f" ｜ 已合格 **{existing_count}** ｜ 待刷新 **{refresh_count}** ｜ 待处理 **{todo_count}**"
        lines.append(stats_line)

    lines.extend(
        [
            "",
            "## 🔗 阅读入口",
            "",
            f"- [日报 Issue]({issue.html_url})",
            f"- [日报 Markdown]({markdown_url})",
            f"- [在线阅读]({portal_url})",
        ]
    )

    if highlights:
        lines.extend(["", "## ✨ 今日亮点", ""])
        for item in highlights[:3]:
            lines.append(f"- {item}")

    if articles:
        lines.extend(["", "## 📚 论文速览", ""])
        for idx, article in enumerate(articles[:6], 1):
            title_text = _short_title(_clean_digest_title(article.get("title", "")), 68)
            summary_text = _short_text(article.get("summary") or "暂无一句话概括。", 78)
            institution_text = _short_text(article.get("institution") or "单位信息见日报", 56)
            issue_text = article.get("issue") or "-"
            detail_url = article.get("issue_url") or ""
            title_line = (
                f"**{idx}. [{title_text}]({detail_url})**"
                if detail_url
                else f"**{idx}. {title_text}**"
            )
            lines.extend(
                [
                    title_line,
                    f"> 📝 {summary_text}",
                    f"> 🏫 {institution_text}",
                    f"> {issue_text}",
                    "",
                    "---",
                    "",
                ]
            )
    elif selected_items:
        lines.extend(["", "## 📚 论文速览", ""])
        for idx, item in enumerate(selected_items, 1):
            lines.append(f"- **{idx}. {_short_title(item.get('title', ''), 72)}**")
    if observations:
        lines.extend(["", "## 🔎 观察", ""])
        for item in observations[:2]:
            lines.append(f"- {item}")
    else:
        body = (issue.body or "").strip()
        preview = body[:1200] + ("\n..." if len(body) > 1200 else "")
        lines.extend(["", "## 日报预览", "", preview])

    return title, "\n".join(lines)


def _run_step(date_str: str, step: str, cmd: list[str], ok_extra: dict | None = None, running_extra: dict | None = None):
    _write_state(date_str, step, "running", running_extra)
    try:
        run(cmd)
    except Exception as exc:
        _write_state(
            date_str,
            step,
            "failed",
            {
                "reason": _format_exc(exc),
                "failed_command": " ".join(cmd),
            },
        )
        raise
    _write_state(date_str, step, "ok", ok_extra)


def resolve_target_dates(today: datetime | None = None) -> list[str]:
    now = today or datetime.now()
    weekday = now.weekday()  # Monday=0

    # 默认按北京时间日期回溯抓取：
    # - 周一：回溯到上周五（-3天）
    # - 周二：顺序补跑周六、周日、周一（-3/-2/-1天）
    # - 其他日期：回溯昨日（-1天）
    # 说明：arXiv published 为 UTC 时间，这里用“工作日日报”的业务口径。
    if weekday == 0:
        deltas = [3]
    elif weekday == 1:
        deltas = [3, 2, 1]
    else:
        deltas = [1]
    return [(now - timedelta(days=delta)).strftime("%Y%m%d") for delta in deltas]


def _process_date(date_str: str, notify: bool, force: bool = False):
    if not force:
        already_done, reason = _date_already_completed(date_str)
        if already_done:
            print(f"SKIP {date_str} | {reason}")
            _write_state(
                date_str,
                "done",
                "skipped",
                {
                    "skip_reason": reason,
                    "notify": notify,
                },
            )
            return

    stats_path = f"memory/rs_daily_stats_{date_str}.json"

    _run_step(
        date_str,
        "filter",
        ["python3", "scripts/daily_arxiv_cross_filter.py", "--date", date_str, "--stats-out", stats_path],
        ok_extra={"stats_path": stats_path},
        running_extra={"notify": notify},
    )

    _run_step(
        date_str,
        "digest",
        ["python3", "scripts/daily_digest_llm_upgrade.py", "--date", date_str, "--stats-json", stats_path],
    )

    _write_state(date_str, "sync", "running")
    max_sync_attempts = 3
    try:
        for attempt in range(1, max_sync_attempts + 1):
            run(["python3", "scripts/sync_daily_reports_to_repo.py"])
            if daily_report_file_exists(_get_repo(), date_str):
                break
            if attempt < max_sync_attempts:
                time.sleep(6)
    except Exception as exc:
        _write_state(
            date_str,
            "sync",
            "failed",
            {
                "reason": _format_exc(exc),
                "failed_command": "python3 scripts/sync_daily_reports_to_repo.py",
            },
        )
        raise
    _write_state(date_str, "sync", "ok", {"sync_attempts": attempt, "daily_report_file": daily_report_file_exists(_get_repo(), date_str)})

    if notify:
        sent_channels: list[str] = []
        issue = get_today_digest_issue(_get_repo(), date_str)
        title, text = _build_notify_message(date_str, stats_path, issue)

        _write_state(date_str, "notify", "running")
        try:
            if send_feishu_message(text):
                sent_channels.append("feishu")
            if send_dingtalk_markdown(title, text):
                sent_channels.append("dingtalk")
        except Exception as exc:
            _write_state(
                date_str,
                "notify",
                "failed",
                {"reason": _format_exc(exc), "channels_sent": sent_channels or None},
            )
            raise
        if not sent_channels:
            _write_state(
                date_str,
                "notify",
                "failed",
                {"reason": "No available notify channel (feishu or dingtalk)"},
            )
            raise RuntimeError("通知已启用，但没有可用的飞书或钉钉通道")
        _write_state(date_str, "notify", "ok", {"channels_sent": sent_channels})

    _write_state(date_str, "done", "ok")


def main(target_date: str | None = None, notify: bool | None = None, force: bool = False):
    if not CONFIG.github_token:
        raise RuntimeError("Missing required environment variable: GITHUB_TOKEN")
    if not CONFIG.bailian_api_key:
        raise RuntimeError("Missing required environment variable: BAILIAN_API_KEY")

    if target_date:
        target_dates = [target_date]
    else:
        target_dates = resolve_target_dates()

    # 默认仅“自动定时模式”发送通知；手动回放/追跑默认不通知
    if notify is None:
        notify = (target_date is None)

    LOCK_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(LOCK_FILE, "w", encoding="utf-8") as lf:
        try:
            fcntl.flock(lf.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            raise RuntimeError("另一个 pipeline 正在运行，请稍后重试")

        # 前置网络检查
        if not check_github_connectivity():
            for date_str in target_dates:
                _write_state(
                    date_str,
                    "precheck",
                    "failed",
                    {"reason": "GitHub connectivity check failed"},
                )
            raise RuntimeError("GitHub 连通性检查失败，请切换代理节点后重试")
        for date_str in target_dates:
            _process_date(date_str, notify, force=force)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", dest="date", help="指定日期，格式 YYYYMMDD，默认为今天")
    parser.add_argument("--notify", action="store_true", help="强制发送通知")
    parser.add_argument("--no-notify", action="store_true", help="禁止发送Feishu通知")
    parser.add_argument("--force", action="store_true", help="即使当天已成功也强制重跑")
    args = parser.parse_args()

    notify = None
    if args.notify:
        notify = True
    if args.no_notify:
        notify = False

    if notify and not has_available_notify_channel():
        raise RuntimeError("No available notify channel. Configure DINGTALK_WEBHOOK or FEISHU_TARGET with a working openclaw binary.")

    main(target_date=args.date, notify=notify, force=args.force)
