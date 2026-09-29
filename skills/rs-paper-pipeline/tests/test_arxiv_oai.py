from dataclasses import replace
from http.client import IncompleteRead
from pathlib import Path
import sys
import tempfile
import unittest
from types import SimpleNamespace
from urllib.error import HTTPError
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from clients import arxiv_oai


def page(created="2026-09-23", token="", identifier="2609.12345"):
    return f'''<OAI-PMH xmlns="http://www.openarchives.org/OAI/2.0/">
    <ListRecords><record><header><datestamp>2026-09-28</datestamp></header>
    <metadata><arXiv xmlns="http://arxiv.org/OAI/arXiv/">
    <id>{identifier}</id><created>{created}</created><title>Remote sensing</title>
    <abstract>Satellite imagery analysis</abstract><authors><author><keyname>Smith</keyname>
    <forenames>Jane</forenames><affiliation>University</affiliation></author></authors>
    </arXiv></metadata></record><resumptionToken>{token}</resumptionToken></ListRecords></OAI-PMH>'''


class OaiTest(unittest.TestCase):
    @patch.object(arxiv_oai.subprocess, "run")
    @patch.object(arxiv_oai.urllib.request, "urlopen")
    def test_406_uses_compressed_curl_and_removes_status_marker(self, urlopen, run):
        urlopen.side_effect = HTTPError("url", 406, "Not Acceptable", {}, None)
        run.return_value = SimpleNamespace(returncode=0, stdout=page().encode() + b"\nRS_HTTP_STATUS:200", stderr=b"")
        self.assertEqual(arxiv_oai._fetch({"verb": "ListRecords"}), page().encode())
        self.assertIn("--compressed", run.call_args.args[0])

    @patch.object(arxiv_oai.subprocess, "run")
    @patch.object(arxiv_oai.urllib.request, "urlopen")
    def test_curl_rate_limit_is_not_retried(self, urlopen, run):
        urlopen.side_effect = HTTPError("url", 406, "Not Acceptable", {}, None)
        run.return_value = SimpleNamespace(returncode=0, stdout=b"Rate exceeded.\nRS_HTTP_STATUS:429", stderr=b"")
        with self.assertRaises(HTTPError) as caught:
            arxiv_oai._fetch({"verb": "ListRecords"})
        self.assertEqual(caught.exception.code, 429)
        self.assertEqual(run.call_count, 1)

    @patch.object(arxiv_oai.subprocess, "run")
    @patch.object(arxiv_oai.urllib.request, "urlopen")
    def test_truncated_response_uses_complete_curl_response(self, urlopen, run):
        urlopen.return_value.__enter__.return_value.read.side_effect = IncompleteRead(b"partial", 100)
        run.return_value = SimpleNamespace(returncode=0, stdout=page().encode() + b"\nRS_HTTP_STATUS:200", stderr=b"")
        self.assertEqual(arxiv_oai._fetch({"verb": "ListRecords"}), page().encode())

    def test_original_submission_date_and_authors(self):
        items, token = arxiv_oai.parse_page(page())
        self.assertEqual(items[0]["published"], "2026-09-23")
        self.assertEqual(items[0]["authors"], ["Jane Smith"])
        self.assertEqual(items[0]["affiliations"], ["University"])
        self.assertEqual(token, "")

    def test_rejects_html_incomplete_records_and_oai_errors(self):
        for data in ("<html/>", page().replace("<abstract>Satellite imagery analysis</abstract>", ""),
                     '<OAI-PMH xmlns="http://www.openarchives.org/OAI/2.0/"><error code="badArgument">bad</error></OAI-PMH>'):
            with self.assertRaises(RuntimeError):
                arxiv_oai.parse_page(data)

    @patch.object(arxiv_oai.time, "sleep")
    @patch.object(arxiv_oai, "_fetch")
    def test_full_pagination_filters_old_updates_and_reuses_cache(self, fetch, sleep):
        with tempfile.TemporaryDirectory() as directory, patch.object(arxiv_oai, "CONFIG", replace(arxiv_oai.CONFIG, memory_dir=Path(directory))):
            fetch.side_effect = [page(created="2020-01-01", token="next"), page()]
            result = arxiv_oai.harvest_since("2026-09-22", lambda text: True)
            self.assertEqual(len(result), 1)
            self.assertEqual(fetch.call_args.args[0], {"verb": "ListRecords", "resumptionToken": "next"})
            arxiv_oai.harvest_since("2026-09-23", lambda text: True)
            self.assertEqual(fetch.call_count, 2)
            self.assertEqual(arxiv_oai.cached_metadata("2609.12345v1")["title"], "Remote sensing")

    @patch.object(arxiv_oai.time, "sleep")
    @patch.object(arxiv_oai, "_fetch")
    def test_failed_page_never_caches_partial_results(self, fetch, sleep):
        with tempfile.TemporaryDirectory() as directory, patch.object(arxiv_oai, "CONFIG", replace(arxiv_oai.CONFIG, memory_dir=Path(directory))):
            fetch.side_effect = [page(token="next"), RuntimeError("network")]
            with self.assertRaises(RuntimeError):
                arxiv_oai.harvest_since("2026-09-22", lambda text: True)
            self.assertFalse((Path(directory) / "arxiv_oai_recent.json").exists())

    @patch.object(arxiv_oai.time, "sleep")
    @patch.object(arxiv_oai, "_fetch", return_value=page(token="repeated"))
    def test_repeated_pagination_token_fails(self, fetch, sleep):
        with tempfile.TemporaryDirectory() as directory, patch.object(arxiv_oai, "CONFIG", replace(arxiv_oai.CONFIG, memory_dir=Path(directory))):
            with self.assertRaisesRegex(RuntimeError, "Repeated"):
                arxiv_oai.harvest_since("2026-09-22", lambda text: True)
