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
                 cache_system_prompt: bool = True,
                 election_context: dict | None = None):
        """
        election_context: dict the final_vote.md.j2 template uses to render
            "It is <date> — polling day in <AC>" and the candidate list.
            Shape:
                {
                  "ac_name": "Bangaon Uttar",
                  "poll_date_human": "17 April 2021",
                  "election_label": "2021 West Bengal Legislative Assembly Election",
                  "candidates": {
                    "BJP":  {"name": "Ashok Kirtania", "note": "Matua"},
                    "AITC": {"name": "Biswanath Das", "note": "incumbent TMC"},
                    "LF":   {"name": "CPI(M) candidate"},
                    ...
                  },
                }
        """
        self.provider = provider
        self.reasoning = reasoning
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.cache_system_prompt = cache_system_prompt
        self.election_context = election_context or {}

    async def ask(self, agent: Agent, election_date: date) -> dict | None:
        system = f"You are {agent.id}.\n\n{agent.self_prompt}\n\n" \
                 "Stay in character. Speak in first person."

        reflections = agent.memory_stream.reflections()
        raw_recent = agent.memory_stream.raw_reactions()[-_RECENT_MEMORY_WINDOW:]

        user = render_template(
            "final_vote.md.j2",
            reflections=reflections,
            recent_memories=raw_recent,
            election_context=self.election_context,
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

        reasoning = (parsed.get("reasoning", "") or "").lower()
        drivers = " ".join(parsed.get("primary_drivers", []) or []).lower()
        full = reasoning + " " + drivers

        # NOTA-resolution guard. The model uses NOTA as a "I'm conflicted"
        # escape hatch even though we framed it as "active refusal only".
        # If the vote is NOTA but the reasoning text reveals a clear lean
        # toward a specific party, override with that party — voter
        # behaviour is to pick the lesser evil, not abstain via NOTA.
        if vote == "NOTA":
            mentions = {
                "BJP":  full.count(" bjp")  + full.count("modi") + full.count("hindutva"),
                "AITC": full.count("aitc") + full.count("tmc") + full.count("mamata") + full.count("didi"),
                "INC":  full.count("congress") + full.count(" inc"),
                "LF":   full.count("cpi(m)") + full.count("cpim") + full.count("left front"),
            }
            negs = ["refuse", "reject", "neither", "none of", "all parties", "no choice",
                    "abstain", "protest"]
            looks_like_active_refusal = any(n in full for n in negs) and \
                                        sum(mentions.values()) <= 1
            if not looks_like_active_refusal:
                top = max(mentions, key=mentions.get)
                if mentions[top] >= 2:                # at least 2 references to that party
                    vote = top                          # lesser-evil override

        return {
            "vote": vote,
            "reasoning": parsed.get("reasoning", ""),
            "confidence": int(parsed.get("confidence", 5)),
            "primary_drivers": parsed.get("primary_drivers", []),
            "nota_override_applied": (vote != parsed.get("vote", "").strip()),
        }
