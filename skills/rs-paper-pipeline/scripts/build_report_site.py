#!/usr/bin/env python3
"""Build same-origin report assets for the existing docs/ GitHub Pages site."""
from __future__ import annotations

import json
import re
from pathlib import Path


def report_index(dates):
    return json.dumps({"version": 1, "dates": sorted(set(dates), reverse=True)}, indent=2) + "\n"


def build(root: Path):
    source = root / "daily_reports"
    target = root / "docs" / "daily_reports"
    dates = []
    for path in sorted(source.glob("*/*.md")):
        if not re.fullmatch(r"\d{8}", path.stem) or path.parent.name != path.stem[:6]:
            continue
        destination = target / path.relative_to(source)
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(path.read_bytes())
        dates.append(path.stem)
    target.mkdir(parents=True, exist_ok=True)
    (target / "index.json").write_text(report_index(dates), encoding="utf-8")
    print(f"Built {len(dates)} reports in {target}")


if __name__ == "__main__":
    build(Path(__file__).resolve().parents[3])
