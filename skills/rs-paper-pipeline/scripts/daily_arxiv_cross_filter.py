#!/usr/bin/env python3
from __future__ import annotations

"""
从 arXiv 拉取今天+昨天提交的论文，先按遥感关键词 OR 初筛，
再用 LLM 筛选“遥感 x 基础模型/计算机视觉/人工智能交叉”论文，
最后去重（已存在于 GitHub issues 的 arXiv id）并调用现有流程更新/创建 issue。
"""

import re
import json
from datetime import datetime
from pathlib import Path

from clients.arxiv_client import fetch_recent_candidates, has_remote_sensing_signal
from clients.llm_client import call_llm
from paper_processor import process_paper
from pipeline_config import get_repo, load_config
from services.filter_assets import load_ai_signal_patterns, render_filter_prompt
from services.digest_builder import extract_author, extract_institution, is_invalid_digest_field
from services.issue_index import ensure_index, lookup_issue, update_index_from_issue, save_index

CONFIG = load_config()
AI_MATCH_PATTERNS = load_ai_signal_patterns()


def has_ai_signal(text: str) -> bool:
    return any(pattern.search(text) for pattern in AI_MATCH_PATTERNS)


def _parse_llm_ids(raw_output: str) -> set[str] | None:
    """Extract arxiv IDs from LLM output. Returns None on parse failure."""
    code_block = re.search(r"```(?:json)?\s*([\s\S]*?)\s*```", raw_output)
    if code_block:
        json_str = code_block.group(1).strip()
    else:
        match = re.search(r"\[[\s\S]*\]", raw_output)
        json_str = match.group(0) if match else raw_output
    arr = json.loads(json_str)
    return {x.strip() for x in arr if isinstance(x, str)}


def _match_id(cid: str, keep_set: set[str]) -> bool:
    if cid in keep_set:
        return True
    cid_base = cid.replace("v1", "").replace("v2", "").rstrip("v")
    for k in keep_set:
        k_base = k.replace("v1", "").replace("v2", "").rstrip("v")
        if cid_base == k_base:
            return True
    return False


def llm_cross_filter(candidates):
    if not candidates:
        return []

    payload = []
    for i, c in enumerate(candidates, 1):
        payload.append(f"[{i}] id={c['arxiv_id']} | title={c['title']} | abstract={c['abstract'][:500]}")

    prompt = render_filter_prompt(payload)

    keep_ids = None
    for attempt in range(2):
        out = call_llm(prompt, max_tokens=1200, timeout=180).strip()
        try:
            keep_ids = _parse_llm_ids(out)
            break
        except Exception as exc:
            print(f"  [LLM 解析] 第 {attempt + 1} 次失败: {exc}")
            if attempt == 0:
                print(f"  [LLM 解析] 原始输出: {out[:200]}")
                print("  [LLM 解析] 重试中...")

    if keep_ids is not None:
        selected = [c for c in candidates if _match_id(c["arxiv_id"], keep_ids)]
        result = [c for c in selected if has_remote_sensing_signal(f"{c['title']}\n{c['abstract']}")]
        print(f"  [LLM 解析] 成功，命中 {len(result)} 篇")
        return result

    # 两次都失败，降级到关键词交叉筛选
    print("  [LLM 解析] 两次均失败，降级为关键词交叉筛选")
    out_items = []
    for c in candidates:
        text = f"{c['title']}\n{c['abstract']}"
        if has_remote_sensing_signal(text) and has_ai_signal(text):
            out_items.append(c)
    print(f"  [关键词降级] 命中 {len(out_items)} 篇")
    return out_items


def compact_item(item: dict[str, str]) -> dict[str, str]:
    return {
        "arxiv_id": item["arxiv_id"],
        "published": item["published"],
        "title": item["title"],
    }


def issue_has_valid_metadata(issue) -> bool:
    body = issue.body or ""
    authors = extract_author(body)
    institution = extract_institution(body)
    return (
        not is_invalid_digest_field(authors)
        and "et al." not in authors
        and not is_invalid_digest_field(institution)
    )


def load_existing_issue_map(repo, index: dict[str, dict], arxiv_ids: list[str]) -> dict[str, object]:
    issue_map: dict[str, object] = {}
    for arxiv_id in arxiv_ids:
        issue = lookup_issue(repo, index, arxiv_id)
        if issue is not None:
            issue_map[arxiv_id] = issue
    return issue_map


