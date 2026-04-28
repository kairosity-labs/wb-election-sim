#!/usr/bin/env python3
"""
064_curate.py — hand-curate AC 064 (Murshidabad) auto-built structures
to align joint parent/child codes with axis category codes.

Fixes applied:
  1. age_cohort: drop child cohorts (0_4..15_17), renormalize.
  2. occupation/class_of_worker: verify_condition (workers only).
  3. caste subgroup_rollups so SC_total covers sub-codes used in joints.
  4. Drop joints whose parent axes don't exist (bilingual_given_media,
     vote_given_welfare).
  5. Asset-flag joint key alignment (TV → Television, Smartphone_internet
     → Smartphone_with_internet, Banking → Banking_access, LPG →
     LPG_clean_cooking_fuel, Improved_water → Improved_drinking_water_source).
  6. caste_given_religion: rebuild Muslim row across all 4 Muslim sub-caste
     leaves (auto-builder collapsed them into one leaf).
  7. caste_given_religion: rename parent 'Muslim_other_OBC_Muslim' → 'Muslim'
     (auto-builder picked the lexical "muslim" leaf as the row label).
  8. migration_given_religion: rename child cats (WB_other_dist → WB_other_district,
     Other_state → Other_Indian_state, Bangladesh → Bangladesh_origin).
  9. lang_given_religion: 'Other' parent → drop or remap (no Other religion in axis).
 10. religion_given_gp: parent values U1_/U2_/U3_ kept as-is (axis already
     uses the prefix); rename children Jain_Other → axis-leaf split.
 11. caste_given_gp / asset_given_gp / amenities_given_gp: parent rename
     Murshidabad_Muni → U1_Murshidabad_municipality, etc.
 12. caste_given_gp: child cat realignment (SC → SC_total, ST → ST_total,
     UC_Hindu → UC_bhadralok, OBC_Other_Hindu → split, Muslim → split across
     muslim sub-caste leaves).
 13. education_given_caste: parent code aliases (Hindu_other_middle →
     Other_Hindu_middle, Bagdi_Bauri_SC + Other_SC → SC_total, ST → ST_total,
     Muslim_Ansari → Muslim_Ansari_Jolaha, Muslim_ashraf →
     Muslim_Syed_Pathan_Mughal, Jain → Christian_Jain_Other);
     and child cat aliases (Sec → Secondary, HS → Higher_Secondary,
     Grad → Graduate, PG → Postgraduate).
 14. asset_given_occupation: parent renames (Ag_labourer → Agricultural_labourer,
     Govt_services → Government_services_teachers, Out_migrant →
     Out_migrant_worker, Transport → Transport).
 15. married_given_age_gender: expand compound buckets (33_47 → 33_37/38_42/
     43_47, 48_62 → 48_52/53_57/58_62, 63 → 63_67/68).
 16. education_given_age_gender: expand compound buckets similarly + mark
     verifier_only.
 17. vote_given_caste: parent code aliases (rename joint keys to axis
     caste leaves).

Run:
    python3 scripts/per_ac/064_curate.py
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SIM_DIR = ROOT / "simulations" / "wb_2021_ac064"
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
            # Declare verifier-only rollups so joints using sub-codes still
            # match. Joints commonly use: Bagdi_Bauri_SC, Other_SC, ST.
            a["subgroup_rollups"] = {
                "SC_total": ["Bagdi_Bauri_SC", "Other_SC"],
                "ST_total": ["ST"],
            }
    return doc


# Mapping for caste_given_gp and other gp-keyed joints
GP_PARENT_RENAMES = {
    "Murshidabad_Muni": "U1_Murshidabad_municipality",
    "Jiaganj_Azimganj_Muni": "U2_Jiaganj_Azimganj_municipality",
    "CDB_rural": "U3_Murshidabad_Jiaganj_CDB_rural",
    # religion_given_gp uses different prefix forms
    "U3_CDB_rural": "U3_Murshidabad_Jiaganj_CDB_rural",
    # U1/U2 already match the axis leaves' names
    "U1_Murshidabad_municipality": "U1_Murshidabad_municipality",
    "U2_Jiaganj_Azimganj_municipality": "U2_Jiaganj_Azimganj_municipality",
}

# Education child code aliases
EDU_CHILD_RENAMES = {
    "Sec": "Secondary",
    "HS": "Higher_Secondary",
    "Grad": "Graduate",
    "PG": "Postgraduate",
}

# Caste-axis-leaf aliases for joint parent codes
CASTE_PARENT_ALIASES = {
    "Hindu_other_middle": "Other_Hindu_middle",
    "Hindu_middle": "Other_Hindu_middle",
    "Bagdi_Bauri_SC": "SC_total",
    "Other_SC": "SC_total",
    "ST": "ST_total",
    "Muslim_Ansari": "Muslim_Ansari_Jolaha",
    "Muslim_ashraf": "Muslim_Syed_Pathan_Mughal",
    "Jain": "Christian_Jain_Other",
    "Jain_merchant": "Christian_Jain_Other",
    "UC_Hindu": "UC_bhadralok",
}


def _alias_parent_keys(table: dict, alias_map: dict[str, str]) -> dict:
    """Rename top-level parent keys; merge if collision (sum)."""
    out: dict = {}
    for k, row in table.items():
        new_k = alias_map.get(k, k)
        if new_k in out and isinstance(row, dict) and isinstance(out[new_k], dict):
            # Merge: average existing + new row
            merged = {}
            keys = set(out[new_k]) | set(row)
            for kk in keys:
                merged[kk] = (out[new_k].get(kk, 0.0) + row.get(kk, 0.0)) / 2.0
            out[new_k] = merged
        else:
            out[new_k] = dict(row) if isinstance(row, dict) else row
    return out


# Muslim sub-caste mass distribution (within Muslim parent), per MD §C.2:
# Sheikh ~48%, Ansari/Jolaha ~30%, Syed/Pathan/Mughal ~8%, OBC-Muslim other ~14%
MUSLIM_SUBCASTE_SHARES = {
    "Muslim_Sheikh": 48.0,
    "Muslim_Ansari_Jolaha": 30.0,
    "Muslim_Syed_Pathan_Mughal": 8.0,
    "Muslim_other_OBC_Muslim": 14.0,
}


def patch_joints(doc: dict) -> dict:
    keep: list[dict] = []
    for j in doc["joints"]:
        # Drop joints whose parent axes don't exist in this AC
        if j["name"] in ("bilingual_given_media", "vote_given_welfare"):
            continue

        # ------------------------------------------------------------------
        # caste_given_religion — auto-builder used 'Muslim_other_OBC_Muslim'
        # as the Muslim row name (it picked the lexical "muslim" leaf).
        # Rebuild Hindu and Muslim rows entirely to match MD targets
        # (% of total reconstructed via Bayes) so the caste marginal lands
        # on target.
        # ------------------------------------------------------------------
        if j["name"] == "caste_given_religion":
            # Hindu sub-caste % of Hindu (sum 100). Derived from MD §C.2
            # (% of total) divided by Hindu marginal 56.5%.
            hindu_dist = {
                "SC_total":              19.5 / 56.5 * 100,  # 34.5
                "ST_total":               2.2 / 56.5 * 100,  # 3.9
                "UC_bhadralok":           5.5 / 56.5 * 100,  # 9.7
                "OBC_Hindu":              8.0 / 56.5 * 100,  # 14.2
                "Other_Hindu_middle":    21.4 / 56.5 * 100,  # 37.9
            }
            j["table"] = {
                "Hindu": hindu_dist,
                "Muslim": dict(MUSLIM_SUBCASTE_SHARES),
                "Christian": {"Christian_Jain_Other": 100.0},
                "Jain": {"Christian_Jain_Other": 100.0},
                "Sikh_Other_Buddhist": {"Christian_Jain_Other": 100.0},
                "Not_stated": {"Other_Hindu_middle": 100.0},
            }

        # ------------------------------------------------------------------
        # migration_given_religion — child code renames + drop 'Other' parent
        # ------------------------------------------------------------------
        if j["name"] == "migration_given_religion":
            new_table = {}
            for parent, row in j["table"].items():
                if parent == "Other":
                    continue  # no Other religion in axis
                new_table[parent] = row
            j["table"] = _rename_flags(new_table, {
                "WB_other_dist": "WB_other_district",
                "Other_state": "Other_Indian_state",
                "Bangladesh": "Bangladesh_origin",
            })

        # ------------------------------------------------------------------
        # lang_given_religion — drop 'Other' parent (no Other religion);
        # rest already match axis.
        # ------------------------------------------------------------------
        if j["name"] == "lang_given_religion":
            j["table"] = {k: v for k, v in j["table"].items() if k != "Other"}

        # ------------------------------------------------------------------
        # asset_given_religion — drop 'Other' parent + rename flag keys
        # ------------------------------------------------------------------
        if j["name"] == "asset_given_religion":
            j["table"] = {k: v for k, v in j["table"].items() if k != "Other"}
            j["table"] = _rename_flags(j["table"], {
                "TV": "Television",
                "Smartphone_internet": "Smartphone_with_internet",
                "Banking": "Banking_access",
            })

        # ------------------------------------------------------------------
        # asset_given_occupation — parent renames + flag renames
        # ------------------------------------------------------------------
        if j["name"] == "asset_given_occupation":
            old = j["table"]
            renames = {
                "Ag_labourer": "Agricultural_labourer",
                "Govt_services": "Government_services_teachers",
                "Out_migrant": "Out_migrant_worker",
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
        # caste_given_gp — parent renames + child realignment
        # ------------------------------------------------------------------
        if j["name"] == "caste_given_gp":
            new_table = {}
            for parent_val, row in j["table"].items():
                new_parent = GP_PARENT_RENAMES.get(parent_val, parent_val)
                # Realign children: SC, ST, UC_Hindu, OBC_Other_Hindu, Muslim
                sc = row.get("SC", 0)
                st = row.get("ST", 0)
                uc = row.get("UC_Hindu", 0)
                obc_other = row.get("OBC_Other_Hindu", 0)
                muslim = row.get("Muslim", 0)
                # Split OBC_Other_Hindu 30:70 between OBC_Hindu and Other_Hindu_middle
                obc = obc_other * 0.30
                ohm = obc_other * 0.70
                # Split Muslim across 4 Muslim sub-caste leaves
                m_sheikh = muslim * 0.48
                m_ansari = muslim * 0.30
                m_syed = muslim * 0.08
                m_other = muslim * 0.14
                new_row = {
                    "SC_total": sc,
                    "ST_total": st,
                    "UC_bhadralok": uc,
                    "OBC_Hindu": obc,
                    "Other_Hindu_middle": ohm,
                    "Muslim_Sheikh": m_sheikh,
                    "Muslim_Ansari_Jolaha": m_ansari,
                    "Muslim_Syed_Pathan_Mughal": m_syed,
                    "Muslim_other_OBC_Muslim": m_other,
                }
                new_row = {k: v for k, v in new_row.items() if v > 0}
                if new_row:
                    new_table[new_parent] = new_row
            j["table"] = new_table

        # ------------------------------------------------------------------
        # asset_given_gp / amenities_given_gp — parent renames + flag renames
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
        # religion_given_gp — also has 'Jain_Other' as child; map to axis
        # ------------------------------------------------------------------
        if j["name"] == "religion_given_gp":
            new_table = {}
            for parent_val, row in j["table"].items():
                # Parent already matches the U1/U2/U3 prefix scheme.
                # If parent is U3_CDB_rural we should rename to
                # U3_Murshidabad_Jiaganj_CDB_rural
                new_parent = GP_PARENT_RENAMES.get(parent_val, parent_val)
                # 'Jain_Other' child → split: Jain (mostly), Christian, Other
                # axis has Hindu, Muslim, Christian, Jain, Sikh_Other_Buddhist,
                # Not_stated. Distribute Jain_Other roughly 70 Jain / 15
                # Christian / 15 Sikh_Other_Buddhist
                jo = row.get("Jain_Other", 0)
                new_row = {
                    "Hindu": row.get("Hindu", 0),
                    "Muslim": row.get("Muslim", 0),
                    "Jain": jo * 0.70,
                    "Christian": jo * 0.15,
                    "Sikh_Other_Buddhist": jo * 0.15,
                }
                new_row = {k: v for k, v in new_row.items() if v > 0}
                if new_row:
                    new_table[new_parent] = new_row
            j["table"] = new_table

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

        # ------------------------------------------------------------------
        # married_given_age_gender — expand compound buckets
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
        # education_given_age_gender — expand compound buckets + verifier_only
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

        # ------------------------------------------------------------------
        # vote_given_religion — drop 'Other' parent (no Other religion in axis)
        # ------------------------------------------------------------------
        if j["name"] == "vote_given_religion":
            j["table"] = {k: v for k, v in j["table"].items() if k != "Other"}

        keep.append(j)
    doc["joints"] = keep
    return doc


def main() -> None:
    print(f"Curating AC 064 structures at {SIM_DIR.relative_to(ROOT.parent)}\n")

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
    print("  python3 simulations/wb_2021_ac064/generate.py baseline_rule")


if __name__ == "__main__":
    main()
