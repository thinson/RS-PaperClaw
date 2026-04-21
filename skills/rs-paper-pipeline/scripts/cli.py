#!/usr/bin/env python3
from __future__ import annotations

import argparse

import daily_arxiv_cross_filter
import daily_digest_llm_upgrade
import doctor
import paper_processor
import reconcile_daily_issue_set
import run_rs_daily_workday
import sync_daily_reports_to_repo


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="RS-PaperClaw pipeline CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    doctor_parser = subparsers.add_parser("doctor", help="检查运行环境")
    doctor_parser.set_defaults(func=lambda args: doctor.main())

    run_parser = subparsers.add_parser("run", help="运行工作日日报主流程")
    run_parser.add_argument("--date", dest="date", help="指定日期，格式 YYYYMMDD")
    run_parser.add_argument("--notify", action="store_true", help="强制发送通知")
    run_parser.add_argument("--no-notify", action="store_true", help="禁止发送通知")
    run_parser.add_argument("--force", action="store_true", help="即使当天已成功也强制重跑")
    run_parser.set_defaults(func=run_command)

    filter_parser = subparsers.add_parser("filter", help="抓取并筛选论文")
    filter_parser.add_argument("--dry-run", action="store_true")
    filter_parser.add_argument("--days", type=int, default=2, help="抓取最近 N 天的论文（默认2天）")
    filter_parser.add_argument("--date", dest="date", help="抓取指定日期（YYYYMMDD）")
    filter_parser.add_argument("--stats-out", dest="stats_out", help="输出统计 JSON 文件路径")
    filter_parser.set_defaults(func=filter_command)

    digest_parser = subparsers.add_parser("digest", help="生成日报 issue")
    digest_parser.add_argument("--date", dest="date", help="仅生成指定日期日报，格式 YYYYMMDD")
    digest_parser.add_argument("--stats-json", dest="stats_json", help="筛选统计 JSON 文件路径")
    digest_parser.set_defaults(func=digest_command)

    reconcile_parser = subparsers.add_parser("reconcile", help="按 stats 清理某天多余 issue 并重建日报")
    reconcile_parser.add_argument("--date", required=True, help="指定日期，格式 YYYYMMDD")
    reconcile_parser.add_argument("--stats-json", dest="stats_json", help="筛选统计 JSON 文件路径")
    reconcile_parser.add_argument("--dry-run", action="store_true", help="仅打印差异，不关闭 issue")
    reconcile_parser.add_argument("--skip-digest", action="store_true", help="仅清理 issue，不重建日报")
    reconcile_parser.add_argument("--skip-sync", action="store_true", help="清理后不执行 sync")
    reconcile_parser.set_defaults(func=reconcile_command)

    sync_parser = subparsers.add_parser("sync", help="同步日报到仓库")
    sync_parser.set_defaults(func=lambda args: sync_daily_reports_to_repo.main())

    paper_parser = subparsers.add_parser("paper", help="处理单篇论文")
    paper_parser.add_argument("arxiv_id", help="论文 arXiv ID")
    paper_parser.add_argument("issue_number", nargs="?", type=int, help="可选，指定更新的 issue 编号")
    paper_parser.add_argument("--dry-run", action="store_true", help="仅在本地生成结果，不更新 GitHub issue")
    paper_parser.add_argument("--output-dir", dest="output_dir", help="dry-run 输出目录")
    paper_parser.set_defaults(func=paper_command)

    return parser


def run_command(args) -> None:
    notify = None
    if args.notify:
        notify = True
    if args.no_notify:
        notify = False
    run_rs_daily_workday.main(target_date=args.date, notify=notify, force=args.force)


def filter_command(args) -> None:
    daily_arxiv_cross_filter.main(
        dry_run=args.dry_run,
        days_back=args.days,
        stats_out=args.stats_out,
        target_date=args.date,
    )


def digest_command(args) -> None:
    daily_digest_llm_upgrade.main(target_date=args.date, stats_json=args.stats_json)


def reconcile_command(args) -> None:
    stats_json = args.stats_json or f"memory/rs_daily_stats_{args.date}.json"
    reconcile_daily_issue_set.reconcile(
        date_str=args.date,
        stats_json=stats_json,
        dry_run=args.dry_run,
        skip_digest=args.skip_digest,
        skip_sync=args.skip_sync,
    )


def paper_command(args) -> None:
    paper_processor.process_paper(args.arxiv_id, args.issue_number, dry_run=args.dry_run, output_dir=args.output_dir)


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    result = args.func(args)
    return int(result) if isinstance(result, int) else 0


if __name__ == "__main__":
    raise SystemExit(main())
