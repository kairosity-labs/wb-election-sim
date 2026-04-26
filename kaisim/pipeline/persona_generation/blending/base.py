"""Blending — combine multiple conditional probability tables into one.

Two distinct blending problems show up in this framework:

    1. **Vote-prior blending** — a persona has values along several axes
       (religion, caste, gender, welfare_dominant) and each axis has its own
       P(vote | axis) table. The blender combines these into a single
       P(vote | persona).

    2. **Welfare overlap reduction** — a persona is exposed to multiple
       welfare schemes simultaneously. The vote_welfare table is keyed by a
       single label, so we need a rule for picking / averaging.

Different methods make different statistical assumptions. We expose them as
plug-in modules so a simulation can swap them via config without code changes.

To add a new vote-blending method:
    1. Implement `VoteBlender` in a new file under `blending/`.
    2. Register it in `blending/__init__.py` (the FACTORY dict).
    3. Reference it by name in the persona_config's `vote.blending.method`.
"""
from __future__ import annotations

from typing import Protocol


class VoteBlender(Protocol):
    """Combine per-axis P(party | axis_value) tables into P(party | persona)."""

    def blend(
        self,
        per_table_probs: dict[str, dict[str, float]],
        weights: dict[str, float],
        parties: list[str],
    ) -> dict[str, float]:
        """Return a normalized distribution over parties.

        per_table_probs   table_name -> {party: pct}    (rates in [0, 100])
        weights           table_name -> contribution weight (>= 0)
        parties           the universe of parties to return probabilities for
        """
        ...


class WelfareOverlapReducer(Protocol):
    """Resolve multi-flag welfare exposure to a vote_welfare table key."""

    def reduce(
        self,
        flags: dict[str, bool],
        vote_welfare_table: dict[str, dict[str, float]],
        parties: list[str],
    ) -> tuple[str, dict[str, float] | None]:
        """Return either (label, None) — pick a single row by label —
        or (label, dist) where `dist` is a pre-blended {party: pct} dict
        the caller should use directly (e.g., from method='mean').
        """
        ...
