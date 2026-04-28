#!/usr/bin/env python3
"""
build_ac_verifier_configs.py
Translate a per-AC calibrated_2019 CSV bundle into starter
verifier configs that the existing population-sampling pipeline can consume:

  simulations/wb_2021_ac<NN>/structures/axes.json
  simulations/wb_2021_ac<NN>/structures/joints.json
  simulations/wb_2021_ac<NN>/structures/aggregate_targets.json

These are STARTERS — every axis/joint is tagged with `needs_review: true`
and `source_csv` so a human can audit overrides, declare derived axes, set
up subgroup rollups, normalize ID codes, etc. This script's job is purely
mechanical: heterogeneous local categories → snake_case identifier codes →
JSON consumable by the existing `pipeline.verifiers.verify_population`.

Run:
    python3 scripts/build_ac_verifier_configs.py 003          # one AC
    python3 scripts/build_ac_verifier_configs.py --all        # every AC

Per-AC custom extensions: see scripts/per_ac/<NN>_extensions.py for any
AC-specific re-shaping the common scaffold doesn't cover (tea-garden
workforce buckets, Sarna sub-religions, etc.). If that file exists, this
script imports its `extend(axes, joints, aggregates)` function as a final
post-processing step.
"""
from __future__ import annotations

import argparse
import csv
import importlib.util
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CAL_DIR = ROOT / "data" / "calibrated_2019"
CSV_DIR = CAL_DIR / "csv"
SIMS_DIR = ROOT / "simulations"
PER_AC_DIR = ROOT / "scripts" / "per_ac"

# Axes that ARE marginals but where rows are independent ownership rates,
# not partition pcts. Verifier treats these as `flag` rather than `partition`.
FLAG_AXES = {"asset_media", "amenities"}

# Axes the persona-generation pipeline treats as derived (computed from
# parents via a Python plugin), not directly sampled.
SUGGEST_DERIVED = {"welfare_exposure"}   # placeholder — depends on sim


def to_snake(label: str) -> str:
    """Convert a human-friendly category label to a snake_case identifier.

    Strips parentheticals, normalizes whitespace, collapses non-alphanumerics
    to underscores. Preserves uppercase initials for known-acronyms (UC, ST,
    SC, OBC, BJP, etc.) by mapping after lowercasing.
    """
    if not label:
        return "Unknown"
    s = re.sub(r"\([^)]*\)", "", label)
    s = re.sub(r"[^A-Za-z0-9]+", "_", s)
    s = re.sub(r"_+", "_", s).strip("_")
    return s or "Unknown"


def load_marginals(ac: str) -> dict[str, list[dict]]:
    """Group marginal CSV rows by axis."""
    path = CSV_DIR / f"{ac}_marginals.csv"
    if not path.exists():
        raise FileNotFoundError(f"{path.name}")
    by_axis: dict[str, list[dict]] = {}
    with path.open() as f:
        for row in csv.DictReader(f):
            by_axis.setdefault(row["axis"], []).append(row)
    return by_axis


