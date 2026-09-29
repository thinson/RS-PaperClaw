"""Official OAI-PMH metadata source for recent submission recovery.

OAI datestamps are modification dates. Harvest from the earliest requested day
through the present, then filter on arXivRaw v1 dates, never created/datestamp.
Only complete harvests are cached; partial pages must not become empty reports.
"""
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
import gzip
from http.client import IncompleteRead
import json
import subprocess
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from urllib.error import HTTPError

from pipeline_config import load_config

CONFIG = load_config()
BASE = "https://oaipmh.arxiv.org/oai"
NS = {"o": "http://www.openarchives.org/OAI/2.0/", "a": "http://arxiv.org/OAI/arXiv/",
      "r": "http://arxiv.org/OAI/arXivRaw/"}


def parse_original_dates(xml):
    root = ET.fromstring(xml)
    error = root.find("o:error", NS)
    if error is not None and error.get("code") == "noRecordsMatch":
        return {}, ""
    if root.find("o:ListRecords", NS) is None or error is not None:
        raise RuntimeError("Invalid OAI version-history response")
    dates = {}
    for record in root.findall("o:ListRecords/o:record", NS):
        header = record.find("o:header", NS)
        if header is not None and header.get("status") == "deleted":
            continue
        node = record.find("o:metadata/r:arXivRaw", NS)
        if node is None:
            raise RuntimeError("Missing OAI version history")
        aid = node.findtext("r:id", namespaces=NS)
        first = node.find("r:version[@version='v1']/r:date", NS)
        if not aid or first is None or not first.text:
            raise RuntimeError(f"Missing original submission date: {aid}")
        dates[aid] = parsedate_to_datetime(first.text).astimezone(timezone.utc).date().isoformat()
    return dates, (root.findtext("o:ListRecords/o:resumptionToken", default="", namespaces=NS) or "").strip()


def parse_page(xml):
    root = ET.fromstring(xml)
    if root.tag != f"{{{NS['o']}}}OAI-PMH":
        raise RuntimeError("Unexpected OAI response (not OAI-PMH XML)")
    error = root.find("o:error", NS)
    if error is not None:
        if error.get("code") == "noRecordsMatch":
            return [], ""
        raise RuntimeError(f"OAI error {error.get('code')}: {error.text}")
    if root.find("o:ListRecords", NS) is None:
        raise RuntimeError("Missing OAI ListRecords")
    items = []
    for record in root.findall("o:ListRecords/o:record", NS):
        header = record.find("o:header", NS)
        if header is not None and header.get("status") == "deleted":
            continue
        node = record.find("o:metadata/a:arXiv", NS)
        if node is None:
            raise RuntimeError("OAI record missing arXiv metadata")
        def value(name):
            return " ".join((node.findtext(f"a:{name}", default="", namespaces=NS)).split())
        item = {"arxiv_id": value("id"), "title": value("title"),
                "abstract": value("abstract"), "published": value("created"),
                "authors": [], "affiliations": []}
        if not all(item[k] for k in ("arxiv_id", "title", "abstract", "published")):
            raise RuntimeError("Incomplete OAI metadata")
        datetime.strptime(item["published"], "%Y-%m-%d")
        for author in node.findall("a:authors/a:author", NS):
            name = " ".join(filter(None, [author.findtext("a:forenames", namespaces=NS),
                                          author.findtext("a:keyname", namespaces=NS)]))
            if name:
                item["authors"].append(name)
            item["affiliations"].extend(a.text.strip() for a in author.findall("a:affiliation", NS) if a.text)
        items.append(item)
    return items, (root.findtext("o:ListRecords/o:resumptionToken", default="", namespaces=NS) or "").strip()


