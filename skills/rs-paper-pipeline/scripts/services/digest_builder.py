#!/usr/bin/env python3
from __future__ import annotations

import json
import re

from clients.llm_client import call_llm
from services.paper_analysis import is_valid_institution_text
from services.report_status import completion_marker


def extract_author(body: str) -> str:
    match = re.search(r"\| \*\*作者\*\* \|([^|]+)\|", body or "")
    return match.group(1).strip() if match else "-"


def extract_institution(body: str) -> str:
    match = re.search(r"\| \*\*(?:单位|机构)\*\* \|([^|]+)\|", body or "")
    return match.group(1).strip() if match else "-"


def is_invalid_digest_field(value: str) -> bool:
    normalized = (value or "").strip()
    return normalized in {"", "-", "待提取", "未知", "Unknown", "N/A"}


def is_invalid_digest_institution(value: str) -> bool:
    return not is_valid_institution_text(value)


def validate_papers_for_digest(papers: list[dict]) -> list[str]:
    errors: list[str] = []
    for paper in papers:
        title = extract_report_title(paper)
        authors = extract_author(paper.get("body") or "")
        institution = extract_institution(paper.get("body") or "")
        if is_invalid_digest_field(authors) or "et al." in authors:
            errors.append(f"{title}: 作者信息不合格")
        if is_invalid_digest_institution(institution):
            errors.append(f"{title}: 单位信息不合格")
    return errors


def extract_report_title(issue: dict) -> str:
    body = issue.get("body") or ""
    match = re.search(r"^#\s*\[(\d{8})\]\s+(.+)$", body, re.MULTILINE)
    if match:
        return f"[{match.group(1)}] {match.group(2).strip()}"
    return issue.get("title") or ""


def extract_paper_date(issue: dict) -> str | None:
    for label in issue.get("labels", []):
        name = label.get("name", "") if isinstance(label, dict) else ""
        if re.fullmatch(r"\d{8}", name):
            return name

    body = issue.get("body") or ""
    body_match = re.search(r"\[(\d{8})\]", body)
    if body_match:
        return body_match.group(1)

    title_match = re.match(r"^\[(\d{8})\]\s+", issue.get("title") or "")
    return title_match.group(1) if title_match else None


