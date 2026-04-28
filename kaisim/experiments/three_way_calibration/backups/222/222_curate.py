#!/usr/bin/env python3
"""
222_curate.py — hand-curate AC 222 (Jhargram) auto-built structures
to align joint parent/child codes with axis category codes.

Jhargram is the heart of WB's Jangalmahal — a tribal-majority Adivasi
region with:
  - **Sarna/ORP** as a 4th religion (~10.9%); the axis has 5 religions
    (Hindu, Muslim, Sarna_ORP, Christian, Other_not_stated).
  - 5 mother-tongues: Bengali / Santali / Mundari / Kurmali / Hindi /
    Other.
  - Tribal sub-castes (Santhal/Munda/Bhumij/Lodha/Ho) load-bearing under
    ST_total; OBC dominated by Mahato/Kurmi.

Fixes applied:
  1. age_cohort: drop child cohorts (0_4..15_17), renormalize.
  2. occupation/class_of_worker: verify_condition (workers only).
  3. caste subgroup_rollups so ST_total covers the tribal sub-leaves.
  4. Drop joints whose parent axes don't exist (bilingual_given_media,
     vote_given_welfare).
  5. religion_given_gp: parent rename U2_Jhargram_CDB_4GP_rural →
     U2_Jhargram_CDB_4GP_rural_share so it matches the gp_location axis.
  6. caste_given_religion: rebuild rows so parent keys match all 5
     religions (axis has Sarna_ORP, Christian, Other_not_stated; auto-
     builder produced Hindu/Muslim/Other only).
  7. migration_given_religion: child rename WB_other_dist→WB_other_district,
     Other_state_Jharkhand split (5 children) → Other_Indian_state +
     Jharkhand_origin, Bangladesh→Bangladesh_origin.  Add Other_not_stated
     and Sarna_ORP-Christian rows kept.
  8. lang_given_religion: add Other_not_stated row (clone Hindu) so we
     don't drop personas of that religion.
  9. asset_given_religion: rename flag keys (TV→Television,
     Smartphone_internet→Smartphone_with_internet, Banking→Banking_access);
     add Other_not_stated row.
 10. asset_given_occupation: rename parent codes (Ag_labourer →
     Agricultural_labourer, Forest_produce_collector →
     Forest_produce_collection, Govt_services_teachers →
     Government_services_teachers_health_workers, Out_migrant →
     Out_migrant_remittance_worker), rename flag keys.
 11. caste_given_gp / asset_given_gp / amenities_given_gp: rename gp
     parents (Jhargram_Muni → U1_Jhargram_Municipality, Jhargram_CDB_rural
     → U2_Jhargram_CDB_4GP_rural_share, Binpur_I → U3_Binpur_I_CD_Block).
 12. caste_given_gp: child realignment to axis caste leaves
     (UC → UC_bhadralok, OBC_Mahato → OBC, SC → SC_total, ST → ST_total,
     Other_Hindu → Other_Hindu_middle_castes, Muslim → Muslim).
 13. asset_given_gp / amenities_given_gp: flag-key renames.
 14. education_given_caste: parent rename + child rename
     (Sec→Secondary etc.).
 15. married_given_age_gender / education_given_age_gender: expand
     compound age buckets to 5-year cohorts.
 16. vote_given_caste: parent rename to caste-axis leaves.
 17. vote_given_religion: drop Other_religion parent; ensure all 5
     religions present.

Run:
    python3 scripts/per_ac/222_curate.py
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SIM_DIR = ROOT / "simulations" / "wb_2021_ac222"
AXES_PATH = SIM_DIR / "structures" / "axes.json"
JOINTS_PATH = SIM_DIR / "structures" / "joints.json"


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
    out = {}
    for old_key, row in table.items():
        targets = expansion.get(old_key, [old_key])
        for t in targets:
            out[t] = dict(row)
    return out


def _rename_flags(table: dict, renames: dict[str, str]) -> dict:
    out = {}
    for parent, row in table.items():
        new_row = {}
        for k, v in row.items():
            new_row[renames.get(k, k)] = v
        out[parent] = new_row
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
            # Tribal sub-castes (in subgroup_rollups already) plus declare
            # additional rollups so any joint key lands in the axis.
            a["subgroup_rollups"] = {
                "ST_total": ["Santhal", "Munda", "Bhumij", "Lodha", "Ho",
                             "Other_ST", "ST_Santhal", "ST_Munda_Ho",
                             "ST_Bhumij", "ST_Lodha"],
                "SC_total": ["Bagdi", "Bauri", "Hari", "Chamar_Mochi",
                             "Other_SC", "SC_Bagdi_Bauri"],
                "OBC": ["OBC_Mahato_Kurmi", "OBC_Mahato"],
                "Other_Hindu_middle_castes": ["Other_Hindu_middle",
                                                "Other_Hindu"],
            }
    return doc


# Map joint gp_location parent codes → axis leaves
GP_PARENT_RENAMES = {
    "Jhargram_Muni": "U1_Jhargram_Municipality",
    "Jhargram_CDB_rural": "U2_Jhargram_CDB_4GP_rural_share",
    "U2_Jhargram_CDB_4GP_rural": "U2_Jhargram_CDB_4GP_rural_share",
    "Binpur_I": "U3_Binpur_I_CD_Block",
}

# Education child code aliases
EDU_CHILD_RENAMES = {
    "Sec": "Secondary",
    "HS": "Higher_Secondary",
    "Grad": "Graduate",
    "PG": "Postgraduate",
}

# Caste-axis-leaf aliases for joint parent codes (used in education_given_caste,
# vote_given_caste). Multiple sub-codes map to the same leaf ⇒ they get merged.
CASTE_PARENT_ALIASES = {
    "UC_bhadralok": "UC_bhadralok",
    "OBC_Mahato_Kurmi": "OBC",
    "OBC_Mahato": "OBC",
    "SC_Bagdi_Bauri": "SC_total",
    "ST_Santhal": "ST_total",
    "ST_Munda_Ho": "ST_total",
    "ST_Bhumij": "ST_total",
    "ST_Lodha": "ST_total",
    "Muslim": "Muslim",
    "Other_Hindu_middle": "Other_Hindu_middle_castes",
    "Other_Hindu": "Other_Hindu_middle_castes",
    "Christian": "Christian_Other",
    "Christian_Other": "Christian_Other",
}


def _alias_parent_keys(table: dict, alias_map: dict[str, str]) -> dict:
    """Rename top-level parent keys; merge if collision (average)."""
    out: dict = {}
    counts: dict[str, int] = {}
    for k, row in table.items():
        new_k = alias_map.get(k, k)
        if new_k in out and isinstance(row, dict) and isinstance(out[new_k], dict):
            # Merge: running mean
            n = counts[new_k]
            merged = {}
            keys = set(out[new_k]) | set(row)
            for kk in keys:
                merged[kk] = (out[new_k].get(kk, 0.0) * n + row.get(kk, 0.0)) / (n + 1)
            out[new_k] = merged
            counts[new_k] = n + 1
        else:
            out[new_k] = dict(row) if isinstance(row, dict) else row
            counts[new_k] = 1
    return out


# Caste-axis leaves for caste_given_religion expansion
CASTE_AXIS_LEAVES = ["ST_total", "SC_total", "UC_bhadralok", "OBC",
                       "Other_Hindu_middle_castes", "Muslim", "Christian_Other"]


def patch_joints(doc: dict) -> dict:
    keep: list[dict] = []
    for j in doc["joints"]:
        # Drop joints whose parent axes don't exist in this AC
        if j["name"] in ("bilingual_given_media", "vote_given_welfare"):
            continue

        # ------------------------------------------------------------------
        # caste_given_religion — Sarna_ORP / Christian / Other_not_stated
        # Re-derived from marginals: Hindu (84.04%), Sarna_ORP (10.9%) so
        # P(ST | Hindu) needs to fill the gap.  Caste marginal targets:
        #   ST_total 22.92, SC_total 19.52, UC 6.5, OBC 12.0,
        #   Other_Hindu_middle 34.0, Muslim 3.44, Christian_Other 1.62.
        # Solving with Sarna_ORP→ST 92, Christian→Christian_Other 100:
        #   P(X | Hindu) = (target_X − P(X | Sarna)*0.109 − ...) / 0.8404
        # ST: (22.92 − 92*0.109) / 84.04 = 12.4   → Hindu ST 12.4
        # SC: 19.52 / 84.04 = 23.2 (SC almost all Hindu)
        # UC: 6.5 / 84.04 = 7.7
        # OBC: (12 − 5*0.109) / 84.04 = 13.6
        # Other_Hindu_middle: (34 − 3*0.109) / 84.04 = 40.0
        # ------------------------------------------------------------------
        if j["name"] == "caste_given_religion":
            new_table: dict = {}
            # Hindu row — re-derived from marginals
            new_table["Hindu"] = {
                "ST_total": 12.4,
                "SC_total": 23.2,
                "UC_bhadralok": 7.7,
                "OBC": 13.6,
                "Other_Hindu_middle_castes": 43.1,
            }
            # Muslim
            new_table["Muslim"] = {"Muslim": 100.0}
            # Sarna_ORP — overwhelmingly tribal
            new_table["Sarna_ORP"] = {
                "ST_total": 92.0,
                "OBC": 5.0,
                "Other_Hindu_middle_castes": 3.0,
            }
            # Christian — Adivasi Christians (Santhal/Munda evangelized)
            new_table["Christian"] = {
                "Christian_Other": 100.0,
            }
            # Other_not_stated → bucket as Christian_Other
            new_table["Other_not_stated"] = {
                "Christian_Other": 100.0,
            }
            j["table"] = new_table

        # ------------------------------------------------------------------
        # migration_given_religion — rebuild table from axis marginal.
        # migration marginal: Native 84, WB_other_district 6,
        # Other_Indian_state 4, Jharkhand_origin 3, Bangladesh_origin 1.5,
        # Out_migrant 1.5. Religion mass: Hindu 84, Muslim 3.4, Sarna 10.9,
        # Christian 0.43, Other 1.19.
        # ------------------------------------------------------------------
        if j["name"] == "migration_given_religion":
            j["table"] = {
                "Hindu": {
                    "Native": 84.0, "WB_other_district": 6.5,
                    "Other_Indian_state": 4.5, "Jharkhand_origin": 2.0,
                    "Bangladesh_origin": 1.5, "Out_migrant": 1.5,
                },
                "Sarna_ORP": {
                    "Native": 80.0, "WB_other_district": 3.0,
                    "Other_Indian_state": 2.0, "Jharkhand_origin": 12.0,
                    "Bangladesh_origin": 0.5, "Out_migrant": 2.5,
                },
                "Muslim": {
                    "Native": 88.0, "WB_other_district": 5.0,
                    "Other_Indian_state": 3.0, "Jharkhand_origin": 1.0,
                    "Bangladesh_origin": 2.0, "Out_migrant": 1.0,
                },
                "Christian": {
                    "Native": 78.0, "WB_other_district": 8.0,
                    "Other_Indian_state": 5.0, "Jharkhand_origin": 5.0,
                    "Bangladesh_origin": 2.0, "Out_migrant": 2.0,
                },
                "Other_not_stated": {
                    "Native": 82.0, "WB_other_district": 6.0,
                    "Other_Indian_state": 5.0, "Jharkhand_origin": 3.0,
                    "Bangladesh_origin": 1.5, "Out_migrant": 2.5,
                },
            }

        # ------------------------------------------------------------------
        # lang_given_religion — rebuild rows so marginal hits target.
        # mother_tongue marginal: Bengali 81.5, Santali 16.0, Mundari 1.5,
        # Kurmali 0.5, Hindi 0.3, Other 0.2.
        # Weighted decomposition (84.04 Hindu, 3.44 Muslim, 10.9 Sarna,
        # 0.43 Christian, 1.19 Other_not_stated):
        #   Hindu: Bengali 93, Santali 5, Mundari 0.5, Kurmali 0.5,
        #          Hindi 0.5, Other 0.5
        #   Sarna: Bengali 16, Santali 75, Mundari 6, Kurmali 2, Other 1
        #   Muslim: Bengali 95, Hindi 4, Other 1
        #   Christian: Bengali 60, Santali 25, Mundari 10, Other 5
        # ------------------------------------------------------------------
        if j["name"] == "lang_given_religion":
            # Solve for Hindu rates so weighted marginal hits target.
            # mother_tongue marginal: Bengali 81.5 / Santali 16.0 /
            # Mundari 1.5 / Kurmali 0.5 / Hindi 0.3 / Other 0.2.
            # Religion mass: Hindu 84.04 / Muslim 3.44 / Sarna 10.9 /
            # Christian 0.43 / Other 1.19.
            j["table"] = {
                "Hindu": {"Bengali": 89.5, "Santali": 9.0, "Mundari": 0.6,
                            "Kurmali": 0.4, "Hindi": 0.3, "Other": 0.2},
                "Sarna_ORP": {"Bengali": 13.0, "Santali": 79.0, "Mundari": 5.0,
                                "Kurmali": 2.5, "Hindi": 0.0, "Other": 0.5},
                "Muslim": {"Bengali": 95.5, "Hindi": 4.0, "Other": 0.5},
                "Christian": {"Bengali": 60.0, "Santali": 25.0,
                                "Mundari": 12.0, "Hindi": 1.0, "Other": 2.0},
                "Other_not_stated": {"Bengali": 92.0, "Santali": 5.0,
                                       "Hindi": 2.0, "Other": 1.0},
            }

        # ------------------------------------------------------------------
        # asset_given_religion — flag renames + missing religions
        # ------------------------------------------------------------------
        if j["name"] == "asset_given_religion":
            if "Other_not_stated" not in j["table"] and "Hindu" in j["table"]:
                j["table"]["Other_not_stated"] = dict(j["table"]["Hindu"])
            j["table"] = _rename_flags(j["table"], {
                "TV": "Television",
                "Smartphone_internet": "Smartphone_with_internet",
                "Banking": "Banking_access",
            })

        # ------------------------------------------------------------------
        # asset_given_occupation — parent + flag renames
        # ------------------------------------------------------------------
        if j["name"] == "asset_given_occupation":
            old = j["table"]
            renames = {
                "Ag_labourer": "Agricultural_labourer",
                "Forest_produce_collector": "Forest_produce_collection",
                "Govt_services_teachers": "Government_services_teachers_health_workers",
                "Out_migrant": "Out_migrant_remittance_worker",
            }
            new = {}
            for k, v in old.items():
                new[renames.get(k, k)] = v
            j["table"] = _rename_flags(new, {
                "TV": "Television",
                "Smartphone_internet": "Smartphone_with_internet",
                "Banking": "Banking_access",
                "Computer": "Computer",
            })

        # ------------------------------------------------------------------
        # religion_given_gp — gp parent rename + add Other_not_stated row
        # ------------------------------------------------------------------
        if j["name"] == "religion_given_gp":
            new_table = {}
            for parent_val, row in j["table"].items():
                new_parent = GP_PARENT_RENAMES.get(parent_val, parent_val)
                new_row = dict(row)
                # Add Other_not_stated mass per axis marginal (~1.19% pop)
                # so the religion axis can hit the Other_not_stated target.
                # Empirically: Muni 0.34, CDB 0.61, Binpur 2.35 (per MD).
                if "U1" in new_parent:
                    new_row["Other_not_stated"] = 0.34
                elif "U2" in new_parent:
                    new_row["Other_not_stated"] = 0.61
                elif "U3" in new_parent:
                    new_row["Other_not_stated"] = 2.35
                new_table[new_parent] = new_row
            j["table"] = new_table

        # ------------------------------------------------------------------
        # caste_given_gp — gp parent rename + child realignment
        # ------------------------------------------------------------------
        if j["name"] == "caste_given_gp":
            new_table = {}
            for parent_val, row in j["table"].items():
                new_parent = GP_PARENT_RENAMES.get(parent_val, parent_val)
                # Realign: UC, OBC_Mahato, SC, ST, Other_Hindu, Muslim
                new_row = {
                    "UC_bhadralok": row.get("UC", 0),
                    "OBC": row.get("OBC_Mahato", row.get("OBC", 0)),
                    "SC_total": row.get("SC", 0),
                    "ST_total": row.get("ST", 0),
                    "Other_Hindu_middle_castes": row.get("Other_Hindu", 0),
                    "Muslim": row.get("Muslim", 0),
                }
                new_row = {k: v for k, v in new_row.items() if v > 0}
                if new_row:
                    new_table[new_parent] = new_row
            j["table"] = new_table

        # ------------------------------------------------------------------
        # asset_given_gp — gp parent + flag renames
        # ------------------------------------------------------------------
        if j["name"] == "asset_given_gp":
            new_table = {}
            for k, v in j["table"].items():
                new_table[GP_PARENT_RENAMES.get(k, k)] = v
            j["table"] = _rename_flags(new_table, {
                "TV": "Television",
                "Smartphone_internet": "Smartphone_with_internet",
                "Banking": "Banking_access",
                "Computer": "Computer",
            })

        # ------------------------------------------------------------------
        # amenities_given_gp — gp parent + flag renames
        # ------------------------------------------------------------------
        if j["name"] == "amenities_given_gp":
            new_table = {}
            for k, v in j["table"].items():
                new_table[GP_PARENT_RENAMES.get(k, k)] = v
            j["table"] = _rename_flags(new_table, {
                "LPG": "LPG_clean_cooking_fuel",
                "Improved_sanitation": "Improved_sanitation",
                "Improved_water": "Improved_drinking_water_source",
                "Electricity": "Electricity",
            })

        # ------------------------------------------------------------------
        # education_given_caste — parent + child aliases
        # ------------------------------------------------------------------
        if j["name"] == "education_given_caste":
            j["table"] = _alias_parent_keys(j["table"], CASTE_PARENT_ALIASES)
            j["table"] = _rename_flags(j["table"], EDU_CHILD_RENAMES)

        # ------------------------------------------------------------------
        # vote_given_caste — parent aliases
        # ------------------------------------------------------------------
        if j["name"] == "vote_given_caste":
            j["table"] = _alias_parent_keys(j["table"], CASTE_PARENT_ALIASES)
            # Make sure Christian_Other exists (clone ST_total which votes
            # similarly for Adivasi Christians)
            if ("Christian_Other" not in j["table"]
                    and "ST_total" in j["table"]):
                j["table"]["Christian_Other"] = dict(j["table"]["ST_total"])

        # ------------------------------------------------------------------
        # vote_given_religion — drop Other_religion; clone for missing
        # ------------------------------------------------------------------
        if j["name"] == "vote_given_religion":
            j["table"] = {k: v for k, v in j["table"].items()
                          if k != "Other_religion"}
            # Add Other_not_stated row by cloning Hindu
            if ("Other_not_stated" not in j["table"]
                    and "Hindu" in j["table"]):
                j["table"]["Other_not_stated"] = dict(j["table"]["Hindu"])

        # ------------------------------------------------------------------
        # married_given_age_gender — expand compound age buckets
        # ------------------------------------------------------------------
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
        # education_given_age_gender — expand compound age buckets +
        # mark verifier_only
        # ------------------------------------------------------------------
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

        keep.append(j)
    doc["joints"] = keep
    return doc


def main() -> None:
    print(f"Curating AC 222 structures at {SIM_DIR.relative_to(ROOT.parent)}\n")

    axes_doc = json.loads(AXES_PATH.read_text())
    axes_doc = patch_axes(axes_doc)
    AXES_PATH.write_text(json.dumps(axes_doc, indent=2, ensure_ascii=False))
    print(f"  patched {AXES_PATH.name}")

    joints_doc = json.loads(JOINTS_PATH.read_text())
    n_before = len(joints_doc["joints"])
    joints_doc = patch_joints(joints_doc)
    n_after = len(joints_doc["joints"])
    JOINTS_PATH.write_text(json.dumps(joints_doc, indent=2, ensure_ascii=False))
    print(f"  patched {JOINTS_PATH.name} ({n_before} -> {n_after} joints)")

    print("\nRe-run baseline:")
    print("  python3 simulations/wb_2021_ac222/generate.py baseline_rule")


if __name__ == "__main__":
    main()
