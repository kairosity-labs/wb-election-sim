#!/usr/bin/env python3
"""
build_constituencies_csv.py — the merger.

Reads every canonical `data/raw/*.csv` produced by the scrapers/parsers, joins
them on `ac_no` against the scaffold in `data/constituencies.csv`, and writes
back with the appropriate confidence tier per source (§1 of methodology.md).

Sources currently wired in:
  - data/raw/ceo_wb_sir2026_electorate.csv  (tier A)
      → total_electors_2026, male_electors, female_electors

Future sources (wire in as scrapers land):
  - data/raw/secc2011_bpl_block.csv         (tier B → bpl_household_pct_secc)
  - data/raw/mgnrega_block.csv              (tier B → mgnrega_worker_share_pct)
  - data/raw/swasthya_sathi_block.csv       (tier B → swasthya_sathi_coverage_pct_est)
  - data/raw/census2011_ac.csv              (tier A → religion, SC/ST, literacy, language)

Design:
  - Sources are additive — a cell only gets overwritten if the new source is
    a higher tier than what's already in the cell (A > B > C > D > E).
  - Rows without a matching source retain their existing value (which might
    have been manually set, e.g. the pilot profile's tier-E imputations).
  - Provenance (`sources_json`) accumulates a list of {field, source, tier}.

Run:
    python3 scripts/build_constituencies_csv.py
"""
from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MAIN_CSV = ROOT / "data" / "constituencies.csv"
RAW = ROOT / "data" / "raw"

TIER_ORDER = {"A": 5, "B": 4, "C": 3, "D": 2, "E": 1, "": 0}


def tier_beats(new: str, existing: str) -> bool:
    """True if `new` tier is strictly higher-confidence than `existing`."""
    return TIER_ORDER.get(new, 0) > TIER_ORDER.get(existing, 0)


# ---------------------------------------------------------------------------
# Source definitions: each entry maps a raw-CSV column to a main-CSV column,
# with the tier assigned to values from that source. The raw-CSV file itself
# must have `ac_no` as a join key.
# ---------------------------------------------------------------------------
SOURCES: list[dict] = [
    {
        "name": "ceo_wb_sir2026",
        "path": RAW / "ceo_wb_sir2026_electorate.csv",
        "url": "https://ceowestbengal.wb.gov.in/Downloads/SIR2026/AC%20wise%20Draft%20Elector%20SIR%202026.pdf",
        "tier": "A",
        "column_map": {
            "total_electors": "total_electors_2026",
            "male_electors": "male_electors",
            "female_electors": "female_electors",
        },
    },
    {
        # District-level Census 2011 rollup to AC. Tier E per methodology §4:
        # "district-share × uniform within-district distribution" imputation.
        # Pilot ACs (e.g. AC 95) already carry tier-E CDB-level values that
        # are more specific than this rollup; tier_beats(E, E) = False so
        # those pilot values are preserved.
        "name": "census2011_wb_district_rollup",
        "path": RAW / "census2011_wb_ac_district_rollup.csv",
        "url": "https://en.wikipedia.org/wiki/(23 WB district pages; see data/sources.md §B)",
        "tier": "E",
        "column_map": {
            "sc_pct": "sc_total_pct",
            "st_pct": "st_total_pct",
            "hindu_pct": "hindu_pct",
            "muslim_pct": "muslim_pct",
            "christian_pct": "christian_pct",
            "other_religion_pct": "other_religion_pct",
            "literacy_rate_overall_pct": "literacy_overall_pct",
            "literacy_rate_male_pct": "literacy_male_pct",
            "literacy_rate_female_pct": "literacy_female_pct",
            "bengali_pct": "bengali_pct",
            "hindi_pct": "hindi_pct",
            "santhali_pct": "santhali_pct",
            "urdu_pct": "urdu_pct",
            "nepali_pct": "nepali_pct",
        },
    },
    # New sources append here as they land.
]


def load_raw(path: Path) -> dict[int, dict]:
    if not path.exists():
        return {}
    with path.open() as f:
        return {int(r["ac_no"]): r for r in csv.DictReader(f)}


def main() -> None:
    # Load main CSV.
    with MAIN_CSV.open() as f:
        reader = csv.reader(f)
        rows = list(reader)
    header = rows[0]
    name_to_idx = {c: i for i, c in enumerate(header)}

    # Load provenance once per row.
    provenance_idx = name_to_idx["sources_json"]
    provenance: dict[int, list] = {}
    for r in rows[1:]:
        ac_no = int(r[name_to_idx["ac_no"]])
        existing = r[provenance_idx]
        try:
            provenance[ac_no] = json.loads(existing) if existing else []
        except json.JSONDecodeError:
            provenance[ac_no] = []

    # Apply each source.
    updates = 0
    for src in SOURCES:
        raw_map = load_raw(src["path"])
        if not raw_map:
            print(f"SKIP {src['name']}: {src['path']} not found")
            continue
        applied = 0
        for r in rows[1:]:
            ac_no = int(r[name_to_idx["ac_no"]])
            raw = raw_map.get(ac_no)
            if not raw:
                continue
            for raw_col, main_col in src["column_map"].items():
                if main_col not in name_to_idx:
                    raise KeyError(f"{main_col} not in main CSV header")
                value = raw.get(raw_col, "")
                if value == "" or value is None:
                    continue
                conf_col = f"{main_col}_conf"
                existing_tier = r[name_to_idx[conf_col]] if conf_col in name_to_idx else ""
                if tier_beats(src["tier"], existing_tier):
                    r[name_to_idx[main_col]] = str(value)
                    if conf_col in name_to_idx:
                        r[name_to_idx[conf_col]] = src["tier"]
                    provenance[ac_no].append({
                        "field": main_col,
                        "source": src["name"],
                        "url": src["url"],
                        "tier": src["tier"],
                    })
                    applied += 1
        print(f"{src['name']:30s} tier {src['tier']}: applied {applied} cell updates")
        updates += applied

    # Dedup + write provenance.
    for r in rows[1:]:
        ac_no = int(r[name_to_idx["ac_no"]])
        # Dedup by (field, source) keeping last.
        seen: dict[tuple[str, str], dict] = {}
        for p in provenance.get(ac_no, []):
            if not isinstance(p, dict):
                continue
            seen[(p.get("field", ""), p.get("source", ""))] = p
        r[provenance_idx] = json.dumps(list(seen.values())) if seen else ""

    with MAIN_CSV.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerows(rows)

    print(f"Total cell updates: {updates}")
    print(f"Wrote {MAIN_CSV}")


if __name__ == "__main__":
    main()
