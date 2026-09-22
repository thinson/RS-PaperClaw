from pathlib import Path
import io
import sys
import unittest
from unittest.mock import patch
from urllib.error import HTTPError


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from clients import arxiv_client


class ArxivClientTest(unittest.TestCase):
    def test_official_endpoint_candidates_preserve_path(self):
        self.assertEqual(
            arxiv_client._arxiv_api_candidates("https://export.arxiv.org/api/query"),
            [
                "https://export.arxiv.org/api/query",
                "https://arxiv.org/api/query",
            ],
        )

    def test_custom_endpoint_does_not_get_rewritten(self):
        self.assertEqual(
            arxiv_client._arxiv_api_candidates("https://papers.example/api/query"),
            ["https://papers.example/api/query"],
        )

    @patch.object(arxiv_client.time, "sleep")
    @patch.object(arxiv_client.urllib.request, "urlopen")
    def test_406_fails_immediately_and_sends_atom_accept_header(self, urlopen, sleep):
        urlopen.side_effect = HTTPError(
            "https://export.arxiv.org/api/query",
            406,
            "Not Acceptable",
            {},
            io.BytesIO(b"request rejected"),
        )

        with self.assertRaises(HTTPError):
            arxiv_client.fetch_url_with_retry(
                "https://export.arxiv.org/api/query?search_query=all%3ASAR",
                retries=6,
            )

        self.assertEqual(urlopen.call_count, 1)
        sleep.assert_not_called()
        request = urlopen.call_args.args[0]
        self.assertIn("application/atom+xml", request.get_header("Accept"))

    @patch.object(arxiv_client, "fetch_url_with_curl")
    @patch.object(arxiv_client, "fetch_url_with_retry")
    def test_query_falls_back_to_second_official_host_after_406(self, fetch, curl):
        fetch.side_effect = [
            HTTPError(
                "https://export.arxiv.org/api/query",
                406,
                "Not Acceptable",
                {},
                io.BytesIO(b"request rejected"),
            ),
            "<feed />",
        ]

        result = arxiv_client.fetch_query_with_fallback(
            {"search_query": "all:SAR", "start": 0, "max_results": 1}
        )

        self.assertEqual(result, "<feed />")
        self.assertEqual(fetch.call_count, 2)
        curl.assert_not_called()
        self.assertTrue(fetch.call_args_list[0].args[0].startswith("https://export.arxiv.org/"))
        self.assertTrue(fetch.call_args_list[1].args[0].startswith("https://arxiv.org/"))

    @patch.object(arxiv_client, "fetch_url_with_curl", return_value="<feed />")
    @patch.object(arxiv_client, "fetch_url_with_retry")
    def test_query_uses_curl_after_both_urllib_hosts_return_406(self, fetch, curl):
        fetch.side_effect = [
            HTTPError(
                "https://export.arxiv.org/api/query",
                406,
                "Not Acceptable",
                {},
                io.BytesIO(b"request rejected"),
            ),
            HTTPError(
                "https://arxiv.org/api/query",
                406,
                "Not Acceptable",
                {},
                io.BytesIO(b"request rejected"),
            ),
        ]

        result = arxiv_client.fetch_query_with_fallback(
            {"search_query": "all:SAR", "start": 0, "max_results": 1}
        )

        self.assertEqual(result, "<feed />")
        self.assertEqual(fetch.call_count, 2)
        self.assertEqual(curl.call_count, 1)
        self.assertTrue(curl.call_args.args[0].startswith("https://export.arxiv.org/"))


if __name__ == "__main__":
    unittest.main()
