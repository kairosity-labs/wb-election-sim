"""Build structures/axes.json + structures/joints.json from the calibrated 2019 CSVs.

One-shot script. Re-run only when the underlying CSVs change.
Outputs are framework-consumable; framework itself never reads the CSVs directly.

Two normalization concerns this script handles centrally:
    1. Source CSVs use long human-readable labels in the marginals but
       short labels in the joint tables (e.g., marginal has "Television",
       joint has "TV"). We rename axis categories to the SHORT canonical
       codes used by joints — see CANONICAL_CODES below.
    2. The religion partition is collapsed from 5 → 3 (Hindu/Muslim/Other)
       to match the dominant joint structure. Christian/Sarna/Other_minor
       are merged into "Other" (they sum to ~1% of the AC).
"""
from __future__ import annotations

import csv
import json
import re
from pathlib import Path

ROOT = Path(__file__).parent
CSV_DIR = ROOT.parent.parent.parent / "constituency_data" / "constituencies" / "095_bangaon_uttar" / "2019" / "csv"
OUT_DIR = ROOT / "structures"


def code(s: str) -> str:
    s = s.strip()
    s = re.sub(r"\(.*?\)", "", s)
    s = s.replace("/", "_").replace("+", "plus").replace("&", "and")
    s = re.sub(r"[^A-Za-z0-9]+", "_", s)
    return s.strip("_")


# ---------------------------------------------------------------------------
# Canonical code renames (applied AFTER initial parse, BEFORE writing JSON)
# Keys: raw codes produced by code() from CSV labels.
# Values: canonical short codes used everywhere (joints, samplers, verifiers).
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
# Audit-driven overrides — applied AFTER parsing the CSV.
# Each override carries a comment with the source + reasoning. Keep the
# original CSV intact; document the correction here so it stays auditable.
# ---------------------------------------------------------------------------
MARGINAL_OVERRIDES = {
    "religion": {
        # Original CSV: Hindu 85.45 / Muslim 13.58 / Other 0.97 with a
        # "+1.0%/yr Hindu projection" assumption that isn't supported by
        # any pre-2019 source (Hindu share has been flat-to-declining).
        # Bangaon CDB Census 2011 (tier A): Hindu 78.17 / Muslim 20.83.
        # AC-weighted with 54.5% Muni × ~83% Hindu + 45.5% rural × 78.2% Hindu
        # ≈ 81% Hindu / 18% Muslim / 1% Other.
        # Source: https://en.wikipedia.org/wiki/Bangaon_(community_development_block)
        "Hindu":  81.0,
        "Muslim": 18.0,
        "Other":   1.0,
    },
    "workforce_status": {
        # Original CSV: Main 31 / Marginal 11 / Non-worker 38 / Student 12 /
        # Unemployed 8. The Non-worker = 38% is mathematically incompatible
        # with PLFS 2017-18 WB female LFPR (19.8% rural / 23.0% overall).
        # Math: 0.49 female × 77% non-LFPR + 0.51 male × 25% non-LFPR ≈ 50%
        # of voter-age population should be Non_worker.
        # Source: https://iwwage.org/wp-content/uploads/2021/04/WB-Factsheet.pdf
        # Re-distributed from Marginal/Student into Non_worker.
        "Main_worker":      30.0,
        "Marginal_worker":   8.0,
        "Non_worker":       48.0,
        "Student":           6.0,
        "Unemployed":        8.0,
    },
}

JOINT_OVERRIDES = {
    "religion_given_gp": {
        # Recompute U1_Muni so AC-weighted (0.545 U1 + 0.455 U2) matches
        # the corrected religion marginal (81 / 18 / 1).
        # 0.545 × 83 + 0.455 × 78.2 = 80.82  ✓ (≈81% Hindu)
        # 0.545 × 16 + 0.455 × 20.8 = 18.18  ✓ (≈18% Muslim)
        "U1_Muni": {"Hindu": 83.0, "Muslim": 16.0, "Other": 1.0},
        # U2_CDB_rural unchanged (Census 2011 anchor).
    },
}

