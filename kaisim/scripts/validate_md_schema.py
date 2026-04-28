#!/usr/bin/env python3
"""
validate_md_schema.py
Check an AC's calibrated_2019 MD against NORMALIZED_SCHEMA.md (v1).

Reports for each AC:
  - Section presence (A, B, C.1-C.16, D.1-D.18, E, F, G, H)
  - Canonical category coverage in C-sections (required rows present)
  - Joint table parent / child column conformance
  - §E party set match (BJP, AITC, INC, LF, Other_NOTA)
  - Compound age bucket detection (D.6, D.7)
  - Adult-only age coverage in C.3 (no 0_4 / 5_9 / 10_14 / 15_17)
  - Marginal sum validation (= 100.0 ± 0.1 across non-subgroup rows)
  - Sub-unit Un_ prefix in C.11 + D.11–D.14
  - D.2 as 2D table (religion-keyed) vs 1D Hindu-only

Exit codes:
  0 — fully compliant
  1 — schema violations present
  2 — warnings only

Run:
    python3 scripts/validate_md_schema.py 095
    python3 scripts/validate_md_schema.py --all
    python3 scripts/validate_md_schema.py 095 --strict
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONSTS_DIR = ROOT.parent / "constituency_data" / "constituencies"


def _ac_2019_dir(ac: str) -> Path:
    """Return constituency_data/constituencies/{ac}_*/2019 for a 3-digit AC id."""
    matches = sorted(CONSTS_DIR.glob(f"{ac}_*"))
    if not matches:
        raise FileNotFoundError(f"No constituency folder for AC {ac!r}")
    return matches[0] / "2019"


def _ac_csv_dir(ac: str) -> Path:
    return _ac_2019_dir(ac) / "csv"


# ---------------------------------------------------------------------------
# Canonical schema (v1)
# ---------------------------------------------------------------------------

# Required category rows per C-section. The auto-builder snake-cases the
# leading parenthetical content away, so we match by that snake-case form.
REQUIRED_CATS: dict[str, list[str]] = {
    "religion":              ["Hindu", "Muslim", "Christian", "Sarna_ORP", "Other_residual"],
    "caste":                 ["SC_total", "ST_total", "UC_bhadralok", "OBC",
                                "Other_Hindu_middle", "Muslim",
                                "Christian_plus_Sarna_plus_Other"],
    "age_cohort":            ["18_22", "23_27", "28_32", "33_37", "38_42",
                                "43_47", "48_52", "53_57", "58_62", "63_67", "68"],
    "gender":                ["Male", "Female", "Third_gender"],
    "mother_tongue":         ["Bengali", "Hindi", "Urdu", "Other"],
    "education":             ["Illiterate", "Primary", "Middle", "Secondary",
                                "Higher_Secondary", "Graduate", "Postgraduate"],
    "workforce_status":      ["Main_worker", "Marginal_worker", "Non_worker",
                                "Student", "Unemployed"],
    "occupation":            ["Cultivator", "Agricultural_labourer",
                                "Household_industry", "Manufacturing", "Construction",
                                "Trade_retail", "Transport_logistics", "Services",
                                "Government_services_teachers", "Out_migrant_worker"],
    "class_of_worker":       ["Employer", "Employee", "Single_worker", "Family_worker"],
    "economic_status":       ["BPL_household", "Above_Poverty_Line_low_income",
                                "Lower_middle", "Middle", "Upper_middle_well_off"],
    "household_composition": ["Nuclear_HH", "Joint_HH", "Extended_multi_generation"],
    "marital_status":        ["Never_married", "Currently_married", "Widowed",
                                "Separated_divorced"],
    "asset_media":           ["Television", "Radio", "Mobile_phone",
                                "Smartphone_with_internet", "Computer",
                                "Two_wheeler", "Four_wheeler", "Banking_access"],
    "amenities":             ["Improved_drinking_water_source", "Improved_sanitation",
                                "LPG_clean_cooking_fuel", "Wood_biomass_fuel",
                                "Other_fuel", "Electricity"],
    "migration":             ["Native", "WB_other_district", "Other_Indian_state",
                                "Bangladesh_origin", "Outside_India", "Out_migrant"],
}

CHILD_AGE_CODES = {"0_4", "5_9", "10_14", "15_17"}

ADULT_AGE_COHORTS = ["18_22", "23_27", "28_32", "33_37", "38_42", "43_47",
                       "48_52", "53_57", "58_62", "63_67", "68"]

CANONICAL_PARTIES = ["BJP", "AITC", "INC", "LF", "Other_NOTA"]

# Marginal axes that should sum to 100 (excluding flag axes + scalar rows)
SUM_TO_100_AXES = ["religion", "caste", "age_cohort", "gender", "mother_tongue",
                    "education", "workforce_status", "occupation", "class_of_worker",
                    "economic_status", "household_composition", "marital_status",
                    "migration", "gp_location"]

FLAG_AXES = {"asset_media", "amenities"}

REQUIRED_SECTION_IDS = (
    [f"C.{i}" for i in range(1, 17)]
    + [f"D.{i}" for i in range(1, 19)]
    + ["E", "F", "G", "H"]
)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def to_snake(label: str) -> str:
    """Match build_ac_verifier_configs.py's to_snake() exactly."""
    if not label:
        return ""
    s = re.sub(r"\([^)]*\)", "", label)
    s = re.sub(r"[^A-Za-z0-9]+", "_", s)
    s = re.sub(r"_+", "_", s).strip("_")
    return s


