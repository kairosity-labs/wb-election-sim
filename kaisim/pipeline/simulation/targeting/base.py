"""TargetingStrategy — pluggable rules for "which news reaches which agent."

Implementations:
    show_all     — every persona sees every event (sanity baseline)
    rule_based   — broadcast scope + tag overlap scoring (default)
    embedding    — semantic similarity (deferred to v2)
    custom       — region-specific plugin (loaded from simulations/<sim>/targeting/)

Strategy choice + per-strategy knobs live in simulation_config YAML.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol

from ..core.agent import Agent
from ..core.event import NewsEvent


@dataclass
class ScoredEvent:
    event: NewsEvent
    score: float
    why: str = ""               # short trace for debugging


class TargetingStrategy(Protocol):
    name: str

    def select(
        self,
        agent: Agent,
        candidate_events: list[NewsEvent],
        period_start_iso: str,
        period_end_iso: str,
    ) -> list[ScoredEvent]:
        """Return events that reach this agent in this period, ordered by relevance."""
        ...
