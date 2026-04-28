"""ShowAllStrategy — every persona sees every event up to an optional cap.

Used by the `show_all` simulation variant: every agent receives all news
that's active in the period (state + AC scope), without any tag- or
scope-based filtering. Sanity baseline + cleanest test of "what if
everyone saw everything."

The optional `cap_per_period` keeps total LLM calls finite when the news
pool is large (state_events_2019_2026.yaml has ~370 events). Default 10:
each persona sees up to 10 events per tick, prioritised by a simple
intensity × media_engagement score so the most salient pieces dominate.
"""
from __future__ import annotations

from ..core.agent import Agent
from ..core.event import NewsEvent
from .base import ScoredEvent


class ShowAllStrategy:
    name = "show_all"

    def __init__(self, cap_per_period: int | None = None, **kwargs):
        # `None` == no cap (default). Pass an int explicitly to bound when
        # the news pool is huge (e.g., the ~370-event state pool).
        self.cap_per_period = cap_per_period

    def select(self, agent: Agent, candidate_events: list[NewsEvent],
               period_start_iso: str, period_end_iso: str) -> list[ScoredEvent]:
        scored = [
            ScoredEvent(event=e,
                        score=float(e.intensity) * agent.media_engagement,
                        why="show_all")
            for e in candidate_events
        ]
        scored.sort(key=lambda s: -s.score)
        if self.cap_per_period is not None:
            return scored[:self.cap_per_period]
        return scored
