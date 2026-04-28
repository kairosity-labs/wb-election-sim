"""NewsEvent + NewsPool — load and query the events YAML.

Events come from `simulations/<sim>/news/events_*.yaml`. Each event has:
    slug, date (or date_start+date_end), temporal, scope, intensity,
    headline, summary, tags, valence, broadcast, sources

NewsPool provides date-range queries and serves the orchestrator.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
from typing import Any, Iterator

import yaml


@dataclass
class NewsEvent:
    slug: str
    headline: str
    summary: str
    scope: str                          # national | state | district | AC
    intensity: int                      # 1-5
    temporal: str                       # chronic | episodic
    tags: list[str] = field(default_factory=list)
    valence: dict[str, str] = field(default_factory=dict)   # tag -> "positive"|"negative"|"ambient"
    broadcast: bool = False
    sources: list[str] = field(default_factory=list)

    # Episodic events have `date`; chronic have `date_start` + `date_end`.
    date: date | None = None
    date_start: date | None = None
    date_end: date | None = None

    @classmethod
    def from_dict(cls, d: dict) -> "NewsEvent":
        def _parse_date(v):
            if v is None:
                return None
            if isinstance(v, date):
                return v
            return date.fromisoformat(v)

        return cls(
            slug=d["slug"],
            headline=d["headline"],
            summary=d.get("summary", ""),
            scope=d["scope"],
            intensity=int(d["intensity"]),
            temporal=d["temporal"],
            tags=d.get("tags", []) or [],
            valence=d.get("valence", {}) or {},
            broadcast=bool(d.get("broadcast", False)),
            sources=d.get("sources", []) or [],
            date=_parse_date(d.get("date")),
            date_start=_parse_date(d.get("date_start")),
            date_end=_parse_date(d.get("date_end")),
        )

    @property
    def primary_date(self) -> date:
        """Best single date for sorting / display."""
        if self.date:
            return self.date
        return self.date_start

    def is_active_in(self, period_start: date, period_end: date) -> bool:
        """True if the event 'happens' or 'is ongoing' in the given window.

        Episodic: date falls inside [period_start, period_end].
        Chronic:  date_start <= period_end AND date_end >= period_start.
        """
        if self.temporal == "episodic":
            return self.date is not None and period_start <= self.date <= period_end
        if self.temporal == "chronic":
            ds = self.date_start or self.date
            de = self.date_end or self.date_start or self.date
            if ds is None:
                return False
            return ds <= period_end and de >= period_start
        return False

    def is_first_appearance_in(self, period_start: date, period_end: date) -> bool:
        """True if this is the FIRST period this event becomes active.

        Used so chronic events are delivered as a 'started happening' shock
        on first occurrence and (optionally) recurring background later.
        """
        if self.temporal == "episodic":
            return self.is_active_in(period_start, period_end)
        ds = self.date_start or self.date
        if ds is None:
            return False
        return period_start <= ds <= period_end


class NewsPool:
    """Loaded events with date-range query."""

    def __init__(self, events: list[NewsEvent], cutoff_date: date | None = None):
        self.events = sorted(events, key=lambda e: e.primary_date)
        self.cutoff_date = cutoff_date

    @classmethod
    def from_yaml(cls, path: str | Path) -> "NewsPool":
        doc = yaml.safe_load(Path(path).read_text())
        events = [NewsEvent.from_dict(e) for e in doc.get("events", [])]
        cutoff = doc.get("cutoff_date")
        cutoff = date.fromisoformat(cutoff) if isinstance(cutoff, str) else cutoff
        return cls(events, cutoff_date=cutoff)

    @classmethod
    def from_yamls(cls, paths: list[str | Path]) -> "NewsPool":
        """Union of multiple events YAMLs.

        Use case: simulation reads the per-AC events.yaml AND the global
        state_events.yaml so personas see both AC-local stories AND
        state/national-scope news that affects all ACs.

        - Events de-duplicate by `slug`. The FIRST occurrence wins, so put
          AC-local files first if you want them to override state-level
          slugs (rare; mostly for republished events with refined per-AC
          metadata).
        - cutoff_date is the EARLIEST across loaded files (conservative —
          don't surface events past the AC's freeze date).
        """
        all_events: list[NewsEvent] = []
        seen_slugs: set[str] = set()
        cutoffs: list[date] = []
        for p in paths:
            p = Path(p)
            if not p.exists():
                continue
            doc = yaml.safe_load(p.read_text()) or {}
            for e in doc.get("events", []) or []:
                ne = NewsEvent.from_dict(e)
                if ne.slug in seen_slugs:
                    continue
                seen_slugs.add(ne.slug)
                all_events.append(ne)
            c = doc.get("cutoff_date")
            if isinstance(c, str):
                cutoffs.append(date.fromisoformat(c))
            elif isinstance(c, date):
                cutoffs.append(c)
        cutoff = min(cutoffs) if cutoffs else None
        return cls(all_events, cutoff_date=cutoff)

    def in_period(self, period_start: date, period_end: date) -> list[NewsEvent]:
        """Events that are active during [period_start, period_end]."""
        return [e for e in self.events if e.is_active_in(period_start, period_end)]

    def first_appearances_in(self, period_start: date, period_end: date) -> list[NewsEvent]:
        """Episodic events on date in window + chronic events that START in window."""
        return [e for e in self.events if e.is_first_appearance_in(period_start, period_end)]

    def __iter__(self) -> Iterator[NewsEvent]:
        return iter(self.events)

    def __len__(self) -> int:
        return len(self.events)
