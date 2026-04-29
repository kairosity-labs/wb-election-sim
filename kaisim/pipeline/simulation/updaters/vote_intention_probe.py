"""VoteIntentionProbe — mid-run "if elections were today, who would you vote for?"

Adds belief-drift accumulation between event ticks. Without this probe, an
agent reacts to each event as a separate memory item but never resolves
those reactions into a directional vote stance until the very last tick.
The persona's frozen self_prompt (already anchored to vote_2019_LS) then
dominates that lone final query.

By probing every K months (K=4 by default), the agent commits to a current
lean and writes it into memory. That memory item — distinct from the
event-reaction items because it explicitly says "I lean X today" — becomes
an anchor that the final-vote query can read back as accumulated evidence
of where the agent has actually moved to.

This is the cheap-prompt-only version of B1 (a structured belief-state
field). We don't add a state field; we just force the LLM to surface its
current lean as text and record it.
"""
from __future__ import annotations

import asyncio
from datetime import date

from ...providers import Provider
from ..core.agent import Agent
from ..core.memory import MemoryItem
from .base import parse_llm_json, render_template


_RECENT_MEMORY_WINDOW = 10            # last N raw reactions to include verbatim


class VoteIntentionProbe:
    name = "vote_intention_probe"

    def __init__(self, provider: Provider, *,
                 reasoning: str | None = None,
                 temperature: float = 0.6,
                 max_tokens: int = 4000,
                 cache_system_prompt: bool = True):
        self.provider = provider
        self.reasoning = reasoning
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.cache_system_prompt = cache_system_prompt

    async def probe(self, agent: Agent, probe_date: date,
                    memory_id: str) -> MemoryItem | None:
        system = (
            f"You are {agent.id}.\n\n{agent.self_prompt}\n\n"
            "Stay in character. Speak in first person. Be honest about how "
            "your views may have shifted; do not over-rationalize old loyalties."
        )

        reflections = agent.memory_stream.reflections()
        raw_recent = agent.memory_stream.raw_reactions()[-_RECENT_MEMORY_WINDOW:]

        user = render_template(
            "vote_intention.md.j2",
            reflections=reflections,
            recent_memories=raw_recent,
            probe_date=probe_date.isoformat(),
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

        lean = (parsed.get("current_lean", "") or "").strip()
        drift = (parsed.get("drift_since_2019", "") or "").strip()
        expl = (parsed.get("explanation", "") or "").strip()

        # Compose the memory paragraph. Explicit "today I lean X" wording is
        # the load-bearing part — the final-vote query reads memories
        # verbatim and this gives it a clear directional anchor.
        content = (
            f"Asked who I'd vote for if elections were today, I said: "
            f"{lean}. Drift since 2019: {drift} Why: {expl}"
        )

        return MemoryItem(
            id=memory_id,
            timestamp=probe_date.isoformat(),
            kind="intention",                 # distinct from "reaction" / "reflection"
            content=content,
            importance=8,                      # high — this is a directional commit
            triggering_event_slug=None,
            structured_delta={"current_lean": lean, "drift_since_2019": drift},
        )