def build_axis(axis_name: str, rows: list[dict]) -> dict:
    """Build one Axis JSON entry."""
    is_flag = axis_name in FLAG_AXES

    # Filter out subgroup rows from partition value space; preserve them for
    # rollups so the verifier can also report SC_total etc.
    leaves = [r for r in rows if r.get("is_subgroup", "no") == "no"]
    subgroups = [r for r in rows if r.get("is_subgroup", "no") == "yes"]

    if is_flag:
        flag_codes = [to_snake(r["category"]) for r in rows]
        rates = {}
        display_names = {}
        for code, r in zip(flag_codes, rows):
            try:
                rates[code] = float(r["pct"])
            except (ValueError, TypeError):
                continue
            display_names[code] = r["category"]
        return {
            "name": axis_name, "kind": "flag",
            "flags": flag_codes, "rates": rates,
            "display_names": display_names,
            "tier": _modal_tier(rows),
            "source_csv": f"{Path(rows[0].get('_csv', f'{axis_name}.csv')).name}",
            "needs_review": True,
            "notes": "Independent ownership rates — see calibrated_2019 MD.",
        }

    cats = []
    marginal: dict[str, float] = {}
    display_names: dict[str, str] = {}
    seen_codes = set()
    for r in leaves:
        label = r["category"]
        code = to_snake(label)
        # disambiguate code collisions (rare)
        base, n = code, 1
        while code in seen_codes:
            n += 1
            code = f"{base}_{n}"
        seen_codes.add(code)
        try:
            pct = float(r["pct"])
        except (ValueError, TypeError):
            continue
        cats.append(code)
        marginal[code] = pct
        display_names[code] = label

    out: dict = {
        "name": axis_name, "kind": "partition",
        "categories": cats,
        "marginal": marginal,
        "display_names": display_names,
        "tier": _modal_tier(leaves),
        "source_csv": f"{cats and rows[0].get('_csv', '')}".replace("\n", "") or None,
        "needs_review": True,
    }
    # If there are subgroup rows, declare them as a verifier-only rollup.
    if subgroups:
        # Convention: name the rollup using the first non-subgroup label
        # that immediately precedes the subgroup block (often "SC total" /
        # "ST total"). Use a heuristic: parent_label is the last leaf row
        # whose category contains "total".
        parent_label = next(
            (r["category"] for r in reversed(leaves)
             if "total" in r["category"].lower()),
            None,
        )
        if parent_label:
            parent_code = to_snake(parent_label)
            sub_codes = [to_snake(r["category"]) for r in subgroups]
            out["subgroup_rollups"] = {parent_code: sub_codes}
    return out


def _modal_tier(rows: list[dict]) -> str | None:
    tiers = [r.get("tier") for r in rows if r.get("tier")]
    if not tiers:
        return None
    from collections import Counter
    return Counter(tiers).most_common(1)[0][0]


# ---------------------------------------------------------------------------
# Joints — straightforward dump from the wide CSVs
# ---------------------------------------------------------------------------

JOINT_FILE_TO_NAME = {
    "joint_religion_lang": ("lang_given_religion", ["religion"], "mother_tongue", "conditional"),
    "joint_religion_caste": ("caste_given_religion", ["religion"], "caste", "conditional"),
    "joint_religion_migration": ("migration_given_religion", ["religion"], "migration", "conditional"),
    "joint_religion_asset": ("asset_given_religion", ["religion"], "asset_media", "flag_rate_conditional"),
    "joint_caste_education": ("education_given_caste", ["caste"], "education", "conditional"),
    "joint_age_gender_education": ("education_given_age_gender", ["age_cohort", "gender"], "education", "flag_rate_conditional"),
    "joint_marital_age_gender": ("married_given_age_gender", ["age_cohort", "gender"], "marital_status", "flag_rate_conditional"),
    "joint_occupation_asset": ("asset_given_occupation", ["occupation"], "asset_media", "flag_rate_conditional"),
    "joint_education_workforce": ("workforce_given_education", ["education"], "workforce_status", "two_indicator_rates"),
    "joint_asset_bilingualism": ("bilingual_given_media", ["media_tier"], "bilingual", "flag_rate_conditional"),
    "joint_gp_religion": ("religion_given_gp", ["gp_location"], "religion", "conditional"),
    "joint_gp_caste": ("caste_given_gp", ["gp_location"], "caste", "conditional"),
    "joint_gp_asset": ("asset_given_gp", ["gp_location"], "asset_media", "flag_rate_conditional"),
    "joint_gp_amenities": ("amenities_given_gp", ["gp_location"], "amenities", "flag_rate_conditional"),
    "vote_religion_2019": ("vote_given_religion", ["religion"], "vote_2019_LS", "vote_conditional"),
    "vote_caste_2019": ("vote_given_caste", ["caste"], "vote_2019_LS", "vote_conditional"),
    "vote_gender_2019": ("vote_given_gender", ["gender"], "vote_2019_LS", "vote_conditional"),
    "vote_welfare_2019": ("vote_given_welfare", ["welfare_exposure"], "vote_2019_LS", "vote_conditional"),
}


