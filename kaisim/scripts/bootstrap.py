#!/usr/bin/env python3
"""
bootstrap.py — one-shot scaffolder.

Reads data/raw/ac_list.csv (the canonical 294 WB Assembly constituency list)
and emits:
  - data/constituencies.csv : full-schema skeleton with identity cols filled,
    every data cell blank, every data cell paired with a *_conf column.
  - constituencies/NNN_<slug>.md : 294 stub profiles with the plan's section
    layout, ready to be filled during the pilot + scale-out passes.

Run:
    python3 scripts/bootstrap.py

Idempotent. Safe to re-run; existing per-AC MD files are NOT overwritten
(so hand-written pilot profiles survive).
"""
from __future__ import annotations

import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
AC_LIST = ROOT / "data" / "raw" / "ac_list.csv"
OUT_CSV = ROOT / "data" / "constituencies.csv"
OUT_MD_DIR = ROOT / "constituencies"


# ---------------------------------------------------------------------------
# Region mapping — coarse 10-group stratification (tier-E modeled label).
# Grounded in DemographicParameters.md §4. Districts map to exactly one region.
# ---------------------------------------------------------------------------
DISTRICT_REGION = {
    "Darjeeling": "North Bengal Hills",
    "Kalimpong": "North Bengal Hills",
    "Cooch Behar": "North Bengal Plains",
    "Alipurduar": "North Bengal Plains",
    "Jalpaiguri": "North Bengal Plains",
    "Uttar Dinajpur": "Border / Muslim-majority North",
    "Dakshin Dinajpur": "Border / Muslim-majority North",
    "Malda": "Border / Muslim-majority North",
    "Murshidabad": "Border / Muslim-majority North",
    "Nadia": "Presidency / Matua Belt",
    "North 24 Parganas": "Presidency / Matua Belt",
    "Kolkata": "Kolkata Metro",
    "Howrah": "Kolkata Metro",
    "Hooghly": "Hooghly / Burdwan Rural",
    "Purba Bardhaman": "Hooghly / Burdwan Rural",
    "Birbhum": "Hooghly / Burdwan Rural",
    "Paschim Bardhaman": "Burdwan Industrial",
    "South 24 Parganas": "South 24 Parganas / Sundarbans",
    "Purba Medinipur": "Purba Medinipur Coast",
    "Paschim Medinipur": "Jangalmahal",
    "Jhargram": "Jangalmahal",
    "Purulia": "Jangalmahal",
    "Bankura": "Jangalmahal",
}


# ---------------------------------------------------------------------------
# Schema — every data column and (where applicable) its paired _conf column.
# Order here defines column order in the CSV.
# Confidence tiers: A/B/C/D/E (see data/methodology.md).
# ---------------------------------------------------------------------------
IDENTITY_COLS = ["ac_no", "ac_name", "district", "region_label", "reservation"]

DATA_COLS = [
    # Electorate
    "total_electors_2026", "male_electors", "female_electors",
    "sir_deletion_count_est", "sir_deletion_pct_est",
    # Religion
    "hindu_pct", "muslim_pct", "christian_pct", "sarna_orp_pct", "other_religion_pct",
    # Caste — SC
    "sc_total_pct", "namasudra_matua_pct_est", "rajbanshi_pct_est",
    "bagdi_pct_est", "poundra_pct_est", "other_sc_pct_est",
    # Caste — ST
    "st_total_pct", "santhal_pct_est", "oraon_pct_est",
    "munda_pct_est", "bhumij_pct_est", "other_st_pct_est",
    # Caste — UC / OBC
    "uc_bhadralok_pct_est", "obc_mahishya_pct_est", "obc_sadgop_pct_est",
    "obc_kurmi_pct_est", "obc_teli_pct_est", "obc_other_pct_est",
    # Language
    "bengali_pct", "hindi_pct", "santhali_pct", "urdu_pct",
    "nepali_pct", "rajbanshi_lang_pct", "kurmali_pct", "other_lang_pct",
    # Income / poverty
    "bpl_household_pct_secc", "mgnrega_worker_share_pct",
    "per_capita_income_band_est", "agri_hh_pct", "out_migrant_worker_pct_est",
    # Education
    "literacy_overall_pct", "literacy_male_pct", "literacy_female_pct",
    "graduate_plus_pct_est", "unemployed_educated_youth_est",
    # Occupation
    "cultivator_pct", "ag_labourer_pct", "tea_worker_pct_est",
    "fishworker_pct_est", "industrial_pct_est", "govt_employee_pct_est",
    "informal_sector_pct_est",
    # Welfare schemes
    "lakshmir_bhandar_beneficiaries_est", "krishak_bandhu_beneficiaries_est",
    "swasthya_sathi_coverage_pct_est", "khadya_sathi_coverage_pct_est",
    "kanyashree_coverage_pct_est", "old_age_widow_pension_est",
]

