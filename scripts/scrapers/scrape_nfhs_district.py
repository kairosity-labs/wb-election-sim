"""
NFHS-5 (2019-21) district fact-sheet scraper for West Bengal.

Source: rchiips.org/nfhs/factsheet_NFHS-5.shtml lists per-district PDFs.
For WB this is 23 districts; one PDF each (~120 indicators per district).

Why scrape this once:
  - Currently calibrated_2019/ MD files cite NFHS-4 WB rural/urban averages.
    NFHS-5 district-level data lets us upgrade Tier-C estimates to Tier-B
    (district-level direct hard data) — relevant for AMENITIES (C.15)
    and ASSETS (C.14).
  - 23 PDFs covers all 294 ACs via district→AC mapping.

Output:
  data/raw/scrapers/nfhs_5/<district_slug>.pdf
  data/nfhs_5/district_indicators_long.csv  (one row per district × indicator)

PDF structure: NFHS-5 fact sheets use a standard 2-column "Indicator | Total %"
layout, sometimes with Urban/Rural splits. The parser below extracts
(indicator, total_pct, urban_pct, rural_pct) per row.

Usage:
    python3 scripts/scrapers/scrape_nfhs_district.py --all
    python3 scripts/scrapers/scrape_nfhs_district.py --district Murshidabad
"""
from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path

import pdfplumber

from _common import ROOT, fetch

OUT_DIR = ROOT / "data" / "nfhs_5"
OUT_DIR.mkdir(parents=True, exist_ok=True)

# WB districts in NFHS-5 (23, post-2017 split). PDF URLs follow rchiips.org pattern.
# These slugs match the published filenames; override via --url-template if needed.
WB_DISTRICTS = [
    "Alipurduar", "Bankura", "Birbhum", "Cooch_Behar", "Dakshin_Dinajpur",
    "Darjeeling", "Hooghly", "Howrah", "Jalpaiguri", "Jhargram", "Kalimpong",
    "Kolkata", "Malda", "Murshidabad", "Nadia", "North_24_Parganas",
    "Paschim_Bardhaman", "Paschim_Medinipur", "Purba_Bardhaman",
    "Purba_Medinipur", "Purulia", "South_24_Parganas", "Uttar_Dinajpur",
]
URL_TEMPLATE = "http://rchiips.org/nfhs/NFHS-5_FCTS/WB/{district}.pdf"


# Numeric token, optionally with decimal and parentheses (urban/rural %)
NUM = re.compile(r"(\d+\.?\d*)")


def fetch_district(district: str, url_template: str) -> Path | None:
    url = url_template.format(district=district)
    try:
        data = fetch(url, source="nfhs_5", binary=True, sleep=0.8)
    except Exception as e:
        print(f"  ! {district}: {e}")
        return None
    sub = ROOT / "data" / "raw" / "scrapers" / "nfhs_5"
    sub.mkdir(parents=True, exist_ok=True)
    path = sub / f"{district}.pdf"
    path.write_bytes(data)
    return path


def parse_factsheet(pdf_path: Path, district: str) -> list[dict]:
    """Extract (indicator, total, urban, rural) rows from an NFHS-5 PDF."""
    rows: list[dict] = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text() or ""
            for line in text.split("\n"):
                # Indicator lines look like "Adult literacy rate ... 76.1 79.3 74.9"
                # or "Households with electricity ... 99.6 (99.8) (99.5)"
                nums = NUM.findall(line)
                if len(nums) < 1:
                    continue
                # Indicator text = everything before the first number
                m = re.match(r"^(.*?)(?=\s\d)", line.strip())
                if not m:
                    continue
                indicator = m.group(1).strip()
                if len(indicator) < 5:
                    continue
                total = nums[0]
                urban = nums[1] if len(nums) > 1 else ""
                rural = nums[2] if len(nums) > 2 else ""
                rows.append({
                    "district": district,
                    "indicator": indicator,
                    "total_pct": total,
                    "urban_pct": urban,
                    "rural_pct": rural,
                })
    return rows


def emit_long(all_rows: list[dict]) -> None:
    out = OUT_DIR / "district_indicators_long.csv"
    with out.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["district", "indicator", "total_pct", "urban_pct", "rural_pct"])
        w.writeheader()
        w.writerows(all_rows)
    print(f"\nWrote {len(all_rows)} rows → {out}")


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--all", action="store_true")
    p.add_argument("--district")
    p.add_argument("--url-template", default=URL_TEMPLATE)
    args = p.parse_args()

    if args.district:
        targets = [args.district]
    elif args.all:
        targets = WB_DISTRICTS
    else:
        p.error("pass --all or --district Name")

    all_rows: list[dict] = []
    for d in targets:
        pdf = fetch_district(d, args.url_template)
        if not pdf:
            continue
        rows = parse_factsheet(pdf, d)
        print(f"[OK] {d}: {len(rows)} indicators")
        all_rows.extend(rows)
    if all_rows:
        emit_long(all_rows)


if __name__ == "__main__":
    main()