def load_joint_csv(path: Path) -> tuple[list[str], list[list[str]]]:
    with path.open() as f:
        reader = csv.reader(f)
        header = next(reader, [])
        rows = [r for r in reader if any(c.strip() for c in r)]
    return header, rows


def build_joint(ac: str, file_stem: str) -> dict | None:
    """Build one joint JSON entry from a wide CSV."""
    if file_stem not in JOINT_FILE_TO_NAME:
        return None
    path = CSV_DIR / f"{ac}_{file_stem}.csv"
    if not path.exists():
        return None
    name, parents, child, semantics = JOINT_FILE_TO_NAME[file_stem]
    header, rows = load_joint_csv(path)
    if not header or not rows:
        return None

    # ---- Special case: D.2 (joint_religion_caste) ----
    # Source MD encodes this as "Hindu-internal sub-structure" — a 1D table
    # of (sub-caste, % of Hindu). Wrap into a religion-keyed joint:
    #   table = { Hindu: {sub-caste: pct, ...},
    #             Muslim: {Muslim: 100},
    #             Other:  {Other: 100} }
    if file_stem == "joint_religion_caste":
        return _build_caste_given_religion(ac, name, header, rows)

    # First column = parent label (or parent×parent compound). Trailing
    # cols often include "Tier"/"Source"/etc.
    parent_col = header[0]
    meta_cols = {"Tier", "Source", "Note"}
    value_cols = [c for c in header[1:] if c and c not in meta_cols]

    table: dict = {}
    last_tier = None
    for row in rows:
        d = {h: v for h, v in zip(header, row)}
        parent_val = d.get(parent_col, "").strip()
        if not parent_val or parent_val.lower() in ("sum", "note"):
            continue
        parent_code = to_snake(parent_val)
        cells = {}
        for c in value_cols:
            try:
                cells[to_snake(c)] = float(str(d.get(c, "")).replace("%", ""))
            except ValueError:
                pass
        if cells:
            table[parent_code] = cells
        last_tier = d.get("Tier") or last_tier

    if not table:
        return None
    out: dict = {
        "name": name, "parents": parents, "child": child,
        "semantics": semantics, "table": table,
        "tier": last_tier,
        "source_csv": f"{ac}_{file_stem}.csv",
        "needs_review": True,
    }
    # For vote joints, list the parties for downstream consumers.
    if semantics == "vote_conditional":
        out["parties"] = [to_snake(c) for c in value_cols]
    return out


def _map_subcat_to_axis_leaf(label: str, axis_leaves: set[str]) -> str | None:
    """Map a D.2 sub-caste label (e.g., 'SC: Rajbanshi / Koch-Rajbanshi')
    to one of the AC's axis leaf categories (e.g., 'SC_total'). Strategy:
      1. If snake-cased label is already a leaf, use it.
      2. Detect leading 'SC:' / 'ST' / 'UC' / 'OBC' / 'Muslim' / 'Christian'
         prefix → map to corresponding *_total leaf if present.
      3. Otherwise, find a leaf whose snake-case is a prefix or substring.
      4. None → caller drops the row.
    """
    code = to_snake(label)
    if code in axis_leaves:
        return code
    low = label.strip().lower()
    # Prefix mapping
    prefix_map = [
        ("sc:", ["SC_total", "SC", "SC_all"]),
        ("sc ", ["SC_total", "SC", "SC_all"]),
        ("st ", ["ST_total", "ST", "ST_all"]),
        ("st:", ["ST_total", "ST", "ST_all"]),
        ("uc ", ["UC_bhadralok", "Upper_caste_bhadralok"]),
        ("upper", ["UC_bhadralok", "Upper_caste_bhadralok"]),
        ("brahmin", ["UC_bhadralok"]),
        ("kayastha", ["UC_bhadralok"]),
        ("obc", ["OBC", "OBC_specific", "OBC_Hindu", "OBC_specific_Mahato"]),
        ("muslim", ["Muslim", "Muslim_all_sub_castes_pooled"]),
        ("christian", ["Christian_plus_Sarna_plus_Other",
                        "Christian_plus_Other"]),
        ("mahishya", ["Mahishya_general_dominant", "Mahishya"]),
        ("sadgop", ["Mahishya_Sadgop_dominant_OBC"]),
        ("mahato", ["OBC_Mahato"]),
        ("rajbanshi", ["SC_total", "Rajbanshi_SC"]),
        ("namasudra", ["SC_total", "Namasudra_Matua"]),
        ("bagdi", ["SC_total", "Bagdi_SC"]),
        ("bauri", ["SC_total"]),
        ("dom", ["SC_total"]),
        ("poundra", ["SC_total"]),
        ("other hindu", ["Other_Hindu_middle_castes", "Other_Hindu_middle",
                          "Other_Hindu_forward_middle"]),
    ]
    for prefix, candidates in prefix_map:
        if low.startswith(prefix) or prefix in low[:20]:
            for c in candidates:
                if c in axis_leaves:
                    return c
    # Substring fallback: leaf code contained in label code or vice versa
    code_low = code.lower()
    for leaf in axis_leaves:
        ll = leaf.lower()
        if code_low.startswith(ll) or ll.startswith(code_low) or ll in code_low:
            return leaf
    return None


