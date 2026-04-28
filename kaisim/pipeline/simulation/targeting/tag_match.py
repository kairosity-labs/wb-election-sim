"""TagMatchStrategy — pure agent-tag ↔ event-tag intersection delivery.

Mental model: every news event has a `tags` list (e.g.,
`[matua_refugee, bjp_supporter, kanyashree_household]`) and every agent has
a derived tag set (from `derive_tags(persona)`). An event reaches an agent
iff their tag sets share **at least one** member.

Differences from `RuleBasedStrategy`:
  * No threshold and **no cap** — every matching event is delivered.
  * Score is just `|agent_tags ∩ event_tags|` (used only for ordering).
  * No scope-weight, intensity, media-engagement, or loss-aversion math —
    the targeting decision is purely "do these tag sets overlap".

Special cases:
  * Events with `broadcast: true` reach every agent regardless of tags
    (state-of-emergency / nation-wide events the agent can't avoid).
  * Events with no tags reach every agent (untagged = broadcast).
  * `mask_tags` config knob suppresses listed tags from the agent's set
    BEFORE intersection — used by the blind_to_prior variant to drop
    `bjp_supporter` / `tmc_supporter` cues.
"""
from __future__ import annotations

from ..core.agent import Agent
from ..core.event import NewsEvent
from .base import ScoredEvent


class TagMatchStrategy:
    name = "tag_match"

    def __init__(self, mask_tags: list[str] | None = None, **kwargs):
        self.mask_tags = frozenset(mask_tags or [])

    def select(self, agent: Agent, candidate_events: list[NewsEvent],
               period_start_iso: str, period_end_iso: str) -> list[ScoredEvent]:
        agent_tags = set(agent.tags) - self.mask_tags
        scored: list[ScoredEvent] = []

        for e in candidate_events:
            event_tags = set(e.tags or [])

            # Untagged or broadcast: reaches everyone.
            if not event_tags or e.broadcast:
                scored.append(ScoredEvent(
                    event=e, score=1.0,
                    why="broadcast" if e.broadcast else "untagged",
                ))
                continue

            overlap = agent_tags & event_tags
            if overlap:
                scored.append(ScoredEvent(
                    event=e, score=float(len(overlap)),
                    why=f"tags:{','.join(sorted(overlap))}",
                ))

        # Most-overlap first — agents see the most relevant news at the top
        # of their feed even though all matching events are delivered.
        scored.sort(key=lambda s: -s.score)
        return scored
