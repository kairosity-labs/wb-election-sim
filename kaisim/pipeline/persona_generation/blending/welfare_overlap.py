"""WelfareOverlap reducers — three configurable methods for resolving
multi-flag welfare exposure into a single P(vote | welfare) signal.

Background: a persona may simultaneously qualify for Krishak Bandhu, Khadya
Sathi, and Swasthya Sathi. The vote_welfare table treats categories as
mutually exclusive (one row per scheme). We need a rule for picking one
or for averaging across qualifying rows.

Methods:
    precedence  — pick the first matching scheme from a configured ordered list.
                  Salient identity-defining schemes go first.
    mean        — average the rows the persona qualifies for. Uses all signal.
                  No precedence config needed.
    dominant    — pick the row with the strongest party tilt (max range across
                  parties). Picks the most differentiated scheme exposure.

If no scheme is active, all methods fall back to the "None" row of the table.
"""
from __future__ import annotations


class WelfareOverlapPrecedence:
    """Pick the first scheme from `precedence` that the persona has."""

    def __init__(self, precedence: list[str]):
        self.precedence = precedence

    def reduce(
        self,
        flags: dict[str, bool],
        vote_welfare_table: dict[str, dict[str, float]],
        parties: list[str],
    ) -> tuple[str, None]:
        for scheme in self.precedence:
            if flags.get(scheme):
                if scheme in vote_welfare_table:
                    return scheme, None
        return "None", None


class WelfareOverlapMean:
    """Average vote_welfare rows the persona qualifies for."""

    def reduce(
        self,
        flags: dict[str, bool],
        vote_welfare_table: dict[str, dict[str, float]],
        parties: list[str],
    ) -> tuple[str, dict[str, float] | None]:
        active = [s for s, on in flags.items() if on and s in vote_welfare_table]
        if not active:
            return "None", None
        agg = {p: 0.0 for p in parties}
        for s in active:
            row = vote_welfare_table[s]
            for p in parties:
                agg[p] += row.get(p, 0.0)
        avg = {p: agg[p] / len(active) for p in parties}
        # Renormalize to 100 (rows may not include 'Other'; gaps already absent).
        total = sum(avg.values())
        if total > 0:
            avg = {p: 100.0 * v / total for p, v in avg.items()}
        return "+".join(sorted(active)), avg


class WelfareOverlapDominant:
    """Pick the row with the largest spread across parties (most differentiated)."""

    def reduce(
        self,
        flags: dict[str, bool],
        vote_welfare_table: dict[str, dict[str, float]],
        parties: list[str],
    ) -> tuple[str, None]:
        active = [s for s, on in flags.items() if on and s in vote_welfare_table]
        if not active:
            return "None", None
        def spread(row: dict[str, float]) -> float:
            vs = [row.get(p, 0.0) for p in parties]
            return max(vs) - min(vs)
        best = max(active, key=lambda s: spread(vote_welfare_table[s]))
        return best, None


def make(method: str, precedence: list[str] | None = None):
    if method == "precedence":
        if not precedence:
            raise ValueError("precedence method requires a non-empty precedence list")
        return WelfareOverlapPrecedence(precedence)
    if method == "mean":
        return WelfareOverlapMean()
    if method == "dominant":
        return WelfareOverlapDominant()
    raise ValueError(f"Unknown welfare_overlap method: {method!r}")