def _load_axis_leaves(ac: str, axis_name: str) -> set[str]:
    """Read just-built marginal CSV → return the set of leaf category codes
    that the auto-builder will declare on this axis. Used to align D.2."""
    import csv as _csv
    p = CSV_DIR / f"{ac}_marginals.csv"
    if not p.exists():
        return set()
    leaves = set()
    with p.open() as f:
        for row in _csv.DictReader(f):
            if row.get("axis") == axis_name and row.get("is_subgroup", "no") == "no":
                leaves.add(to_snake(row["category"]))
    return leaves


def _build_caste_given_religion(ac: str, name: str, header: list[str],
                                  rows: list[list[str]]) -> dict | None:
    """Build caste_given_religion from a 1D 'sub-caste % of Hindu' table.

    The Hindu sub-caste distribution comes from the CSV rows. Muslim and
    'Other' are degenerate single-cell rows. Each sub-cat label is mapped
    to one of the AC's caste-axis LEAVES (e.g., 'SC: Rajbanshi' → 'SC_total')
    so the sampler's output stays in the legal axis value-space.
    """
    if len(header) < 2:
        return None
    pct_col = header[1]
    axis_leaves = _load_axis_leaves(ac, "caste")

    # Aggregate sub-cat pcts onto the matching axis leaf.
    hindu_dist: dict[str, float] = {}
    unmapped = []
    last_tier = None
    for r in rows:
        d = dict(zip(header, r))
        cat = (d.get(header[0]) or "").strip()
        if not cat or cat.lower() in ("sum", "note"):
            continue
        try:
            v = float(str(d.get(pct_col, "")).replace("%", ""))
        except ValueError:
            continue
        if v <= 0:
            continue
        leaf = _map_subcat_to_axis_leaf(cat, axis_leaves)
        if leaf is None:
            unmapped.append(cat)
            continue
        hindu_dist[leaf] = hindu_dist.get(leaf, 0.0) + v
        last_tier = d.get("Tier") or last_tier
    if not hindu_dist:
        return None

    # Pick best Muslim and Other leaves from axis_leaves
    muslim_leaf = next((c for c in axis_leaves if "muslim" in c.lower()),
                       "Muslim")
    other_leaf = next((c for c in axis_leaves
                        if "christian" in c.lower() or "sarna" in c.lower()
                        or c.lower() == "other"), None)
    notes = ("D.2 is a 1D 'Hindu sub-caste % of Hindu' table; wrapped into a "
              "religion-keyed conditional. Sub-caste rows aggregated onto "
              "this AC's caste-axis leaves via prefix-matching. ")
    if unmapped:
        notes += f"Unmapped (dropped): {unmapped}. "

    table: dict = {"Hindu": hindu_dist, muslim_leaf: {muslim_leaf: 100.0}}
    if other_leaf:
        table["Other"] = {other_leaf: 100.0}

    return {
        "name": name,
        "parents": ["religion"],
        "child": "caste",
        "semantics": "conditional",
        "table": table,
        "tier": last_tier,
        "source_csv": f"{ac}_joint_religion_caste.csv",
        "needs_review": True,
        "notes": notes,
    }