AGGREGATE_OVERRIDES = {
    "vote_aggregate_2019_LS": {
        # Original CSV target: BJP 48 / AITC 44 / Left+INC 6 / Other 2 was
        # constructed by adding +3pp to AITC over the LS-aggregate. That +3pp
        # adjustment is unsourced and likely backwards: AC-95 (Bangaon Uttar)
        # is the Thakurnagar Matua heartland — ground zero for the BJP swing
        # in 2019. The AC segment is plausibly more BJP-skewed than the LS
        # aggregate (BJP 48.85 / AITC 40.92 / CPM 6.40 / INC 1.61 per ECI).
        # Defensible direction: undo the +3pp AITC bump.
        # Source: https://en.wikipedia.org/wiki/Bangaon_Lok_Sabha_constituency
        "BJP":                50.0,
        "AITC":               40.0,
        "Left_INC_combined":   8.0,
        "Other_NOTA":          2.0,
    },
}


CANONICAL_CODES = {
    "gp_location": {
        "U1_Bangaon_Municipality":   "U1_Muni",
        "U2_CDB_Bangaon_rural_share": "U2_CDB_rural",
    },
    "asset_media": {
        "Television":              "TV",
        "Mobile_phone":            "Mobile",
        "Smartphone_with_internet": "Smartphone",
        "Two_wheeler":             "TwoWheeler",
        "Four_wheeler":            "FourWheeler",
        "Banking_access":          "Banking",
    },
    "amenities": {
        "Improved_drinking_water_source": "Improved_drinking_water_source",
        "Improved_sanitation":            "Improved_sanitation_latrine",
        "LPG_clean_cooking_fuel":         "LPG",
        "Wood_biomass_fuel":              "Wood",
    },
    "migration": {
        "Native":             "Native",
        "WB_other_district":  "WB_other_district",
        "Other_Indian_state": "Other_Indian_state",
        "Bangladesh_origin":  "Bangladesh",
        "Out_migrant":        "Out_migrant",
    },
    # Collapse religion 5 → 3 categories to match dominant joint structure.
    # Christian / Sarna_ORP / Other_minor → "Other" (combined ~0.97% of AC).
    "religion": {
        "Hindu":    "Hindu",
        "Muslim":   "Muslim",
        "Christian": "Other",
        "Sarna_ORP": "Other",
        "Other":     "Other",  # was "Other (Sikh/Jain/Buddhist)" pre-code
    },
}

# If True, filter age_cohort to voters (18+) and renormalize. Other axes
# (workforce, education, etc.) are already voter-population targets, so this
# alignment is needed to keep verification meaningful.
VOTERS_ONLY = True
VOTER_AGE_CODES = {"18_22", "23_27", "28_32", "33_37", "38_42",
                   "43_47", "48_52", "53_57", "58_62", "63_67", "68plus"}


AXIS_KIND = {
    "religion": "partition",
    "caste": "partition_with_subgroups",
    "age_cohort": "partition",
    "gender": "partition",
    "mother_tongue": "partition",
    "education": "partition",
    "workforce_status": "partition",
    "occupation": "partition",
    "class_of_worker": "partition",
    "economic_status": "partition",
    "gp_location": "partition",
    "household_composition": "mixed",
    "marital_status": "partition",
    "asset_media": "flag",
    "amenities": "flag",
    "migration": "partition",
}
CASTE_SUBGROUP_PARENT = "SC_total"


def _canon(axis: str, raw_code: str) -> str:
    """Look up canonical short code, else passthrough."""
    return CANONICAL_CODES.get(axis, {}).get(raw_code, raw_code)


# ---------------------------------------------------------------------------
# Marginal axes
# ---------------------------------------------------------------------------

