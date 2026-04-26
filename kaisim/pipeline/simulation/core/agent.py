"""Agent — a persona + accumulated memory + identity tags.

An Agent wraps an immutable Persona (from the persona-generation pipeline)
with mutable belief state: a memory stream that grows over the simulation
and a tag set computed once at init time for targeting.

The Persona's `narrative.self_prompt` is the frozen identity the LLM keeps
reading every call (cached via prompt-caching). The memory_stream is the
mutable inner monologue that grows.
"""
from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from ...core.persona import Persona
from .memory import MemoryItem, MemoryStream


@dataclass
class Agent:
    id: str                              # persona ID
    persona: Persona                     # frozen
    tags: set[str] = field(default_factory=set)        # derived once at init
    memory_stream: MemoryStream = field(default_factory=MemoryStream)
    media_engagement: float = 1.0        # 0.3..1.5 multiplier; derived once

    @property
    def self_prompt(self) -> str:
        n = self.persona.narrative or {}
        return n.get("self_prompt", "")

    @property
    def initial_party(self) -> str | None:
        """The persona's 2019 vote prior — used as the 'prior party' for
        targeting heuristics like loss-aversion."""
        return self.persona.fields.get("vote_2019_LS")

    def save(self, root: Path) -> None:
        root = Path(root)
        root.mkdir(parents=True, exist_ok=True)
        # Snapshot persona once
        (root / "persona.json").write_text(json.dumps(self.persona.to_dict(), indent=2))
        # Memory stream as jsonl
        self.memory_stream.to_jsonl(root / "memory_stream.jsonl")
        # Belief narrative — concatenated reactions + reflections, chronological
        narrative_lines = []
        for m in self.memory_stream.items:
            narrative_lines.append(f"## [{m.timestamp}] ({m.kind}, importance {m.importance})\n")
            narrative_lines.append(m.content + "\n\n")
        (root / "belief_narrative.md").write_text("".join(narrative_lines))
        # Structured history (per-event extractions only)
        with (root / "structured_history.jsonl").open("w") as f:
            for m in self.memory_stream.items:
                if m.structured_delta:
                    f.write(json.dumps({
                        "timestamp": m.timestamp,
                        "triggering_event_slug": m.triggering_event_slug,
                        "delta": m.structured_delta,
                    }) + "\n")
        # Identity-tags + meta
        (root / "agent_meta.json").write_text(json.dumps({
            "id": self.id,
            "tags": sorted(self.tags),
            "media_engagement": self.media_engagement,
            "initial_party": self.initial_party,
            "n_memories": len(self.memory_stream),
            "n_reactions": len(self.memory_stream.raw_reactions()),
            "n_reflections": len(self.memory_stream.reflections()),
        }, indent=2))