def _fetch(params):
    url = BASE + "?" + urllib.parse.urlencode(params)
    request = urllib.request.Request(url, headers={"User-Agent": CONFIG.arxiv_user_agent,
                                                   "Accept-Encoding": "gzip"})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(request, timeout=60) as response:
                data = response.read()
                if response.headers.get("Content-Encoding") == "gzip":
                    data = gzip.decompress(data)
            return data
        except Exception as exc:
            if getattr(exc, "code", None) in (429, 503):
                raise
            if getattr(exc, "code", None) == 406 or isinstance(exc, IncompleteRead) or attempt == 2:
                # Some networks reject urllib while the same official request
                # succeeds with curl. Keep compression for multi-MB OAI pages.
                result = subprocess.run([
                    "curl", "--silent", "--show-error", "--compressed", "--location",
                    "--max-time", "60", "--user-agent", CONFIG.arxiv_user_agent,
                    "--write-out", "\nRS_HTTP_STATUS:%{http_code}", url,
                ], capture_output=True, check=False)
                body, marker, status = result.stdout.rpartition(b"\nRS_HTTP_STATUS:")
                if result.returncode == 0 and marker and status.strip() == b"200":
                    return body
                if marker and status.strip() in {b"429", b"503"}:
                    raise HTTPError(url, int(status.strip()), "OAI upstream unavailable", {}, None)
                if result.returncode != 0 and attempt < 2:
                    time.sleep(10 * (attempt + 1))
                    continue
                raise RuntimeError(f"OAI curl failed: HTTP {status.decode(errors='replace').strip()}; "
                                   f"{result.stderr.decode(errors='replace')[:200]}") from exc
            time.sleep(10 * (attempt + 1))


def harvest_since(start: str, signal_match):
    cache = CONFIG.memory_dir / "arxiv_oai_recent.json"
    now = datetime.now(timezone.utc)
    if cache.exists():
        try:
            saved = json.loads(cache.read_text(encoding="utf-8"))
            age = now.timestamp() - saved["fetched_at"]
            if saved.get("schema_version") == 2 and saved["from"] <= start and 0 <= age < 21600:
                return saved["items"]
        except (ValueError, KeyError, TypeError):
            pass
    params = {"verb": "ListRecords", "metadataPrefix": "arXiv", "from": start}
    seen_tokens = set()
    items = {}
    for page in range(200):
        if page:
            time.sleep(4)
        records, token = parse_page(_fetch(params))
        for item in records:
            if item["published"] >= start and signal_match(item["title"] + "\n" + item["abstract"]):
                items[item["arxiv_id"]] = item
        print(f"  [OAI] page={page + 1} records={len(records)} remote_sensing={len(items)} more={bool(token)}", flush=True)
        if not token:
            break
        if token in seen_tokens:
            raise RuntimeError("Repeated OAI pagination token")
        seen_tokens.add(token)
        params = {"verb": "ListRecords", "resumptionToken": token}
    else:
        raise RuntimeError("OAI harvest exceeded 200 pages; refusing partial results")
    # The normal arXiv format's `created` can describe a replacement version.
    # Only arXivRaw v1 history is authoritative for the original submission.
    params = {"verb": "ListRecords", "metadataPrefix": "arXivRaw", "from": start}
    seen_tokens = set()
    original_dates = {}
    for page in range(200):
        time.sleep(4)
        dates, token = parse_original_dates(_fetch(params))
        original_dates.update(dates)
        print(f"  [OAI history] page={page + 1} records={len(dates)} more={bool(token)}", flush=True)
        if not token:
            break
        if token in seen_tokens:
            raise RuntimeError("Repeated OAI history pagination token")
        seen_tokens.add(token)
        params = {"verb": "ListRecords", "resumptionToken": token}
    else:
        raise RuntimeError("OAI version history incomplete")
    result = []
    for aid, item in items.items():
        if aid not in original_dates:
            raise RuntimeError(f"Original submission date unavailable: {aid}")
        item["latest_published"] = item["published"]
        item["published"] = original_dates[aid]
        if item["published"] >= start:
            result.append(item)
    cache.parent.mkdir(parents=True, exist_ok=True)
    temporary = cache.with_suffix(".tmp")
    temporary.write_text(json.dumps({"schema_version": 2, "from": start, "fetched_at": now.timestamp(),
                                    "original_submission_dates": {aid: original_dates[aid] for aid in items},
                                    "items": result}, ensure_ascii=False), encoding="utf-8")
    temporary.replace(cache)
    return result


def cached_metadata(arxiv_id):
    cache = CONFIG.memory_dir / "arxiv_oai_recent.json"
    if not cache.exists():
        return None
    data = json.loads(cache.read_text(encoding="utf-8"))
    if data.get("schema_version") != 2 or time.time() - data["fetched_at"] >= 21600:
        return None
    base_id = arxiv_id.split("v")[0]
    return next((item for item in data["items"] if item["arxiv_id"] == base_id), None)