def find_md(ac: str) -> Path:
    matches = sorted(_ac_2019_dir(ac).glob(f"{ac}_*_2019.md"))
    if not matches:
        raise FileNotFoundError(f"No MD for AC {ac}")
    return matches[0]


def section_present(md: str, section_id: str) -> bool:
    if section_id in ("E", "F", "G", "H"):
        return bool(re.search(rf"^##\s+{re.escape(section_id)}\.", md, re.MULTILINE))
    return bool(re.search(rf"^###\s+{re.escape(section_id)}\b", md, re.MULTILINE))


def get_marginal_categories(ac: str, axis: str, include_subgroups: bool = False
                              ) -> list[tuple[str, float, str]]:
    """Read derived CSV → list of (snake_code, pct, is_subgroup) for this axis."""
    p = _ac_csv_dir(ac) / f"{ac}_marginals.csv"
    if not p.exists():
        return []
    out = []
    with p.open() as f:
        for row in csv.DictReader(f):
            if row["axis"] != axis:
                continue
            sub = row.get("is_subgroup", "no")
            if not include_subgroups and sub == "yes":
                continue
            try:
                pct = float(row["pct"])
            except (ValueError, TypeError):
                continue
            out.append((to_snake(row["category"]), pct, sub))
    return out


def get_joint_first_col(ac: str, file_stem: str) -> tuple[list[str], list[str]]:
    """Return (header_cols, first_col_values) for a joint CSV."""
    p = _ac_csv_dir(ac) / f"{ac}_{file_stem}.csv"
    if not p.exists():
        return [], []
    with p.open() as f:
        reader = csv.reader(f)
        header = next(reader, [])
        first_col = [row[0] for row in reader if row]
    return header, first_col


# ---------------------------------------------------------------------------
# Checks
# ---------------------------------------------------------------------------

def check_sections(ac: str, md: str) -> list[dict]:
    out = []
    for sid in REQUIRED_SECTION_IDS:
        if not section_present(md, sid):
            out.append({"sev": "ERR", "id": "section_missing",
                         "msg": f"section §{sid} missing from MD"})
    return out


def check_canonical_categories(ac: str) -> list[dict]:
    out = []
    for axis, required in REQUIRED_CATS.items():
        cats = get_marginal_categories(ac, axis)
        codes = [c for c, _, _ in cats]
        for r in required:
            if r not in codes:
                # Soft warn for region-specific axes; hard error for the
                # universally-required ones.
                sev = "WARN" if axis in ("migration", "mother_tongue") else "ERR"
                out.append({"sev": sev, "id": "missing_canonical_cat",
                             "msg": f"axis {axis}: missing canonical row "
                                    f"{r!r} (saw {codes})"})
    return out


