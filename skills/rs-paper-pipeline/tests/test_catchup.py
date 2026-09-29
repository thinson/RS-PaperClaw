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
        repo.get_contents.side_effect = [
            [SimpleNamespace(name=f"202608{day}.md") for day in (28, 29, 31)],
            [SimpleNamespace(name="20260901.md")],
        ]
        self.assertEqual(missing_report_dates(repo, ["20260903"], 7),
                         ["20260830", "20260902", "20260903"])

    def test_only_missing_directory_is_treated_as_empty(self):
        repo = Mock()
        error = RuntimeError("access denied")
        error.status = 403
        repo.get_contents.side_effect = error
        with self.assertRaises(RuntimeError):
            missing_report_dates(repo, ["20260928"])
        error.status = 404
        self.assertEqual(len(missing_report_dates(repo, ["20260928"])), 7)

    def test_keeps_scheduled_dates_for_normal_completion_check(self):
        repo = Mock()
        repo.get_contents.return_value = [SimpleNamespace(name="20260928.md")]
        self.assertEqual(missing_report_dates(repo, ["20260928"], 1), ["20260928"])
