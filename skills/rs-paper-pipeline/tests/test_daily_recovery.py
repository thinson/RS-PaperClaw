from dataclasses import replace
from pathlib import Path
import subprocess
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import Mock, patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
if sys.platform == "win32":
    sys.modules.setdefault("fcntl", SimpleNamespace(flock=Mock(), LOCK_EX=1, LOCK_NB=2))
import run_rs_daily_workday as runner


class RecoveryTest(unittest.TestCase):
    @patch.object(runner.time, "sleep")
    @patch.object(runner, "_write_state")
    @patch.object(runner, "_run_step")
    @patch.object(runner, "run")
    @patch.object(runner, "_get_repo")
    @patch.object(runner, "daily_report_file_exists", return_value=False)
    def test_missing_archive_cannot_finish_successfully(self, exists, repo, run, step, state, sleep):
        with self.assertRaisesRegex(RuntimeError, "archive still missing"):
            runner._process_date("20260923", False, force=True)
        self.assertEqual(run.call_count, 3)
        self.assertEqual(state.call_args.args[:3], ("20260923", "sync", "failed"))

    @patch.object(runner.time, "sleep")
    @patch.object(runner.subprocess, "run")
    def test_upstream_exit_is_not_retried(self, run, sleep):
        run.side_effect = subprocess.CalledProcessError(75, ["filter"])
        with self.assertRaises(subprocess.CalledProcessError):
            runner.run(["filter"])
        self.assertEqual(run.call_count, 1)
        sleep.assert_not_called()

    def exercise(self, failure):
        with tempfile.TemporaryDirectory() as directory:
            config = replace(runner.CONFIG, github_token="test", llm_api_key="test")
            with patch.object(runner, "CONFIG", config), patch.object(runner, "LOCK_FILE", Path(directory) / "lock"), \
                 patch.object(runner, "check_github_connectivity", return_value=True), \
                 patch.object(runner, "resolve_target_dates", return_value=["20260928"]), \
                 patch.object(runner, "_get_repo"), \
                 patch.object(runner, "missing_report_dates", return_value=["20260923", "20260928"]), \
                 patch.object(runner, "_process_date", side_effect=[failure, None]) as process:
                with self.assertRaises(RuntimeError):
                    runner.main()
                return process.call_args_list

    def test_regular_failure_continues_and_historical_notification_is_disabled(self):
        calls = self.exercise(RuntimeError("paper processing failed"))
        self.assertEqual(len(calls), 2)
        self.assertEqual(calls[0].args, ("20260923", False))
        self.assertEqual(calls[1].args, ("20260928", True))

    def test_upstream_failure_defers_remaining_dates(self):
        self.assertEqual(len(self.exercise(subprocess.CalledProcessError(75, ["filter"]))), 1)