def parse_marginals() -> dict:
    rows = list(csv.DictReader((CSV_DIR / "095_marginals.csv").open()))
    by_axis: dict[str, list[dict]] = {}
    for r in rows:
        by_axis.setdefault(r["axis"], []).append(r)

    axes = []
    for axis_name, rs in by_axis.items():
        kind = AXIS_KIND[axis_name]

        if kind == "partition":
            cats: list[str] = []
            display = {}
            marginal: dict[str, float] = {}
            for r in rs:
                c_raw = code(r["category"])
                c = _canon(axis_name, c_raw)
                # Filter age_cohort to voter ages only.
                if VOTERS_ONLY and axis_name == "age_cohort" and c not in VOTER_AGE_CODES:
                    continue
                if c not in cats:
                    cats.append(c)
                display[c] = r["category"]
                marginal[c] = marginal.get(c, 0.0) + float(r["pct"])  # collapse if rename merges
            # Renormalize after filtering.
            total = sum(marginal.values())
            if total > 0 and abs(total - 100.0) > 0.5:
                marginal = {k: round(v * 100.0 / total, 4) for k, v in marginal.items()}
            tier = max(r["tier"] for r in rs)
            axes.append({
                "name": axis_name, "kind": "partition",
                "categories": cats, "display_names": display,
                "marginal": {k: round(v, 4) for k, v in marginal.items()},
                "tier": tier, "source_csv": "095_marginals.csv",
            })

        elif kind == "partition_with_subgroups":
            leaves: list[str] = []
            display = {}
            marginal: dict[str, float] = {}
            subgroup_members = {CASTE_SUBGROUP_PARENT: []}
            for r in rs:
                c = _canon(axis_name, code(r["category"]))
                if r.get("is_subgroup") == "yes":
                    subgroup_members[CASTE_SUBGROUP_PARENT].append(c)
                    leaves.append(c); display[c] = r["category"]; marginal[c] = float(r["pct"])
                elif c == CASTE_SUBGROUP_PARENT:
                    continue
                else:
                    leaves.append(c); display[c] = r["category"]; marginal[c] = float(r["pct"])
            axes.append({
                "name": axis_name, "kind": "partition",
                "categories": leaves, "display_names": display,
                "marginal": marginal,
                "subgroup_rollups": subgroup_members,
                "tier": max(r["tier"] for r in rs),
                "source_csv": "095_marginals.csv",
                "notes": "Partition over leaves; SC_total is a verifier roll-up.",
            })

        elif kind == "flag":
            flags: list[str] = []
            display = {}
            rates: dict[str, float] = {}
            for r in rs:
                c = _canon(axis_name, code(r["category"]))
                if c not in flags:
                    flags.append(c)
                display[c] = r["category"]
                rates[c] = float(r["pct"])
            axes.append({
                "name": axis_name, "kind": "flag",
                "flags": flags, "display_names": display, "rates": rates,
                "tier": max(r["tier"] for r in rs),
                "source_csv": "095_marginals.csv",
                "notes": "Independent Bernoulli per flag (not a partition).",
            })

        elif kind == "mixed":
            partition_rows = [r for r in rs if r["category"].endswith("HH") or "Extended" in r["category"]]
            scalar_rows = [r for r in rs if "Avg" in r["category"]]
            cats = [code(r["category"]) for r in partition_rows]
            axes.append({
                "name": "household_type", "kind": "partition",
                "categories": cats,
                "display_names": {code(r["category"]): r["category"] for r in partition_rows},
                "marginal": {code(r["category"]): float(r["pct"]) for r in partition_rows},
                "tier": max(r["tier"] for r in partition_rows),
                "source_csv": "095_marginals.csv",
            })
            if scalar_rows:
                axes.append({
                    "name": "household_size_avg", "kind": "scalar",
                    "value": scalar_rows[0]["pct"], "tier": scalar_rows[0]["tier"],
                    "source_csv": "095_marginals.csv",
                    "notes": "Mean only; not sampled per-persona in v1.",
                })

    # Mark axes that are conditional on workforce status — verifier should only
    # include personas where the persona is a worker.
    for ax in axes:
        if ax["name"] in {"occupation", "class_of_worker"}:
            ax["verify_condition"] = {
                "field": "workforce_status",
                "values": ["Main_worker", "Marginal_worker"],
            }

    # Derived axes
    axes.append({
        "name": "welfare_exposure", "kind": "derived",
        "parents": ["occupation", "gender", "age_cohort", "economic_status",
                    "household_type", "marital_status", "education"],
        "module": "derived.welfare_exposure", "function": "derive",
        "flags": ["Krishak_Bandhu", "Kanyashree", "Sabuj_Sathi", "Swasthya_Sathi", "Khadya_Sathi"],
        "rates": None,  # derived; no per-flag marginal target
        "notes": "Multi-flag scheme exposure; rule-based from prior fields. "
                 "Kanyashree/Sabuj_Sathi are HH-level (parental + grandparental + personal).",
    })
    axes.append({
        "name": "welfare_dominant", "kind": "derived",
        "parents": ["welfare_exposure"],
        "module": "derived.welfare_exposure", "function": "dominant",
        "categories": ["Krishak_Bandhu", "Kanyashree", "Sabuj_Sathi",
                       "Swasthya_Sathi", "Khadya_Sathi", "None"],
        "marginal": None,
        "notes": "Single label from welfare_exposure; method configurable.",
    })

    return {"$schema_version": "1.0", "axes": axes}


# ---------------------------------------------------------------------------
# Joints
# ---------------------------------------------------------------------------

