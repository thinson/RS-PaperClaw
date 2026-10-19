from pathlib import Path
import sys
import unittest
from types import SimpleNamespace
from unittest.mock import Mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from services.catchup import missing_report_dates


class CatchupTest(unittest.TestCase):
    def test_recovers_gaps_across_month_boundary_without_future_dates(self):
        repo = Mock()
        repo.get_issues.return_value = []
        repo.get_contents.side_effect = [
            [SimpleNamespace(name=f"202608{day}.md") for day in (28, 29, 31)],
            [SimpleNamespace(name="20260901.md")],
        ]
        self.assertEqual(missing_report_dates(repo, ["20260903"], 7),
                         ["20260830", "20260902", "20260903"])

    def test_only_missing_directory_is_treated_as_empty(self):
        repo = Mock()
        repo.get_issues.return_value = []
        error = RuntimeError("access denied")
        error.status = 403
        repo.get_contents.side_effect = error
        with self.assertRaises(RuntimeError):
            missing_report_dates(repo, ["20260928"])
        error.status = 404
        self.assertEqual(missing_report_dates(repo, ["20260928"]), ["20260928"])

    def test_keeps_scheduled_dates_for_normal_completion_check(self):
        repo = Mock()
        repo.get_issues.return_value = []
        repo.get_contents.return_value = [SimpleNamespace(name="20260928.md")]
        self.assertEqual(missing_report_dates(repo, ["20260928"], 1), ["20260928"])

    def test_default_finds_old_gaps_and_unverified_empty_reports(self):
        repo = Mock()
        repo.get_issues.return_value = []
        repo.get_contents.side_effect = [
            [SimpleNamespace(name="202609"), SimpleNamespace(name="README.md")],
            [SimpleNamespace(name="20260901.md", size=3000),
             SimpleNamespace(name="20260903.md", size=400)],
            SimpleNamespace(decoded_content=b"# empty report"),
        ]
        self.assertEqual(missing_report_dates(repo, ["20260904"]),
                         ["20260902", "20260903", "20260904"])

    def test_verified_empty_and_small_nonempty_report_are_complete(self):
        from services.report_status import completion_marker
        marker = completion_marker("20260901", {"source_complete": True,
            "source_checked_at": "2026-09-06T00:00:00+00:00", "candidate_count": 0}, 0)
        repo = Mock()
        repo.get_issues.return_value = []
        repo.get_contents.side_effect = [
            [SimpleNamespace(name="20260901.md", size=400), SimpleNamespace(name="20260902.md", size=1000)],
            SimpleNamespace(decoded_content=marker.encode()),
            SimpleNamespace(decoded_content=b"https://github.com/example/repo/issues/1"),
        ]
        self.assertEqual(missing_report_dates(repo, ["20260903"], 3), ["20260903"])

    def test_large_empty_digest_with_failures_is_also_recovered(self):
        repo = Mock()
        repo.get_contents.return_value = [SimpleNamespace(name="20260901.md", size=5000)]
        repo.get_issues.return_value = [SimpleNamespace(title="日报 20260901", body="failed paper rows\n" * 300)]
        self.assertEqual(missing_report_dates(repo, ["20260902"], 2), ["20260901", "20260902"])
