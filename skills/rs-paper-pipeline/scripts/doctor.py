#!/usr/bin/env python3
from __future__ import annotations

import importlib
import os
import platform
import shutil
import sys

from pipeline_config import DEFAULT_ENV_FILES, load_config


CONFIG = load_config()


def check_mark(label: str, ok: bool, detail: str) -> str:
    status = "OK" if ok else "FAIL"
    return f"[{status}] {label}: {detail}"


def suggestion_for(binary: str) -> str:
    system = platform.system().lower()
    if binary == "PyGithub":
        return "python3 -m pip install -r requirements.txt"
    if binary in {"pdftoppm", "pdftotext"}:
        if system == "darwin":
            return "brew install poppler"
        if system == "linux":
            return "sudo apt-get install -y poppler-utils"
    return ""


def main() -> int:
    checks: list[tuple[bool, str]] = []
    suggestions: list[str] = []
    in_ci = os.environ.get("GITHUB_ACTIONS") == "true" or os.environ.get("CI") == "true"

    checks.append(
        (
            sys.version_info >= (3, 9),
            check_mark("python", sys.version_info >= (3, 9), sys.version.split()[0]),
        )
    )

    env_path = next((path for path in DEFAULT_ENV_FILES if path.exists()), None)
    env_ok = env_path is not None or in_ci
    env_detail = str(env_path) if env_path else ("missing (.env), allowed in CI" if in_ci else "missing (.env)")
    checks.append(
        (
            env_ok,
            check_mark("env-file", env_ok, env_detail),
        )
    )

    for var_name in ("GITHUB_TOKEN", "BAILIAN_API_KEY"):
        present = bool(os.environ.get(var_name))
        checks.append((present, check_mark(var_name, present, "set" if present else "missing")))

    try:
        importlib.import_module("github")
        github_ok = True
        github_detail = "installed"
    except ModuleNotFoundError:
        github_ok = False
        github_detail = "missing PyGithub"
    checks.append((github_ok, check_mark("PyGithub", github_ok, github_detail)))
    if not github_ok:
        suggestions.append(suggestion_for("PyGithub"))

    for bin_name, required in (("pdftoppm", True), ("pdftotext", True), ("openclaw", False)):
        resolved = shutil.which(bin_name)
        ok = resolved is not None or not required
        detail = resolved or ("optional" if not required else "missing")
        checks.append((ok, check_mark(bin_name, ok, detail)))
        if required and resolved is None:
            hint = suggestion_for(bin_name)
            if hint:
                suggestions.append(hint)

    root_ok = CONFIG.root_dir.exists() and CONFIG.scripts_dir.exists()
    workspace_detail = str(CONFIG.root_dir)
    if CONFIG.workspace_warning:
        workspace_detail = f"{workspace_detail} ({CONFIG.workspace_warning})"
    checks.append((root_ok, check_mark("workspace", root_ok, workspace_detail)))

    temp_ok = CONFIG.temp_dir.exists() or CONFIG.temp_dir.parent.exists()
    checks.append((temp_ok, check_mark("temp-dir", temp_ok, str(CONFIG.temp_dir))))

    print("RS Pipeline Doctor")
    print("=" * 18)
    for _, line in checks:
        print(line)

    failures = [line for ok, line in checks if not ok]
    if failures:
        print("\nSummary: environment is not ready")
        unique_suggestions = []
        for item in suggestions:
            if item and item not in unique_suggestions:
                unique_suggestions.append(item)
        if unique_suggestions:
            print("Suggested fixes:")
            for item in unique_suggestions:
                print(f"- {item}")
        return 1

    print("\nSummary: environment looks ready")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