CASTE_EDU_BUCKET_MAP = {
    "UC_bhadralok":       ["UC_bhadralok"],
    "Namasudra_Matua":    ["Namasudra_Matua"],
    "Bagdi_other_SC":     ["Bagdi", "Poundra", "Other_SC"],
    "ST":                 ["ST_total"],
    "OBC_specific":       ["OBC_specific"],
    "Other_Hindu_middle": ["Other_Hindu_middle_castes",
                           "Christian_plus_Sarna_plus_Other"],
    "Muslim":             ["Muslim"],
}
VOTE_CASTE_BUCKET_MAP = {
    "UC":              ["UC_bhadralok"],
    "OBC":             ["OBC_specific"],
    "Namasudra_Matua": ["Namasudra_Matua"],
    "Other_SC":        ["Bagdi", "Poundra", "Other_SC"],
    "ST":              ["ST_total"],
    "Muslim":          ["Muslim"],
}
HINDU_SUB_TO_CASTE_LEAF = {
    "SC_Namasudra_Matua":      "Namasudra_Matua",
    "SC_Bagdi":                "Bagdi",
    "SC_Poundra":              "Poundra",
    "SC_Other":                "Other_SC",
    "ST":                      "ST_total",
    "UC_bhadralok":            "UC_bhadralok",
    "OBC_specific":            "OBC_specific",
    "Other_Hindu_middle_castes": "Other_Hindu_middle_castes",
}


def _read_csv(name: str) -> list[dict]:
    with (CSV_DIR / name).open() as f:
        return list(csv.DictReader(f))


def _gp_key(label: str) -> str:
    return "U1_Muni" if "Muni" in label else "U2_CDB_rural"


