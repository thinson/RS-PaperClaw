#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from pathlib import Path

import daily_arxiv_cross_filter
import daily_digest_llm_upgrade
import sync_daily_reports_to_repo
from clients.github_ops import extract_arxiv_id_from_issue
from pipeline_config import get_repo, load_config


CONFIG = load_config()


def ensure_stats(stats_json: str, date_str: str) -> dict:
    path = Path(stats_json)
    if not path.exists():
        print(f"STATS_MISSING {stats_json} -> rebuilding via filter --dry-run")
        daily_arxiv_cross_filter.main(
            dry_run=True,
            days_back=2,
            stats_out=stats_json,
            target_date=date_str,
        )
    return load_stats(stats_json, date_str)


def load_stats(stats_json: str, date_str: str) -> dict:
    path = Path(stats_json)
    if not path.exists():
        raise RuntimeError(f"stats file not found: {stats_json}")
    obj = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(obj, dict):
        raise RuntimeError(f"invalid stats json: {stats_json}")
    if obj.get("date") != date_str:
        raise RuntimeError(f"stats date mismatch: expected {date_str}, got {obj.get('date')}")
    if not obj.get("selected_arxiv_ids"):
        raise RuntimeError(
            f"stats file missing selected_arxiv_ids: {stats_json}. rerun filter first."
        )
    return obj


def get_open_date_issues(repo, date_str: str):
    issues = list(repo.get_issues(state="open", labels=[date_str]))
    issues.sort(key=lambda x: x.number)
    return issues


def split_date_issues(issues):
    digest_issue = None
    paper_issues = []
    for issue in issues:
        if "日报" in issue.title:
            digest_issue = issue
        else:
            paper_issues.append(issue)
    return digest_issue, paper_issues


def reconcile(date_str: str, stats_json: str, dry_run: bool = False, skip_digest: bool = False, skip_sync: bool = False) -> int:
    stats = ensure_stats(stats_json, date_str)
    expected_ids = set(stats["selected_arxiv_ids"])
    repo = get_repo(CONFIG)
    digest_issue, paper_issues = split_date_issues(get_open_date_issues(repo, date_str))

    keep = []
    extra = []
    missing = set(expected_ids)
    unknown = []

    for issue in paper_issues:
        arxiv_id = extract_arxiv_id_from_issue(issue)
        if not arxiv_id:
            unknown.append(issue)
            continue
        if arxiv_id in expected_ids:
            keep.append(issue)
            missing.discard(arxiv_id)
        else:
            extra.append(issue)

    print(f"DATE {date_str}")
    print(f"EXPECTED {len(expected_ids)}")
    print(f"KEEP {len(keep)}")
    print(f"EXTRA {len(extra)}")
    print(f"MISSING {len(missing)}")
    print(f"UNKNOWN {len(unknown)}")

    for issue in extra:
        print(f"EXTRA #{issue.number} | {extract_arxiv_id_from_issue(issue) or '-'} | {issue.title}")
    for issue in unknown:
        print(f"UNKNOWN #{issue.number} | {issue.title}")
    for arxiv_id in sorted(missing):
        print(f"MISSING_ARXIV {arxiv_id}")

    if dry_run:
        print("DRY_RUN no changes applied")
        return 0

    comment = (
        f"Closed after reconciling the {date_str} paper set against the latest selected_arxiv_ids "
        f"from {stats_json}; this issue is outside the final kept set for that date."
    )
    for issue in extra:
        issue.create_comment(comment)
        issue.edit(state="closed")
        print(f"CLOSED #{issue.number}")

    if missing:
        raise RuntimeError(
            f"cannot regenerate digest for {date_str}; missing expected arxiv ids: {', '.join(sorted(missing))}"
        )

    if not skip_digest:
        daily_digest_llm_upgrade.main(target_date=date_str, stats_json=stats_json)
    if not skip_sync:
        sync_daily_reports_to_repo.main()

    return 0


def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--date", required=True, help="指定日期，格式 YYYYMMDD")
    parser.add_argument(
        "--stats-json",
        dest="stats_json",
        help="筛选统计 JSON 文件路径，默认 memory/rs_daily_stats_YYYYMMDD.json",
    )
    parser.add_argument("--dry-run", action="store_true", help="仅打印差异，不关闭 issue")
    parser.add_argument("--skip-digest", action="store_true", help="仅清理 issue，不重建日报")
    parser.add_argument("--skip-sync", action="store_true", help="清理后不执行 sync")
    args = parser.parse_args()

    stats_json = args.stats_json or f"memory/rs_daily_stats_{args.date}.json"
    return reconcile(
        date_str=args.date,
        stats_json=stats_json,
        dry_run=args.dry_run,
        skip_digest=args.skip_digest,
        skip_sync=args.skip_sync,
    )


if __name__ == "__main__":
    raise SystemExit(main())