# region_label gets a confidence column too (it's a modeled label, tier E).
REGION_LABEL_HAS_CONF = True

PROVENANCE_COL = "sources_json"


def build_header() -> list[str]:
    cols = list(IDENTITY_COLS)
    if REGION_LABEL_HAS_CONF:
        # Insert region_label_conf right after region_label.
        idx = cols.index("region_label") + 1
        cols.insert(idx, "region_label_conf")
    for c in DATA_COLS:
        cols.append(c)
        cols.append(f"{c}_conf")
    cols.append(PROVENANCE_COL)
    return cols


def slugify(name: str) -> str:
    s = name.lower()
    s = re.sub(r"[^a-z0-9]+", "_", s)
    s = s.strip("_")
    return s


def main() -> None:
    with AC_LIST.open() as f:
        acs = list(csv.DictReader(f))
    assert len(acs) == 294, f"expected 294 ACs, got {len(acs)}"

    # --- CSV skeleton ---------------------------------------------------
    header = build_header()
    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with OUT_CSV.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(header)
        for ac in acs:
            row = {col: "" for col in header}
            row["ac_no"] = ac["ac_no"]
            row["ac_name"] = ac["ac_name"]
            row["district"] = ac["district"]
            row["reservation"] = ac["reservation"]
            region = DISTRICT_REGION.get(ac["district"], "")
            row["region_label"] = region
            row["region_label_conf"] = "E"  # modeled stratification
            w.writerow([row[col] for col in header])

    # --- Stub MD files --------------------------------------------------
    OUT_MD_DIR.mkdir(parents=True, exist_ok=True)
    created = 0
    skipped = 0
    for ac in acs:
        ac_no = int(ac["ac_no"])
        slug = slugify(ac["ac_name"])
        fname = f"{ac_no:03d}_{slug}.md"
        fpath = OUT_MD_DIR / fname
        if fpath.exists():
            skipped += 1
            continue
        reservation = ac["reservation"]
        district = ac["district"]
        region = DISTRICT_REGION.get(district, "")
        content = STUB_TEMPLATE.format(
            ac_no=ac_no,
            ac_name=ac["ac_name"],
            reservation=reservation,
            district=district,
            region=region,
        )
        fpath.write_text(content)
        created += 1

    print(f"CSV written   : {OUT_CSV} ({len(header)} cols, 294 rows)")
    print(f"Stub MD files : {created} created, {skipped} skipped (existing)")


STUB_TEMPLATE = """# AC {ac_no:03d} — {ac_name} ({reservation})

**District:** {district} · **Region:** {region} · **2026 Phase:** TBD · **Total electors:** TBD

> _Stub — pending Step 3 (pilot) or Step 4 (scale-out) population._

## 1. Demographic snapshot
TBD

## 2. Caste composition
TBD

## 3. Language & ethnicity
TBD

## 4. Economic profile
TBD

## 5. Education
TBD

## 6. Welfare scheme footprint
TBD

## 7. Political dynamics (historical vote 2016 / 2019 / 2021 / 2024)
TBD

## 8. Sources & caveats
TBD
"""


if __name__ == "__main__":
    main()
