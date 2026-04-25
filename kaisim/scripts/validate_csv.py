#!/usr/bin/env python3
"""
validate_csv.py — internal-consistency validator for data/constituencies.csv.

Enforces the §5 Verification checks from data/methodology.md.

Exit code:
  0 = all checks pass
  1 = hard failures (row count, missing columns, null tiers on populated cells)
  2 = soft warnings (sum mismatches, district roll-up drift)

Run:
    python3 scripts/validate_csv.py
"""
from __future__ import annotations

import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CSV_PATH = ROOT / "data" / "constituencies.csv"

RELIGION_COLS = ["hindu_pct", "muslim_pct", "christian_pct", "sarna_orp_pct", "other_religion_pct"]
LANGUAGE_COLS = [
    "bengali_pct", "hindi_pct", "santhali_pct", "urdu_pct",
    "nepali_pct", "rajbanshi_lang_pct", "kurmali_pct", "other_lang_pct",
]
SC_SUB_COLS = [
    "namasudra_matua_pct_est", "rajbanshi_pct_est",
    "bagdi_pct_est", "poundra_pct_est", "other_sc_pct_est",
]
ST_SUB_COLS = [
    "santhal_pct_est", "oraon_pct_est", "munda_pct_est",
    "bhumij_pct_est", "other_st_pct_est",
]


def _f(s: str) -> float | None:
    if s == "" or s is None:
        return None
    try:
        return float(s)
    except ValueError:
        return None


def main() -> int:
    if not CSV_PATH.exists():
        print(f"ERROR: {CSV_PATH} missing")
        return 1
    with CSV_PATH.open() as f:
        rows = list(csv.reader(f))
    header = rows[0]
    idx = {c: i for i, c in enumerate(header)}
    data = rows[1:]

    hard_fails: list[str] = []
    warnings: list[str] = []

    # --- Hard checks -----------------------------------------------------
    if len(data) != 294:
        hard_fails.append(f"row count {len(data)}, expected 294")

    # Every cell with a value should have a non-empty confidence tier.
    for r in data:
        ac_no = r[idx["ac_no"]]
        for col_name, col_idx in idx.items():
            if col_name.endswith("_conf") or col_name in {"ac_no", "ac_name", "district", "reservation", "sources_json"}:
                continue
            value = r[col_idx]
            if value == "":
                continue
            conf_col = f"{col_name}_conf"
            if conf_col not in idx:
                continue  # column without a conf pair, ok
            if r[idx[conf_col]] == "":
                hard_fails.append(f"AC {ac_no}: {col_name}={value} has empty tier")

    # --- Soft checks (per-row sum consistency) ---------------------------
    def _row_sum(row, cols):
        vals = [_f(row[idx[c]]) for c in cols]
        populated = [v for v in vals if v is not None]
        return sum(populated) if populated else None, len(populated), len(cols)

    for r in data:
        ac_no = r[idx["ac_no"]]

        rel_sum, rel_pop, rel_n = _row_sum(r, RELIGION_COLS)
        if rel_sum is not None and rel_pop == rel_n and abs(rel_sum - 100.0) > 0.5:
            warnings.append(f"AC {ac_no}: religion sum {rel_sum:.2f}, expected 100 ± 0.5")

        lang_sum, lang_pop, lang_n = _row_sum(r, LANGUAGE_COLS)
        if lang_sum is not None and lang_pop == lang_n and abs(lang_sum - 100.0) > 0.5:
            warnings.append(f"AC {ac_no}: language sum {lang_sum:.2f}, expected 100 ± 0.5")

        sc_total = _f(r[idx["sc_total_pct"]])
        sc_sub_sum, sc_pop, sc_n = _row_sum(r, SC_SUB_COLS)
        if sc_total is not None and sc_sub_sum is not None and sc_pop == sc_n:
            if abs(sc_sub_sum - sc_total) > 1.0:
                warnings.append(
                    f"AC {ac_no}: SC sub-group sum {sc_sub_sum:.2f} vs sc_total_pct {sc_total:.2f} (Δ>1)"
                )

        st_total = _f(r[idx["st_total_pct"]])
        st_sub_sum, st_pop, st_n = _row_sum(r, ST_SUB_COLS)
        if st_total is not None and st_sub_sum is not None and st_pop == st_n:
            if abs(st_sub_sum - st_total) > 1.0:
                warnings.append(
                    f"AC {ac_no}: ST sub-group sum {st_sub_sum:.2f} vs st_total_pct {st_total:.2f} (Δ>1)"
                )

        # Electorate consistency: if M+F+TG populated, must sum to total (±0).
        m = _f(r[idx["male_electors"]])
        fe = _f(r[idx["female_electors"]])
        tot = _f(r[idx["total_electors_2026"]])
        if m is not None and fe is not None and tot is not None:
            if abs(m + fe - tot) > 100:  # allow small TG slack
                warnings.append(f"AC {ac_no}: M+F ({m+fe:.0f}) vs total ({tot:.0f}) Δ>100")

    # --- Report ----------------------------------------------------------
    print("=" * 70)
    print(f"validate_csv.py — {CSV_PATH}")
    print("=" * 70)
    print(f"Rows: {len(data)} (expect 294)")
    print(f"Cols: {len(header)}")
    populated = sum(1 for r in data if r[idx['total_electors_2026']])
    print(f"Electorate populated: {populated}/294")

    if not hard_fails and not warnings:
        print("\n✓ ALL CHECKS PASS")
        return 0

    if hard_fails:
        print(f"\n✗ {len(hard_fails)} HARD FAILURES:")
        for msg in hard_fails[:20]:
            print(f"  - {msg}")
        if len(hard_fails) > 20:
            print(f"  ... and {len(hard_fails) - 20} more")

    if warnings:
        print(f"\n⚠ {len(warnings)} WARNINGS:")
        for msg in warnings[:20]:
            print(f"  - {msg}")
        if len(warnings) > 20:
            print(f"  ... and {len(warnings) - 20} more")

    return 1 if hard_fails else 2


if __name__ == "__main__":
    sys.exit(main())
