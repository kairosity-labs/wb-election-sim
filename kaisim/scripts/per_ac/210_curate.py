#!/usr/bin/env python3
"""
210_curate.py — hand-curate AC 210 (Nandigram) auto-built structures to align
joint parent codes / child cats with axis category codes.

Run AFTER build_ac_verifier_configs.py to fix the alignment issues that block
the verifier from passing budget.

Run:
    python3 kaisim/scripts/per_ac/210_curate.py
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SIM_DIR = ROOT / "simulations" / "wb_2021_ac210"
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
    axis["notes"] = ((axis.get("notes") or "")
                     + " [restricted to adults 18+ for Phase-2 voter sim]").strip()


def _expand_age_buckets(table: dict, expansion: dict[str, list[str]]) -> dict:
    out = {}
    for old_key, row in table.items():
        targets = expansion.get(old_key, [old_key])
        for t in targets:
            out[t] = dict(row)
    return out


def _rename_keys(d: dict, renames: dict[str, str]) -> dict:
    return {renames.get(k, k): v for k, v in d.items()}


def _rename_flags(table: dict, renames: dict[str, str]) -> dict:
    out = {}
    for parent, row in table.items():
        if isinstance(row, dict):
            out[parent] = _rename_keys(row, renames)
        else:
            out[parent] = row
    return out


# ---- Renames ----

# Migration child-cat renames. Axis cats: Native, WB_other_district,
# Other_Indian_state, Bangladesh_origin, Outside_India, Out_migrant
MIGRATION_CHILD_RENAMES = {
    "WB_other_dist": "WB_other_district",
    "Other_state": "Other_Indian_state",
    "Bangladesh": "Bangladesh_origin",
}

# Asset_media child-flag renames. Axis flags: Television, Radio, Mobile_phone,
# Smartphone_with_internet, Computer, Two_wheeler, Four_wheeler, Banking_access
ASSET_FLAG_RENAMES = {
    "TV": "Television",
    "Smartphone_internet": "Smartphone_with_internet",
    "Banking": "Banking_access",
    "Mobile": "Mobile_phone",
    "Two_wheeler": "Two_wheeler",
    "Four_wheeler": "Four_wheeler",
    "Computer": "Computer",
}

# Amenities flag renames.
AMENITIES_FLAG_RENAMES = {
    "LPG": "LPG_clean_cooking_fuel",
    "Improved_sanitation": "Improved_sanitation",
    "Improved_water": "Improved_drinking_water_source",
    "Electricity": "Electricity",
    "Wood_biomass": "Wood_biomass_fuel",
    "Other_fuel": "Other_fuel",
}

# Education child-cat renames (for joints whose child is `education`).
# Axis cats: Illiterate, Primary, Middle, Secondary, Higher_Secondary,
#            Graduate, Postgraduate
EDUCATION_CHILD_RENAMES = {
    "Sec": "Secondary",
    "HS": "Higher_Secondary",
    "Grad": "Graduate",
    "PG": "Postgraduate",
}

# Caste parent renames (for education_given_caste, vote_given_caste).
# Axis cats: SC_total, ST_total, Mahishya, Tili_Teli,
#            Kayastha_Brahmin_UC_bhadralok, Other_Hindu_middle_castes,
#            Muslim, Christian_Other
CASTE_PARENT_RENAMES = {
    "UC_bhadralok": "Kayastha_Brahmin_UC_bhadralok",
    "Tili_OBC": "Tili_Teli",
    "Bagdi": "SC_total",        # Bagdi rolls up to SC_total
    "Namasudra": "SC_total",    # Namasudra rolls up to SC_total
    "Other_SC_ST": "SC_total",  # Generic SC/ST, biased toward SC
    "Other_SC": "SC_total",
    # Mahishya, Muslim unchanged
}

# Occupation parent renames (for asset_given_occupation).
# Axis cats: Cultivator, Agricultural_labourer, Household_industry,
#            Manufacturing, Construction, Trade_retail, Transport_fishing,
#            Services, Government_services_teachers
OCCUPATION_PARENT_RENAMES = {
    "Ag_labourer": "Agricultural_labourer",
    "Govt_services": "Government_services_teachers",
}

# GP parent renames — joint table uses Nandigram_I/Nandigram_II but axis
# uses U1_Nandigram_I_CDB / U2_Nandigram_II_CDB.
GP_PARENT_RENAMES = {
    "Nandigram_I": "U1_Nandigram_I_CDB",
    "Nandigram_II": "U2_Nandigram_II_CDB",
}


def patch_axes(doc: dict) -> dict:
    for a in doc["axes"]:
        if a["name"] == "age_cohort":
            _drop_children_renormalize(a)
        if a["name"] in ("occupation", "class_of_worker"):
            # These marginals are "% of workers", not "% of all personas".
            a["verify_condition"] = {
                "field": "workforce_status",
                "values": ["Main_worker", "Marginal_worker"],
            }
        if a["name"] == "caste":
            # Declare verifier-only rollups: sub-codes used in joints
            a["subgroup_rollups"] = {
                "SC_total": ["Bagdi", "Namasudra", "Bauri", "Other_SC",
                             "Other_SC_ST"],
                "ST_total": ["ST"],
                "Kayastha_Brahmin_UC_bhadralok": ["UC_bhadralok"],
                "Tili_Teli": ["Tili_OBC"],
            }
    return doc


def patch_joints(doc: dict) -> dict:
    keep: list[dict] = []
    for j in doc["joints"]:
        # ----- Drop joints whose parent axes don't exist -----
        if j["name"] in ("bilingual_given_media", "vote_given_welfare"):
            continue

        # ----- migration_given_religion: rename child cats -----
        if j["name"] == "migration_given_religion":
            j["table"] = _rename_flags(j["table"], MIGRATION_CHILD_RENAMES)

        # ----- asset_given_religion / asset_given_gp / asset_given_occupation:
        #       rename flag names ------
        if j["name"] in ("asset_given_religion", "asset_given_gp",
                         "asset_given_occupation"):
            j["table"] = _rename_flags(j["table"], ASSET_FLAG_RENAMES)

        # ----- asset_given_occupation: rename parent occ codes -----
        if j["name"] == "asset_given_occupation":
            j["table"] = _rename_keys(j["table"], OCCUPATION_PARENT_RENAMES)

        # ----- amenities_given_gp: rename flag names + parent GP codes -----
        if j["name"] == "amenities_given_gp":
            j["table"] = _rename_flags(j["table"], AMENITIES_FLAG_RENAMES)
            j["table"] = _rename_keys(j["table"], GP_PARENT_RENAMES)

        # ----- caste_given_gp: parent rename + child caste rename -----
        if j["name"] == "caste_given_gp":
            # First, collapse compound child cats onto axis leaves.
            new_table = {}
            for parent_val, row in j["table"].items():
                sc = row.get("SC", 0)
                st = row.get("ST", 0)
                mahishya = row.get("Mahishya", 0)
                uc = row.get("UC", 0)
                other_hindu = row.get("Other_Hindu", 0)
                muslim = row.get("Muslim", 0)
                # Other_Hindu in this AC = Tili_Teli (3pp) + Other_Hindu_middle (~22pp)
                # Total Hindu = ~73.51% with Tili 3pp, Other 21.95pp.
                # So Other_Hindu in joint splits: ~12% Tili, ~88% Other_Hindu_middle
                tili_share = 0.12
                ohm_share = 0.88
                tili = other_hindu * tili_share
                ohm = other_hindu * ohm_share
                new_row = {
                    "SC_total": sc, "ST_total": st, "Mahishya": mahishya,
                    "Kayastha_Brahmin_UC_bhadralok": uc,
                    "Tili_Teli": tili,
                    "Other_Hindu_middle_castes": ohm,
                    "Muslim": muslim,
                }
                # Drop zeros
                new_row = {k: v for k, v in new_row.items() if v > 0}
                if new_row:
                    new_table[parent_val] = new_row
            # Then rename parent GP codes.
            new_table = _rename_keys(new_table, GP_PARENT_RENAMES)
            j["table"] = new_table

        # ----- asset_given_gp: rename parent GP codes -----
        if j["name"] == "asset_given_gp":
            j["table"] = _rename_keys(j["table"], GP_PARENT_RENAMES)

        # ----- caste_given_religion: child cats look mostly OK; verify -----
        # The Hindu row has: Mahishya, Tili_Teli, SC_total, ST_total,
        # Other_Hindu_middle_castes — all match axis. UC_bhadralok dropped
        # (note in joint says "Unmapped: UC bhadralok"). Add it back.
        if j["name"] == "caste_given_religion":
            hindu_row = j["table"].get("Hindu", {})
            # Add UC and rebalance: UC ~= 6.8% of Hindu (from MD).
            if "Kayastha_Brahmin_UC_bhadralok" not in hindu_row:
                hindu_row["Kayastha_Brahmin_UC_bhadralok"] = 6.8
                # Slightly reduce Other to compensate (was 29.9 → 23.1)
                if "Other_Hindu_middle_castes" in hindu_row:
                    hindu_row["Other_Hindu_middle_castes"] = max(
                        hindu_row["Other_Hindu_middle_castes"] - 6.8, 0)
                j["table"]["Hindu"] = hindu_row

        # ----- education_given_caste: rename parent caste + child education -----
        if j["name"] == "education_given_caste":
            # First, collapse SC sub-codes (Bagdi, Namasudra, Other_SC_ST)
            # by averaging into a single SC_total row.
            old = j["table"]
            sc_rows = [old.get("Bagdi"), old.get("Namasudra"),
                       old.get("Other_SC_ST")]
            sc_rows = [r for r in sc_rows if r]
            new_table = {}
            for parent_key, row in old.items():
                if parent_key in ("Bagdi", "Namasudra", "Other_SC_ST"):
                    continue  # handled below
                new_parent = CASTE_PARENT_RENAMES.get(parent_key, parent_key)
                new_table[new_parent] = dict(row)
            if sc_rows:
                # Average row values across SC sub-codes.
                merged = {}
                keys = set()
                for r in sc_rows:
                    keys |= set(r.keys())
                for k in keys:
                    vals = [r.get(k, 0) for r in sc_rows]
                    merged[k] = sum(vals) / len(sc_rows)
                new_table["SC_total"] = merged
            # Rename child education cats (Sec→Secondary, etc.)
            new_table = _rename_flags(new_table, EDUCATION_CHILD_RENAMES)
            # Add ST_total + Other_Hindu_middle_castes + Christian_Other rows
            # so the joint covers all axis castes.
            if "ST_total" not in new_table:
                new_table["ST_total"] = dict(new_table.get("SC_total", {
                    "Illiterate": 22.0, "Primary": 28.0, "Middle": 22.0,
                    "Secondary": 14.0, "Higher_Secondary": 8.0,
                    "Graduate": 5.0, "Postgraduate": 1.0,
                }))
            if "Other_Hindu_middle_castes" not in new_table:
                # Same pattern as Mahishya (general caste)
                new_table["Other_Hindu_middle_castes"] = dict(
                    new_table.get("Mahishya", {
                        "Illiterate": 11.0, "Primary": 21.0, "Middle": 22.0,
                        "Secondary": 19.0, "Higher_Secondary": 13.0,
                        "Graduate": 10.0, "Postgraduate": 4.0,
                    }))
            if "Christian_Other" not in new_table:
                new_table["Christian_Other"] = dict(
                    new_table.get("Mahishya", {
                        "Illiterate": 9.0, "Primary": 20.0, "Middle": 23.0,
                        "Secondary": 20.0, "Higher_Secondary": 14.0,
                        "Graduate": 11.0, "Postgraduate": 3.0,
                    }))
            j["table"] = new_table

        # ----- vote_given_religion: align Hindu AITC + INC to AC-level targets ----
        # AC targets: AITC 63.14, BJP 30.09, CPI 4.52, INC 0.86, BSP 0.44,
        # NOTA 0.59, Other 1.05. Joint default values were too BJP-Hindu /
        # too INC-everywhere given final AC result. Recompute Hindu row to
        # reconcile macro AITC and INC, with Muslim row left as-is (it's
        # already near-block-AITC).
        if j["name"] == "vote_given_religion":
            # Hindu mass: 73.51%, Muslim mass: 26.35%. Other: 0.14%.
            # AITC: 63.14 = 0.7351*h_aitc + 0.2635*82 → h_aitc = 56.5
            # BJP: 30.09 = 0.7351*h_bjp + 0.2635*3 → h_bjp = 30.0
            # CPI/LF: 4.52 = 0.7351*h_lf + 0.2635*6 → h_lf = 4.0
            # INC: 0.86 = 0.7351*h_inc + 0.2635*8 → h_inc = -1.7 (impossible)
            #   → push Muslim INC down to 1; then h_inc = 0.7
            # Recalc Muslim: AITC 82, BJP 3, LF 6, INC 1, Other 8 (was 1)
            # Hindu: AITC 56.5, BJP 30, LF 4, INC 0.7, Other 8.8 (residual)
            if "Hindu" in j["table"]:
                j["table"]["Hindu"] = {
                    "AITC": 56.5, "BJP": 30.0, "LF": 4.0,
                    "INC": 0.7, "Other": 8.8,
                }
            if "Muslim" in j["table"]:
                j["table"]["Muslim"] = {
                    "AITC": 82.0, "BJP": 3.0, "LF": 6.0,
                    "INC": 1.0, "Other": 8.0,
                }
            if "Other" in j["table"]:
                j["table"]["Other"] = {
                    "AITC": 50.0, "BJP": 30.0, "LF": 5.0,
                    "INC": 5.0, "Other": 10.0,
                }

        # ----- vote_given_caste: rename parent caste codes + add missing rows ----
        if j["name"] == "vote_given_caste":
            old = j["table"]
            sc_rows = [old.get("Bagdi"), old.get("Other_SC")]
            sc_rows = [r for r in sc_rows if r]
            new_table = {}
            for parent_key, row in old.items():
                if parent_key in ("Bagdi", "Other_SC"):
                    continue
                new_parent = CASTE_PARENT_RENAMES.get(parent_key, parent_key)
                new_table[new_parent] = dict(row)
            if sc_rows:
                merged = {}
                keys = set()
                for r in sc_rows:
                    keys |= set(r.keys())
                for k in keys:
                    vals = [r.get(k, 0) for r in sc_rows]
                    merged[k] = sum(vals) / len(sc_rows)
                new_table["SC_total"] = merged
            # Add missing axis cats
            if "ST_total" not in new_table:
                new_table["ST_total"] = dict(new_table.get("SC_total", {
                    "BJP": 38.0, "AITC": 50.0, "INC": 5.0,
                    "LF": 5.0, "Other": 2.0,
                }))
            if "Other_Hindu_middle_castes" not in new_table:
                new_table["Other_Hindu_middle_castes"] = dict(
                    new_table.get("Mahishya", {
                        "BJP": 35.0, "AITC": 52.0, "INC": 5.0,
                        "LF": 6.0, "Other": 2.0,
                    }))
            if "Christian_Other" not in new_table:
                new_table["Christian_Other"] = {
                    "BJP": 30.0, "AITC": 50.0, "INC": 10.0,
                    "LF": 5.0, "Other": 5.0,
                }
            # Scale INC down across all caste rows to match AC target ~0.86%.
            # Excess INC redirected to AITC (dominant local party).
            for caste_key, row in new_table.items():
                if not isinstance(row, dict):
                    continue
                inc = row.get("INC", 0)
                if inc > 1.5:
                    excess = inc - 1.0
                    row["INC"] = 1.0
                    if "AITC" in row:
                        row["AITC"] = row["AITC"] + excess
            j["table"] = new_table

        # ----- vote_given_gender: scale INC + align AITC to macro target -----
        if j["name"] == "vote_given_gender":
            # AC targets: AITC 63.14, BJP 30.09, INC 0.86. Default joint had
            # Male AITC 57 / Female AITC 67, INC 4 / 3 — INC too high.
            # Compute mean: 0.5*57 + 0.5*67 = 62. Close enough to 63.14.
            # Scale INC to 1; redirect to AITC.
            for parent, row in j["table"].items():
                if not isinstance(row, dict):
                    continue
                inc = row.get("INC", 0)
                if inc > 1.5:
                    excess = inc - 1.0
                    row["INC"] = 1.0
                    if "AITC" in row:
                        row["AITC"] = row["AITC"] + excess

        # ----- married_given_age_gender: expand compound buckets -----
        if j["name"] == "married_given_age_gender":
            j["table"] = _expand_age_buckets(j["table"], {
                "18_22": ["18_22"],
                "23_27": ["23_27"],
                "28_32": ["28_32"],
                "33_47": ["33_37", "38_42", "43_47"],
                "48_62": ["48_52", "53_57", "58_62"],
                "63": ["63_67", "68"],
            })
            # Mirror Male_married → Male and Female_married → Female so
            # the AC-specific marital plugin can read them; keep originals
            # too so verifier can interpret as flag-rate (not strictly
            # required since the plugin sets marital_status via marginal).
            for k, row in j["table"].items():
                if isinstance(row, dict):
                    if "Male_married" in row and "Male" not in row:
                        row["Male"] = row["Male_married"]
                    if "Female_married" in row and "Female" not in row:
                        row["Female"] = row["Female_married"]
            # Mark verifier_only — the plugin handles marital sampling
            # and the joint's flag-rate semantics doesn't cleanly map to
            # the partition-axis verifier flow.
            j["use"] = "verifier_only"

        # ----- education_given_age_gender: expand + mark verifier_only -----
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
    print(f"Curating AC 210 structures at {SIM_DIR.relative_to(ROOT.parent)}\n")

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
    print("  python3 kaisim/simulations/wb_2021_ac210/generate.py baseline_rule")


if __name__ == "__main__":
    main()
