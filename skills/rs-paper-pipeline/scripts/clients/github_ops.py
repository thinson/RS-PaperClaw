#!/usr/bin/env python3
from __future__ import annotations

import re

from pipeline_config import load_config


CONFIG = load_config()


def extract_arxiv_id_from_text(text: str) -> str | None:
    match = re.search(r"arxiv\.org/abs/([^\)\s]+)", text or "")
    return match.group(1).strip() if match else None


def extract_arxiv_id_from_issue(issue) -> str | None:
    return extract_arxiv_id_from_text(issue.body or "")


def get_today_digest_issue(repo, date_str: str):
    title = f"日报 {date_str}"
    for issue in repo.get_issues(state="open"):
        if issue.title.strip() == title:
            return issue
    return None


def daily_report_file_exists(repo, date_str: str) -> bool:
    ym = date_str[:6]
    path = f"daily_reports/{ym}/{date_str}.md"
    try:
        repo.get_contents(path)
        return True
    except Exception:
        return False


def load_existing_arxiv_ids(repo) -> set[str]:
    arxiv_ids: set[str] = set()
    for issue in repo.get_issues(state="all"):
        arxiv_id = extract_arxiv_id_from_issue(issue)
        if arxiv_id:
            arxiv_ids.add(arxiv_id)
    return arxiv_ids


def upsert_repo_file(repo, path: str, content: str, message: str) -> None:
    data = content.encode("utf-8")
    try:
        existing = repo.get_contents(path)
        existing_text = existing.decoded_content.decode("utf-8")
        if existing_text == content:
            print(f"UNCHANGED {path}")
            return
        repo.update_file(path=path, message=message, content=data, sha=existing.sha)
        print(f"UPDATED {path}")
    except Exception:
        repo.create_file(path=path, message=message, content=data)
        print(f"CREATED {path}")


def cleanup_legacy_daily_reports(repo, base_dir: str = "daily_reports") -> None:
    try:
        entries = repo.get_contents(base_dir)
    except Exception:
        return

    for entry in entries:
        if entry.type == "file" and re.fullmatch(r"\d{8}\.md", entry.name):
            repo.delete_file(
                path=entry.path,
                message=f"cleanup legacy daily report file {entry.name}",
                sha=entry.sha,
            )
            print(f"DELETED {entry.path}")
