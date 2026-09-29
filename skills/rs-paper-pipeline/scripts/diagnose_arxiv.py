"""Read-only arXiv connectivity diagnostics; never sends application credentials."""
import subprocess
import time
import urllib.parse

from clients.arxiv_client import CONFIG, RS_QUERY_TERMS


def main():
    terms = " OR ".join(f'all:"{term}"' if " " in term else f"all:{term}" for term in RS_QUERY_TERMS)
    queries = ["all:remote", f"({terms}) AND submittedDate:[202609230000 TO 202609232359]"]
    for host in ["export.arxiv.org", "arxiv.org"]:
        for query in queries:
            url = f"https://{host}/api/query?" + urllib.parse.urlencode({
                "search_query": query, "start": 0, "max_results": 1,
                "sortBy": "submittedDate", "sortOrder": "descending",
            })
            print(f"PROBE {url}", flush=True)
            result = subprocess.run([
                "curl", "-sS", "-i", "-L", "--connect-timeout", "10", "--max-time", "25",
                "-A", CONFIG.arxiv_user_agent,
                "-H", "Accept: application/atom+xml, application/xml;q=0.9, */*;q=0.8", url,
            ], capture_output=True, text=True)
            print(result.stdout[:5000], result.stderr[:1000], flush=True)
            time.sleep(4)


if __name__ == "__main__":
    main()