# ---------------------------------------------------------------------------
# Aggregate target — §E vote calibration
# ---------------------------------------------------------------------------

def _looks_like_party(s: str) -> bool:
    """True if string looks like a party name (BJP/AITC/INC/...) — NOT a meta
    row like 'Total polled' or 'Margin' or 'NOTA' (well, NOTA we want)."""
    if not s:
        return False
    sl = s.strip().lower()
    if any(k in sl for k in ("total ", "margin", "lead over",
                              "electors", "turnout", "valid evm")):
        return False
    return True


def _detect_pct_column(header: list[str], rows: list[list[str]]) -> int | None:
    """Pick the column whose values are mostly small floats in [0, 100].
    Skips column 0 (party) and any column that looks like a vote count."""
    if not header:
        return None
    # Prefer header-name hints first.
    for i, col in enumerate(header):
        cl = col.lower()
        if "%" in col or "pct" in cl or "share" in cl or "estimate" in cl:
            return i
    # Otherwise: scan each non-zero column, pick the one with the highest
    # fraction of in-range floats.
    best_idx, best_score = None, 0.0
    for i in range(1, len(header)):
        ok = 0
        total = 0
        for r in rows:
            if i >= len(r): continue
            cell = (r[i] or "").replace(",", "").replace("%", "").strip()
            try:
                v = float(cell)
                total += 1
                if 0 <= v <= 100:
                    ok += 1
            except ValueError:
                pass
        if total == 0: continue
        score = ok / total
        if score > best_score:
            best_score, best_idx = score, i
    return best_idx


def build_aggregate_target(ac: str) -> dict | None:
    path = CSV_DIR / f"{ac}_calibration_target_2019.csv"
    if not path.exists():
        return None
    with path.open() as f:
        reader = csv.reader(f)
        rows = [r for r in reader if any(c.strip() for c in r)]
    if len(rows) < 2:
        return None
    header = rows[0]
    data = rows[1:]
    pct_idx = _detect_pct_column(header, data)
    if pct_idx is None:
        return None

    buckets = []
    tier_idx = next((i for i, c in enumerate(header) if c.lower() == "tier"), None)
    for r in data:
        party = (r[0] if r else "").strip()
        if not _looks_like_party(party):
            continue
        cell = r[pct_idx] if pct_idx < len(r) else ""
        try:
            pct = float(str(cell).replace(",", "").replace("%", ""))
        except ValueError:
            continue
        if pct < 0 or pct > 100:
            continue
        tier = (r[tier_idx] if tier_idx is not None and tier_idx < len(r)
                else "").strip() or None
        buckets.append({
            "name": to_snake(party),
            "display_name": party,
            "target_pct": pct,
            "vote_values": [to_snake(party)],
            "tier": tier,
        })
    if not buckets:
        return None
    return {
        "$schema_version": "1.0",
        "aggregate_targets": [{
            "name": "vote_2019_LS_share",
            "field": "vote_2019_LS",
            "buckets": buckets,
            "tier": _modal_tier_buckets(buckets),
            "source_csv": f"{ac}_calibration_target_2019.csv",
            "needs_review": True,
        }],
    }


def _modal_tier_buckets(buckets: list[dict]) -> str | None:
    tiers = [b.get("tier") for b in buckets if b.get("tier")]
    if not tiers: return None
    from collections import Counter
    return Counter(tiers).most_common(1)[0][0]


# ---------------------------------------------------------------------------
# Top-level
# ---------------------------------------------------------------------------

def attach_csv_source(rows: list[dict], csv_name: str) -> None:
    for r in rows:
        r["_csv"] = csv_name


