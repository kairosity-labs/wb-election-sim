#!/usr/bin/env python3
"""
One-off: populate row for AC 95 (Bangaon Uttar) in data/constituencies.csv.

Rationale: the pilot profile /constituencies/095_bangaon_uttar.md is the
source of truth for the values + tiers. This script propagates them to the
machine-readable CSV so the SCM can read the same row. Rerunnable.

NOT part of the production pipeline — will be superseded by
scripts/build_constituencies_csv.py in Step 4. Kept for audit trail.
"""
from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CSV_PATH = ROOT / "data" / "constituencies.csv"

# (value, confidence_tier) for every column we have a defensible value for.
# Blank cells (None) are intentional — per methodology §6 they stay null until
# a scraper provides a measurement. Downstream SCM should handle missingness.
AC_95_VALUES: dict[str, tuple[object, str] | None] = {
    # Identity already present from bootstrap; re-assert for safety.
    "region_label": ("Presidency / Matua Belt", "E"),
    # Electorate
    "total_electors_2026": (241337, "A"),
    "male_electors": (124052, "A"),
    "female_electors": (117260, "A"),
    "sir_deletion_count_est": (34109, "D"),
    "sir_deletion_pct_est": (12.4, "E"),
    # Religion (imputed from Bangaon sub-division, Census 2011)
    "hindu_pct": (85.6, "E"),
    "muslim_pct": (13.7, "E"),
    "christian_pct": (0.3, "E"),
    "sarna_orp_pct": (0.0, "E"),
    "other_religion_pct": (0.4, "E"),
    # Caste — SC
    "sc_total_pct": (46.0, "E"),
    "namasudra_matua_pct_est": (40.0, "E"),
    "rajbanshi_pct_est": (0.5, "E"),
    "bagdi_pct_est": (2.0, "E"),
    "poundra_pct_est": (1.0, "E"),
    "other_sc_pct_est": (2.5, "E"),
    # Caste — ST
    "st_total_pct": (3.6, "E"),
    "santhal_pct_est": None,
    "oraon_pct_est": None,
    "munda_pct_est": None,
    "bhumij_pct_est": None,
    "other_st_pct_est": (3.6, "E"),
    # Caste — UC / OBC
    "uc_bhadralok_pct_est": (10.0, "E"),
    "obc_mahishya_pct_est": None,
    "obc_sadgop_pct_est": None,
    "obc_kurmi_pct_est": None,
    "obc_teli_pct_est": None,
    "obc_other_pct_est": (22.0, "E"),
    # Language — sum to 100 (Bangaon CDB: Bengali 99.19% Census 2011 A).
    "bengali_pct": (99.0, "E"),
    "hindi_pct": (0.5, "E"),
    "santhali_pct": (0.0, "E"),
    "urdu_pct": (0.3, "E"),
    "nepali_pct": (0.0, "E"),
    "rajbanshi_lang_pct": (0.0, "E"),
    "kurmali_pct": (0.0, "E"),
    "other_lang_pct": (0.2, "E"),
    # Income / poverty — blanks pending scrapers
    "bpl_household_pct_secc": None,
    "mgnrega_worker_share_pct": None,
    "per_capita_income_band_est": (3, "D"),
    "agri_hh_pct": (55.0, "E"),
    "out_migrant_worker_pct_est": (11.0, "D"),
    # Education
    "literacy_overall_pct": (80.6, "E"),
    "literacy_male_pct": (84.3, "E"),
    "literacy_female_pct": (74.8, "E"),
    "graduate_plus_pct_est": (8.0, "E"),
    "unemployed_educated_youth_est": (18.0, "D"),
    # Occupation
    "cultivator_pct": (20.0, "E"),
    "ag_labourer_pct": (30.0, "E"),
    "tea_worker_pct_est": (0.0, "E"),
    "fishworker_pct_est": (2.0, "E"),
    "industrial_pct_est": (5.0, "E"),
    "govt_employee_pct_est": (5.0, "E"),
    "informal_sector_pct_est": (25.0, "E"),
    # Welfare schemes
    "lakshmir_bhandar_beneficiaries_est": (60000, "E"),
    "krishak_bandhu_beneficiaries_est": (17500, "E"),
    "swasthya_sathi_coverage_pct_est": (92.0, "E"),
    "khadya_sathi_coverage_pct_est": (87.0, "E"),
    "kanyashree_coverage_pct_est": (85.0, "E"),
    "old_age_widow_pension_est": (10000, "E"),
}

# Provenance: point to the MD profile which carries the full URL list. A
# compact JSON array keeps the CSV cell small while preserving traceability.
SOURCES_JSON = json.dumps([
    {"ref": "see /constituencies/095_bangaon_uttar.md §8 for full URL list",
     "tier_range": "A-E",
     "accessed": "2026-04-24"},
])


def main() -> None:
    with CSV_PATH.open() as f:
        reader = csv.reader(f)
        rows = list(reader)

    header = rows[0]
    name_to_idx = {c: i for i, c in enumerate(header)}

    # Locate AC 95
    target = None
    for i, row in enumerate(rows[1:], start=1):
        if row[name_to_idx["ac_no"]] == "95":
            target = i
            break
    if target is None:
        raise SystemExit("AC 95 row not found")

    row = rows[target]
    for col, spec in AC_95_VALUES.items():
        if col not in name_to_idx:
            raise KeyError(f"column {col!r} not in header")
        if spec is None:
            # Leave blank — also blank the conf column.
            row[name_to_idx[col]] = ""
            conf_col = f"{col}_conf"
            if conf_col in name_to_idx:
                row[name_to_idx[conf_col]] = ""
            continue
        value, tier = spec
        row[name_to_idx[col]] = str(value)
        conf_col = f"{col}_conf"
        if conf_col in name_to_idx:
            row[name_to_idx[conf_col]] = tier

    row[name_to_idx["sources_json"]] = SOURCES_JSON
    rows[target] = row

    with CSV_PATH.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerows(rows)

    populated = sum(1 for v in AC_95_VALUES.values() if v is not None)
    print(f"AC 95 Bangaon Uttar: {populated}/{len(AC_95_VALUES)} cells populated")


if __name__ == "__main__":
    main()
