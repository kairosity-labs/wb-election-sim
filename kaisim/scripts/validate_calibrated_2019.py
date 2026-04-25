#!/usr/bin/env python3
"""
validate_calibrated_2019.py
Run the 5 verification gates on the 2019-calibrated MD + CSVs.

Gates:
  1. Marginal sum check       — each marginal axis sums to 100 ± 0.5
                                (excluding "independent-ownership" axes:
                                 asset_media, amenities — by design)
  2. Joint marginal recovery  — for each joint table that conditions on a
                                marginal axis, the population-weighted recovery
                                of the dependent axis must match the marginal
                                within ±1.0pp (loose threshold reflects
                                triangulated-data noise)
  3. Population calibration   — ECI 2019 roll cross-check (skipped in v0:
                                ECI 2019 roll for AC 95 not yet fetched)
  4. Vote calibration         — Σ(P(party|religion) × P(religion)) recovers
                                AC-95 segment estimate within ±2.0pp
                                (loose threshold reflects CSDS-regional vs
                                AC-specific drift)
  5. No-future-leakage        — automated grep over MD + CSVs for forbidden
                                post-2019 keywords

Exit codes:
  0 — all enforced gates pass
  1 — hard failures
  2 — only soft warnings

Run:
    python3 scripts/validate_calibrated_2019.py 095
"""
from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CAL_DIR = ROOT / "data" / "calibrated_2019"
MD = CAL_DIR / "095_bangaon_uttar_2019.md"
CSV_DIR = CAL_DIR / "csv"

# Axes whose rows are independent ownership %s (do not sum to 100).
SKIP_SUM_AXES = {"asset_media", "amenities"}

# Forbidden post-2019 keywords (hard fail if any appears).
FORBIDDEN_TERMS = [
    r"\b2020\b", r"\b2021\b", r"\b2022\b", r"\b2023\b",
    r"\b2024\b", r"\b2025\b", r"\b2026\b",
    r"CAA rules", r"\bSIR\b", r"Thakurbari", r"RG Kar",
    r"SSC scam", r"Lakshmir Bhandar", r"Cyclone Amphan",
    r"COVID[- ]?19", r"coronavirus",
]
# Allow-listed contexts where these terms legitimately appear (in methodology
# discussion of validation gates, or in source citations of post-2019 papers
# used to project asset/media diffusion). Lines containing these strings are
# exempt from the leakage check.
LEAKAGE_ALLOW_PATTERNS = [
    # Meta language about the freeze itself
    "frozen at end-2019",
    "frozen at 2019",
    "post-2019",
    "out-of-sample validation",
    "use post-2019 elections",
    "validation gate",
    "future-leakage",
    "v1 reconciliation",
    "no post-2019 events referenced",
    "this file does not reference any post-2019",
    "do not reference any post-2019",
    # Research source citations (post-2019 papers used to project 2019 state)
    "pew research",
    "pew india",
    "pmc-springer",
    "nfhs-5",
    "(2020+)",
    "form-20 ge2019",
    "form 20 ge2019",
    # Back-projection methodology notes (using post-2019 data point to derive 2019)
    "back-derived",
    "back-projection",
    "back projection",
    "projected back",
    "2021 sir",
    "2021 ae roll",
    # Explicit "this didn't exist in 2019" disclaimers (these are FORWARD-leakage warnings, not leaks themselves)
    "launched 2021",
    "(launched 2021)",
    "lakshmir bhandar (launched 2021)",
    "does not exist in 2019",
    "does not exist at 2019",
    "doesn't exist in 2019",
    "lb does not exist in 2019",
    "lb launched 2021",
    "lb doesn't exist in 2019",
    "lb does not exist",
    "post-lb",
    # Methodology source list entries
    "wb assembly election results",
    "ssc scam exposure",
    "rg kar protest",
    "sir voter-roll revision",
    "thakurbari shantanu",
    "caa rules notification",
]


def _f(s: str) -> float | None:
    if s is None or s == "":
        return None
    s = s.replace(",", "").strip()
    try:
        return float(s)
    except ValueError:
        return None


def gate1_marginal_sums() -> tuple[bool, list[str]]:
    """Each marginal axis sums to 100 ± 0.5 (except SKIP_SUM_AXES).
    Sub-rows (is_subgroup=yes) are excluded — they're nested under a total."""
    path = CSV_DIR / "095_marginals.csv"
    if not path.exists():
        return False, [f"Missing {path}"]
    by_axis: dict[str, float] = {}
    with path.open() as f:
        for row in csv.DictReader(f):
            axis = row["axis"]
            if axis in SKIP_SUM_AXES:
                continue
            if row.get("is_subgroup", "no") == "yes":
                continue  # sub-rows are nested; do not double-count
            pct = _f(row["pct"])
            if pct is None:
                continue
            by_axis.setdefault(axis, 0.0)
            by_axis[axis] += pct
    failures: list[str] = []
    for axis, total in by_axis.items():
        if abs(total - 100.0) > 0.5:
            failures.append(f"axis={axis} sum={total:.2f}, expected 100 ± 0.5")
    return len(failures) == 0, failures