def build_one(ac: str, force: bool = False) -> dict:
    """Build all 3 config files for one AC. Return a per-AC summary.

    Refuses to overwrite an existing axes.json / joints.json unless
    `force=True`. AC 095 has hand-curated structures from earlier work; do
    not clobber without explicit consent.
    """
    out_dir = SIMS_DIR / f"wb_2021_ac{ac}" / "structures"
    out_dir.mkdir(parents=True, exist_ok=True)
    summary = {"ac": ac, "axes_written": 0, "joints_written": 0,
                "aggregate_buckets": 0, "extension": None,
                "skipped_existing": False}
    if not force and ((out_dir / "axes.json").exists()
                       or (out_dir / "joints.json").exists()):
        summary["skipped_existing"] = True
        return summary

    # Axes
    by_axis = load_marginals(ac)
    csv_name = f"{ac}_marginals.csv"
    axes = []
    for axis_name, rows in by_axis.items():
        attach_csv_source(rows, csv_name)
        axes.append(build_axis(axis_name, rows))

    # Joints
    joints = []
    for stem in JOINT_FILE_TO_NAME:
        j = build_joint(ac, stem)
        if j:
            joints.append(j)

    # Aggregate target
    aggregates = build_aggregate_target(ac)

    # Per-AC extension hook
    ext_path = PER_AC_DIR / f"{ac}_extensions.py"
    if ext_path.exists():
        spec = importlib.util.spec_from_file_location(f"per_ac_{ac}", ext_path)
        if spec and spec.loader:
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            if hasattr(module, "extend"):
                axes, joints, aggregates = module.extend(axes, joints, aggregates)
                summary["extension"] = ext_path.name

    # Write
    (out_dir / "axes.json").write_text(
        json.dumps({"$schema_version": "1.0", "axes": axes}, indent=2,
                    ensure_ascii=False)
    )
    (out_dir / "joints.json").write_text(
        json.dumps({"$schema_version": "1.0", "joints": joints}, indent=2,
                    ensure_ascii=False)
    )
    if aggregates:
        (out_dir / "aggregate_targets.json").write_text(
            json.dumps(aggregates, indent=2, ensure_ascii=False)
        )

    summary["axes_written"] = len(axes)
    summary["joints_written"] = len(joints)
    summary["aggregate_buckets"] = (
        len(aggregates["aggregate_targets"][0]["buckets"]) if aggregates else 0
    )
    return summary


def discover_acs() -> list[str]:
    out = []
    for p in sorted(CAL_DIR.glob("*_2019.md")):
        m = re.match(r"^(\d{3})_", p.name)
        if m: out.append(m.group(1))
    return out


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("ac", nargs="?", default=None)
    p.add_argument("--all", action="store_true")
    p.add_argument("--force", action="store_true",
                    help="Overwrite existing structures/{axes,joints}.json. "
                         "Use only when intentionally regenerating from CSVs.")
    args = p.parse_args()

    targets = (discover_acs() if args.all
               else [args.ac.zfill(3)] if args.ac else [])
    if not targets:
        p.error("provide AC number or --all")
        return 2

    mode = "FORCE-overwriting" if args.force else "skip-if-exists"
    print(f"Building verifier configs for {len(targets)} AC(s) "
           f"[mode: {mode}]: {targets}\n")
    summaries = []
    for ac in targets:
        try:
            s = build_one(ac, force=args.force)
            if s["skipped_existing"]:
                print(f"  AC {ac}: ◌ skipped (structures/ already exists; "
                       f"use --force to regenerate)")
                summaries.append(s)
                continue
            ext_note = f"  [extension: {s['extension']}]" if s["extension"] else ""
            print(f"  AC {ac}: axes={s['axes_written']:>2}  "
                  f"joints={s['joints_written']:>2}  "
                  f"aggregate_buckets={s['aggregate_buckets']:>2}{ext_note}")
            summaries.append(s)
        except FileNotFoundError as e:
            print(f"  AC {ac}: ✗ {e}")

    print(f"\nWrote configs to:")
    for s in summaries:
        print(f"  simulations/wb_2021_ac{s['ac']}/structures/")
    print(f"\n📌 All entries tagged 'needs_review: true' — audit before "
          f"running population sampling.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
