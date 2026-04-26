"""Greedy subset selection — pick the K personas (out of N >= K) that best
match the target distributions.

Use case: the LLM batch sampler over-generates during the correction phase
(target_n + correction batches → ~130 candidates), and we want to return
exactly target_n=100 personas with the best chi-sq fit.

Algorithm:
    while len(pop) > target_n:
        for each persona p in pop:
            score_without_p = composite_chi_sq(pop \ {p})
        remove the persona whose removal most LOWERS the score

Complexity: O(K * N * V) where K = N - target_n, V = cost of one
verify_population call. For N=130, target=100, V≈5ms in pure Python →
~30 * 130 * 5ms ≈ 20 seconds. Fast enough for our scale; if needed, a
cell-incremental scorer would drop this another order of magnitude.

Why greedy beats EMD/KL for this problem: our verifier already computes a
chi-sq composite (a tier-weighted Pearson statistic which is asymptotically
KL-equivalent under the null). We're directly minimizing the same quantity
we'll report, so there's no need to pick a different distance metric.
"""
from __future__ import annotations

from ..core.config import SimulationContext
from ..core.persona import Persona
from ..verifiers import verify_population


def greedy_subset_selection(
    ctx: SimulationContext,
    personas: list[Persona],
    target_n: int,
    *,
    tolerance: dict | None = None,
    tier_weights: dict | None = None,
    verbose: bool = True,
) -> tuple[list[Persona], list[Persona]]:
    """Greedily reduce `personas` to exactly `target_n` by removing the
    persona whose removal most improves the composite chi-sq.

    Returns (kept, removed). Persona IDs are NOT renumbered — kept IDs may
    have gaps reflecting the original generation order.
    """
    if len(personas) <= target_n:
        return list(personas), []

    pop = list(personas)
    removed: list[Persona] = []
    initial_score = verify_population(ctx, pop, tolerance=tolerance,
                                       tier_weights=tier_weights).composite_score
    if verbose:
        print(f"  greedy trim: starting n={len(pop)}, target={target_n}, "
              f"initial composite={initial_score:.1f}")

    while len(pop) > target_n:
        best_i = -1
        best_score = float("inf")
        for i in range(len(pop)):
            trial = pop[:i] + pop[i + 1:]
            r = verify_population(ctx, trial, tolerance=tolerance,
                                  tier_weights=tier_weights)
            if r.composite_score < best_score:
                best_score = r.composite_score
                best_i = i
        removed.append(pop.pop(best_i))
        if verbose and (len(removed) % 5 == 0 or len(pop) == target_n):
            print(f"    removed {len(removed):>2}/{len(personas) - target_n}, "
                  f"n={len(pop)}, composite={best_score:.1f}")

    final_score = verify_population(ctx, pop, tolerance=tolerance,
                                    tier_weights=tier_weights).composite_score
    if verbose:
        print(f"  greedy trim done: n={len(pop)}, composite={final_score:.1f} "
              f"(was {initial_score:.1f}, Δ={final_score - initial_score:+.1f})")
    return pop, removed
