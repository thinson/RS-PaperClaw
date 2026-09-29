from pathlib import Path
from dataclasses import replace
import sys
import unittest
from types import SimpleNamespace
from unittest.mock import Mock, patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from services.author_block import author_block_has_no_affiliation
from services.issue_index import lookup_issue
import daily_digest_llm_upgrade as digest
import daily_arxiv_cross_filter as cross_filter


class IntegrityTest(unittest.TestCase):
    def test_failed_selected_paper_stops_publication(self):
        candidate = {"arxiv_id": "2609.12345", "published": "2026-09-23", "title": "Satellite AI"}
        with patch.object(cross_filter, "CONFIG", replace(cross_filter.CONFIG, github_token="test", llm_api_key="test")), \
             patch.object(cross_filter, "get_repo"), patch.object(cross_filter, "ensure_index", return_value={}), \
             patch.object(cross_filter, "fetch_recent_candidates", return_value=[candidate]), \
             patch.object(cross_filter, "llm_cross_filter", return_value=[candidate]), \
             patch.object(cross_filter, "lookup_issue", return_value=None), \
             patch.object(cross_filter, "process_paper", return_value=(None, "quality gate")), \
             patch.object(cross_filter, "save_index"):
            with self.assertRaises(SystemExit) as caught:
                cross_filter.main(target_date="20260923")
            self.assertEqual(caught.exception.code, 65)

    def test_author_block_requires_positive_complete_evidence(self):
        author = '<div class="ltx_authors"><span class="ltx_personname">Shoichi Otomo</span>{}</div>'
        self.assertTrue(author_block_has_no_affiliation(author.format("")))
        self.assertTrue(author_block_has_no_affiliation(author.format("† thanks: E-mail: name at gmail.com")))
        for value in ("University of Somewhere", "Independent researcher", "Acme Labs", '<span class="ltx_affiliation"></span>'):
            self.assertFalse(author_block_has_no_affiliation(author.format(value)))
        self.assertFalse(author_block_has_no_affiliation("<html>not available</html>"))
        self.assertFalse(author_block_has_no_affiliation(author.format("")[:-6]))

    def test_version_alias_uses_original_issue(self):
        repo = Mock()
        lookup_issue(repo, {"2609.12345v1": {"number": 5}, "2609.12345": {"number": 9}}, "2609.12345v12")
        repo.get_issue.assert_called_once_with(5)

    @patch.object(digest, "ensure_index", return_value={})
    @patch.object(digest, "lookup_issue")
    def test_stats_are_authoritative_for_digest_membership(self, lookup, index):
        lookup.return_value = SimpleNamespace(_rawData={"number": 2})
        stats = {"selected_arxiv_ids": ["2609.12345"], "successful_selected_arxiv_ids": ["2609.12345"]}
        self.assertEqual(digest._augment_papers_from_stats(Mock(), [{"number": 1}, {"number": 2}], stats), [{"number": 2}])
        self.assertEqual(digest._augment_papers_from_stats(Mock(), [{"number": 1}], {"selected_arxiv_ids": []}), [])
        with self.assertRaises(RuntimeError):
            digest._augment_papers_from_stats(Mock(), [], {"selected_arxiv_ids": ["2609.12345"]})
