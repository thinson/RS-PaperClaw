#!/usr/bin/env python3
"""Persistent issue index for fast arxiv_id → issue_number lookup.

Index file lives at ``papers/issue_index.json`` in the repo (committed).
Avoids full ``repo.get_issues()`` scans on every pipeline run.
"""

from __future__ import annotations

import json
import re
from datetime import datetime, timezone

from clients.github_ops import upsert_repo_file

INDEX_PATH = "papers/issue_index.json"


def _extract_arxiv_id(body: str) -> str | None:
    match = re.search(r"arxiv\.org/abs/([^\)\s]+)", body or "")
    return match.group(1).strip() if match else None


def load_index(repo) -> dict[str, dict]:
    """Load the index from the repo file. Returns {} if not found."""
    try:
        content = repo.get_contents(INDEX_PATH)
        data = json.loads(content.decoded_content.decode("utf-8"))
        return data if isinstance(data, dict) else {}
    except Exception:
        return {}


def save_index(repo, index: dict[str, dict]) -> None:
    """Persist the index to the repo."""
    body = json.dumps(index, ensure_ascii=False, indent=2) + "\n"
    upsert_repo_file(repo, INDEX_PATH, body, "update issue index")


def rebuild_index(repo) -> dict[str, dict]:
    """Full scan: build index from all issues in the repo."""
    index: dict[str, dict] = {}
    for issue in repo.get_issues(state="all"):
        body = issue.body or ""
        arxiv_id = _extract_arxiv_id(body)
        if not arxiv_id:
            continue
        index[arxiv_id] = {
            "number": issue.number,
            "updated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        }
    return index


def ensure_index(repo) -> dict[str, dict]:
    """Load index; auto-rebuild if empty."""
    index = load_index(repo)
    if not index:
        print("[issue_index] index empty, rebuilding...")
        index = rebuild_index(repo)
        save_index(repo, index)
        print(f"[issue_index] rebuilt with {len(index)} entries")
    return index


def lookup_issue(repo, index: dict[str, dict], arxiv_id: str):
    """Fetch a single issue by number from the index. Returns None if not found."""
    entry = index.get(arxiv_id)
    if not entry:
        return None
    try:
        return repo.get_issue(entry["number"])
    except Exception:
        return None


def update_index_from_issue(index: dict[str, dict], arxiv_id: str, issue) -> bool:
    """Update index entry for an arxiv_id. Returns True if index changed."""
    if not arxiv_id:
        return False
    index[arxiv_id] = {
        "number": issue.number,
        "updated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }
    return True


def commit_index_if_dirty(repo, index: dict[str, dict]) -> bool:
    """Save index to repo if it has been modified. Returns True if saved."""
    if not index:
        return False
    save_index(repo, index)
    return True
