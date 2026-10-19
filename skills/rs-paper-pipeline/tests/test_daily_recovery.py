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
    def test_github_client_honors_configured_runtime_proxy(self):
        import os
        from pipeline_config import get_github_client
        with patch.dict(os.environ, {"RS_PROXY_URL": "http://127.0.0.1:9999"}, clear=True):
            client = get_github_client(replace(runner.CONFIG, github_token="test"))
            self.assertEqual(os.environ["https_proxy"], "http://127.0.0.1:9999")
            client.close()

    @patch.object(runner, "_get_repo")
    @patch.object(runner, "get_today_digest_issue")
    @patch.object(runner, "daily_report_matches_digest", return_value=False)
    def test_populated_issue_with_stale_empty_archive_is_not_skipped(self, matches, digest, repo):
        digest.return_value = SimpleNamespace(number=1, body="https://github.com/example/repo/issues/2")
        self.assertFalse(runner._date_already_completed("20261009")[0])

    def test_archive_and_website_must_both_match_current_issue(self):
        from clients.github_ops import daily_report_matches_digest
        repo = Mock()
        repo.get_contents.side_effect = [SimpleNamespace(decoded_content=b"new digest\n"),
                                       SimpleNamespace(decoded_content=b"old empty digest\n")]
        self.assertFalse(daily_report_matches_digest(repo, "20261009", "new digest"))
        repo.get_contents.side_effect = [SimpleNamespace(decoded_content=b"new digest\n"),
                                       SimpleNamespace(decoded_content=b"new digest\n")]
        self.assertTrue(daily_report_matches_digest(repo, "20261009", "new digest"))

    def test_sync_uses_direct_receipt_when_new_digest_is_not_in_listing(self):
        import json
        import sync_daily_reports_to_repo as sync
        with tempfile.TemporaryDirectory() as directory:
            config = replace(sync.CONFIG, memory_dir=Path(directory))
            Path(directory, "digest_issue_20261009.json").write_text(json.dumps(
                {"repo": config.github_repo, "date": "20261009", "number": 1501}))
            repo = Mock()
            issue = SimpleNamespace(number=1501, title="日报 20261009")
            repo.get_issue.return_value = issue
            with patch.object(sync, "CONFIG", config):
                self.assertIs(sync.load_digest_receipt(repo, "20261009"), issue)
                issue.title = "Different paper"
                with self.assertRaises(RuntimeError):
                    sync.load_digest_receipt(repo, "20261009")

    @patch.object(runner, "_get_repo")
    def test_precheck_uses_authenticated_repository_client(self, repo):
        repo.return_value.full_name = runner.CONFIG.github_repo
        self.assertTrue(runner.check_github_connectivity())

    @patch.object(runner.time, "sleep")
    @patch.object(runner, "_get_repo")
    def test_precheck_recovers_from_transient_network_failure(self, repo, sleep):
        repo.side_effect = [OSError("temporary outage"), SimpleNamespace(full_name=runner.CONFIG.github_repo)]
        self.assertTrue(runner.check_github_connectivity())
        self.assertEqual(repo.call_count, 2)

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

    def test_unpublished_empty_date_is_deferred_while_other_dates_continue(self):
        with tempfile.TemporaryDirectory() as directory:
            with patch.object(runner, "CONFIG", replace(runner.CONFIG, github_token="test", llm_api_key="test")), \
                 patch.object(runner, "LOCK_FILE", Path(directory) / "lock"), \
                 patch.object(runner, "check_github_connectivity", return_value=True), \
                 patch.object(runner, "resolve_target_dates", return_value=["20260928"]), \
                 patch.object(runner, "_get_repo"), \
                 patch.object(runner, "missing_report_dates", return_value=["20260926", "20260928"]), \
                 patch.object(runner, "_process_date", side_effect=[subprocess.CalledProcessError(76, ["filter"]), None]) as process:
                runner.main(notify=False)
                self.assertEqual(process.call_count, 2)
