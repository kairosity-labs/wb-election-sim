"""Reflection — periodic compression of older raw memories into a gist.

Models fuzzy-trace theory (Reyna-Brainerd): verbatim memory decays fast
(~30 days), but the *gist* persists much longer (~18 months). After a
reflection, the older raw reactions are removed from the agent's memory
stream and replaced by the gist paragraph.
"""
from __future__ import annotations

import asyncio
from datetime import date, timedelta
from typing import Any

from ...providers import Provider
from ..core.agent import Agent
from ..core.memory import MemoryItem
from .base import parse_llm_json, render_template


def _build_system_prompt(agent: Agent) -> str:
    return f"You are {agent.id}.\n\n{agent.self_prompt}\n\n" \
           "Stay in character. Speak in first person."


def _build_user_prompt(memories: list[MemoryItem], period_start: str,
                        period_end: str) -> str:
    return render_template(
        "reflection.md.j2",
        memories=memories,
        period_start=period_start,
        period_end=period_end,
    )


class ReflectionUpdater:
    name = "reflection"

    def __init__(self, provider: Provider, *,
                 reasoning: str | None = "low",
                 temperature: float = 0.7,
                 max_tokens: int = 1500,
                 cache_system_prompt: bool = True):
        self.provider = provider
        self.reasoning = reasoning
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.cache_system_prompt = cache_system_prompt

    async def reflect(self, agent: Agent, period_start_iso: str, period_end_iso: str,
                       memory_id: str) -> MemoryItem | None:
        """Compress agent's raw reactions in [period_start, period_end] into a
        single gist paragraph. Replaces them in the memory stream."""
        # Collect raw reactions in window
        raws = [m for m in agent.memory_stream.raw_reactions()
                if period_start_iso <= m.timestamp <= period_end_iso]
        if not raws:
            return None

        system = _build_system_prompt(agent)
        user = _build_user_prompt(raws, period_start_iso, period_end_iso)

        response = await asyncio.to_thread(
            self.provider.generate,
            system, user,
            max_tokens=self.max_tokens,
            temperature=self.temperature,
            reasoning=self.reasoning,
            cache_system=self.cache_system_prompt,
        )
        parsed = parse_llm_json(response.text)
        if not parsed or "content" not in parsed:
            return None

        item = MemoryItem(
            id=memory_id,
            timestamp=period_end_iso,
            kind="reflection",
            content=parsed["content"],
            importance=int(parsed.get("importance", 5)),
            triggering_event_slug=None,
            structured_delta=None,
        )
        # Replace older raws with the reflection
        # Cutoff: anything strictly after period_end stays as raw; everything
        # in [start, end] gets replaced by the gist.
        next_day = (date.fromisoformat(period_end_iso) + timedelta(days=1)).isoformat()
        agent.memory_stream.replace_older_than(next_day, item)
        return item
