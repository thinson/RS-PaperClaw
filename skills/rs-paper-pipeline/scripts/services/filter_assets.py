#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from functools import lru_cache
from pathlib import Path

from pipeline_config import load_config


CONFIG = load_config()


def _read_text(path: Path) -> str:
    if not path.exists():
        raise RuntimeError(f"Missing filter asset file: {path}")
    return path.read_text(encoding="utf-8").strip()


def _read_json(path: Path) -> dict:
    if not path.exists():
        raise RuntimeError(f"Missing filter config file: {path}")
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise RuntimeError(f"Invalid filter config file: {path}")
    return data


def _load_string_list(data: dict, key: str, path: Path) -> list[str]:
    value = data.get(key)
    if not isinstance(value, list) or not value or not all(isinstance(item, str) and item.strip() for item in value):
        raise RuntimeError(f"Invalid '{key}' in filter config: {path}")
    return [item.strip() for item in value]


@lru_cache(maxsize=1)
def load_filter_keywords() -> dict[str, list[str]]:
    data = _read_json(CONFIG.filter_keywords_path)
    return {
        "rs_query_terms": _load_string_list(data, "rs_query_terms", CONFIG.filter_keywords_path),
        "rs_signal_patterns": _load_string_list(data, "rs_signal_patterns", CONFIG.filter_keywords_path),
        "ai_signal_patterns": _load_string_list(data, "ai_signal_patterns", CONFIG.filter_keywords_path),
        "non_rs_application_patterns": data.get("non_rs_application_patterns", []),
        "explicit_rs_application_patterns": data.get("explicit_rs_application_patterns", []),
    }


@lru_cache(maxsize=1)
def load_filter_prompt_template() -> str:
    template = _read_text(CONFIG.filter_prompt_path)
    if "{{candidate_lines}}" not in template:
        raise RuntimeError(f"Filter prompt template must contain {{candidate_lines}}: {CONFIG.filter_prompt_path}")
    return template


@lru_cache(maxsize=1)
def load_rs_query_terms() -> list[str]:
    return load_filter_keywords()["rs_query_terms"]


@lru_cache(maxsize=1)
def load_rs_signal_patterns() -> list[re.Pattern[str]]:
    return [re.compile(pattern) for pattern in load_filter_keywords()["rs_signal_patterns"]]


@lru_cache(maxsize=1)
def load_ai_signal_patterns() -> list[re.Pattern[str]]:
    return [re.compile(pattern) for pattern in load_filter_keywords()["ai_signal_patterns"]]


def load_application_patterns(key: str) -> list[re.Pattern[str]]:
    values = load_filter_keywords()[key]
    if not isinstance(values, list) or not all(isinstance(value, str) for value in values):
        raise RuntimeError(f"Invalid filter pattern list: {key}")
    return [re.compile(pattern) for pattern in values]


def render_filter_prompt(candidate_lines: list[str]) -> str:
    template = load_filter_prompt_template()
    return template.replace("{{candidate_lines}}", "\n".join(candidate_lines))
