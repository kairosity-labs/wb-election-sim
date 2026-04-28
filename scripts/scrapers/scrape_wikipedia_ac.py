"""
Wikipedia AC + LS infobox scraper.

Pulls per-AC pages (Vidhan Sabha constituency) and rolled-up LS pages,
extracts:
  - Reservation status, district, LS parent
  - Historical results table (year, winner, party, %, runner-up, %, margin)
  - Demographic infobox if present (electorate, polling stations)

Output: data/wikipedia/<ac_no>_<slug>.json (one JSON per AC) +
        data/wikipedia/wb_ac_history_long.csv (one row per AC×year×candidate)

Usage:
    python3 scripts/scrapers/scrape_wikipedia_ac.py --all
    python3 scripts/scrapers/scrape_wikipedia_ac.py --ac 95
    python3 scripts/scrapers/scrape_wikipedia_ac.py --slug Bangaon_Uttar
"""
from __future__ import annotations

import argparse
import csv
import json
import re
from pathlib import Path

from bs4 import BeautifulSoup

from _common import ROOT, fetch

OUT_DIR = ROOT / "data" / "wikipedia"
OUT_DIR.mkdir(parents=True, exist_ok=True)

# Page URL patterns to try in order. Wikipedia has inconsistent slug suffixes.
URL_PATTERNS = [
    "https://en.wikipedia.org/wiki/{slug}_(Vidhan_Sabha_constituency)",
    "https://en.wikipedia.org/wiki/{slug}_Assembly_constituency",
    "https://en.wikipedia.org/wiki/{slug}_(Assembly_constituency)",
    "https://en.wikipedia.org/wiki/{slug}",
]


def fetch_ac_page(slug: str) -> tuple[str, str] | None:
    """Try URL patterns in order; return (resolved_url, html) on first 200."""
    for pat in URL_PATTERNS:
        url = pat.format(slug=slug)
        try:
            html = fetch(url, source="wikipedia")
            # Wikipedia "page does not exist" returns 200 with a "noarticletext" div
            if 'class="noarticletext"' in html:
                continue
            return url, html
        except Exception:
            continue
    return None


def parse_infobox(soup: BeautifulSoup) -> dict:
    """Extract infobox fields → {label: value}."""
    box = soup.find("table", class_=re.compile(r"\binfobox\b"))
    out: dict[str, str] = {}
    if not box:
        return out
    for row in box.find_all("tr"):
        th, td = row.find("th"), row.find("td")
        if not th or not td:
            continue
        label = th.get_text(" ", strip=True)
        val = td.get_text(" ", strip=True)
        out[label] = val
    return out


def parse_results_tables(soup: BeautifulSoup) -> list[dict]:
    """Extract election-results tables: rows like Year | Party | Candidate | Votes | %.
    Wikipedia's election-result tables vary; we capture liberally and tag by table caption."""
    rows: list[dict] = []
    for tbl in soup.find_all("table", class_=re.compile(r"\bwikitable\b")):
        caption = tbl.find("caption")
        cap_text = caption.get_text(" ", strip=True) if caption else ""
        # Header
        header = [th.get_text(" ", strip=True) for th in tbl.find_all("th", recursive=False)] or \
                 [th.get_text(" ", strip=True) for th in (tbl.find("tr").find_all("th") if tbl.find("tr") else [])]
        if not header:
            continue
        for tr in tbl.find_all("tr")[1:]:
            tds = [td.get_text(" ", strip=True) for td in tr.find_all(["td", "th"])]
            if len(tds) < 3:
                continue
            row = {"_caption": cap_text}
            for i, val in enumerate(tds):
                col = header[i] if i < len(header) else f"col_{i}"
                row[col] = val
            rows.append(row)
    return rows


def scrape_one(ac_no: int, slug: str) -> dict | None:
    fetched = fetch_ac_page(slug)
    if not fetched:
        return None
    url, html = fetched
    soup = BeautifulSoup(html, "html.parser")
    title = soup.find("h1", id="firstHeading")
    record = {
        "ac_no": ac_no,
        "slug": slug,
        "resolved_url": url,
        "title": title.get_text(strip=True) if title else None,
        "infobox": parse_infobox(soup),
        "result_tables": parse_results_tables(soup),
    }
    out = OUT_DIR / f"{ac_no:03d}_{slug.lower()}.json"
    out.write_text(json.dumps(record, indent=2, ensure_ascii=False))
    return record


def emit_long_csv(records: list[dict]) -> None:
    """Flatten result tables into a long CSV: ac_no, slug, year, party, candidate, votes, pct."""
    out = OUT_DIR / "wb_ac_history_long.csv"
    fieldnames = ["ac_no", "slug", "year", "party", "candidate", "votes", "pct", "raw_caption"]
    with out.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for rec in records:
            for row in rec.get("result_tables", []):
                year = next((row[k] for k in row if "year" in k.lower()), "")
                party = next((row[k] for k in row if "party" in k.lower()), "")
                cand = next((row[k] for k in row if "candidate" in k.lower() or "name" in k.lower()), "")
                votes = next((row[k] for k in row if "vote" in k.lower()), "")
                pct = next((row[k] for k in row if "%" in k or "percent" in k.lower()), "")
                if not (year or party or cand):
                    continue
                w.writerow({
                    "ac_no": rec["ac_no"], "slug": rec["slug"], "year": year,
                    "party": party, "candidate": cand, "votes": votes, "pct": pct,
                    "raw_caption": row.get("_caption", ""),
                })


def load_ac_list() -> list[tuple[int, str]]:
    """Read 294-AC master so we know every (ac_no, slug)."""
    master = ROOT / "data" / "master" / "wb_ac_master_v3.csv"
    if not master.exists():
        master = ROOT / "data" / "master" / "wb_ac_master.csv"
    out: list[tuple[int, str]] = []
    with master.open() as f:
        for row in csv.DictReader(f):
            ac_no = int(row.get("ac_no") or row.get("AC_No") or row.get("ac_number"))
            name = row.get("ac_name") or row.get("AC_Name") or row.get("name")
            slug = name.replace(" ", "_").replace("-", "_")
            out.append((ac_no, slug))
    return out


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--all", action="store_true")
    p.add_argument("--ac", type=int)
    p.add_argument("--slug")
    args = p.parse_args()

    if args.ac and args.slug:
        targets = [(args.ac, args.slug)]
    elif args.ac:
        all_acs = load_ac_list()
        targets = [(n, s) for n, s in all_acs if n == args.ac]
    elif args.all:
        targets = load_ac_list()
    else:
        p.error("pass --all, --ac N, or --ac N --slug Foo_Bar")

    records = []
    for ac_no, slug in targets:
        rec = scrape_one(ac_no, slug)
        status = "OK" if rec else "MISS"
        print(f"[{status}] AC {ac_no:>3} — {slug}")
        if rec:
            records.append(rec)
    if records:
        emit_long_csv(records)
        print(f"\nWrote {len(records)} records to {OUT_DIR}/")


if __name__ == "__main__":
    main()
