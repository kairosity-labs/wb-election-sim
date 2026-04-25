#!/usr/bin/env python3
"""
parse_ceo_wb_sir_pdf.py
Parse CEO West Bengal's AC-wise SIR 2026 Draft Elector PDF into a canonical CSV.

Source PDF:
  https://ceowestbengal.wb.gov.in/Downloads/SIR2026/AC%20wise%20Draft%20Elector%20SIR%202026.pdf
  (cached at data/raw/pdfs/ceo_wb_sir2026_ac_wise.pdf)

Output:
  data/raw/ceo_wb_sir2026_electorate.csv with columns:
    ac_no, ac_name_pdf, district_pdf, polling_stations,
    male_electors, female_electors, third_gender_electors, total_electors

Tier A. This is the tier-A electorate source used by build_constituencies_csv.py
to populate total_electors_2026 / male_electors / female_electors for all 294 ACs.

Run:
    python3 scripts/parse_ceo_wb_sir_pdf.py
"""
from __future__ import annotations

import csv
import re
from pathlib import Path

import pdfplumber

ROOT = Path(__file__).resolve().parent.parent
PDF = ROOT / "data" / "raw" / "pdfs" / "ceo_wb_sir2026_ac_wise.pdf"
OUT = ROOT / "data" / "raw" / "ceo_wb_sir2026_electorate.csv"


def _clean_int(s: str | None) -> int | None:
    if s is None:
        return None
    s = s.strip().replace(",", "")
    if not s:
        return None
    return int(s)


def main() -> None:
    rows: list[dict] = []
    with pdfplumber.open(PDF) as pdf:
        for page in pdf.pages:
            tables = page.extract_tables()
            if not tables:
                continue
            for t in tables:
                for row in t:
                    # Skip header rows; data rows have int-parseable AC no in col 1.
                    if not row or len(row) < 8:
                        continue
                    ac_no_raw = (row[1] or "").strip()
                    if not re.fullmatch(r"\d{1,3}", ac_no_raw):
                        continue
                    ac_no = int(ac_no_raw)
                    if not 1 <= ac_no <= 294:
                        continue
                    rows.append({
                        "ac_no": ac_no,
                        "ac_name_pdf": (row[2] or "").strip(),
                        "district_pdf": (row[0] or "").strip(),
                        "polling_stations": _clean_int(row[3]),
                        "male_electors": _clean_int(row[4]),
                        "female_electors": _clean_int(row[5]),
                        "third_gender_electors": _clean_int(row[6]),
                        "total_electors": _clean_int(row[7]),
                    })

    # Dedup + sort.
    seen: set[int] = set()
    deduped: list[dict] = []
    for r in sorted(rows, key=lambda x: x["ac_no"]):
        if r["ac_no"] in seen:
            continue
        seen.add(r["ac_no"])
        deduped.append(r)

    # Validate: expect 294 rows.
    if len(deduped) != 294:
        got = sorted(seen)
        missing = [n for n in range(1, 295) if n not in seen]
        raise SystemExit(
            f"Expected 294 AC rows, got {len(deduped)}. "
            f"Missing: {missing[:20]}{'...' if len(missing) > 20 else ''}"
        )

    # Validate: male+female+TG = total per row (allow ±0 exact).
    mismatches: list[tuple[int, int, int]] = []
    for r in deduped:
        s = (r["male_electors"] or 0) + (r["female_electors"] or 0) + (r["third_gender_electors"] or 0)
        if s != r["total_electors"]:
            mismatches.append((r["ac_no"], s, r["total_electors"]))
    if mismatches:
        print(f"WARNING: {len(mismatches)} rows with M+F+TG != Total:")
        for ac_no, s, tot in mismatches[:10]:
            print(f"  AC {ac_no}: {s} vs {tot}")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(deduped[0].keys()))
        w.writeheader()
        w.writerows(deduped)

    print(f"Wrote {OUT} — {len(deduped)} rows")
    total_electors = sum(r["total_electors"] for r in deduped if r["total_electors"])
    total_m = sum(r["male_electors"] for r in deduped if r["male_electors"])
    total_f = sum(r["female_electors"] for r in deduped if r["female_electors"])
    total_tg = sum(r["third_gender_electors"] for r in deduped if r["third_gender_electors"] is not None)
    print(f"Totals: {total_electors:,} electors ({total_m:,} M / {total_f:,} F / {total_tg:,} TG)")


if __name__ == "__main__":
    main()
