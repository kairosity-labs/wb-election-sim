#!/usr/bin/env python3
"""
_fill_ac.py — generalized pilot-AC fill.

Reads per-AC value dictionaries (tier-E pilot imputations from CDB/block-level
research) from scripts/_pilot_values.py and patches the corresponding rows in
data/constituencies.csv. Each (column, tier) pair is applied conservatively:
only overwritten if the new tier beats the existing tier.

The pilot profiles in constituencies/NNN_name.md remain the human-readable
source of truth for these values; this script is just the machine sync.

Run:
    python3 scripts/_fill_ac.py            # apply all pilots in _pilot_values
    python3 scripts/_fill_ac.py 95         # apply only AC 95
"""
from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CSV_PATH = ROOT / "data" / "constituencies.csv"

TIER_ORDER = {"A": 5, "B": 4, "C": 3, "D": 2, "E": 1, "": 0}


def tier_beats(new: str, existing: str) -> bool:
    return TIER_ORDER.get(new, 0) > TIER_ORDER.get(existing, 0)


def apply_values(ac_no: int, values: dict, sources_ref: str) -> int:
    """Patch constituencies.csv row for `ac_no` with `values`.

    values: {column_name: (value, tier) | None} — None means clear the cell.
    Returns number of cells updated.
    """
    with CSV_PATH.open() as f:
        reader = csv.reader(f)
        rows = list(reader)
    header = rows[0]
    idx = {c: i for i, c in enumerate(header)}

    target = None
    for i, r in enumerate(rows[1:], start=1):
        if r[idx["ac_no"]] == str(ac_no):
            target = i
            break
    if target is None:
        raise SystemExit(f"AC {ac_no} row not found")

    r = rows[target]
    updates = 0
    for col, spec in values.items():
        if col not in idx:
            raise KeyError(f"column {col!r} not in header")
        if spec is None:
            # Clear cell and paired conf.
            r[idx[col]] = ""
            conf_col = f"{col}_conf"
            if conf_col in idx:
                r[idx[conf_col]] = ""
            updates += 1
            continue
        value, tier = spec
        conf_col = f"{col}_conf"
        existing_tier = r[idx[conf_col]] if conf_col in idx else ""
        if not tier_beats(tier, existing_tier) and existing_tier != tier:
            continue
        r[idx[col]] = str(value)
        if conf_col in idx:
            r[idx[conf_col]] = tier
        updates += 1

    # Merge sources_json: preserve existing entries, add a pointer to the
    # profile MD for this AC.
    prov_idx = idx["sources_json"]
    try:
        existing = json.loads(r[prov_idx]) if r[prov_idx] else []
    except json.JSONDecodeError:
        existing = []
    existing = [p for p in existing if not (isinstance(p, dict) and p.get("ref") == sources_ref)]
    existing.append({"ref": sources_ref, "tier_range": "A-E", "accessed": "2026-04-24"})
    r[prov_idx] = json.dumps(existing)

    rows[target] = r
    with CSV_PATH.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerows(rows)
    return updates


def main() -> None:
    # Local import so the _pilot_values file can be edited in isolation.
    sys.path.insert(0, str(ROOT / "scripts"))
    try:
        from _pilot_values import PILOTS
    except ImportError:
        raise SystemExit("scripts/_pilot_values.py not found — create it first")

    target_ac = int(sys.argv[1]) if len(sys.argv) > 1 else None
    total = 0
    for ac_no, cfg in PILOTS.items():
        if target_ac is not None and ac_no != target_ac:
            continue
        updates = apply_values(ac_no, cfg["values"], cfg["sources_ref"])
        total += updates
        print(f"AC {ac_no} {cfg['name']}: {updates} cells updated")
    print(f"Total: {total} cell updates across {len(PILOTS) if target_ac is None else 1} AC(s)")


if __name__ == "__main__":
    main()
