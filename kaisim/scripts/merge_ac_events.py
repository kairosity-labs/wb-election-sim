#!/usr/bin/env python3
"""
merge_ac_events.py
For each of the 10 calibrated ACs, merge the three per-AC event files
(2019_2021, 2019_2024, 2019_2026) into a single chronological events.yaml
and write it to constituency_data/constituencies/{id}_{name}/events.yaml.

Merge rules:
  - Deduplicate by slug; later timeline file wins (2019_2026 > 2019_2024 > 2019_2021)
  - Events are sorted by date (date_start preferred, then date)
  - Header comment + cutoff_date taken from the latest file (2019_2026)
  - Any event present in an older file but absent in a newer one is included

Run:
    python3 kaisim/scripts/merge_ac_events.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
NEWS_ROOT = ROOT / "simulations" / "wb_2021_ac095" / "news"
CONSTS_DIR = ROOT.parent / "constituency_data" / "constituencies"

TIMELINES = ["2019_2021", "2019_2024", "2019_2026"]

# Map name slug (part after acNNN_) → constituency_data folder
def _build_slug_map() -> dict[str, Path]:
    mapping = {}
    for d in sorted(CONSTS_DIR.iterdir()):
        if not d.is_dir():
            continue
        # e.g. "003_cooch_behar_uttar" → slug = "cooch_behar_uttar"
        parts = d.name.split("_", 1)
        if len(parts) == 2:
            mapping[parts[1]] = d
    return mapping


def _event_date_key(ev: dict) -> str:
    """Return a sortable date string (YYYY-MM-DD) for an event."""
    d = ev.get("date") or ev.get("date_start") or "9999-12-31"
    return str(d)


def _load_yaml(path: Path) -> dict:
    with path.open() as f:
        return yaml.safe_load(f) or {}


def merge_for_slug(news_slug: str, dest_dir: Path) -> dict:
    """Load the three timeline files for news_slug, merge, write events.yaml."""
    # Collect source dirs, newest last so later files win in dedup
    sources: list[tuple[str, Path]] = []
    for tl in TIMELINES:
        tl_dir = NEWS_ROOT / tl
        matches = sorted(tl_dir.glob(f"ac*_{news_slug}"))
        if matches:
            src_file = matches[0] / f"events_{tl}.yaml"
            if src_file.exists():
                sources.append((tl, src_file))

    if not sources:
        return {"slug": news_slug, "error": "no source files found"}

    # Merge: slug → event dict (later source wins)
    merged: dict[str, dict] = {}
    cutoff_date = None
    latest_data: dict = {}

    for tl, src_file in sources:
        data = _load_yaml(src_file)
        events = data.get("events") or []
        for ev in events:
            slug = ev.get("slug")
            if slug:
                merged[slug] = ev   # later wins
        # Keep the latest file's metadata
        latest_data = data
        if data.get("cutoff_date"):
            cutoff_date = data["cutoff_date"]

    # Sort by date
    sorted_events = sorted(merged.values(), key=_event_date_key)

    # Build output dict
    output: dict = {}
    if cutoff_date:
        output["cutoff_date"] = cutoff_date
    output["events"] = sorted_events

    # Write
    out_path = dest_dir / "events.yaml"
    with out_path.open("w") as f:
        yaml.dump(
            output,
            f,
            allow_unicode=True,
            default_flow_style=False,
            sort_keys=False,
            width=88,
        )

    return {
        "slug": news_slug,
        "dest": str(out_path.relative_to(ROOT.parent)),
        "sources": [tl for tl, _ in sources],
        "event_count": len(sorted_events),
    }


def main() -> int:
    slug_map = _build_slug_map()

    # Discover news slugs from the 2019_2026 timeline (most complete)
    news_slugs: list[str] = []
    for d in sorted((NEWS_ROOT / "2019_2026").iterdir()):
        if d.is_dir():
            m = re.match(r"^ac\d+_(.+)$", d.name)
            if m:
                news_slugs.append(m.group(1))

    print(f"Merging events for {len(news_slugs)} ACs\n")

    for news_slug in news_slugs:
        dest_dir = slug_map.get(news_slug)
        if dest_dir is None:
            print(f"  ✗ {news_slug}: no matching constituency_data folder")
            continue
        result = merge_for_slug(news_slug, dest_dir)
        if "error" in result:
            print(f"  ✗ {news_slug}: {result['error']}")
        else:
            print(f"  ✓ {result['dest']}")
            print(f"      sources: {result['sources']}  events: {result['event_count']}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
