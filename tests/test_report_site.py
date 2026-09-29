"""Run with python -m unittest discover -s tests -p 'test_*.py'."""
import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import types
import unittest
from unittest.mock import patch

SCRIPTS = Path(__file__).resolve().parents[1] / "skills/rs-paper-pipeline/scripts"


def load(name):
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


builder = load("build_report_site")


class ReportSiteTests(unittest.TestCase):
    def test_build_copies_reports_and_sorts_index(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "daily_reports/202609"
            source.mkdir(parents=True)
            for date in ("20260927", "20260928"):
                (source / f"{date}.md").write_text(f"# 日报 {date}\n", encoding="utf-8")
            (source / "README.md").write_text("ignore")
            builder.build(root)
            target = root / "docs/daily_reports"
            self.assertEqual(json.loads((target / "index.json").read_text())["dates"],
                             ["20260928", "20260927"])
            self.assertEqual((source / "20260928.md").read_bytes(),
                             (target / "202609/20260928.md").read_bytes())

    def test_targeted_sync_publishes_body_before_index_preserving_archive(self):
        writes = []
        issue = types.SimpleNamespace(title="日报 20260928", body="# 日报 20260928\n")
        repo = types.SimpleNamespace(
            get_issues=lambda **kwargs: [issue],
            get_contents=lambda path: types.SimpleNamespace(
                decoded_content=b'{"dates":["20260305"]}'))
        github = types.ModuleType("clients.github_ops")
        github.cleanup_legacy_daily_reports = lambda *args: None
        github.upsert_repo_file = lambda repo, path, content, message: writes.append((path, content))
        config = types.ModuleType("pipeline_config")
        config.load_config = lambda: None
        config.get_repo = lambda config: repo
        with patch.dict(sys.modules, {"clients.github_ops": github, "pipeline_config": config,
                                      "build_report_site": builder}):
            sync = load("sync_daily_reports_to_repo")
            sync.main("20260928")
        paths = [path for path, _ in writes]
        self.assertLess(paths.index("docs/daily_reports/202609/20260928.md"),
                        paths.index("docs/daily_reports/index.json"))
        index = dict(writes)["docs/daily_reports/index.json"]
        self.assertEqual(json.loads(index)["dates"], ["20260928", "20260305"])


if __name__ == "__main__":
    unittest.main()
