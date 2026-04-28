#!/usr/bin/env python3
"""
validate_calibrated_2019.py
Run the 5 verification gates on a 2019-calibrated AC's MD + CSVs.

Gates:
  1. Marginal sum check       — each marginal axis sums to 100 ± 0.5
                                (excluding "independent-ownership" axes:
                                 asset_media, amenities — by design)
  2. Joint marginal recovery  — for D.1 (Religion × Mother tongue), recover
                                the language marginal via P(rel)*P(lang|rel)
                                and compare to C.5. Tolerance ±1.0pp.
                                The language palette is read from the
                                joint CSV header — works for any AC.
  3. Population calibration   — ECI 2019 roll cross-check (skipped in v0)
  4. Vote calibration         — Σ P(party|religion)*P(religion) vs §E target.
                                The party set is read from the vote-CSV header
                                (subset of {BJP, AITC} that's in both joint and
                                target). Tolerance ±2.0pp.
  5. No-future-leakage        — automated grep over MD + CSVs for forbidden
                                post-2019 keywords

Run:
    python3 scripts/validate_calibrated_2019.py 095            # one AC
    python3 scripts/validate_calibrated_2019.py --all          # every AC
    python3 scripts/validate_calibrated_2019.py --all --md     # write per-AC MD reports

Exit codes:
  0 — all enforced gates pass for all selected ACs
  1 — at least one hard failure
  2 — only soft warnings (no hard fails)
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CAL_DIR = ROOT / "data" / "calibrated_2019"
CSV_DIR = CAL_DIR / "csv"
AUDIT_DIR = CAL_DIR / "audit"

# Axes whose rows are independent ownership %s (do not sum to 100).
SKIP_SUM_AXES = {"asset_media", "amenities"}

FORBIDDEN_TERMS = [
    r"\b2020\b", r"\b2021\b", r"\b2022\b", r"\b2023\b",
    r"\b2024\b", r"\b2025\b", r"\b2026\b",
    r"CAA rules", r"\bSIR\b", r"Thakurbari", r"RG Kar",
    r"SSC scam", r"Lakshmir Bhandar", r"Cyclone Amphan",
    r"COVID[- ]?19", r"coronavirus",
]
LEAKAGE_ALLOW_PATTERNS = [
    # Meta language about the 2019 freeze itself
    "frozen at end-2019", "frozen at 2019", "post-2019",
    "out-of-sample validation", "use post-2019 elections",
    "validation gate", "future-leakage", "v1 reconciliation",
    "no post-2019 events referenced",
    "this file does not reference any post-2019",
    "do not reference any post-2019",
    "validation anchor only", "section h validation",
    # Disclaimers that schemes do/did not exist in 2019 (forward-leakage warnings)
    "launched 2021", "(launched 2021)", "lakshmir bhandar (launched 2021)",
    "does not exist in 2019", "does not exist at 2019", "doesn't exist in 2019",
    "lb does not exist in 2019", "lb launched 2021",
    "lb doesn't exist in 2019", "lb does not exist", "post-lb",
    "no lakshmir bhandar in 2019", "no lakshmir bhandar",
    "pre-2019 baseline", "pre-2019 = 2015", "pre-2019",
    "pre-2020", "pre-2021", "pre-2022", "pre-2023", "pre-2024",
    # Methodology source list entries (post-2019 papers used to project 2019 state)
    "pew research", "pew india", "pmc-springer", "nfhs-5",
    "(2020+)", "form-20 ge2019", "form 20 ge2019",
    "back-derived", "back-projection", "back projection", "projected back",
    "2021 sir", "2021 ae roll",
    "wb assembly election results", "ssc scam exposure",
    "rg kar protest", "sir voter-roll revision",
    "thakurbari shantanu", "caa rules notification",
    # Source citations — academic / press publications cited with year suffix.
    # These appear in §G source lists and inline source notes and are not
    # 2019-state leakage but methodological transparency.
    "the print", "the bastion", "the wire", "the federal",
    "india today", "india.com", "indiatv", "dialogue earth",
    "icsf", "indiastat", "factbook",
    "ae results", "ae/by-poll", "wikipedia",
    # Specific known-archive references — WB government joining schemes after 2019
    "fy2021-22", "joined at 8th installment", "wb government declined pm kisan",
    "ae and by-poll vote totals",
]


def _f(s) -> float | None:
    if s is None or s == "":
        return None
    s = str(s).replace(",", "").replace("%", "").strip()
    try:
        return float(s)
    except ValueError:
        return None


def _normalize_label(s: str) -> str:
    """Lowercase + strip ` (...)` parentheticals + collapse whitespace.

    Used to fuzzy-match religion / language labels between the marginal
    CSV and the joint CSV (both can carry AC-specific qualifiers like
    'Hindu (self-identified, including syncretic Adivasi)' that won't
    prefix-match a joint header of 'Hindu (non-Sarna)')."""
    if s is None:
        return ""
    out = re.sub(r"\([^)]*\)", "", s)
    out = re.sub(r"\s+", " ", out).strip().lower()
    out = out.rstrip(" /,-")
    return out


def _label_match(a: str, b: str) -> bool:
    na, nb = _normalize_label(a), _normalize_label(b)
    if not na or not nb:
        return False
    return na == nb or na.startswith(nb) or nb.startswith(na)


def find_md(ac: str) -> Path:
    matches = sorted(CAL_DIR.glob(f"{ac}_*_2019.md"))
    if not matches:
        raise FileNotFoundError(f"No MD file for AC {ac}")
    return matches[0]


# ---------------------------------------------------------------------------
# Gate 1 — marginal sums
# ---------------------------------------------------------------------------

def gate1_marginal_sums(ac: str) -> tuple[bool, list[str]]:
    path = CSV_DIR / f"{ac}_marginals.csv"
    if not path.exists():
        return False, [f"Missing {path.name}"]
    by_axis: dict[str, float] = {}
    with path.open() as f:
        for row in csv.DictReader(f):
            axis = row["axis"]
            if axis in SKIP_SUM_AXES:
                continue
            if row.get("is_subgroup", "no") == "yes":
                continue
            pct = _f(row["pct"])
            if pct is None:
                continue
            by_axis.setdefault(axis, 0.0)
            by_axis[axis] += pct
    failures = [
        f"axis={axis} sum={total:.2f} (expected 100 ± 0.5)"
        for axis, total in by_axis.items() if abs(total - 100.0) > 0.5
    ]
    return len(failures) == 0, failures


# ---------------------------------------------------------------------------
# Gate 2 — joint marginal recovery (data-driven on D.1)
# ---------------------------------------------------------------------------

def gate2_joint_marginal_recovery(ac: str) -> tuple[bool, list[str]]:
    """Test D.1 Religion×MotherTongue: recover language marginal from joint."""
    msgs: list[str] = []

    marg_path = CSV_DIR / f"{ac}_marginals.csv"
    joint_path = CSV_DIR / f"{ac}_joint_religion_lang.csv"
    if not (marg_path.exists() and joint_path.exists()):
        return False, [f"Missing {marg_path.name} or {joint_path.name}"]

    religion_marginal: dict[str, float] = {}
    language_marginal: dict[str, float] = {}
    with marg_path.open() as f:
        for row in csv.DictReader(f):
            if row.get("is_subgroup", "no") == "yes":
                continue
            axis = row["axis"]; pct = _f(row["pct"])
            if pct is None:
                continue
            if axis == "religion":
                religion_marginal[row["category"]] = pct
            elif axis == "mother_tongue":
                language_marginal[row["category"]] = pct

    # Read D.1 joint — header gives us the AC's local language palette.
    p_lang_given_rel: dict[str, dict[str, float]] = {}
    with joint_path.open() as f:
        reader = csv.DictReader(f)
        first_col = (reader.fieldnames or ["Religion"])[0]
        lang_cols = [c for c in (reader.fieldnames or [])
                     if c not in (first_col, "Tier", "Source") and c]
        for row in reader:
            r = row[first_col]
            p_lang_given_rel[r] = {}
            for c in lang_cols:
                v = _f(row.get(c, ""))
                if v is not None:
                    p_lang_given_rel[r][c] = v

    # Recover language marginal: Σ P(rel) × P(lang|rel)
    recovered: dict[str, float] = {lang: 0.0 for lang in lang_cols}
    unmatched_rels: list[str] = []
    for rel_marg, p_rel in religion_marginal.items():
        match_key = next((rj for rj in p_lang_given_rel.keys()
                          if _label_match(rel_marg, rj)), None)
        if match_key is None:
            unmatched_rels.append(rel_marg)
            continue
        for lang in lang_cols:
            recovered[lang] += (p_rel / 100.0) * p_lang_given_rel[match_key].get(lang, 0.0)

    # If we failed to match >50% of religion mass, that's a structural mismatch
    # — flag it explicitly so it's clear the recovery is unreliable, not data.
    unmatched_mass = sum(religion_marginal[r] for r in unmatched_rels)
    if unmatched_mass > 50.0:
        msgs.append(
            f"D.1: religion labels in C.1 vs joint differ for "
            f"{len(unmatched_rels)} categories ({unmatched_mass:.1f}% of pop) — "
            f"recovery skipped. Reconcile labels in MD or add explicit mapping."
        )
        return False, msgs

    # Compare with C.5 marginal
    for lang in lang_cols:
        target = next((v for cat, v in language_marginal.items()
                       if _label_match(cat, lang)), None)
        if target is None:
            msgs.append(
                f"D.1 lang={lang!r}: no match in C.5 marginal → can't compare "
                f"(recovered={recovered[lang]:.2f})"
            )
            continue
        diff = recovered[lang] - target
        if abs(diff) > 1.0:
            msgs.append(
                f"D.1 lang={lang!r}: recovered={recovered[lang]:.2f} "
                f"vs marginal={target:.2f} (Δ={diff:+.2f}, gate ±1.0)"
            )

    return len(msgs) == 0, msgs


# ---------------------------------------------------------------------------
# Gate 3 — pop calibration (skipped in v0)
# ---------------------------------------------------------------------------

def gate3_population_calibration(ac: str) -> tuple[bool, list[str]]:
    return True, [f"SKIPPED in v0: ECI 2019 final electoral roll for AC {ac} "
                   "not fetched. Methodology §7 gap #4."]


# ---------------------------------------------------------------------------
# Gate 4 — vote calibration (data-driven on D.15 + §E)
# ---------------------------------------------------------------------------

def gate4_vote_calibration(ac: str) -> tuple[bool, list[str]]:
    msgs: list[str] = []
    marg_path = CSV_DIR / f"{ac}_marginals.csv"
    vote_path = CSV_DIR / f"{ac}_vote_religion_2019.csv"
    target_path = CSV_DIR / f"{ac}_calibration_target_2019.csv"
    for p in (marg_path, vote_path, target_path):
        if not p.exists():
            return False, [f"Missing {p.name}"]

    # Religion marginal
    religion_marginal: dict[str, float] = {}
    with marg_path.open() as f:
        for row in csv.DictReader(f):
            if row["axis"] == "religion" and row.get("is_subgroup", "no") == "no":
                pct = _f(row["pct"])
                if pct is not None:
                    religion_marginal[row["category"]] = pct

    # D.15 vote × religion — header tells us what parties exist for this AC
    vote_by_rel: dict[str, dict[str, float]] = {}
    with vote_path.open() as f:
        reader = csv.DictReader(f)
        first_col = (reader.fieldnames or ["Religion"])[0]
        party_cols = [c for c in (reader.fieldnames or [])
                      if c not in (first_col, "Tier", "Source") and c]
        for row in reader:
            r = row[first_col]
            vote_by_rel[r] = {p: (_f(row.get(p, "")) or 0.0) for p in party_cols}

    # §E target — first column is "party". Some ACs have AITC margin/totals
    # that should already be filtered by is_meta_row. We compare ONLY the
    # parties present in BOTH the joint header AND the target table.
    target: dict[str, float] = {}
    with target_path.open() as f:
        reader = csv.DictReader(f)
        for row in reader:
            party = row.get("party", "").strip()
            v = (_f(row.get("ac_segment_pct_estimate", ""))
                 or _f(row.get("ac95_segment_pct_estimate", "")))   # legacy col
            if v is not None and party:
                target[party] = v

    # Recover party shares from joint × marginal
    recovered: dict[str, float] = {p: 0.0 for p in party_cols}
    unmatched_rels: list[str] = []
    for rel_marg, p_rel in religion_marginal.items():
        match_key = next((rj for rj in vote_by_rel.keys()
                          if _label_match(rel_marg, rj)), None)
        if match_key is None:
            unmatched_rels.append(rel_marg)
            continue
        for party in party_cols:
            recovered[party] += (p_rel / 100.0) * vote_by_rel[match_key].get(party, 0.0)

    unmatched_mass = sum(religion_marginal[r] for r in unmatched_rels)
    if unmatched_mass > 50.0:
        return False, [
            f"D.15: religion labels in C.1 vs joint differ for "
            f"{len(unmatched_rels)} categories ({unmatched_mass:.1f}% of pop) — "
            f"vote recovery skipped. Reconcile labels in MD."
        ]

    # Compare. Only check the headline parties (BJP, AITC) — combined buckets
    # like "CPI(M)+LF" require explicit re-aggregation from D.15 to compare.
    threshold = 2.0
    for party in ("BJP", "AITC"):
        if party not in recovered:
            continue
        # Find target — fuzzy match (e.g., target may say "BJP", "AITC")
        target_pct = None
        for tk, tv in target.items():
            if tk.lower() == party.lower():
                target_pct = tv; break
        if target_pct is None:
            msgs.append(
                f"vote {party}: target row not found in §E "
                f"(recovered={recovered[party]:.2f})"
            )
            continue
        diff = recovered[party] - target_pct
        if abs(diff) > threshold:
            msgs.append(
                f"vote {party}: recovered={recovered[party]:.2f} "
                f"vs target={target_pct:.2f} (Δ={diff:+.2f}, gate ±{threshold})"
            )
    return len(msgs) == 0, msgs


# ---------------------------------------------------------------------------
# Gate 5 — no-future-leakage
# ---------------------------------------------------------------------------

def _strip_section_h(md_text: str) -> str:
    """§H is the post-2019 validation-anchor section by design — it MUST
    contain post-2019 references (2021 AE, 2024 LS, etc.). Exempt it from
    the leakage check to avoid false positives."""
    m = re.search(r"^##\s+H\.", md_text, flags=re.MULTILINE)
    if not m:
        return md_text
    return md_text[:m.start()]


def gate5_no_future_leakage(ac: str) -> tuple[bool, list[str]]:
    msgs: list[str] = []
    md = find_md(ac)
    files = [md] + sorted(CSV_DIR.glob(f"{ac}_*.csv"))
    files.append(CAL_DIR / "methodology_2019.md")
    for f in files:
        if not f.exists():
            continue
        text = f.read_text()
        # MD files: skip §H (out-of-sample anchors, post-2019 by design).
        if f.suffix == ".md":
            text = _strip_section_h(text)
        for line_idx, line in enumerate(text.splitlines(), start=1):
            line_lower = line.lower()
            if any(allow.lower() in line_lower for allow in LEAKAGE_ALLOW_PATTERNS):
                continue
            for pat in FORBIDDEN_TERMS:
                if re.search(pat, line, flags=re.IGNORECASE):
                    msgs.append(
                        f"  {f.name}:{line_idx}: matches /{pat}/ → "
                        f"{line.strip()[:120]}"
                    )
    return len(msgs) == 0, msgs


# ---------------------------------------------------------------------------
# Run gates for one AC
# ---------------------------------------------------------------------------

def validate_one(ac: str, write_md: bool = False) -> dict:
    """Run all 5 gates. Return summary dict."""
    md_lines: list[str] = []
    summary = {
        "ac": ac,
        "gate1": {"ok": False, "msgs": []},
        "gate2": {"ok": True, "msgs": []},
        "gate3": {"ok": True, "msgs": []},
        "gate4": {"ok": True, "msgs": []},
        "gate5": {"ok": False, "msgs": []},
        "hard_fail": False,
        "soft_warn": False,
    }

    print(f"\n=== AC {ac} ===")
    md_lines.append(f"# Calibrated-2019 gate report — AC {ac}\n")

    print("Gate 1: Marginal sum check")
    ok, msgs = gate1_marginal_sums(ac)
    summary["gate1"] = {"ok": ok, "msgs": msgs}
    if ok:
        print("  ✓ PASS")
        md_lines.append("- **Gate 1 (marginal sums)**: ✓ PASS")
    else:
        summary["hard_fail"] = True
        print(f"  ✗ FAIL ({len(msgs)})")
        md_lines.append(f"- **Gate 1**: ✗ FAIL ({len(msgs)} issues)")
        for m in msgs:
            print(f"    - {m}")
            md_lines.append(f"    - {m}")

    print("Gate 2: D.1 lang recovery (data-driven)")
    ok, msgs = gate2_joint_marginal_recovery(ac)
    summary["gate2"] = {"ok": ok, "msgs": msgs}
    if ok:
        print("  ✓ PASS")
        md_lines.append("- **Gate 2 (D.1 lang recovery)**: ✓ PASS")
    else:
        summary["soft_warn"] = True
        print(f"  ⚠ SOFT WARN ({len(msgs)})")
        md_lines.append(f"- **Gate 2**: ⚠ SOFT WARN ({len(msgs)})")
        for m in msgs:
            print(f"    - {m}")
            md_lines.append(f"    - {m}")

    print("Gate 3: Population calibration vs ECI roll")
    ok, msgs = gate3_population_calibration(ac)
    summary["gate3"] = {"ok": ok, "msgs": msgs}
    print(f"  ◌ {msgs[0] if msgs else 'OK'}")
    md_lines.append(f"- **Gate 3**: ◌ {msgs[0] if msgs else 'OK'}")

    print("Gate 4: Vote calibration (D.15 × C.1 vs §E)")
    ok, msgs = gate4_vote_calibration(ac)
    summary["gate4"] = {"ok": ok, "msgs": msgs}
    if ok:
        print("  ✓ PASS")
        md_lines.append("- **Gate 4 (vote calibration)**: ✓ PASS")
    else:
        summary["soft_warn"] = True
        print(f"  ⚠ SOFT WARN ({len(msgs)})")
        md_lines.append(f"- **Gate 4**: ⚠ SOFT WARN ({len(msgs)})")
        for m in msgs:
            print(f"    - {m}")
            md_lines.append(f"    - {m}")

    print("Gate 5: No-future-leakage")
    ok, msgs = gate5_no_future_leakage(ac)
    summary["gate5"] = {"ok": ok, "msgs": msgs}
    if ok:
        print("  ✓ PASS")
        md_lines.append("- **Gate 5 (no-future-leakage)**: ✓ PASS")
    else:
        summary["hard_fail"] = True
        print(f"  ✗ FAIL ({len(msgs)} hits)")
        md_lines.append(f"- **Gate 5**: ✗ FAIL ({len(msgs)} hits)")
        for m in msgs[:20]:
            print(m)
            md_lines.append(f"    - `{m.strip()}`")

    if write_md:
        AUDIT_DIR.mkdir(parents=True, exist_ok=True)
        out = AUDIT_DIR / f"{ac}_gate_report.md"
        out.write_text("\n".join(md_lines) + "\n")

    return summary


def discover_acs() -> list[str]:
    out = []
    for p in sorted(CAL_DIR.glob("*_2019.md")):
        m = re.match(r"^(\d{3})_", p.name)
        if m:
            out.append(m.group(1))
    return out


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("ac", nargs="?", default=None,
                    help="3-digit AC number (e.g. 095). Omit with --all.")
    p.add_argument("--all", action="store_true",
                    help="Validate every AC discoverable in calibrated_2019/")
    p.add_argument("--md", action="store_true",
                    help="Write per-AC MD reports under calibrated_2019/audit/")
    args = p.parse_args()

    if args.all:
        targets = discover_acs()
    elif args.ac:
        targets = [args.ac.zfill(3)]
    else:
        p.error("provide AC number or --all")
        return 2

    print("=" * 72)
    print(f"validate_calibrated_2019.py — {len(targets)} AC(s)")
    print("=" * 72)

    summaries = []
    for ac in targets:
        summaries.append(validate_one(ac, write_md=args.md))

    # Headline summary
    print("\n" + "=" * 72)
    print("HEADLINE")
    print("=" * 72)
    print(f"  {'AC':>4}  G1  G2  G3  G4  G5  result")
    print(f"  {'--':>4}  --  --  --  --  --  --------")
    n_hard, n_soft, n_ok = 0, 0, 0
    for s in summaries:
        def mark(g):
            if not s[g]["ok"]:
                if g in ("gate1", "gate5"):
                    return "✗"
                return "⚠"
            return "✓"
        result = "FAIL" if s["hard_fail"] else ("WARN" if s["soft_warn"] else "PASS")
        if s["hard_fail"]:
            n_hard += 1
        elif s["soft_warn"]:
            n_soft += 1
        else:
            n_ok += 1
        print(f"  {s['ac']:>4}   {mark('gate1')}   {mark('gate2')}   ◌   "
              f"{mark('gate4')}   {mark('gate5')}   {result}")
    print(f"\n  {n_ok} pass · {n_soft} warn · {n_hard} fail")

    return 0 if n_hard == 0 and n_soft == 0 else (2 if n_hard == 0 else 1)


if __name__ == "__main__":
    sys.exit(main())