def build_digest_with_llm(date: str, papers: list, stats: dict | None = None, failed_items: list[dict] | None = None) -> str:
    items = []
    for i, paper in enumerate(papers, 1):
        labels = [label["name"] for label in paper.get("labels", []) if label["name"] not in [date, "日报"]]
        items.append(
            {
                "idx": i,
                "issue": paper["number"],
                "title": extract_report_title(paper),
                "authors": extract_author(paper.get("body") or ""),
                "institution": extract_institution(paper.get("body") or ""),
                "labels": labels,
                "url": paper["html_url"],
            }
        )

    if not items:
        candidate_count = (stats or {}).get("candidate_count", 0)
        llm_selected_count = (stats or {}).get("llm_selected_count", len(failed_items or []))
        overview_text = (
            f"今日共检索候选论文 {candidate_count} 篇；"
            f"关键词+LLM 智能匹配遥感交叉论文 {llm_selected_count} 篇；"
            "最终纳入日报 0 篇。\n\n"
        )
        if llm_selected_count:
            overview_text += "当日筛中论文均未通过处理或质检，未纳入日报。"
        else:
            overview_text += "当日未检索到符合条件并纳入日报的论文。"

        lines = [f"# 日报 {date}", "", "## 📌 今日概况", "", overview_text, ""]
        append_failed_items(lines, failed_items)
        verified = bool(completion_marker(date, stats, 0))
        observations = ([
            "- 已在元数据公开后重新核查，确认当日没有符合遥感与 AI / 计算机视觉范围的论文。",
            "- 此为已复核的无匹配结果，无论文处理失败。",
        ] if verified else [
            "- 当日无成功纳入论文，建议优先检查候选筛选结果与失败原因。",
            "- 若连续出现空日报，应复核 arXiv 日期窗口、关键词配置与 LLM 筛选输出。",
        ])
        lines += [
            "## 🔎 观察",
            "",
            *observations,
            "",
            "---",
            "",
            "Powered by OpenClaw🦞",
        ]
        return "\n".join(lines) + completion_marker(date, stats, 0)

    prompt = (
        "你是遥感AI日报编辑。请基于给定论文列表输出严格JSON：\n"
        "{\n"
        '  "overview": "120-180字，概述今日研究趋势",\n'
        '  "highlights": ["3条，每条20-40字"],\n'
        '  "one_liners": [{"idx":1,"summary":"每篇一句话，25-45字"}],\n'
        '  "observations": ["2条，偏分析判断，每条24-48字"]\n'
        "}\n"
        "要求：中文、客观、不要编造细节。\n\n"
        f"日期: {date}\n候选: {json.dumps(items, ensure_ascii=False)}"
    )
    output = call_llm(prompt, max_tokens=1800, timeout=240)
    match = re.search(r"\{[\s\S]*\}", output)
    data = {"overview": "", "highlights": [], "one_liners": []}
    if match:
        try:
            data = json.loads(match.group(0))
        except Exception:
            pass

    one_liners = {
        item.get("idx"): item.get("summary", "")
        for item in data.get("one_liners", [])
        if isinstance(item, dict)
    }

    overview_text = data.get("overview") or "今日论文总体呈现出遥感与AI交叉深化趋势。"
    candidate_count = (stats or {}).get("candidate_count")
    llm_selected_count = (stats or {}).get("llm_selected_count")
    included_count = len(items)

    if candidate_count is None:
        candidate_count = included_count
    if llm_selected_count is None:
        llm_selected_count = included_count

    overview_text = (
        f"今日共检索候选论文 {candidate_count} 篇；"
        f"关键词+LLM 智能匹配遥感交叉论文 {llm_selected_count} 篇；"
        f"最终纳入日报 {included_count} 篇。\n\n{overview_text}"
    )

    lines = [f"# 日报 {date}", "", "## 📌 今日概况", "", overview_text, ""]

    highlights = data.get("highlights") or []
    if highlights:
        lines += ["## ✨ 今日亮点", ""]
        for highlight in highlights[:3]:
            lines.append(f"- {highlight}")
        lines.append("")

    lines += ["## 🗂 今日文章列表", "", "| 标题 | 作者 | 单位 | 一句话概括 | Issue |", "|---|---|---|---|---|"]
    for i, paper in enumerate(items, 1):
        summary = one_liners.get(i) or (
            f"聚焦{('、'.join(paper['labels'][:2]) if paper['labels'] else '遥感AI方法')}，给出可复现的模型与评测方案。"
        )
        lines.append(
            f"| {paper['title']} | {paper['authors']} | {paper['institution']} | {summary} | [#{paper['issue']}]({paper['url']}) |"
        )

    append_failed_items(lines, failed_items)

    observations = data.get("observations") or [
        "基础模型与遥感任务结合持续增强，评测与推理能力成为关键。",
        "多数工作关注算法有效性与泛化，而非硬件实现。",
    ]
    lines += ["", "## 🔎 观察", ""]
    for observation in observations[:2]:
        lines.append(f"- {observation}")

    lines += ["", "---", "", "Powered by OpenClaw🦞"]
    return "\n".join(lines) + completion_marker(date, stats, len(items))


def append_failed_items(lines: list[str], failed_items: list[dict] | None) -> None:
    if not failed_items:
        return

    lines += ["", "## ⚠️ 未纳入日报的匹配论文", ""]
    lines.append("以下论文通过关键词/LLM 筛选，但在处理过程中失败未纳入日报。点击 arXiv 链接可查看原文。")
    lines.append("")
    lines.append("| 标题 | arXiv | 失败原因 |")
    lines.append("|------|-------|----------|")
    for item in failed_items:
        title = item.get("title", "Unknown")
        aid = item.get("arxiv_id", "")
        error = item.get("error") or item.get("reason") or "未知"
        arxiv_link = f"[{aid}](https://arxiv.org/abs/{aid})" if aid else "-"
        lines.append(f"| {title} | {arxiv_link} | {error} |")
    lines.append("")