def main(dry_run=False, days_back=2, stats_out: str | None = None, target_date: str | None = None):
    if not CONFIG.github_token:
        raise RuntimeError("Missing required environment variable: GITHUB_TOKEN")
    if not CONFIG.bailian_api_key:
        raise RuntimeError("Missing required environment variable: BAILIAN_API_KEY")

    repo = get_repo(CONFIG)
    index = ensure_index(repo)

    if target_date:
        print(f"[1/5] 拉取指定日期 {target_date} 候选...")
        cands = fetch_recent_candidates(max_results=180, days_back=days_back, target_date=target_date)
    else:
        print(f"[1/5] 拉取最近 {days_back} 天候选...")
        cands = fetch_recent_candidates(max_results=180, days_back=days_back)
    cand_count = len(cands)
    print(f"  候选数: {cand_count}")

    print("[2/5] LLM 交叉筛选...")
    selected = llm_cross_filter(cands)
    selected_count = len(selected)
    print(f"  入选数: {selected_count}")

    print("[3/5] 读取 issue 去重...")
    selected_arxiv_ids = [x["arxiv_id"] for x in selected]
    existing_issue_map = load_existing_issue_map(repo, index, selected_arxiv_ids)
    todo = []
    keep = []
    refresh = []
    for item in selected:
        issue = existing_issue_map.get(item["arxiv_id"])
        if issue is None:
            todo.append({"candidate": item, "issue_number": None, "reason": "missing"})
            continue
        if issue_has_valid_metadata(issue):
            keep.append(item)
        else:
            refresh.append(item)
            todo.append({"candidate": item, "issue_number": issue.number, "reason": "stale_metadata"})

    existing_count = len(keep)
    refresh_count = len(refresh)
    todo_count = len(todo)
    print(f"  已合格: {existing_count}，待刷新: {refresh_count}，待处理总数: {todo_count}")

    stats = {
        "date": target_date or datetime.now().strftime("%Y%m%d"),
        "candidate_count": cand_count,
        "llm_selected_count": selected_count,
        "existing_count": existing_count,
        "refresh_count": refresh_count,
        "todo_count": todo_count,
        "candidate_arxiv_ids": [x["arxiv_id"] for x in cands],
        "selected_arxiv_ids": [x["arxiv_id"] for x in selected],
        "existing_arxiv_ids": [x["arxiv_id"] for x in keep],
        "refresh_arxiv_ids": [x["arxiv_id"] for x in refresh],
        "todo_arxiv_ids": [x["candidate"]["arxiv_id"] for x in todo],
        "candidate_items": [compact_item(x) for x in cands],
        "selected_items": [compact_item(x) for x in selected],
        "successful_selected_arxiv_ids": [x["arxiv_id"] for x in keep],
        "successful_selected_items": [compact_item(x) for x in keep],
        "failed_arxiv_ids": [],
        "failed_items": [],
        "todo_items": [
            {
                **compact_item(x["candidate"]),
                "issue_number": x["issue_number"],
                "reason": x["reason"],
            }
            for x in todo
        ],
    }
    if stats_out:
        Path(stats_out).parent.mkdir(parents=True, exist_ok=True)
        Path(stats_out).write_text(json.dumps(stats, ensure_ascii=False), encoding="utf-8")

    if dry_run:
        print("[DRY RUN] 列表如下:")
        for x in todo:
            item = x["candidate"]
            print(
                f"  - {item['arxiv_id']} | {item['published']} | issue={x['issue_number'] or '-'} | "
                f"reason={x['reason']} | {item['title'][:90]}"
            )
        return

    print("[4/5] 提交 issue（不重复）...")
    for task in todo:
        aid = task["candidate"]["arxiv_id"]
        issue_number = task["issue_number"]
        print(f"  -> 处理 {aid} | issue={issue_number or '-'} | reason={task['reason']}")
        result = process_paper(aid, issue_number=issue_number)
        if result is not None and hasattr(result, "number"):
            update_index_from_issue(index, aid, result)
        if result is None:
            stats["failed_arxiv_ids"].append(aid)
            stats["failed_items"].append(
                {
                    **compact_item(task["candidate"]),
                    "issue_number": issue_number,
                    "reason": task["reason"],
                }
            )
        else:
            stats["successful_selected_arxiv_ids"].append(aid)
            stats["successful_selected_items"].append(compact_item(task["candidate"]))

        if stats_out:
            Path(stats_out).write_text(json.dumps(stats, ensure_ascii=False), encoding="utf-8")

    save_index(repo, index)
    print("[5/5] 完成")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--days", type=int, default=2, help="抓取最近 N 天的论文（默认2天）")
    parser.add_argument("--date", dest="date", help="抓取指定日期（YYYYMMDD）")
    parser.add_argument("--stats-out", dest="stats_out", help="输出统计 JSON 文件路径")
    args = parser.parse_args()

    main(dry_run=args.dry_run, days_back=args.days, stats_out=args.stats_out, target_date=args.date)
