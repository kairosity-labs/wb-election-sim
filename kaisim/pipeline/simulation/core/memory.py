"""MemoryItem + MemoryStream — normalized agent memory schema.

Memory items are NL paragraphs the agent has produced (reactions to events
or periodic reflections). The stream is chronological. Recent items go into
the prompt verbatim; older items get compressed via Reflection.
"""
from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field
from datetime import date
from pathlib import Path
from typing import Any


@dataclass
class MemoryItem:
    id: str                                     # e.g., "p0001_m042"
    timestamp: str                              # ISO date (YYYY-MM-DD)
    kind: str                                   # "reaction" | "reflection" | "seed"
    content: str                                # NL paragraph
    importance: int = 5                         # 1-10, LLM-rated
    triggering_event_slug: str | None = None    # which news event drove this (None for reflection)
    structured_delta: dict | None = None        # extracted structured belief change (for analytics)

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, d: dict) -> "MemoryItem":
        return cls(
            id=d["id"],
            timestamp=d["timestamp"],
            kind=d["kind"],
            content=d["content"],
            importance=int(d.get("importance", 5)),
            triggering_event_slug=d.get("triggering_event_slug"),
            structured_delta=d.get("structured_delta"),
        )


@dataclass
class MemoryStream:
    items: list[MemoryItem] = field(default_factory=list)

    # ---- mutation ----
    def add(self, item: MemoryItem) -> None:
        self.items.append(item)

    def replace_older_than(self, cutoff_iso: str, replacement: MemoryItem) -> int:
        """Delete items strictly before `cutoff_iso` and insert `replacement` at
        the start. Used by reflection compression. Returns count removed."""
        before = [i for i in self.items if i.timestamp < cutoff_iso]
        kept = [i for i in self.items if i.timestamp >= cutoff_iso]
        self.items = [replacement] + kept
        return len(before)

    # ---- views ----
    def recent(self, n: int) -> list[MemoryItem]:
        return self.items[-n:] if n else []

    def since(self, iso_date: str) -> list[MemoryItem]:
        return [i for i in self.items if i.timestamp >= iso_date]

    def reflections(self) -> list[MemoryItem]:
        return [i for i in self.items if i.kind == "reflection"]

    def raw_reactions(self) -> list[MemoryItem]:
        return [i for i in self.items if i.kind == "reaction"]

    def intentions(self) -> list[MemoryItem]:
        """Mid-run vote-intention probe results (kind='intention').
        Distinct from reactions/reflections so consumers can include them
        explicitly in recent-memory windows when they want belief drift
        signal vs raw event reactions."""
        return [i for i in self.items if i.kind == "intention"]

    def recent_inputs(self, n: int) -> list[MemoryItem]:
        """Last n items that count as 'agent's belief inputs' — reactions +
        intentions. Excludes reflections (they're shown separately, and
        their content is already a compressed form of the underlying
        reactions). Sorted chronologically."""
        eligible = [i for i in self.items if i.kind in ("reaction", "intention")]
        return eligible[-n:] if n else []

    def __len__(self) -> int:
        return len(self.items)

    # ---- I/O ----
    def to_jsonl(self, path: Path) -> None:
        with Path(path).open("w") as f:
            for it in self.items:
                f.write(json.dumps(it.to_dict()) + "\n")

    @classmethod
    def from_jsonl(cls, path: Path) -> "MemoryStream":
        items = []
        for line in Path(path).read_text().splitlines():
            line = line.strip()
            if line:
                items.append(MemoryItem.from_dict(json.loads(line)))
        return cls(items=items)