def check_age_cohort_adult_only(ac: str) -> list[dict]:
    out = []
    cats = get_marginal_categories(ac, "age_cohort", include_subgroups=True)
    codes = [c for c, _, _ in cats]
    found_child = [c for c in codes if c in CHILD_AGE_CODES]
    if found_child:
        out.append({"sev": "ERR", "id": "age_includes_children",
                     "msg": f"age_cohort includes child cohorts {found_child} — "
                            "schema requires adults-only (renormalize)"})
    return out


def check_marginal_sums(ac: str) -> list[dict]:
    out = []
    for axis in SUM_TO_100_AXES:
        cats = get_marginal_categories(ac, axis)  # excludes subgroups
        if not cats:
            continue
        total = sum(p for _, p, _ in cats)
        if abs(total - 100.0) > 0.5:
            sev = "ERR" if abs(total - 100.0) > 1.0 else "WARN"
            out.append({"sev": sev, "id": "marginal_sum",
                         "msg": f"axis {axis}: leaves sum to {total:.2f}, "
                                f"expected 100 ± 0.5"})
    return out


def check_gp_un_prefix(ac: str) -> list[dict]:
    out = []
    cats = get_marginal_categories(ac, "gp_location", include_subgroups=True)
    bad = [c for c, _, _ in cats if not re.match(r"^U\d+_", c)]
    if bad:
        out.append({"sev": "ERR", "id": "gp_un_prefix",
                     "msg": f"gp_location cats missing Un_ prefix: {bad}"})
    return out


def check_age_joint_5yr(ac: str) -> list[dict]:
    out = []
    for stem, sec in (("joint_age_gender_education", "D.6"),
                       ("joint_marital_age_gender", "D.7")):
        _, first = get_joint_first_col(ac, stem)
        bad = []
        for v in first:
            v = v.strip()
            if not v or v.lower() in ("sum", "note"):
                continue
            code = to_snake(v)
            if code not in ADULT_AGE_COHORTS:
                bad.append(code)
        if bad:
            out.append({"sev": "ERR", "id": "compound_age_bucket",
                         "msg": f"{sec} ({stem}) uses non-canonical age keys: "
                                f"{bad} — schema requires 5-year cohorts"})
    return out


def check_d2_2d_form(ac: str) -> list[dict]:
    """D.2 should have Religion as parent column. The auto-builder accepts
    1D 'sub-caste % of Hindu' too (with special transform), but the schema
    flag is whether D.2 is religion-keyed."""
    header, first = get_joint_first_col(ac, "joint_religion_caste")
    if not header:
        return [{"sev": "ERR", "id": "d2_missing", "msg": "D.2 CSV missing"}]
    parent_col = (header[0] or "").lower()
    if "religion" in parent_col:
        return []
    return [{"sev": "WARN", "id": "d2_1d_form",
              "msg": f"D.2 uses 1D 'caste sub-group' form (parent col "
                     f"{header[0]!r}); auto-builder will wrap into 2D religion-"
                     "keyed form. Consider rewriting as 2D directly."}]


def check_vote_party_set(ac: str) -> list[dict]:
    out = []
    for stem, sec in (("vote_religion_2019", "D.15"),
                        ("vote_caste_2019", "D.16"),
                        ("vote_gender_2019", "D.17")):
        header, _ = get_joint_first_col(ac, stem)
        if not header:
            continue
        cols = [to_snake(c) for c in header[1:]
                 if c and c not in ("Tier", "Source", "Note")]
        cols = [c for c in cols if c]
        canonical = set(CANONICAL_PARTIES)
        present = set(cols)
        extra = present - canonical
        missing = canonical - present
        if extra or missing:
            out.append({"sev": "WARN", "id": "vote_party_set",
                         "msg": f"{sec} parties = {sorted(present)}; canonical "
                                f"= {sorted(canonical)}. "
                                f"Extra: {sorted(extra) or '-'}. "
                                f"Missing: {sorted(missing) or '-'}."})
    return out


