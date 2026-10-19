"""Discover archive gaps and unverified empty reports, including old failures."""
from datetime import datetime, timedelta
import re

from services.report_status import PAPER_LINK, is_verified_empty


def missing_report_dates(repo, target_dates: list[str], lookback_days: int | None = None) -> list[str]:
    latest = datetime.strptime(max(target_dates), "%Y%m%d")
    if lookback_days is None:
        try:
            months = [entry.name for entry in repo.get_contents("daily_reports")
                      if re.fullmatch(r"\d{6}", entry.name) and entry.name <= latest.strftime("%Y%m")]
        except Exception as exc:
            if getattr(exc, "status", None) != 404:
                raise
            months = []
        if not months:
            return sorted(set(target_dates))
        earliest = datetime.strptime(min(months) + "01", "%Y%m%d")
        lookback_days = (latest - earliest).days + 1
    if lookback_days < 1:
        raise ValueError("lookback_days must be positive")
    dates = [(latest - timedelta(days=i)).strftime("%Y%m%d") for i in range(lookback_days)]
    archived = set()
    retry_empty = set()
    for month in sorted({date[:6] for date in dates}):
        try:
            entries = repo.get_contents(f"daily_reports/{month}")
        except Exception as exc:
            if getattr(exc, "status", None) == 404:
                continue
            raise
        for entry in entries:
            if not re.fullmatch(r"\d{8}\.md", entry.name):
                continue
            date = entry.name[:-3]
            archived.add(date)
            # Empty reports are small. Fetch only these bodies, not every
            # historical report or the repository's preview images.
            if date in dates and getattr(entry, "size", 10000) < 2000:
                body = repo.get_contents(f"daily_reports/{month}/{entry.name}").decoded_content.decode("utf-8")
                if not PAPER_LINK.search(body) and not is_verified_empty(body, date):
                    retry_empty.add(date)
    # The first archived month can start partway through the month.
    if archived:
        dates = [date for date in dates if date >= min(archived)]
    # Issue bodies arrive in a paginated list, so also inspect them without
    # downloading every archive. This covers long empty digests with many
    # failed-paper rows that exceed the small-file check above.
    for issue in repo.get_issues(state="open", labels=["日报"]):
        match = re.fullmatch(r"日报\s*(\d{8})", (issue.title or "").strip())
        if match and match.group(1) in dates:
            date = match.group(1)
            if not PAPER_LINK.search(issue.body or "") and not is_verified_empty(issue.body or "", date):
                retry_empty.add(date)
    return sorted(set(target_dates) | (set(dates) - archived) | retry_empty)