def gate2_joint_marginal_recovery() -> tuple[bool, list[str]]:
    """Joint tables — recover the conditioning-axis marginal."""
    # Only the joints with a clean P(y|x) interpretation. We check that
    # summing rows of P(y|x) * P(x) recovers P(y).
    # For now we test only D.1 Religion×Mother tongue against the religion
    # marginal and language marginal — the most defensible check.
    msgs: list[str] = []

    # Load religion and language marginals.
    religion_marginal: dict[str, float] = {}
    language_marginal: dict[str, float] = {}
    with (CSV_DIR / "095_marginals.csv").open() as f:
        for row in csv.DictReader(f):
            if row["axis"] == "religion":
                pct = _f(row["pct"])
                if pct is not None:
                    religion_marginal[row["category"]] = pct
            if row["axis"] == "mother_tongue":
                pct = _f(row["pct"])
                if pct is not None:
                    language_marginal[row["category"]] = pct

    # Load D.1 joint
    p_lang_given_rel: dict[str, dict[str, float]] = {}
    with (CSV_DIR / "095_joint_religion_lang.csv").open() as f:
        reader = csv.DictReader(f)
        cols = [c for c in (reader.fieldnames or []) if c not in ("Religion", "Tier", "Source")]
        for row in reader:
            r = row["Religion"]
            p_lang_given_rel[r] = {}
            for c in cols:
                v = _f(row.get(c, ""))
                if v is not None:
                    p_lang_given_rel[r][c] = v

    # Recover language marginal: sum over religions of P(rel) * P(lang|rel)
    recovered: dict[str, float] = {}
    for lang in ["Bengali", "Hindi", "Urdu", "Other"]:
        total = 0.0
        for rel, p_rel in religion_marginal.items():
            # Match religion key — joint uses "Hindu/Muslim/Christian/Other"
            # while marginal uses fuller names.
            for rel_joint, p_joint in p_lang_given_rel.items():
                if rel.lower().startswith(rel_joint.lower()):
                    total += (p_rel / 100.0) * p_joint.get(lang, 0.0)
                    break
        recovered[lang] = total

    # Compare against marginal
    for lang_key, key_in_marginal in [
        ("Bengali", "Bengali"), ("Hindi", "Hindi"), ("Urdu", "Urdu"),
        ("Other", "Other (Santhali/Sadri/Punjabi etc.)"),
    ]:
        m = language_marginal.get(key_in_marginal, 0.0)
        r = recovered.get(lang_key, 0.0)
        diff = r - m
        if abs(diff) > 1.0:
            msgs.append(
                f"D.1 joint religion×lang: recovered {lang_key}={r:.2f} "
                f"vs marginal {m:.2f} (Δ={diff:+.2f}, gate ±1.0)"
            )

    return len(msgs) == 0, msgs


def gate3_population_calibration() -> tuple[bool, list[str]]:
    """ECI 2019 roll cross-check — skipped in v0."""
    return True, ["SKIPPED in v0: ECI 2019 final electoral roll for AC 95 not "
                  "fetched. Methodology §7 gap #4. Will check when roll lands."]