def parse_joints() -> dict:
    joints = []

    # 1. religion | gp
    rows = _read_csv("095_joint_gp_religion.csv")
    table = {_gp_key(r["Sub-unit"]): {
        "Hindu":  float(r["Hindu"]),
        "Muslim": float(r["Muslim"]),
        "Other":  float(r["Other"]),
    } for r in rows}
    joints.append({
        "name": "religion_given_gp", "parents": ["gp_location"], "child": "religion",
        "semantics": "conditional", "table": table,
        "tier": "E", "source_csv": "095_joint_gp_religion.csv",
        "notes": "Religion axis collapsed to 3 cats; joint matches directly.",
    })

    # 2. caste | religion (Hindu sub-cats from religion_caste; Muslim/Other passthrough)
    rows = _read_csv("095_joint_religion_caste.csv")
    hindu_caste_table = {}
    for r in rows:
        leaf = HINDU_SUB_TO_CASTE_LEAF[code(r["Caste sub-group"])]
        hindu_caste_table[leaf] = float(r["% of Hindu"])
    joints.append({
        "name": "caste_given_religion", "parents": ["religion"], "child": "caste",
        "semantics": "conditional",
        "table": {
            "Hindu": hindu_caste_table,
            "Muslim": {"Muslim": 100.0},
            "Other": {"Christian_plus_Sarna_plus_Other": 100.0},
        },
        "tier": "E", "source_csv": "095_joint_religion_caste.csv",
    })

    # 3. mother_tongue | religion
    rows = _read_csv("095_joint_religion_lang.csv")
    table = {}
    for r in rows:
        rel = r.get("Religion", "").strip()
        if not rel or rel.lower() in {"source", "tier"}:
            continue
        # Map source religion labels (Hindu/Muslim/Christian/Other) to canonical 3.
        rel_canon = {"Christian": "Other", "Other": "Other"}.get(rel, rel)
        row = {col: float(r[col]) for col in ["Bengali", "Hindi", "Urdu", "Other"]}
        if rel_canon in table:
            # Average with existing (e.g., Christian + Other both → "Other")
            for k in row: table[rel_canon][k] = (table[rel_canon][k] + row[k]) / 2
        else:
            table[rel_canon] = row
    joints.append({
        "name": "lang_given_religion", "parents": ["religion"], "child": "mother_tongue",
        "semantics": "conditional", "table": table,
        "tier": "E", "source_csv": "095_joint_religion_lang.csv",
    })

    # 4. migration | religion
    rows = _read_csv("095_joint_religion_migration.csv")
    mig_col_map = {
        "Native": "Native", "WB-other-dist": "WB_other_district",
        "Other state": "Other_Indian_state", "Bangladesh": "Bangladesh",
        "Outside-India": "Outside_India",
    }
    table = {}
    for r in rows:
        rel = r.get("Religion", "").strip()
        if not rel or rel.lower() in {"source", "tier"}:
            continue
        rel_canon = {"Christian": "Other", "Other": "Other"}.get(rel, rel)
        row = {mig_col_map[col]: float(r[col]) for col in mig_col_map}
        if rel_canon in table:
            for k in row: table[rel_canon][k] = (table[rel_canon][k] + row[k]) / 2
        else:
            table[rel_canon] = row
    joints.append({
        "name": "migration_given_religion", "parents": ["religion"], "child": "migration",
        "semantics": "conditional", "table": table,
        "tier": "D", "source_csv": "095_joint_religion_migration.csv",
    })

    # 5. asset.{TV, Smartphone, Banking} | religion
    rows = _read_csv("095_joint_religion_asset.csv")
    asset_col_map = {"TV": "TV", "Smartphone-internet": "Smartphone", "Banking": "Banking"}
    table = {}
    for r in rows:
        rel = r.get("Religion", "").strip()
        if not rel or rel.lower() in {"source", "tier"}:
            continue
        rel_canon = {"Christian": "Other", "Other": "Other"}.get(rel, rel)
        row = {asset_col_map[col]: float(r[col]) for col in asset_col_map}
        if rel_canon in table:
            for k in row: table[rel_canon][k] = (table[rel_canon][k] + row[k]) / 2
        else:
            table[rel_canon] = row
    joints.append({
        "name": "asset_given_religion", "parents": ["religion"], "child": "asset_media",
        "semantics": "flag_rate_conditional",
        "flags": ["TV", "Smartphone", "Banking"], "table": table,
        "tier": "C", "source_csv": "095_joint_religion_asset.csv",
    })

    # 6. education | caste (with bucket map)
    rows = _read_csv("095_joint_caste_education.csv")
    edu_cols = ["Illiterate", "Primary", "Middle", "Sec", "HS", "Grad", "PG"]
    edu_short_to_axis = {"Illiterate": "Illiterate", "Primary": "Primary",
                         "Middle": "Middle", "Sec": "Secondary",
                         "HS": "Higher_Secondary", "Grad": "Graduate", "PG": "Postgraduate"}
    table = {}
    for r in rows:
        bucket = code(r["Caste"])
        table[bucket] = {edu_short_to_axis[c]: float(r[c]) for c in edu_cols}
    joints.append({
        "name": "education_given_caste", "parents": ["caste"], "child": "education",
        "semantics": "conditional", "table": table,
        "caste_bucket_map": CASTE_EDU_BUCKET_MAP,
        "tier": "E", "source_csv": "095_joint_caste_education.csv",
    })

    # 7. P(Grad+ | age, gender)
    rows = _read_csv("095_joint_age_gender_education.csv")
    age_label_map = {
        "18–22": "18_22", "23–27": "23_27", "28–32": "28_32",
        "33–42": "33_42_compound", "43–57": "43_57_compound", "58+": "58plus_compound",
    }
    table = {}
    for r in rows:
        ak = age_label_map.get(r["Cohort"], code(r["Cohort"]))
        table[ak] = {"Male": float(r["Male grad+"]), "Female": float(r["Female grad+"])}
    joints.append({
        "name": "grad_plus_given_age_gender",
        "parents": ["age_cohort", "gender"], "child": "education_is_graduate_plus",
        "semantics": "flag_rate_conditional", "flags": ["GradPlus"], "table": table,
        "age_compound_buckets": {
            "33_42_compound": ["33_37", "38_42"],
            "43_57_compound": ["43_47", "48_52", "53_57"],
            "58plus_compound": ["58_62", "63_67", "68plus"],
        },
        "tier": "E", "source_csv": "095_joint_age_gender_education.csv",
        "notes": "Verifier-only target for Grad+ share within (age,gender).",
        "use": "sampling_only",
    })

    # 8. P(Currently_married | age, gender)
    rows = _read_csv("095_joint_marital_age_gender.csv")
    age_label_map_marital = {
        "18–22": "18_22", "23–27": "23_27", "28–32": "28_32",
        "33–47": "33_47_compound", "48–62": "48_62_compound", "63+": "63plus_compound",
    }
    table = {}
    for r in rows:
        ak = age_label_map_marital.get(r["Age"], code(r["Age"]))
        table[ak] = {"Male": float(r["Male married"]), "Female": float(r["Female married"])}
    joints.append({
        "name": "married_given_age_gender",
        "parents": ["age_cohort", "gender"], "child": "marital_status",
        "semantics": "flag_rate_conditional", "flags": ["Currently_married"], "table": table,
        "age_compound_buckets": {
            "33_47_compound": ["33_37", "38_42", "43_47"],
            "48_62_compound": ["48_52", "53_57", "58_62"],
            "63plus_compound": ["63_67", "68plus"],
        },
        "tier": "E", "source_csv": "095_joint_marital_age_gender.csv",
        "notes": "Sampler uses marital_sampling plugin; joint compound buckets not verifier-friendly.",
        "use": "sampling_only",
    })

    # 9. workforce indicators | education
    rows = _read_csv("095_joint_education_workforce.csv")
    table = {}
    for r in rows:
        edu_short_in = r["Education"]  # raw label from CSV
        edu = {"Illiterate": "Illiterate", "Primary": "Primary", "Middle": "Middle",
               "Secondary": "Secondary", "Higher Secondary": "Higher_Secondary",
               "Graduate": "Graduate", "Postgraduate": "Postgraduate"}.get(edu_short_in, edu_short_in)
        table[edu] = {
            "Unemployed_seeking": float(r["Unemployed-seeking"]),
            "Main_worker_rate":   float(r["Main-worker rate"]),
        }
    joints.append({
        "name": "workforce_indicators_given_education",
        "parents": ["education"], "child": "workforce_status",
        "semantics": "two_indicator_rates",
        "indicators": ["Unemployed_seeking", "Main_worker_rate"],
        "table": table,
        "tier": "E", "source_csv": "095_joint_education_workforce.csv",
        "notes": "Sampler uses workforce_sampling plugin; two-indicator semantics not directly verifiable.",
        "use": "sampling_only",
    })

    # 10. asset.{TV, Smartphone} | occupation
    rows = _read_csv("095_joint_occupation_asset.csv")
    occ_col_map = {"Smartphone-internet": "Smartphone", "TV": "TV"}
    table = {}
    occ_remap = {  # CSV occupation -> canonical occupation axis code
        "Cultivator": "Cultivator", "Ag-labourer": "Agricultural_labourer",
        "Household industry": "Household_industry", "Manufacturing": "Manufacturing",
        "Construction": "Construction", "Trade / retail": "Trade_retail",
        "Transport (incl. Petrapole)": "Transport", "Services (private)": "Services",
        "Govt services": "Government_services_teachers", "Out-migrant": "Out_migrant_worker",
    }
    for r in rows:
        occ_raw = (r.get("Occupation") or "").strip()
        if not occ_raw or occ_raw.lower() in {"source", "tier"}:
            continue
        occ = occ_remap.get(occ_raw, code(occ_raw))
        table[occ] = {asset_short: float(r[csv_col]) for csv_col, asset_short in occ_col_map.items()}
    joints.append({
        "name": "asset_given_occupation", "parents": ["occupation"], "child": "asset_media",
        "semantics": "flag_rate_conditional", "flags": ["TV", "Smartphone"], "table": table,
        "tier": "C", "source_csv": "095_joint_occupation_asset.csv",
    })

    # 11. asset.{TV, Smartphone, Computer, Banking} | gp
    rows = _read_csv("095_joint_gp_asset.csv")
    table = {}
    for r in rows:
        gp_label = (r.get("Sub-unit") or "").strip()
        if not gp_label or gp_label.lower() in {"source"}:
            continue
        table[_gp_key(gp_label)] = {
            "TV": float(r["TV"]),
            "Smartphone": float(r["Smartphone-internet"]),
            "Computer": float(r["Computer"]),
            "Banking": float(r["Banking"]),
        }
    joints.append({
        "name": "asset_given_gp", "parents": ["gp_location"], "child": "asset_media",
        "semantics": "flag_rate_conditional",
        "flags": ["TV", "Smartphone", "Computer", "Banking"], "table": table,
        "tier": "C", "source_csv": "095_joint_gp_asset.csv",
    })

    # 12. amenity.{LPG, Sanitation, Water, Electricity} | gp
    rows = _read_csv("095_joint_gp_amenities.csv")
    table = {}
    for r in rows:
        gp_label = (r.get("Sub-unit") or "").strip()
        if not gp_label or gp_label.lower() in {"source"}:
            continue
        table[_gp_key(gp_label)] = {
            "LPG":                            float(r["LPG"]),
            "Improved_sanitation_latrine":   float(r["Improved sanitation"]),
            "Improved_drinking_water_source": float(r["Improved water"]),
            "Electricity":                    float(r["Electricity"]),
        }
    joints.append({
        "name": "amenity_given_gp", "parents": ["gp_location"], "child": "amenities",
        "semantics": "flag_rate_conditional",
        "flags": ["LPG", "Improved_sanitation_latrine",
                  "Improved_drinking_water_source", "Electricity"],
        "table": table,
        "tier": "C", "source_csv": "095_joint_gp_amenities.csv",
    })

    # 13. caste | gp  (verifier-only)
    rows = _read_csv("095_joint_gp_caste.csv")
    gp_caste_col_map = {  # CSV column -> our coarse bucket
        "UC": "UC", "Namasudra-Matua SC": "Namasudra_Matua", "Other SC": "Other_SC",
        "ST": "ST", "OBC + Other Hindu": "OBC_Other_Hindu", "Muslim": "Muslim",
    }
    table = {}
    for r in rows:
        gp_label = (r.get("Sub-unit") or "").strip()
        if not gp_label or gp_label.lower() in {"source"}:
            continue
        table[_gp_key(gp_label)] = {our: float(r[col]) for col, our in gp_caste_col_map.items()}
    joints.append({
        "name": "caste_given_gp", "parents": ["gp_location"], "child": "caste",
        "semantics": "conditional", "table": table,
        "caste_bucket_map": {
            "UC": ["UC_bhadralok"],
            "Namasudra_Matua": ["Namasudra_Matua"],
            "Other_SC": ["Bagdi", "Poundra", "Other_SC"],
            "ST": ["ST_total"],
            "OBC_Other_Hindu": ["OBC_specific", "Other_Hindu_middle_castes",
                                "Christian_plus_Sarna_plus_Other"],
            "Muslim": ["Muslim"],
        },
        "tier": "E", "source_csv": "095_joint_gp_caste.csv",
        "use": "verifier_only",
    })

    # 14. bilingual | media tier (deferred — needs derived axis)
    # Skipped from joints.json for now; bilingual itself isn't a sampleable axis in v1.

    # ----- Vote tables -----
    parties = ["BJP", "AITC", "INC", "LF", "Other"]

    # vote | religion (collapse Christian/Other rows into 'Other')
    rows = _read_csv("095_vote_religion_2019.csv")
    table = {}
    for r in rows:
        rel = r.get("Religion", "").strip()
        if not rel or rel.lower() in {"source", "tier"}:
            continue
        rel_canon = {"Christian": "Other", "Other": "Other"}.get(rel, rel)
        row = {p: float(r[p]) for p in parties}
        if rel_canon in table:
            for p in parties: table[rel_canon][p] = (table[rel_canon][p] + row[p]) / 2
        else:
            table[rel_canon] = row
    joints.append({
        "name": "vote_given_religion", "parents": ["religion"], "child": "vote_2019_LS",
        "semantics": "vote_conditional", "table": table, "parties": parties,
        "tier": "C", "source_csv": "095_vote_religion_2019.csv",
    })

    # vote | caste (with bucket map)
    rows = _read_csv("095_vote_caste_2019.csv")
    table = {}
    for r in rows:
        bucket = code(r["Caste"])
        table[bucket] = {p: float(r[p]) for p in parties}
    joints.append({
        "name": "vote_given_caste", "parents": ["caste"], "child": "vote_2019_LS",
        "semantics": "vote_conditional", "table": table,
        "caste_bucket_map": VOTE_CASTE_BUCKET_MAP, "parties": parties,
        "tier": "C", "source_csv": "095_vote_caste_2019.csv",
    })

    # vote | gender
    rows = _read_csv("095_vote_gender_2019.csv")
    table = {}
    for r in rows:
        g = r.get("Gender", "").strip()
        if not g or g.lower() in {"source", "tier"}:
            continue
        table[g] = {p: float(r[p]) for p in parties}
    joints.append({
        "name": "vote_given_gender", "parents": ["gender"], "child": "vote_2019_LS",
        "semantics": "vote_conditional", "table": table, "parties": parties,
        "tier": "C", "source_csv": "095_vote_gender_2019.csv",
    })

    # vote | welfare_dominant
    rows = _read_csv("095_vote_welfare_2019.csv")
    welfare_parties = ["BJP", "AITC", "INC", "LF"]
    welfare_label_map = {
        "Krishak_Bandhu_cultivator_HH": "Krishak_Bandhu",
        "Kanyashree_girl_student_HH":   "Kanyashree",
        "Swasthya_Sathi_enrollee":      "Swasthya_Sathi",
        "Sabuj_Sathi_bicycle_HH":       "Sabuj_Sathi",
        "Khadya_Sathi_PDS":             "Khadya_Sathi",
        "No_state_scheme_exposure":     "None",
    }
    table = {}
    for r in rows:
        raw = code(r["Exposure"])
        label = welfare_label_map.get(raw, raw)
        table[label] = {p: float(r[p]) for p in welfare_parties}
    joints.append({
        "name": "vote_given_welfare", "parents": ["welfare_dominant"], "child": "vote_2019_LS",
        "semantics": "vote_conditional", "table": table, "parties": welfare_parties,
        "tier": "C", "source_csv": "095_vote_welfare_2019.csv",
    })

    # ----- Aggregate target -----
    rows = _read_csv("095_calibration_target_2019.csv")
    raw_target = {r["party"]: float(r["ac95_segment_pct_estimate"]) for r in rows}
    aggregate_buckets = [
        {"name": "BJP",               "target_pct": raw_target["BJP"],          "vote_values": ["BJP"]},
        {"name": "AITC",              "target_pct": raw_target["AITC"],         "vote_values": ["AITC"]},
        {"name": "Left_INC_combined", "target_pct": raw_target["CPI(M) + INC"], "vote_values": ["INC", "LF"]},
        {"name": "Other_NOTA",        "target_pct": raw_target["Other / NOTA"], "vote_values": ["Other"]},
    ]
    return {
        "$schema_version": "1.0",
        "joints": joints,
        "aggregate_targets": [{
            "name": "vote_aggregate_2019_LS", "field": "vote_2019_LS",
            "buckets": aggregate_buckets, "tier": "D",
            "source_csv": "095_calibration_target_2019.csv",
        }],
    }


