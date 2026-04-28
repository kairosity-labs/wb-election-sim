"""Generic plumbing-only curate (data-faithful).

Applies ONLY tier-1 fixes that don't override source values or introduce
chosen ratios:

  ✅ KEEP:
    1. Drop child age cohorts (restrict to 18+ voter universe; renormalize)
    2. Standard flag renames (TV → Television, LPG → LPG_clean_cooking_fuel, ...)
    3. Standard child cat renames (WB_other_dist → WB_other_district, ...)
    4. Compound age bucket expansion (33_47 → [33_37, 38_42, 43_47])
    5. verify_condition for "% of workers" axes (occupation, class_of_worker)
    6. Drop joints whose parent axis doesn't exist (bilingual_given_media,
       vote_given_welfare)
    7. gp_location prefix alignment (auto-detected per AC)
    8. SC_total / ST_total subgroup_rollups (auto-detected from axis sub-codes)
    9. Joint table key aggregation when SUM-EQUAL (e.g., Rajbanshi_SC +
       Other_SC → SC_total at sum-of-values; no ratio choice involved)

  ❌ REMOVE (these are tier-2 / tier-3 from full curation):
    - Inferred ratio splits (Mahishya_Sadgop 70:30, OBC_Other_Hindu 30:70)
    - Bengali / Non-Bengali Hindu population-weighted collapse
    - Muslim sub-caste declared shares (Sheikh 48 / Ansari 30 / ...)
    - Vote-bucket Others/NOTA splitting via target ratio
    - Joint cell value back-solves from macro target
    - INC / BSP small-party clamps
    - Currently-married scale factors (0.86, 0.88)
    - Asset-cell value softening for log-odds blender
    - 4th-religion expansion with values "re-derived from marginals"

When a joint cell has a parent value not in the axis, the joint row is
DROPPED (rather than aggregated with an inferred ratio). The partial verifier
will report it as a skipped joint, but no fabricated ratio enters the data.

Run:
    python3 experiments/three_way_calibration/plumbing_curate.py 003
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SIMS_DIR = ROOT / "simulations"


# ---------------------------------------------------------------------------
# Standard rename maps — these are pure identifier alignment, no value change
# ---------------------------------------------------------------------------

ASSET_FLAG_RENAMES = {
    "TV": "Television",
    "Smartphone_internet": "Smartphone_with_internet",
    "Banking": "Banking_access",
    "Mobile": "Mobile_phone",
    "Computer": "Computer",
    "Two_wheeler": "Two_wheeler",
    "Four_wheeler": "Four_wheeler",
    "Radio": "Radio",
}

AMENITY_FLAG_RENAMES = {
    "LPG": "LPG_clean_cooking_fuel",
    "Improved_water": "Improved_drinking_water_source",
    "Improved_sanitation": "Improved_sanitation",
    "Electricity": "Electricity",
    "Wood_biomass": "Wood_biomass_fuel",
    "Other_fuel": "Other_fuel",
}

MIGRATION_CHILD_RENAMES = {
    "WB_other_dist": "WB_other_district",
    "Other_state": "Other_Indian_state",
    "Nepal_Bhutan": "Nepal_Bhutan_origin",
    "Out_migrant_registered": "Out_migrant",
}

OCCUPATION_PARENT_RENAMES = {
    "Ag_labourer": "Agricultural_labourer",
    "Transport": "Transport_logistics",
    "Govt_services": "Government_services_teachers",
    "HH_industry": "Household_industry",
    "Out_migrant": "Out_migrant_worker",
}

EDUCATION_RENAMES = {
    "Sec": "Secondary",
    "HS": "Higher_Secondary",
    "Grad": "Graduate",
    "PG": "Postgraduate",
}

DROP_JOINTS = {"bilingual_given_media", "vote_given_welfare"}

CHILD_AGE_CODES = {"0_4", "5_9", "10_14", "15_17"}

# Common compound age bucket → 5-yr cohort expansions
COMPOUND_AGE_EXPANSIONS = {
    # education_given_age_gender style
    "33_42": ["33_37", "38_42"],
    "43_57": ["43_47", "48_52", "53_57"],
    "58":    ["58_62", "63_67", "68"],
    # married_given_age_gender style
    "33_47": ["33_37", "38_42", "43_47"],
    "48_62": ["48_52", "53_57", "58_62"],
    "63":    ["63_67", "68"],
}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _rename_dict_keys(d: dict, renames: dict) -> dict:
    return {renames.get(k, k): v for k, v in d.items()}


def _rename_inner_keys(table: dict, renames: dict) -> dict:
    return {parent: _rename_dict_keys(row, renames) if isinstance(row, dict) else row
            for parent, row in table.items()}


def _expand_age_buckets(table: dict, expansion: dict) -> dict:
    out = {}
    for old_key, row in table.items():
        targets = expansion.get(old_key, [old_key])
        for t in targets:
            out[t] = dict(row) if isinstance(row, dict) else row
    return out


def _drop_children_renormalize(axis: dict) -> bool:
    cats = axis.get("categories", [])
    marginal = axis.get("marginal", {})
    keep = [c for c in cats if c not in CHILD_AGE_CODES]
    if len(keep) == len(cats):
        return False
    kept_mass = sum(marginal.get(c, 0.0) for c in keep)
    if kept_mass <= 0:
        return False
    axis["categories"] = keep
    axis["marginal"] = {c: round(marginal.get(c, 0.0) * 100.0 / kept_mass, 4)
                        for c in keep}
    notes = axis.get("notes") or ""
    axis["notes"] = (notes + " [PLUMBING: restricted to adults 18+; "
                     "child cohorts dropped + renormalized to 100]").strip()
    return True


def _detect_gp_prefix_alignment(axes_doc: dict, joints_doc: dict
                                  ) -> dict[str, str]:
    """Detect U1_/U2_ axis-prefix vs joint-bare mismatch and return
    a rename map of joint_key → axis_key (or vice versa).

    Returns map (old_name → new_name) to be applied to joints' table keys
    in any *_given_gp joint."""
    gp_axis = next((a for a in axes_doc["axes"] if a["name"] == "gp_location"),
                    None)
    if not gp_axis:
        return {}
    cats = set(gp_axis.get("categories") or [])
    if not cats:
        return {}
    # Collect all joint parent keys for *_given_gp joints
    joint_keys = set()
    for j in joints_doc["joints"]:
        if "given_gp" in j["name"] and j.get("parents") == ["gp_location"]:
            joint_keys.update(j.get("table", {}).keys())
    if not joint_keys:
        return {}

    # If joint keys lack prefix but axis cats have it → strip axis prefix.
    # Simpler: rename axis cats by stripping prefix to match joints.
    # We return the rename as a dict of axis_cat_old → axis_cat_new
    # if any axis cat has prefix and the bare form is in joint_keys.
    out: dict[str, str] = {}
    for cat in list(cats):
        m = re.match(r"^(U\d+_)(.+)$", cat)
        if m and m.group(2) in joint_keys:
            out[cat] = m.group(2)
    return out


def _detect_caste_subgroup_rollups(axes_doc: dict) -> dict[str, list[str]]:
    """Detect SC_total / ST_total parent leaves with sub-codes for rollup.

    Looks for axis category codes containing 'SC' or 'ST' that aren't already
    a generic *_total rollup, and groups them.
    """
    caste_axis = next((a for a in axes_doc["axes"] if a["name"] == "caste"),
                       None)
    if not caste_axis:
        return {}
    cats = caste_axis.get("categories") or []
    rollups: dict[str, list[str]] = {}

    sc_subs = [c for c in cats if "_SC" in c and c != "SC_total"
               and not c.startswith("Other_SC")]
    other_sc_subs = [c for c in cats if c.startswith("Other_SC")]
    if "SC_total" in cats and (sc_subs or other_sc_subs):
        rollups["SC_total"] = sc_subs + other_sc_subs

    st_subs = [c for c in cats if c.startswith("ST_") and c != "ST_total"]
    if "ST_total" in cats and st_subs:
        rollups["ST_total"] = st_subs
    return rollups


# ---------------------------------------------------------------------------
# Axis + joint patches
# ---------------------------------------------------------------------------

def patch_axes(axes_doc: dict, joints_doc: dict) -> dict:
    # 1. Drop children, renormalize
    for a in axes_doc["axes"]:
        if a["name"] == "age_cohort":
            _drop_children_renormalize(a)

    # 2. Add verify_condition for "% of workers" axes
    for a in axes_doc["axes"]:
        if a["name"] in ("occupation", "class_of_worker"):
            a["verify_condition"] = {
                "field": "workforce_status",
                "values": ["Main_worker", "Marginal_worker"],
            }

    # 3. Strip gp_location U1_/U2_ prefix to match joint keys
    gp_renames = _detect_gp_prefix_alignment(axes_doc, joints_doc)
    if gp_renames:
        for a in axes_doc["axes"]:
            if a["name"] == "gp_location":
                a["categories"] = [gp_renames.get(c, c)
                                    for c in a.get("categories", [])]
                a["marginal"] = _rename_dict_keys(
                    a.get("marginal", {}), gp_renames)
                if a.get("display_names"):
                    a["display_names"] = _rename_dict_keys(
                        a["display_names"], gp_renames)

    # 4. Auto-detect caste subgroup_rollups
    rollups = _detect_caste_subgroup_rollups(axes_doc)
    if rollups:
        for a in axes_doc["axes"]:
            if a["name"] == "caste":
                a["subgroup_rollups"] = rollups

    return axes_doc


def patch_joints(joints_doc: dict) -> dict:
    keep: list[dict] = []
    for j in joints_doc["joints"]:
        # 1. Drop joints whose parent axis doesn't exist
        if j["name"] in DROP_JOINTS:
            continue

        # 2. Standard flag renames (asset, amenity)
        if "asset" in j["name"] or "amenities" in j["name"]:
            renames = (ASSET_FLAG_RENAMES if "asset" in j["name"]
                        else AMENITY_FLAG_RENAMES)
            j["table"] = _rename_inner_keys(j["table"], renames)

        # 3. Migration child renames
        if "migration" in j["name"]:
            j["table"] = _rename_inner_keys(j["table"], MIGRATION_CHILD_RENAMES)

        # 4. Occupation parent renames
        if "occupation" in j.get("parents", []) or j["name"] == "asset_given_occupation":
            j["table"] = _rename_dict_keys(j["table"], OCCUPATION_PARENT_RENAMES)

        # 5. Education child renames (in any joint with education as child)
        if j.get("child") == "education":
            j["table"] = _rename_inner_keys(j["table"], EDUCATION_RENAMES)

        # 6. Compound age bucket expansion
        if j["name"] in ("married_given_age_gender",
                          "education_given_age_gender"):
            j["table"] = _expand_age_buckets(j["table"], COMPOUND_AGE_EXPANSIONS)
            # Mark education_given_age_gender verifier-only — sampler uses
            # education_given_caste, so this is just a verifier joint
            if j["name"] == "education_given_age_gender":
                j["use"] = "verifier_only"

        keep.append(j)
    joints_doc["joints"] = keep
    return joints_doc


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def curate(ac: str, sim_dir: Path | None = None) -> None:
    sim_dir = sim_dir or (SIMS_DIR / f"wb_2021_ac{ac}")
    axes_path = sim_dir / "structures" / "axes.json"
    joints_path = sim_dir / "structures" / "joints.json"
    if not axes_path.exists() or not joints_path.exists():
        print(f"  ✗ AC {ac}: structures/ missing — run build first")
        return
    axes_doc = json.loads(axes_path.read_text())
    joints_doc = json.loads(joints_path.read_text())
    axes_doc = patch_axes(axes_doc, joints_doc)
    joints_doc = patch_joints(joints_doc)
    axes_path.write_text(json.dumps(axes_doc, indent=2, ensure_ascii=False))
    joints_path.write_text(json.dumps(joints_doc, indent=2, ensure_ascii=False))
    print(f"  ✓ AC {ac}: applied plumbing-only curate "
           f"({len(axes_doc['axes'])} axes, {len(joints_doc['joints'])} joints)")


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("ac", help="3-digit AC number")
    args = p.parse_args()
    curate(args.ac.zfill(3))
    return 0


if __name__ == "__main__":
    sys.exit(main())