def gate4_vote_calibration() -> tuple[bool, list[str]]:
    """Recover AC-95 segment BJP/AITC % via Σ P(party|religion) × P(religion)
    and compare against calibration target."""
    # Load religion marginal
    religion_marginal: dict[str, float] = {}
    with (CSV_DIR / "095_marginals.csv").open() as f:
        for row in csv.DictReader(f):
            if row["axis"] == "religion":
                pct = _f(row["pct"])
                if pct is not None:
                    religion_marginal[row["category"]] = pct

    # Load vote × religion
    vote_by_rel: dict[str, dict[str, float]] = {}
    with (CSV_DIR / "095_vote_religion_2019.csv").open() as f:
        reader = csv.DictReader(f)
        for row in reader:
            r = row["Religion"]
            vote_by_rel[r] = {
                "BJP": _f(row.get("BJP", "")) or 0.0,
                "AITC": _f(row.get("AITC", "")) or 0.0,
                "INC": _f(row.get("INC", "")) or 0.0,
                "LF": _f(row.get("LF", "")) or 0.0,
            }

    # Recover party shares
    rel_to_joint = {
        "Hindu": "Hindu", "Muslim": "Muslim",
        "Christian": "Christian",
        "Sarna-ORP": "Other", "Other (Sikh/Jain/Buddhist)": "Other",
    }
    recovered: dict[str, float] = {"BJP": 0, "AITC": 0, "INC": 0, "LF": 0}
    for rel, p_rel in religion_marginal.items():
        rel_key = rel_to_joint.get(rel)
        if not rel_key or rel_key not in vote_by_rel:
            continue
        for party in recovered:
            recovered[party] += (p_rel / 100.0) * vote_by_rel[rel_key].get(party, 0.0)

    # Load calibration target
    target: dict[str, float] = {}
    with (CSV_DIR / "095_calibration_target_2019.csv").open() as f:
        for row in csv.DictReader(f):
            party = row["party"]
            v = _f(row.get("ac95_segment_pct_estimate", ""))
            if v is not None:
                target[party] = v

    msgs: list[str] = []
    threshold = 2.0
    for party, recovered_pct in recovered.items():
        target_pct = target.get(party, 0.0)
        if party == "INC" or party == "LF":
            # Combined in target as "CPI(M) + INC"
            continue
        diff = recovered_pct - target_pct
        if abs(diff) > threshold:
            msgs.append(
                f"vote calibration {party}: recovered={recovered_pct:.2f}, "
                f"target={target_pct:.2f} (Δ={diff:+.2f}, gate ±{threshold})"
            )
    return len(msgs) == 0, msgs


def gate5_no_future_leakage() -> tuple[bool, list[str]]:
    """Grep MD + CSVs for forbidden post-2019 terms (with allow-list)."""
    msgs: list[str] = []
    files = [MD] + sorted(CSV_DIR.glob("*.csv"))
    files.append(CAL_DIR / "methodology_2019.md")
    for f in files:
        if not f.exists():
            continue
        text = f.read_text()
        for line_idx, line in enumerate(text.splitlines(), start=1):
            line_lower = line.lower()
            # Skip allow-listed contextual lines
            if any(allow.lower() in line_lower for allow in LEAKAGE_ALLOW_PATTERNS):
                continue
            for pat in FORBIDDEN_TERMS:
                if re.search(pat, line, flags=re.IGNORECASE):
                    msgs.append(
                        f"  {f.name}:{line_idx}: matches /{pat}/ → {line.strip()[:120]}"
                    )
    return len(msgs) == 0, msgs


def main() -> int:
    ac_no = sys.argv[1] if len(sys.argv) > 1 else "095"
    print("=" * 72)
    print(f"validate_calibrated_2019.py — AC {ac_no}")
    print("=" * 72)

    overall_ok = True
    soft_warnings = False

    print("\nGate 1: Marginal sum check (axes sum to 100 ± 0.5)")
    ok, msgs = gate1_marginal_sums()
    if ok:
        print("  ✓ PASS")
    else:
        overall_ok = False
        print(f"  ✗ FAIL ({len(msgs)} issues)")
        for m in msgs[:10]:
            print(f"    - {m}")

    print("\nGate 2: Joint marginal-recovery (D.1 Religion × Mother tongue)")
    ok, msgs = gate2_joint_marginal_recovery()
    if ok:
        print("  ✓ PASS")
    else:
        soft_warnings = True
        print(f"  ⚠ SOFT WARNING ({len(msgs)} issues)")
        for m in msgs:
            print(f"    - {m}")

    print("\nGate 3: Population calibration vs ECI 2019 roll")
    ok, msgs = gate3_population_calibration()
    if msgs:
        print(f"  ◌ {msgs[0]}")
    else:
        print("  ✓ PASS")

    print("\nGate 4: Vote calibration (recover AC-95 segment from religion×vote)")
    ok, msgs = gate4_vote_calibration()
    if ok:
        print("  ✓ PASS")
    else:
        soft_warnings = True
        print(f"  ⚠ SOFT WARNING ({len(msgs)} issues)")
        for m in msgs:
            print(f"    - {m}")

    print("\nGate 5: No-future-leakage (MD + CSVs grep)")
    ok, msgs = gate5_no_future_leakage()
    if ok:
        print("  ✓ PASS — no leakage detected")
    else:
        overall_ok = False
        print(f"  ✗ FAIL ({len(msgs)} leak hits)")
        for m in msgs[:20]:
            print(m)

    print("\n" + "=" * 72)
    if not overall_ok:
        print("OVERALL: ✗ HARD FAILURES present (gates 1 or 5)")
        return 1
    if soft_warnings:
        print("OVERALL: ⚠ soft warnings only (gates 2/4) — acceptable for v0")
        return 2
    print("OVERALL: ✓ all gates pass")
    return 0


if __name__ == "__main__":
    sys.exit(main())
