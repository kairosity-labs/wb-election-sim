"""
Shared helpers for scrapers/*.py.

Conventions:
- Every fetched raw artifact lands under data/raw/scrapers/<source>/.
- Cache by content hash of (url, params) to make reruns idempotent.
- Never commit binary PDFs > 5 MB unless they are in .gitattributes LFS.
- Parsed/derived CSVs land under data/<source>/, NOT data/raw/.
"""
from __future__ import annotations

import hashlib
import json
import time
from pathlib import Path
from typing import Any
from urllib.parse import urlencode

import requests

ROOT = Path(__file__).resolve().parents[2]
RAW_ROOT = ROOT / "data" / "raw" / "scrapers"
RAW_ROOT.mkdir(parents=True, exist_ok=True)

DEFAULT_HEADERS = {
    "User-Agent": "wb-election-sim/0.1 (academic; contact: jajoo@kairosity.ai)",
    "Accept-Language": "en-IN,en;q=0.9",
}


def cache_key(url: str, params: dict[str, Any] | None = None) -> str:
    blob = url + "?" + urlencode(sorted((params or {}).items()))
    return hashlib.sha256(blob.encode()).hexdigest()[:16]


def fetch(
    url: str,
    *,
    source: str,
    params: dict[str, Any] | None = None,
    binary: bool = False,
    sleep: float = 0.5,
    force: bool = False,
) -> bytes | str:
    """Fetch with on-disk cache. Returns bytes (binary=True) or text."""
    sub = RAW_ROOT / source
    sub.mkdir(parents=True, exist_ok=True)
    key = cache_key(url, params)
    suffix = ".bin" if binary else ".txt"
    cached = sub / f"{key}{suffix}"
    meta = sub / f"{key}.meta.json"
    if cached.exists() and not force:
        return cached.read_bytes() if binary else cached.read_text(encoding="utf-8")

    time.sleep(sleep)
    r = requests.get(url, params=params, headers=DEFAULT_HEADERS, timeout=60)
    r.raise_for_status()
    cached.write_bytes(r.content) if binary else cached.write_text(r.text, encoding="utf-8")
    meta.write_text(json.dumps({"url": url, "params": params, "status": r.status_code, "fetched_at": time.time()}))
    return r.content if binary else r.text


def ac_slug(ac_no: int, ac_name: str) -> str:
    """003_cooch_behar_uttar style slug used everywhere in this repo."""
    norm = ac_name.lower().replace("-", "_").replace(" ", "_")
    return f"{ac_no:03d}_{norm}"
