from datetime import datetime, timezone
from pathlib import Path
import sys
import unittest
from dataclasses import replace
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from services.report_status import completion_marker, empty_result_is_settled, is_verified_empty
from clients import arxiv_client
import daily_arxiv_cross_filter as cross_filter


class EmptyReportRecoveryTest(unittest.TestCase):
    def test_empty_report_must_be_rechecked_after_publication_delay(self):
        self.assertFalse(empty_result_is_settled("20261010", "2026-10-13T23:59:59+00:00"))
        self.assertTrue(empty_result_is_settled("20261010", "2026-10-14T00:00:00+00:00"))
        self.assertFalse(is_verified_empty("# 日报 20261010\n候选 0 篇", "20261010"))
        stats = {"source_complete": True, "source_checked_at": "2026-10-15T00:00:00+00:00", "candidate_count": 0}
        marker = completion_marker("20261010", stats, 0)
        self.assertTrue(is_verified_empty(marker, "20261010"))
        self.assertFalse(is_verified_empty(marker, "20261011"))
        stats["source_checked_at"] = "2026-10-11T00:00:00+00:00"
        with self.assertRaises(ValueError):
            completion_marker("20261010", stats, 0)

    def test_recent_zero_candidates_defers_without_publishing_or_processing(self):
        date = datetime.now(timezone.utc).strftime("%Y%m%d")
        with patch.object(cross_filter, "CONFIG", replace(cross_filter.CONFIG, github_token="test", llm_api_key="test")), \
             patch.object(cross_filter, "get_repo"), patch.object(cross_filter, "ensure_index", return_value={}), \
             patch.object(cross_filter, "fetch_recent_candidates", return_value=[]), \
             patch.object(cross_filter, "save_index") as save:
            with self.assertRaises(SystemExit) as caught:
                cross_filter.main(target_date=date)
            self.assertEqual(caught.exception.code, 76)
            save.assert_not_called()

    @patch.object(arxiv_client, "fetch_query_with_fallback")
    def test_historical_zero_query_does_not_scan_recent_thousands(self, fetch):
        fetch.return_value = '<feed xmlns="http://www.w3.org/2005/Atom" xmlns:o="http://a9.com/-/spec/opensearch/1.1/"><o:totalResults>0</o:totalResults></feed>'
        with patch.dict("os.environ", {"ARXIV_SOURCE": "oai"}):
            self.assertEqual(arxiv_client.fetch_recent_candidates(target_date="20260503"), [])
        fetch.assert_called_once()

    @patch.object(arxiv_client, "fetch_query_with_fallback")
    def test_truncated_historical_query_cannot_be_published(self, fetch):
        fetch.return_value = '<feed xmlns="http://www.w3.org/2005/Atom" xmlns:o="http://a9.com/-/spec/opensearch/1.1/"><o:totalResults>200</o:totalResults></feed>'
        with self.assertRaises(arxiv_client.ArxivUnavailableError):
            arxiv_client.fetch_recent_candidates(target_date="20260503")

    @patch.object(arxiv_client, "fetch_query_with_fallback")
    def test_incomplete_api_response_is_never_treated_as_zero_papers(self, fetch):
        for xml in ('<feed xmlns="http://www.w3.org/2005/Atom"/>',
                    '<feed xmlns="http://www.w3.org/2005/Atom" xmlns:o="http://a9.com/-/spec/opensearch/1.1/"><o:totalResults>1</o:totalResults></feed>'):
            fetch.return_value = xml
            with self.assertRaises(arxiv_client.ArxivUnavailableError):
                arxiv_client.fetch_recent_candidates(target_date="20260503")