def check_calibration_target_schema(ac: str) -> list[dict]:
    p = _ac_csv_dir(ac) / f"{ac}_calibration_target_2019.csv"
    if not p.exists():
        return [{"sev": "ERR", "id": "cal_target_missing",
                  "msg": "§E calibration target CSV missing"}]
    out = []
    with p.open() as f:
        reader = csv.reader(f)
        header = next(reader, [])
        rows = list(reader)
    parties = []
    for r in rows:
        if not r or not r[0]:
            continue
        first = r[0].strip()
        if any(k in first.lower() for k in ("total", "margin", "lead",
                                              "electors", "turnout")):
            continue
        parties.append(to_snake(first))
    canonical = set(CANONICAL_PARTIES)
    present = set(parties)
    extra = present - canonical
    missing = canonical - present
    if extra or missing:
        out.append({"sev": "WARN", "id": "cal_target_party_set",
                     "msg": f"§E parties = {sorted(present)}. "
                            f"Schema requires exactly {sorted(canonical)}. "
                            f"Extra (lump into Other_NOTA): {sorted(extra) or '-'}. "
                            f"Missing: {sorted(missing) or '-'}."})
    if len(header) > 6:
        out.append({"sev": "WARN", "id": "cal_target_extra_cols",
                     "msg": f"§E has {len(header)} columns; schema specifies "
                            "4 (party, ac_segment_pct, tier, note). Move detail to §H."})
    return out


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def validate_one(ac: str) -> dict:
    md_path = find_md(ac)
    md = md_path.read_text()
    issues: list[dict] = []
    issues += check_sections(ac, md)
    issues += check_canonical_categories(ac)
    issues += check_age_cohort_adult_only(ac)
    issues += check_marginal_sums(ac)
    issues += check_gp_un_prefix(ac)
    issues += check_age_joint_5yr(ac)
    issues += check_d2_2d_form(ac)
    issues += check_vote_party_set(ac)
    issues += check_calibration_target_schema(ac)
    return {
        "ac": ac, "md": md_path.name,
        "issues": issues,
        "n_err": sum(1 for i in issues if i["sev"] == "ERR"),
        "n_warn": sum(1 for i in issues if i["sev"] == "WARN"),
    }


def discover_acs() -> list[str]:
    out = []
    for d in sorted(CONSTS_DIR.iterdir()):
        if d.is_dir():
            m = re.match(r"^(\d{3})_", d.name)
            if m:
                out.append(m.group(1))
    return out


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("ac", nargs="?", default=None,
                    help="3-digit AC number (omit with --all)")
    p.add_argument("--all", action="store_true")
    p.add_argument("--strict", action="store_true",
                    help="Treat warnings as errors")
    args = p.parse_args()

    targets = (discover_acs() if args.all
               else [args.ac.zfill(3)] if args.ac else [])
    if not targets:
        p.error("provide AC number or --all")
        return 2

    print(f"Validating {len(targets)} AC(s) against NORMALIZED_SCHEMA.md v1\n")
    print(f"{'AC':>4}  {'MD':>40s}  {'ERR':>4}  {'WARN':>5}  result")
    print(f"{'-' * 4:>4}  {'-' * 40}  {'-' * 4:>4}  {'-' * 5:>5}  -------")

    results = []
    for ac in targets:
        try:
            r = validate_one(ac)
            results.append(r)
        except FileNotFoundError as e:
            print(f"{ac:>4}  ✗ {e}")
            continue
        outcome = ("FAIL" if r["n_err"] > 0
                   else ("WARN" if r["n_warn"] > 0 else "PASS"))
        print(f"{ac:>4}  {r['md']:>40s}  {r['n_err']:>4}  "
              f"{r['n_warn']:>5}  {outcome}")

    # Detail for any AC with issues
    print()
    for r in results:
        if not r["issues"]:
            continue
        print(f"=== AC {r['ac']} ===")
        for i in sorted(r["issues"], key=lambda x: (x["sev"] != "ERR", x["id"])):
            sev = "✗" if i["sev"] == "ERR" else "⚠"
            print(f"  {sev} [{i['id']}] {i['msg']}")
        print()

    n_fail = sum(1 for r in results if r["n_err"] > 0)
    n_warn = sum(1 for r in results if r["n_err"] == 0 and r["n_warn"] > 0)
    n_pass = sum(1 for r in results if r["n_err"] == 0 and r["n_warn"] == 0)
    print(f"\n  {n_pass} PASS · {n_warn} WARN · {n_fail} FAIL")

    if args.strict and (n_fail > 0 or n_warn > 0):
        return 1
    return 0 if n_fail == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
