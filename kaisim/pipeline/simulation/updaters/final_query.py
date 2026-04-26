"""FinalVoteQuery — ask the agent in-persona who they vote for on poll day.

Park 2024 ("1000 People") found 85% replication of GSS responses by asking
LLM agents in-persona. Same approach: assemble persona + full memory + the
voting prompt, get a structured response."""
from __future__ import annotations

import asyncio
from datetime import date
from typing import Any

from ...providers import Provider
from ..core.agent import Agent
from .base import parse_llm_json, render_template


_RECENT_MEMORY_WINDOW = 12           # vote query gets a wider window than per-event update


class FinalVoteQuery:
    name = "final_vote"

    def __init__(self, provider: Provider, *,
                 reasoning: str | None = "medium",   # vote choice deserves a bit more thought
                 temperature: float = 0.6,           # slight reduction for stability
                 max_tokens: int = 2000,
                 cache_system_prompt: bool = True):
        self.provider = provider
        self.reasoning = reasoning
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.cache_system_prompt = cache_system_prompt

    async def ask(self, agent: Agent, election_date: date) -> dict | None:
        system = f"You are {agent.id}.\n\n{agent.self_prompt}\n\n" \
                 "Stay in character. Speak in first person."

        reflections = agent.memory_stream.reflections()
        raw_recent = agent.memory_stream.raw_reactions()[-_RECENT_MEMORY_WINDOW:]

        user = render_template(
            "final_vote.md.j2",
            reflections=reflections,
            recent_memories=raw_recent,
        )

        response = await asyncio.to_thread(
            self.provider.generate,
            system, user,
            max_tokens=self.max_tokens,
            temperature=self.temperature,
            reasoning=self.reasoning,
            cache_system=self.cache_system_prompt,
        )
        parsed = parse_llm_json(response.text)
        if not parsed:
            return None

        # Normalize vote field
        vote = parsed.get("vote", "").strip()
        if vote not in {"BJP", "AITC", "INC", "LF", "Other", "NOTA"}:
            return None

        return {
            "vote": vote,
            "reasoning": parsed.get("reasoning", ""),
            "confidence": int(parsed.get("confidence", 5)),
            "primary_drivers": parsed.get("primary_drivers", []),
        }
