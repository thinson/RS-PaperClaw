#!/usr/bin/env python3
from __future__ import annotations

import re
import json
from collections import defaultdict
from pathlib import Path

from pipeline_config import get_repo, load_config
from services.digest_builder import build_digest_with_llm, extract_paper_date, validate_papers_for_digest
from services.issue_index import ensure_index, lookup_issue

CONFIG = load_config()


def issue_data(issue) -> dict:
    return getattr(issue, "_rawData", None) or {}


def load_open_issues(repo):
    issues = []
    for issue in repo.get_issues(state="open"):
        raw_data = getattr(issue, "_rawData", None) or {}
        if "pull_request" in raw_data:
            continue
        issues.append(issue)
    return issues


def collect_papers_by_date(issues):
    paper_by_date = defaultdict(list)
    digest_issue_by_date = {}

    for it in issues:
        raw = issue_data(it)
        t = raw.get("title") or it.title
        if "日报" not in t:
            paper_date = extract_paper_date(raw)
            if paper_date:
                paper_by_date[paper_date].append(raw)
        dm = re.search(r"日报\s*(\d{8})", t)
        if dm:
            digest_issue_by_date[dm.group(1)] = it

    return paper_by_date, digest_issue_by_date


def _paper_key(paper: dict) -> int | None:
    number = paper.get("number")
    return number if isinstance(number, int) else None


def _merge_paper(papers: list[dict], paper: dict) -> None:
    number = _paper_key(paper)
    if number is not None and any(_paper_key(item) == number for item in papers):
        return
    papers.append(paper)


def _load_stats_map(stats_json: str | None) -> dict[str, dict]:
    stats_map: dict[str, dict] = {}
    if not stats_json:
        return stats_map
    try:
        obj = json.loads(Path(stats_json).read_text(encoding="utf-8"))
        if isinstance(obj, dict) and obj.get("date"):
            stats_map[obj["date"]] = obj
    except Exception:
        pass
    return stats_map


def _augment_papers_from_stats(repo, papers: list[dict], stats: dict | None) -> list[dict]:
    if not stats:
        return papers

    selected_ids = stats.get("successful_selected_arxiv_ids") or []
    if not selected_ids:
        return papers

    index = ensure_index(repo)
    by_issue_number = {
        _paper_key(paper): paper
        for paper in papers
        if _paper_key(paper) is not None
    }
    merged = list(papers)

    for arxiv_id in selected_ids:
        issue = lookup_issue(repo, index, arxiv_id)
        if issue is None:
            continue

        raw = issue_data(issue)
        number = _paper_key(raw)
        if number is not None and number in by_issue_number:
            continue
        _merge_paper(merged, raw)
        if number is not None:
            by_issue_number[number] = raw

    return merged


def main(target_date: str | None = None, stats_json: str | None = None):
    if not CONFIG.github_token:
        raise RuntimeError("Missing required environment variable: GITHUB_TOKEN")
    if not CONFIG.bailian_api_key:
        raise RuntimeError("Missing required environment variable: BAILIAN_API_KEY")

    repo = get_repo(CONFIG)

    stats_map = _load_stats_map(stats_json)

    issues = load_open_issues(repo)
    paper_by_date, digest_issue_by_date = collect_papers_by_date(issues)

    out_dir = CONFIG.temp_dir / "RS-PaperClaw" / "daily_reports"
    out_dir.mkdir(parents=True, exist_ok=True)

    dates = sorted(set(paper_by_date.keys()) | set(stats_map.keys()))
    if target_date:
        dates = [d for d in dates if d == target_date]

    if not dates:
        print(f"NO_DIGEST_DATE target={target_date or 'ALL'}")
        return

    for date in dates:
        # Open issue list is eventually consistent right after paper creation.
        # Use stats + issue_index to fetch just-created successful papers by
        # issue number, then merge with the regular date-labeled issue scan.
        papers = _augment_papers_from_stats(repo, paper_by_date.get(date, []), stats_map.get(date))
        papers = sorted(papers, key=lambda x: x["number"])
        if not papers:
            print(f"NO_PAPERS date={date}")
            continue
        validation_errors = validate_papers_for_digest(papers)
        if validation_errors:
            raise RuntimeError(
                f"digest paper validation failed for {date}: " + " | ".join(validation_errors[:8])
            )
        md = build_digest_with_llm(
            date,
            papers,
            stats=stats_map.get(date),
            failed_items=(stats_map.get(date) or {}).get("failed_items"),
        )
        (out_dir / f"{date}.md").write_text(md, encoding="utf-8")

        title = f"日报 {date}"
        labels = [date, "日报"]
        if date in digest_issue_by_date:
            digest_issue_by_date[date].edit(body=md, title=title, labels=labels)
            print(f"UPDATED digest issue {date} -> #{digest_issue_by_date[date].number}")
        else:
            ni = repo.create_issue(title=title, body=md, labels=labels)
            print(f"CREATED digest issue {date} -> #{ni.number}")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--date", dest="date", help="仅生成指定日期日报，格式 YYYYMMDD")
    parser.add_argument("--stats-json", dest="stats_json", help="筛选统计 JSON 文件路径")
    args = parser.parse_args()

    main(target_date=args.date, stats_json=args.stats_json)
