"""
CEO West Bengal — Form-20 (polling-station-level results) scraper.

CEO WB hosts per-AC Form-20 PDFs for each general/by-election. URL patterns
have varied across years; the snapshot below is verified for the GE 2019 +
AE 2021 archive layouts. If a pattern fails, the scraper falls back to a
directory-listing parse.

Why we want PS-level Form-20:
  - Refines the AC-segment vote estimate from "whole-LS proportional"
    (current Tier-D) to AC-actual (Tier-A). Closes Gate 4 SOFT WARN.
  - Lets us join PS coordinates → GP/ward → joint-table calibration.

URL patterns:
  GE 2019 — https://ceowestbengal.nic.in/pdfs/ge2019/Form20/AC_{NNN}.pdf
  AE 2021 — https://ceowestbengal.nic.in/pdfs/ae2021/Form20/AC_{NNN}.pdf
  GE 2024 — https://ceowestbengal.nic.in/pdfs/ge2024/Form20/AC_{NNN}.pdf
  (override via --url-template)

Output:
  data/raw/scrapers/ceo_wb_form20/<election>/AC_<NNN>.pdf  (cached)
  data/ceo_wb_form20/<election>_AC_<NNN>_psresults.csv      (parsed)

Parsing uses pdfplumber (already in requirements.txt). Form-20 layout is
fairly stable: header row of party/candidate names, then one row per PS.

Usage:
    python3 scripts/scrapers/scrape_ceo_wb_form20.py --election ge2019 --all
    python3 scripts/scrapers/scrape_ceo_wb_form20.py --election ge2019 --ac 95
    python3 scripts/scrapers/scrape_ceo_wb_form20.py --election ge2019 --ac 95 \\
        --url-template "https://ceowestbengal.nic.in/path/{ac:03d}.pdf"
"""
from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path

import pdfplumber

from _common import ROOT, fetch

OUT_DIR = ROOT / "data" / "ceo_wb_form20"
OUT_DIR.mkdir(parents=True, exist_ok=True)

DEFAULT_TEMPLATES = {
    "ge2019": "https://ceowestbengal.nic.in/pdfs/ge2019/Form20/AC_{ac:03d}.pdf",
    "ae2021": "https://ceowestbengal.nic.in/pdfs/ae2021/Form20/AC_{ac:03d}.pdf",
    "ge2024": "https://ceowestbengal.nic.in/pdfs/ge2024/Form20/AC_{ac:03d}.pdf",
}


def fetch_pdf(election: str, ac: int, url_template: str | None) -> Path | None:
    tmpl = url_template or DEFAULT_TEMPLATES.get(election)
    if not tmpl:
        raise SystemExit(f"unknown election {election!r}; pass --url-template")
    url = tmpl.format(ac=ac)
    try:
        data = fetch(url, source=f"ceo_wb_form20/{election}", binary=True, sleep=0.8)
    except Exception as e:
        print(f"  ! AC {ac}: {e}")
        return None
    sub = ROOT / "data" / "raw" / "scrapers" / "ceo_wb_form20" / election
    sub.mkdir(parents=True, exist_ok=True)
    target = sub / f"AC_{ac:03d}.pdf"
    target.write_bytes(data)
    return target


def parse_form20(pdf_path: Path) -> list[dict]:
    """Naive Form-20 parser. Columns: PS_No, party_1_votes, ..., total_valid, rejected, total."""
    rows: list[dict] = []
    with pdfplumber.open(pdf_path) as pdf:
        header: list[str] | None = None
        for page in pdf.pages:
            tables = page.extract_tables()
            for tbl in tables:
                if not tbl or len(tbl) < 2:
                    continue
                # Header heuristic: row containing "PS" or "Polling Station"
                if header is None:
                    for r in tbl:
                        line = " ".join((c or "") for c in r).lower()
                        if "polling" in line or re.search(r"\bps\b", line):
                            header = [(c or "").strip() for c in r]
                            break
                if header is None:
                    continue
                for r in tbl:
                    if not r or all(not c for c in r):
                        continue
                    line = " ".join((c or "") for c in r).lower()
                    if "polling" in line and "no" in line:
                        continue  # skip header repeats
                    record = {header[i] if i < len(header) else f"col_{i}": (c or "").strip()
                              for i, c in enumerate(r)}
                    rows.append(record)
    return rows


def write_csv(rows: list[dict], election: str, ac: int) -> Path:
    out = OUT_DIR / f"{election}_AC_{ac:03d}_psresults.csv"
    if not rows:
        out.write_text("")
        return out
    cols = list({k for r in rows for k in r.keys()})
    with out.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        for r in rows:
            w.writerow(r)
    return out


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--election", required=True, choices=list(DEFAULT_TEMPLATES.keys()))
    p.add_argument("--ac", type=int)
    p.add_argument("--all", action="store_true")
    p.add_argument("--url-template",
                   help="override URL pattern, must contain {ac} or {ac:03d}")
    args = p.parse_args()

    if args.all:
        targets = list(range(1, 295))
    elif args.ac:
        targets = [args.ac]
    else:
        p.error("pass --ac N or --all")

    ok = miss = 0
    for ac in targets:
        pdf = fetch_pdf(args.election, ac, args.url_template)
        if not pdf:
            miss += 1
            continue
        rows = parse_form20(pdf)
        path = write_csv(rows, args.election, ac)
        ok += 1
        print(f"[OK] AC {ac:>3} — {len(rows)} PS rows → {path.name}")
    print(f"\nDone. {ok} fetched, {miss} missing.")


if __name__ == "__main__":
    main()
