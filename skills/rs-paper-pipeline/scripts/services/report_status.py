"""Durable evidence for completed empty reports, shared by recovery and skip checks."""
from datetime import datetime, timedelta, timezone
import json
import re


EMPTY_SETTLE_DAYS = 4
MARKER = re.compile(r"<!-- rs-pipeline: (\{[^\n]*\}) -->")
PAPER_LINK = re.compile(r"github\.com/[^/]+/[^/]+/issues/\d+")


def empty_result_is_settled(date: str, checked_at: str) -> bool:
    checked = datetime.fromisoformat(checked_at.replace("Z", "+00:00"))
    if checked.tzinfo is None:
        raise ValueError("Metadata check time must include a timezone")
    deadline = datetime.strptime(date, "%Y%m%d").replace(tzinfo=timezone.utc) + timedelta(days=EMPTY_SETTLE_DAYS)
    return checked >= deadline


def completion_marker(date: str, stats: dict | None, paper_count: int) -> str:
    if not stats or not stats.get("source_checked_at") or not stats.get("source_complete"):
        return ""
    selected = stats.get("selected_arxiv_ids", [])
    successful = stats.get("successful_selected_arxiv_ids", [])
    if stats.get("failed_arxiv_ids") or set(selected) != set(successful) or len(set(selected)) != paper_count:
        raise ValueError("Cannot mark an incomplete report as completed")
    evidence = {"date": date, "source": stats.get("metadata_source"),
                "checked_at": stats["source_checked_at"], "source_complete": True,
                "candidate_count": stats["candidate_count"], "paper_count": paper_count}
    if not paper_count and not empty_result_is_settled(date, evidence["checked_at"]):
        raise ValueError("Empty result is too recent to finalize")
    return "\n\n<!-- rs-pipeline: " + json.dumps(evidence, ensure_ascii=False) + " -->"


def is_verified_empty(body: str, date: str) -> bool:
    match = MARKER.search(body or "")
    if not match:
        return False
    try:
        data = json.loads(match.group(1))
        return (data["date"] == date and data["source_complete"] is True
                and data["paper_count"] == 0 and isinstance(data["candidate_count"], int)
                and data["candidate_count"] >= 0 and not PAPER_LINK.search(body)
                and empty_result_is_settled(date, data["checked_at"]))
    except (ValueError, KeyError, TypeError):
        return False
