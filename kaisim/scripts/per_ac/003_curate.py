#!/usr/bin/env python3
"""
003_curate.py — hand-curate AC 003's auto-built structures to align
joint parent codes with axis category codes. Run AFTER
build_ac_verifier_configs.py to fix the alignment issues that block the
verifier from passing budget.

Fixes applied:
  1. gp_location axis cats: drop U1/U2 prefix → match joint keys
  2. caste subgroup_rollups: SC_total = [Rajbanshi_SC, Bagdi_SC,
     Namasudra_SC, Other_SC]; ST_total = [ST]
  3. caste_bucket_map on caste-parent joints: bucket sub-codes into leaves
  4. age_cohort_bucket_map on age-parent joints: 5-yr cohorts → joint buckets
  5. occupation joint key normalization (Ag_labourer → Agricultural_labourer)
  6. Drop bilingual_given_media + vote_given_welfare from joints (no axis)
  7. Add occupation bucket aliases

Run:
    python3 scripts/per_ac/003_curate.py
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SIM_DIR = ROOT / "simulations" / "wb_2021_ac003"
AXES_PATH = SIM_DIR / "structures" / "axes.json"
JOINTS_PATH = SIM_DIR / "structures" / "joints.json"


def _expand_age_buckets(table: dict, expansion: dict[str, list[str]]) -> dict:
    """Expand compound-bucket joint keys (e.g. '33_47') to constituent 5-yr
    cohorts, copying the row values."""
    out = {}
    for old_key, row in table.items():
        targets = expansion.get(old_key, [old_key])
        for t in targets:
            out[t] = dict(row)
    return out


CHILD_AGE_CODES = {"0_4", "5_9", "10_14", "15_17"}


def _drop_children_renormalize(axis: dict) -> None:
    """Restrict age_cohort axis to 18+; renormalize remaining marginal pcts.

    Phase-2 simulation operates on voters (18+). Including child cohorts in
    the persona axis poisons workforce_status (children all force Non_worker)
    and skews aggregates against an adult-targeting marginal."""
    cats = axis.get("categories", [])
    marginal = axis.get("marginal", {})
    keep = [c for c in cats if c not in CHILD_AGE_CODES]
    if len(keep) == len(cats):
        return  # nothing to drop
    kept_mass = sum(marginal.get(c, 0.0) for c in keep)
    if kept_mass <= 0:
        return
    axis["categories"] = keep
    axis["marginal"] = {c: round(marginal.get(c, 0.0) * 100.0 / kept_mass, 4)
                        for c in keep}
    axis.setdefault("notes", "")
    axis["notes"] = (axis["notes"] + " [restricted to adults 18+ for "
                     "Phase-2 voter simulation; child cohorts dropped + "
                     "remaining cohorts renormalized to sum 100]").strip()


def patch_axes(doc: dict) -> dict:
    for a in doc["axes"]:
        if a["name"] == "age_cohort":
            _drop_children_renormalize(a)
        if a["name"] in ("occupation", "class_of_worker"):
            # These marginals are "% of workers", not "% of all personas".
            # Verifier should only score among workers.
            a["verify_condition"] = {
                "field": "workforce_status",
                "values": ["Main_worker", "Marginal_worker"],
            }
        if a["name"] == "gp_location":
            # Rename leaves to drop U1/U2 prefix to match joint keys
            old_to_new = {
                "U1_Census_towns_cluster": "Census_towns_cluster",
                "U2_CDB_II_rural_GPs": "CDB_II_rural_GPs",
            }
            a["categories"] = [old_to_new.get(c, c) for c in a["categories"]]
            a["marginal"] = {old_to_new.get(k, k): v
                              for k, v in a["marginal"].items()}
            a["display_names"] = {old_to_new.get(k, k): v
                                    for k, v in (a.get("display_names") or {}).items()}
        if a["name"] == "caste":
            # Declare verifier-only rollups from sub-codes used in joints
            a["subgroup_rollups"] = {
                "SC_total": ["Rajbanshi_SC", "Bagdi_SC", "Namasudra_SC",
                              "Bagdi_Hari_Jhalo_Malo_SC", "Other_SC"],
                "ST_total": ["ST"],
            }
    return doc


def patch_joints(doc: dict) -> dict:
    keep: list[dict] = []
    for j in doc["joints"]:
        # Drop joints whose parent axes don't exist in this AC
        if j["name"] in ("bilingual_given_media", "vote_given_welfare"):
            continue

        # caste_given_religion: already has Hindu/Muslim/Other keys → fine.
        # But the Hindu row's child cats may use SC_total etc. — it does
        # since the builder's D.2 transformer maps subcats to leaves.

        # education_given_caste — joint uses sub-codes (Rajbanshi_SC, ST,
        # Other_SC). Add caste_bucket_map mapping these to the Hindu sub-
        # caste codes the persona will have.
        if j["name"] == "education_given_caste":
            j["caste_bucket_map"] = {
                "Rajbanshi_SC": ["SC_total"],     # most common SC bucket
                "Other_SC": ["SC_total"],
                "ST": ["ST_total"],
                "UC_bhadralok": ["UC_bhadralok"],
                "OBC": ["OBC"],
                "Other_Hindu_middle": ["Other_Hindu_forward_middle"],
                "Muslim": ["Muslim"],
            }
            # Normalize bucket keys in the joint table to match axis leaves
            old = j["table"]
            new = {
                "SC_total": old.get("Rajbanshi_SC", old.get("Other_SC", {})),
                "ST_total": old.get("ST", {}),
                "UC_bhadralok": old.get("UC_bhadralok", {}),
                "OBC": old.get("OBC", {}),
                "Other_Hindu_forward_middle": old.get("Other_Hindu_middle", {}),
                "Muslim": old.get("Muslim", {}),
            }
            j["table"] = {k: v for k, v in new.items() if v}

        # vote_given_caste — same shape
        if j["name"] == "vote_given_caste":
            old = j["table"]
            new = {
                "SC_total": old.get("Rajbanshi_SC", old.get("Other_SC", {})),
                "ST_total": old.get("ST", {}),
                "UC_bhadralok": old.get("UC_bhadralok", {}),
                "OBC": old.get("OBC", {}),
                "Other_Hindu_forward_middle": old.get("Other_Hindu_middle", {}),
                "Muslim": old.get("Muslim", {}),
            }
            j["table"] = {k: v for k, v in new.items() if v}

        # education_given_age_gender — joint uses compound buckets
        # like {33_42, 43_57}. Expand into 5-year cohorts so the verifier's
        # parent-lookup matches the persona's age_cohort directly.
        if j["name"] == "education_given_age_gender":
            j["table"] = _expand_age_buckets(j["table"], {
                "18_22": ["18_22"],
                "23_27": ["23_27"],
                "28_32": ["28_32"],
                "33_42": ["33_37", "38_42"],
                "43_57": ["43_47", "48_52", "53_57"],
                "58": ["58_62", "63_67", "68"],
            })
            # Also mark verifier-only since the rule_based sampler doesn't
            # use this joint to set education (it uses education_given_caste).
            j["use"] = "verifier_only"

        if j["name"] == "married_given_age_gender":
            j["table"] = _expand_age_buckets(j["table"], {
                "18_22": ["18_22"],
                "23_27": ["23_27"],
                "28_32": ["28_32"],
                "33_47": ["33_37", "38_42", "43_47"],
                "48_62": ["48_52", "53_57", "58_62"],
                "63": ["63_67", "68"],
            })

        # asset_given_occupation — joint uses abbreviated parent codes
        if j["name"] == "asset_given_occupation":
            old = j["table"]
            new = dict(old)
            renames = {
                "Ag_labourer": "Agricultural_labourer",
                "Transport": "Transport_logistics",
                "Govt_services": "Government_services_teachers",
                "HH_industry": "Household_industry",
                "Out_migrant": "Out_migrant_worker",
            }
            for old_key, new_key in renames.items():
                if old_key in new:
                    new[new_key] = new.pop(old_key)
            j["table"] = new

        # FLAG-NAME ALIGNMENT — joint cells use abbreviated names; rename
        # to match the asset_media / amenities axis flag list.
        if j["name"] in ("asset_given_religion", "asset_given_gp",
                          "asset_given_occupation"):
            j["table"] = _rename_flags(j["table"], {
                "TV": "Television",
                "Smartphone_internet": "Smartphone_with_internet",
                "Banking": "Banking_access",
                "Mobile": "Mobile_phone",
                "Two_wheeler": "Two_wheeler",
                "Four_wheeler": "Four_wheeler",
                "Computer": "Computer",
            })
        if j["name"] == "amenities_given_gp":
            j["table"] = _rename_flags(j["table"], {
                "LPG": "LPG_clean_cooking_fuel",
                "Improved_sanitation": "Improved_sanitation",
                "Improved_water": "Improved_drinking_water_source",
                "Electricity": "Electricity",
                "Wood_biomass": "Wood_biomass_fuel",
                "Other_fuel": "Other_fuel",
            })

        # lang_given_religion — child cat alignment.
        if j["name"] == "lang_given_religion":
            j["table"] = _rename_flags(j["table"], {
                "Rajbongshi": "Rajbongshi_Rajbanshi",
            })

        # migration_given_religion — child cat alignment.
        if j["name"] == "migration_given_religion":
            j["table"] = _rename_flags(j["table"], {
                "WB_other_dist": "WB_other_district",
                "Other_state": "Other_Indian_state",
                "Nepal_Bhutan": "Nepal_Bhutan_origin",
            })

        # caste_given_gp — child cat codes need realignment to match the
        # caste axis leaves. The CSV uses Rajbanshi_SC / Other_SC / ST /
        # UC / OBC_Other_Hindu / Muslim, but the axis has SC_total /
        # ST_total / UC_bhadralok / OBC / Other_Hindu_forward_middle /
        # Muslim / Christian_Other.
        if j["name"] == "caste_given_gp":
            new_table = {}
            for parent_val, row in j["table"].items():
                # Aggregate sub-codes onto axis leaves.
                sc = row.get("Rajbanshi_SC", 0) + row.get("Other_SC", 0)
                st = row.get("ST", 0)
                uc = row.get("UC", 0)
                # OBC_Other_Hindu split — Cooch Behar has small OBC, dominant
                # Other_Hindu_middle (~30/70 ratio per marginals).
                ohm_total = row.get("OBC_Other_Hindu", 0)
                obc = ohm_total * 0.30
                ohm = ohm_total * 0.70
                new_row = {
                    "SC_total": sc, "ST_total": st, "UC_bhadralok": uc,
                    "OBC": obc, "Other_Hindu_forward_middle": ohm,
                    "Muslim": row.get("Muslim", 0),
                }
                # Drop zero entries.
                new_row = {k: v for k, v in new_row.items() if v > 0}
                if new_row:
                    new_table[parent_val] = new_row
            if new_table:
                j["table"] = new_table

        keep.append(j)
    doc["joints"] = keep
    return doc


def _rename_flags(table: dict, renames: dict[str, str]) -> dict:
    """For each parent-keyed row, rename flag keys per the map."""
    out = {}
    for parent, row in table.items():
        new_row = {}
        for k, v in row.items():
            new_row[renames.get(k, k)] = v
        out[parent] = new_row
    return out


def main() -> None:
    print(f"Curating AC 003 structures at {SIM_DIR.relative_to(ROOT.parent)}\n")

    axes_doc = json.loads(AXES_PATH.read_text())
    axes_doc = patch_axes(axes_doc)
    AXES_PATH.write_text(json.dumps(axes_doc, indent=2, ensure_ascii=False))
    print(f"  ✓ patched {AXES_PATH.name}")

    joints_doc = json.loads(JOINTS_PATH.read_text())
    n_before = len(joints_doc["joints"])
    joints_doc = patch_joints(joints_doc)
    n_after = len(joints_doc["joints"])
    JOINTS_PATH.write_text(json.dumps(joints_doc, indent=2, ensure_ascii=False))
    print(f"  ✓ patched {JOINTS_PATH.name} ({n_before} → {n_after} joints)")

    print("\nRe-run baseline:")
    print("  python3 simulations/wb_2021_ac003/generate.py baseline_rule")


if __name__ == "__main__":
    main()
