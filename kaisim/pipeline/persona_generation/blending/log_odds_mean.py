"""Log-odds mean (geometric mean of probabilities).

For each party p:
    logit_p = sum_i w_i * logit(P_i(p))  /  sum_i w_i
    P(p)    = softmax(logit_p) over all parties

Conservative: doesn't assume conditional independence the way naive-Bayes
does. Equivalent to a weighted geometric mean of probabilities followed by
re-normalization.

Edge cases:
    - P_i(p) == 0     → clipped to 1e-4 to avoid -inf logit
    - P_i(p) == 100   → clipped to 99.99
    - Missing party in some tables → skipped for that table only
"""
from __future__ import annotations

import math


_EPS = 1e-4


def _logit(p: float) -> float:
    p = max(_EPS, min(1.0 - _EPS, p))
    return math.log(p / (1.0 - p))


class LogOddsMean:
    """See module docstring."""

    def blend(
        self,
        per_table_probs: dict[str, dict[str, float]],
        weights: dict[str, float],
        parties: list[str],
    ) -> dict[str, float]:
        # Compute weighted-mean log-odds per party.
        logit_means: dict[str, float] = {}
        for party in parties:
            num = 0.0
            den = 0.0
            for table_name, dist in per_table_probs.items():
                if party not in dist:
                    continue
                w = weights.get(table_name, 1.0)
                num += w * _logit(dist[party] / 100.0)
                den += w
            if den == 0:
                logit_means[party] = _logit(1.0 / len(parties))  # uninformed prior
            else:
                logit_means[party] = num / den

        # Convert log-odds to probabilities, then renormalize across parties.
        # (Each logit corresponds to a Bernoulli; normalization makes them
        # comparable as a categorical.)
        raw = {p: 1.0 / (1.0 + math.exp(-logit_means[p])) for p in parties}
        total = sum(raw.values())
        if total == 0:
            return {p: 1.0 / len(parties) for p in parties}
        return {p: 100.0 * raw[p] / total for p in parties}
