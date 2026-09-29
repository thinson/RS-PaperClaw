"""Read-only arXiv connectivity diagnostics; never sends application credentials."""
import subprocess
import time
import urllib.parse
from datetime import datetime, timedelta, timezone

from clients.arxiv_client import CONFIG, RS_QUERY_TERMS


def main():
    terms = " OR ".join(f'all:"{term}"' if " " in term else f"all:{term}" for term in RS_QUERY_TERMS)
    date = (datetime.now(timezone.utc) - timedelta(days=1)).strftime("%Y%m%d")
    queries = ["all:remote", f"({terms}) AND submittedDate:[{date}0000 TO {date}2359]"]
    failed = False
    for host in ["export.arxiv.org", "arxiv.org"]:
        for query in queries:
            url = f"https://{host}/api/query?" + urllib.parse.urlencode({
                "search_query": query, "start": 0, "max_results": 1,
                "sortBy": "submittedDate", "sortOrder": "descending",
            })
            print(f"PROBE {url}", flush=True)
            result = subprocess.run([
                "curl", "-sS", "-i", "-L", "--connect-timeout", "10", "--max-time", "25",
                "--write-out", "\nRS_HTTP_STATUS:%{http_code}",
                "-A", CONFIG.arxiv_user_agent,
                "-H", "Accept: application/atom+xml, application/xml;q=0.9, */*;q=0.8", url,
            ], capture_output=True, text=True)
            print(result.stdout[:5000], result.stderr[:1000], flush=True)
            status = result.stdout.rpartition("\nRS_HTTP_STATUS:")[2].strip()
            if status in {"429", "503"}:
                print("Upstream rate limited or unavailable; stopping diagnostics.", flush=True)
                return 1
            failed = failed or result.returncode != 0 or status != "200"
            time.sleep(4)
    return int(failed)


if __name__ == "__main__":
    raise SystemExit(main())
