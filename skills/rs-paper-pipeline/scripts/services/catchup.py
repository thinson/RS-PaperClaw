"""Discover missing report archives within a bounded recovery window."""
from datetime import datetime, timedelta


def missing_report_dates(repo, target_dates: list[str], lookback_days: int = 7) -> list[str]:
    latest = datetime.strptime(max(target_dates), "%Y%m%d")
    dates = [(latest - timedelta(days=i)).strftime("%Y%m%d") for i in range(lookback_days)]
    archived = set()
    for month in sorted({date[:6] for date in dates}):
        try:
            entries = repo.get_contents(f"daily_reports/{month}")
        except Exception as exc:
            if getattr(exc, "status", None) == 404:
                continue
            raise
        archived.update(entry.name[:-3] for entry in entries if entry.name.endswith(".md"))
    return sorted(set(target_dates) | (set(dates) - archived))
