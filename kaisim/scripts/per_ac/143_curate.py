#!/usr/bin/env python3
"""
143_curate.py — hand-curate AC 143 (Diamond Harbour) auto-built structures.

Fixes applied (mechanical alignment of joint/axis category codes):
  1. age_cohort: drop child cohorts (0_4..15_17), renormalize to 100
  2. occupation / class_of_worker: verify_condition restricts to workers
  3. caste subgroup_rollups: align Hindu sub-caste codes used in joints
  4. caste_given_religion: Hindu-row keys already match axis (verified)
  5. migration_given_religion: rename child cats to axis leaves
  6. lang_given_religion: child cat alignment (already aligned)
  7. asset/amenity flag-name alignment in the GP/religion/occupation joints
  8. asset_given_occupation: rename parent codes (Ag_labourer → ...)
  9. caste_given_gp: rename parent values (Muni → U1_..., CDB_I_rural → U2_...,
     CDB_II_rural → U3_...) and aggregate child sub-codes onto axis leaves
 10. asset_given_gp / amenities_given_gp: rename parent values to U1/U2/U3
 11. education_given_caste: rename parent codes + expand abbreviated edu codes
 12. education_given_age_gender: expand compound age buckets to 5-yr cohorts;
     mark verifier_only since rule sampler uses education_given_caste
 13. married_given_age_gender: expand compound age buckets to 5-yr cohorts
 14. vote_given_caste: rename parent codes to axis caste leaves
 15. Drop bilingual_given_media + vote_given_welfare (no parent axis)
 16. Aggregate-target vote bucket alignment: CPI → CPI_LF, Others → Other,
     drop NOTA bucket (not in vote conditional joints)

Run:
    python3 kaisim/scripts/per_ac/143_curate.py
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SIM_DIR = ROOT / "simulations" / "wb_2021_ac143"
AXES_PATH = SIM_DIR / "structures" / "axes.json"
JOINTS_PATH = SIM_DIR / "structures" / "joints.json"
AGG_PATH = SIM_DIR / "structures" / "aggregate_targets.json"


CHILD_AGE_CODES = {"0_4", "5_9", "10_14", "15_17"}


def _drop_children_renormalize(axis: dict) -> None:
    cats = axis.get("categories", [])
    marginal = axis.get("marginal", {})
    keep = [c for c in cats if c not in CHILD_AGE_CODES]
    if len(keep) == len(cats):
        return
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


def _expand_age_buckets(table: dict, expansion: dict[str, list[str]]) -> dict:
    """Expand compound-bucket joint keys (e.g. '33_47') to constituent 5-yr
    cohorts, copying the row values."""
    out = {}
    for old_key, row in table.items():
        targets = expansion.get(old_key, [old_key])
        for t in targets:
            out[t] = dict(row)
    return out


def _rename_flags(table: dict, renames: dict[str, str]) -> dict:
    """For each parent-keyed row, rename flag keys per the map."""
    out = {}
    for parent, row in table.items():
        new_row = {}
        for k, v in row.items():
            new_row[renames.get(k, k)] = v
        out[parent] = new_row
    return out


def _rename_parents(table: dict, renames: dict[str, str]) -> dict:
    out = {}
    for parent, row in table.items():
        out[renames.get(parent, parent)] = row
    return out


def patch_axes(doc: dict) -> dict:
    for a in doc["axes"]:
        if a["name"] == "age_cohort":
            _drop_children_renormalize(a)
        if a["name"] in ("occupation", "class_of_worker"):
            a["verify_condition"] = {
                "field": "workforce_status",
                "values": ["Main_worker", "Marginal_worker"],
            }
        if a["name"] == "caste":
            # Declare verifier-only rollups so the verifier can map joint
            # sub-caste codes (UC_bhadralok, Mahishya_Sadgop_OBC, etc.) onto
            # axis leaves. These names are used in education_given_caste and
            # caste_given_religion's Hindu sub-caste structure.
            a["subgroup_rollups"] = {
                "Upper_caste_bhadralok": ["UC_bhadralok"],
                "OBC_specific": ["Mahishya_Sadgop_OBC"],
                "SC_total": ["Namasudra_Bagdi_SC", "Other_SC"],
                "Other_Hindu_middle_castes": ["Other_Hindu_middle"],
            }
    return doc


def patch_joints(doc: dict) -> dict:
    keep: list[dict] = []
    for j in doc["joints"]:
        # Drop joints whose parent axes don't exist in this AC
        if j["name"] in ("bilingual_given_media", "vote_given_welfare"):
            continue

        # ------------------------------------------------------------------
        # migration_given_religion — rename child categories to match axis
        if j["name"] == "migration_given_religion":
            j["table"] = _rename_flags(j["table"], {
                "Native_S24P": "Native",
                "WB_other_dist": "WB_other_district",
                "Other_state": "Other_Indian_state",
                "Out_migrant": "Seasonal_out_migrant",
                "Other": "Outside_India",
            })

        # ------------------------------------------------------------------
        # education_given_caste — rename parent codes to axis caste leaves;
        # expand abbreviated edu codes (Sec/HS/Grad/PG → Secondary/...)
        if j["name"] == "education_given_caste":
            edu_renames = {
                "Sec": "Secondary",
                "HS": "Higher_Secondary",
                "Grad": "Graduate",
                "PG": "Postgraduate",
            }
            j["table"] = _rename_flags(j["table"], edu_renames)
            # Now realign parent codes to axis leaves. The joint uses sub-
            # caste codes; the axis has SC_total / OBC_specific / etc. plus
            # Muslim (which is the same).
            old = j["table"]
            new_tbl = {}
            if "UC_bhadralok" in old:
                new_tbl["Upper_caste_bhadralok"] = old["UC_bhadralok"]
            if "Mahishya_Sadgop_OBC" in old:
                new_tbl["OBC_specific"] = old["Mahishya_Sadgop_OBC"]
            # SC_total: average Namasudra_Bagdi_SC + Other_SC (50/50)
            sc_rows = []
            for k in ("Namasudra_Bagdi_SC", "Other_SC"):
                if k in old:
                    sc_rows.append(old[k])
            if sc_rows:
                edu_keys = set()
                for r in sc_rows:
                    edu_keys.update(r.keys())
                avg = {}
                for ek in edu_keys:
                    vals = [r.get(ek, 0.0) for r in sc_rows]
                    avg[ek] = sum(vals) / len(vals)
                new_tbl["SC_total"] = avg
            if "Muslim" in old:
                new_tbl["Muslim"] = old["Muslim"]
            if "Other_Hindu_middle" in old:
                new_tbl["Other_Hindu_middle_castes"] = old["Other_Hindu_middle"]
            # ST_total + Christian_Other don't have rows; will be skipped (small)
            j["table"] = new_tbl

        # ------------------------------------------------------------------
        # education_given_age_gender — joint stores Male_grad / Female_grad
        # as flag rates. Expand compound age buckets into 5-yr cohorts.
        if j["name"] == "education_given_age_gender":
            j["table"] = _expand_age_buckets(j["table"], {
                "18_22": ["18_22"],
                "23_27": ["23_27"],
                "28_32": ["28_32"],
                "33_42": ["33_37", "38_42"],
                "43_57": ["43_47", "48_52", "53_57"],
                "58": ["58_62", "63_67", "68"],
            })
            j["use"] = "verifier_only"

        # ------------------------------------------------------------------
        # married_given_age_gender — expand compound age buckets to 5-yr.
        # Joint cells are Male_married / Female_married flag rates.
        if j["name"] == "married_given_age_gender":
            j["table"] = _expand_age_buckets(j["table"], {
                "18_22": ["18_22"],
                "23_27": ["23_27"],
                "28_32": ["28_32"],
                "33_47": ["33_37", "38_42", "43_47"],
                "48_62": ["48_52", "53_57", "58_62"],
                "63": ["63_67", "68"],
            })

        # ------------------------------------------------------------------
        # asset_given_occupation — rename parent codes to axis occupation
        # leaves + flag-name alignment in cells.
        if j["name"] == "asset_given_occupation":
            occ_renames = {
                "Ag_labourer": "Agricultural_labourer",
                "Fisher_pisciculture": "Fishing_pisciculture",
                "Govt_services": "Government_services_teachers",
                "Out_migrant": "Out_migrant",  # axis leaf is Out_migrant
            }
            j["table"] = _rename_parents(j["table"], occ_renames)

        # ------------------------------------------------------------------
        # FLAG-NAME ALIGNMENT — joint cells use abbreviated names; rename
        # to match the asset_media / amenities axis flag list.
        if j["name"] in ("asset_given_religion", "asset_given_gp",
                         "asset_given_occupation"):
            j["table"] = _rename_flags(j["table"], {
                "TV": "Television",
                "Smartphone_internet": "Smartphone_with_internet",
                "Banking": "Banking_access",
                "Mobile": "Mobile_phone",
            })
        if j["name"] == "amenities_given_gp":
            j["table"] = _rename_flags(j["table"], {
                "LPG": "LPG_clean_cooking_fuel",
                "Improved_water": "Improved_drinking_water_source",
                "Improved_sanitation": "Improved_sanitation",
                "Electricity": "Electricity",
            })

        # ------------------------------------------------------------------
        # GP-parented joints — rename parent values to U1/U2/U3 axis codes.
        if j["name"] in ("caste_given_gp", "asset_given_gp", "amenities_given_gp"):
            j["table"] = _rename_parents(j["table"], {
                "Muni": "U1_Diamond_Harbour_Municipality",
                "CDB_I_rural": "U2_CDB_I_rural_GP_share",
                "CDB_II_rural": "U3_CDB_II_rural_GP_share",
            })

        # ------------------------------------------------------------------
        # caste_given_gp — child cats need realignment to axis caste leaves.
        if j["name"] == "caste_given_gp":
            new_table = {}
            for parent_val, row in j["table"].items():
                # axis caste leaves: SC_total / ST_total / Upper_caste_bhadralok
                # / OBC_specific / Other_Hindu_middle_castes / Muslim /
                # Christian_Other
                new_row = {
                    "Upper_caste_bhadralok": row.get("UC", 0),
                    "SC_total": row.get("SC", 0),
                    "ST_total": row.get("ST", 0),
                    "OBC_specific": row.get("OBC_Mahishya", 0),
                    "Other_Hindu_middle_castes": row.get("Other_Hindu", 0),
                    "Muslim": row.get("Muslim", 0),
                }
                new_row = {k: v for k, v in new_row.items() if v > 0}
                if new_row:
                    new_table[parent_val] = new_row
            if new_table:
                j["table"] = new_table

        # ------------------------------------------------------------------
        # vote_given_caste — rename parent codes to axis caste leaves
        if j["name"] == "vote_given_caste":
            j["table"] = _rename_parents(j["table"], {
                "UC_bhadralok": "Upper_caste_bhadralok",
                "OBC": "OBC_specific",
                "SC": "SC_total",
                "Other_Hindu_middle": "Other_Hindu_middle_castes",
            })

        keep.append(j)
    doc["joints"] = keep
    return doc


def patch_aggregates(doc: dict) -> dict:
    """Align vote_2019_LS_share buckets with the parties produced by the
    vote conditional joints (BJP / AITC / CPI_LF / INC / Other).
    """
    for tgt in doc.get("aggregate_targets", []):
        if tgt.get("name") != "vote_2019_LS_share":
            continue
        new_buckets = []
        for b in tgt.get("buckets", []):
            name = b.get("name", "")
            if name == "CPI":
                # Map CPI(M) target to CPI_LF (which is what joint emits;
                # combined CPI(M)+LF bucket — the calibrated_2019 source CSV
                # only lists CPI(M) at 8.19% which is also the CPI_LF mass)
                b["vote_values"] = ["CPI_LF"]
                new_buckets.append(b)
            elif name == "Others":
                b["vote_values"] = ["Other"]
                new_buckets.append(b)
            elif name == "NOTA":
                # Vote conditional joints don't emit NOTA — drop bucket.
                continue
            else:
                new_buckets.append(b)
        tgt["buckets"] = new_buckets
    return doc


def main() -> None:
    print(f"Curating AC 143 structures at {SIM_DIR.relative_to(ROOT.parent)}\n")

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

    if AGG_PATH.exists():
        agg_doc = json.loads(AGG_PATH.read_text())
        agg_doc = patch_aggregates(agg_doc)
        AGG_PATH.write_text(json.dumps(agg_doc, indent=2, ensure_ascii=False))
        print(f"  ✓ patched {AGG_PATH.name}")

    print("\nRe-run baseline:")
    print("  python3 kaisim/simulations/wb_2021_ac143/generate.py baseline_rule")


if __name__ == "__main__":
    main()
