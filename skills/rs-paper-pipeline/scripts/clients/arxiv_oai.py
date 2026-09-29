"""Official OAI-PMH metadata source for recent submission recovery.

OAI datestamps are modification dates. Harvest from the earliest requested day
through the present, then filter on the original created date, never datestamp.
Only complete harvests are cached; partial pages must not become empty reports.
"""
from datetime import datetime, timezone
import gzip
import json
from pathlib import Path
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

from pipeline_config import load_config

CONFIG = load_config()
BASE = "https://oaipmh.arxiv.org/oai"
NS = {"o": "http://www.openarchives.org/OAI/2.0/", "a": "http://arxiv.org/OAI/arXiv/"}


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
            if getattr(exc, "code", None) in (429, 503) or attempt == 2:
                raise
            time.sleep(10 * (attempt + 1))


def harvest_since(start: str, signal_match):
    cache = CONFIG.memory_dir / "arxiv_oai_recent.json"
    now = datetime.now(timezone.utc)
    if cache.exists():
        try:
            saved = json.loads(cache.read_text(encoding="utf-8"))
            age = now.timestamp() - saved["fetched_at"]
            if saved["from"] <= start and 0 <= age < 21600:
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
    result = list(items.values())
    cache.parent.mkdir(parents=True, exist_ok=True)
    temporary = cache.with_suffix(".tmp")
    temporary.write_text(json.dumps({"from": start, "fetched_at": now.timestamp(), "items": result}, ensure_ascii=False), encoding="utf-8")
    temporary.replace(cache)
    return result


def cached_metadata(arxiv_id):
    cache = CONFIG.memory_dir / "arxiv_oai_recent.json"
    if not cache.exists():
        return None
    data = json.loads(cache.read_text(encoding="utf-8"))
    if time.time() - data["fetched_at"] >= 21600:
        return None
    base_id = arxiv_id.split("v")[0]
    return next((item for item in data["items"] if item["arxiv_id"] == base_id), None)