def _apply_marginal_overrides(axes_doc: dict) -> None:
    for axis_name, overrides in MARGINAL_OVERRIDES.items():
        for ax in axes_doc["axes"]:
            if ax["name"] != axis_name:
                continue
            ax.setdefault("notes", "")
            ax["notes"] = (ax.get("notes", "") + " · audit-overridden marginal").strip(" ·")
            for cat, pct in overrides.items():
                if "marginal" in ax and cat in ax["marginal"]:
                    ax["marginal"][cat] = pct
            # Re-normalize in case overrides don't sum to exactly 100.
            if "marginal" in ax:
                total = sum(ax["marginal"].values())
                if total > 0 and abs(total - 100.0) > 0.5:
                    ax["marginal"] = {k: round(v * 100.0 / total, 4)
                                      for k, v in ax["marginal"].items()}


def _apply_joint_overrides(joints_doc: dict) -> None:
    for joint_name, parent_overrides in JOINT_OVERRIDES.items():
        for j in joints_doc["joints"]:
            if j["name"] != joint_name:
                continue
            j.setdefault("notes", "")
            j["notes"] = (j.get("notes", "") + " · audit-overridden cells").strip(" ·")
            for parent_value, child_dist in parent_overrides.items():
                if parent_value in j["table"]:
                    j["table"][parent_value].update(child_dist)


def _apply_aggregate_overrides(joints_doc: dict) -> None:
    for target_name, bucket_overrides in AGGREGATE_OVERRIDES.items():
        for t in joints_doc.get("aggregate_targets", []):
            if t["name"] != t["name"] or t["name"] != target_name:
                continue
            for b in t["buckets"]:
                if b["name"] in bucket_overrides:
                    b["target_pct"] = bucket_overrides[b["name"]]
            t["notes"] = (t.get("notes", "") + " · audit-overridden buckets").strip(" ·")


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    axes = parse_marginals()
    joints = parse_joints()
    _apply_marginal_overrides(axes)
    _apply_joint_overrides(joints)
    _apply_aggregate_overrides(joints)
    (OUT_DIR / "axes.json").write_text(json.dumps(axes, indent=2))
    (OUT_DIR / "joints.json").write_text(json.dumps(joints, indent=2))
    print(f"axes:   {len(axes['axes'])} written")
    print(f"joints: {len(joints['joints'])} written")
    print(f"overrides applied: "
          f"{len(MARGINAL_OVERRIDES)} marginal, "
          f"{len(JOINT_OVERRIDES)} joint, "
          f"{len(AGGREGATE_OVERRIDES)} aggregate")


if __name__ == "__main__":
    main()
