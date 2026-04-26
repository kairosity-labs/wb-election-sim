"""Sampler — produces a list of Personas from a SimulationContext + PersonaConfig.

Implementations:
    RuleBasedSampler   — walks the DAG, deterministic-per-seed, no LLM.
                         Generates demographics + vote prior, NO narrative.
    LLMBatchSampler    — (Phase 1.2) batched LLM generation with verifier feedback.
                         Generates demographics + vote + narrative.

A Sampler is constructed with the simulation context + a parsed persona_config,
and yields personas via `sample_many(n)`.
"""
from __future__ import annotations

from typing import Protocol

from ...core.config import PersonaConfig, SimulationContext
from ...core.persona import Persona


class Sampler(Protocol):
    def __init__(
        self,
        ctx: SimulationContext,
        persona_config: PersonaConfig,
        *,
        seed: int | None = None,
    ): ...

    def sample_one(self, idx: int) -> Persona: ...

    def sample_many(self, n: int) -> list[Persona]: ...
