#!/usr/bin/env python3
"""
split_events_state_vs_ac.py

Splits the 10 per-AC events.yaml files into:

  constituency_data/state_events_2019_2026.yaml
      — all events with scope=national or scope=state, deduped by slug
        (richest version kept when multiple ACs carry the same slug)

  constituency_data/constituencies/{name}/events.yaml
      — only events with scope=district or scope=AC (in-place rewrite)

Run:
    python3 kaisim/scripts/split_events_state_vs_ac.py
"""
from __future__ import annotations

import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
CONSTS_DIR = ROOT.parent / "constituency_data" / "constituencies"
STATE_FILE = ROOT.parent / "constituency_data" / "state_events_2019_2026.yaml"

STATE_SCOPES = {"national", "state"}
LOCAL_SCOPES = {"district", "AC"}


def _richness(ev: dict) -> int:
    """Score an event by content volume — used to pick the best copy of a dupe slug."""
    return (
        len(ev.get("summary") or "") +
        len(ev.get("sources") or []) * 20 +
        len(ev.get("tags") or []) * 5 +
        len(ev.get("valence") or {}) * 5
    )


def _date_key(ev: dict) -> str:
    return str(ev.get("date") or ev.get("date_start") or "9999-12-31")


def main() -> int:
    ac_files = sorted(CONSTS_DIR.glob("*/events.yaml"))
    if not ac_files:
        print("ERROR: no events.yaml files found under constituency_data/constituencies/")
        return 1

    # --- Pass 1: collect all national/state events across all ACs ---
    state_pool: dict[str, dict] = {}   # slug → richest event

    for path in ac_files:
        data = yaml.safe_load(path.read_text()) or {}
        for ev in data.get("events", []):
            if ev.get("scope") not in STATE_SCOPES:
                continue
            slug = ev.get("slug")
            if not slug:
                continue
            existing = state_pool.get(slug)
            if existing is None or _richness(ev) > _richness(existing):
                state_pool[slug] = ev

    sorted_state = sorted(state_pool.values(), key=_date_key)
    print(f"State/national pool: {len(sorted_state)} unique events")

    # --- Write state_events_2019_2026.yaml ---
    # Preserve cutoff_date from any AC file (they all share the same value)
    cutoff = None
    for path in ac_files:
        d = yaml.safe_load(path.read_text()) or {}
        if d.get("cutoff_date"):
            cutoff = d["cutoff_date"]
            break

    state_out: dict = {}
    if cutoff:
        state_out["cutoff_date"] = cutoff
    state_out["events"] = sorted_state

    with STATE_FILE.open("w") as f:
        yaml.dump(state_out, f, allow_unicode=True, default_flow_style=False,
                  sort_keys=False, width=88)
    print(f"Wrote: {STATE_FILE.relative_to(ROOT.parent)}\n")

    # --- Pass 2: rewrite each AC file keeping only district/AC events ---
    state_slugs = set(state_pool.keys())

    for path in ac_files:
        data = yaml.safe_load(path.read_text()) or {}
        all_events = data.get("events", [])

        local_events = [
            ev for ev in all_events
            if ev.get("scope") in LOCAL_SCOPES
        ]

        # Sanity: warn about any events with unexpected scope
        unknown = [
            ev for ev in all_events
            if ev.get("scope") not in STATE_SCOPES | LOCAL_SCOPES
        ]
        if unknown:
            print(f"  ⚠ {path.parent.name}: {len(unknown)} events with unrecognised scope "
                  f"({[e.get('scope') for e in unknown[:3]]}…) — kept in AC file")
            local_events += unknown

        local_events.sort(key=_date_key)

        ac_out: dict = {}
        if data.get("cutoff_date"):
            ac_out["cutoff_date"] = data["cutoff_date"]
        ac_out["events"] = local_events

        with path.open("w") as f:
            yaml.dump(ac_out, f, allow_unicode=True, default_flow_style=False,
                      sort_keys=False, width=88)

        removed = len(all_events) - len(local_events) + len(unknown)
        print(f"  {path.parent.name}: {len(all_events)} → {len(local_events)} events "
              f"(removed {removed} state/national)")

    return 0


if __name__ == "__main__":
    sys.exit(main())
