"""ParkMinimalUpdater — one LLM call per (agent, event).

Park-style: agent's persona is the system prompt (cached), agent's memory
+ the new event is the user prompt. The LLM decides engagement, reaction,
importance — no psychological scaffolding beyond a one-line "be honest"
framing in the template.

Returns a MemoryItem if the agent reacted (engaged or shifted) or None if
the agent scrolled past without engaging.
"""
from __future__ import annotations

import asyncio
from datetime import date
from typing import Any

from ...providers import Provider
from ..core.agent import Agent
from ..core.event import NewsEvent
from ..core.memory import MemoryItem
from .base import parse_llm_json, render_template


_RECENT_MEMORY_WINDOW = 8           # last N raw reactions to include verbatim


def _build_user_prompt(agent: Agent, event: NewsEvent, current_date: date) -> str:
    reflections = agent.memory_stream.reflections()
    raw_recent = [m for m in agent.memory_stream.raw_reactions()
                  if m.timestamp >= "0000-00-00"][-_RECENT_MEMORY_WINDOW:]
    return render_template(
        "update_minimal.md.j2",
        reflections=reflections,
        recent_memories=raw_recent,
        event=event,
        event_date=current_date.isoformat(),
    )


def _build_system_prompt(agent: Agent) -> str:
    """Cached prefix — the persona's identity. Same for every call for this agent."""
    return f"You are {agent.id}.\n\n{agent.self_prompt}\n\n" \
           "Throughout your responses, stay in character. " \
           "Speak in first person. Be specific to who you are and what you've " \
           "lived through. Do not break character."


class ParkMinimalUpdater:
    name = "park_minimal"

    def __init__(self, provider: Provider, *,
                 reasoning: str | None = "low",
                 temperature: float = 0.7,
                 max_tokens: int = 4000,
                 cache_system_prompt: bool = True):
        self.provider = provider
        self.reasoning = reasoning
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.cache_system_prompt = cache_system_prompt

    async def update(self, agent: Agent, event: NewsEvent, current_date: date,
                     memory_id: str) -> tuple[MemoryItem | None, dict, str]:
        """Returns (memory_item, parsed_response, raw_text).

        memory_item is None if the agent scrolled_past or response was malformed.
        """
        system = _build_system_prompt(agent)
        user = _build_user_prompt(agent, event, current_date)

        # provider.generate is sync; dispatch to a thread for async-friendliness
        response = await asyncio.to_thread(
            self.provider.generate,
            system, user,
            max_tokens=self.max_tokens,
            temperature=self.temperature,
            reasoning=self.reasoning,
            cache_system=self.cache_system_prompt,
        )
        raw = response.text
        parsed = parse_llm_json(raw)
        if parsed is None:
            return None, {}, raw

        engagement = parsed.get("engagement", "scrolled_past")
        reaction = parsed.get("reaction", "ignored")
        monologue = parsed.get("monologue")
        importance = int(parsed.get("importance", 1))
        delta = parsed.get("structured_delta")

        # Only record a memory if the agent actually engaged (had thoughts).
        # "scrolled_past" + "ignored" → no memory item, no narrative drift.
        if engagement == "scrolled_past" or not monologue:
            return None, parsed, raw

        item = MemoryItem(
            id=memory_id,
            timestamp=current_date.isoformat(),
            kind="reaction",
            content=monologue,
            importance=importance,
            triggering_event_slug=event.slug,
            structured_delta=delta if isinstance(delta, dict) else None,
        )
        return item, parsed, raw
