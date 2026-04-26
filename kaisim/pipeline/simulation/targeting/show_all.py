"""ShowAllStrategy — every persona sees every event (sanity baseline)."""
from __future__ import annotations

from ..core.agent import Agent
from ..core.event import NewsEvent
from .base import ScoredEvent


class ShowAllStrategy:
    name = "show_all"

    def __init__(self, **kwargs):
        # No config; ignores everything
        pass

    def select(self, agent: Agent, candidate_events: list[NewsEvent],
               period_start_iso: str, period_end_iso: str) -> list[ScoredEvent]:
        return [ScoredEvent(event=e, score=1.0, why="show_all") for e in candidate_events]
