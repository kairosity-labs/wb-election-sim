"""Naive-Bayes-style blending — assumes conditional independence given party.

For each party p:
    log P(p | persona) ∝ log P(p) + sum_i w_i * (log P_i(p) - log P(p))

We use a uniform prior P(p) = 1/|parties| (could be made configurable).

Differs from log-odds-mean by:
    - using log probabilities (not log odds), so a near-zero P_i(p) drives the
      whole product near zero (a true "veto")
    - product over tables rather than weighted average — much sharper

Useful when you genuinely believe the per-table evidences are independent
given the party. For political vote tables this assumption is heroic, so
log_odds_mean is a safer default.
"""
from __future__ import annotations

import math


_EPS = 1e-4


def _safe_log(p: float) -> float:
    return math.log(max(_EPS, p))


class NaiveBayes:
    def blend(
        self,
        per_table_probs: dict[str, dict[str, float]],
        weights: dict[str, float],
        parties: list[str],
    ) -> dict[str, float]:
        prior = 1.0 / len(parties)
        log_post: dict[str, float] = {}
        for party in parties:
            lp = math.log(prior)
            for table_name, dist in per_table_probs.items():
                if party not in dist:
                    continue
                w = weights.get(table_name, 1.0)
                # likelihood ratio contribution, weighted
                lp += w * (_safe_log(dist[party] / 100.0) - math.log(prior))
            log_post[party] = lp

        # Softmax normalize
        m = max(log_post.values())
        exps = {p: math.exp(log_post[p] - m) for p in parties}
        total = sum(exps.values())
        return {p: 100.0 * exps[p] / total for p in parties}
