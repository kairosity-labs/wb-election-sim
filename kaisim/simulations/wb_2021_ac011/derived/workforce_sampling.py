"""AC 011 (Kalchini) — workforce-status sampler.

Tea-belt specifics:
  - Workforce_status has BOTH Main_worker_tea_garden_wage_labor (34%) AND
    Main_worker_non_tea (6%). We split incoming "main worker" into 85/15 between
    these two buckets to hit the marginal.
  - Female labour-force participation in tea-belt is HIGH (women are the
    primary tea-pickers). LOWER the housewife rate to ~10% (vs 75% generic).
  - 'Unemployed' marginal is 8% (closed-garden / displaced) — boost.

Marginal targets:
  Main_worker_tea_garden_wage_labor 34, Main_worker_non_tea 6,
  Marginal_worker 8, Non_worker 38, Student 6, Unemployed 8.
"""
from __future__ import annotations

import random as _r
from pipeline.persona_generation.generic_plugins import _pick_category


def _sample_from_marginal(rng, axis):
    cats = list(axis.categories or [])
    weights = [(axis.marginal or {}).get(c, 0.0) for c in cats]
    if sum(weights) <= 0:
        return cats[0]
    return rng.choices(cats, weights=weights, k=1)[0]


def sample(rng, ctx, axis, persona, persona_config=None, **kwargs):
    age = persona.get("age_cohort") or ""
    gender = persona.get("gender")
    edu = persona.get("education")

    # Children -> Non_worker (defensive; child cohorts dropped).
    if any(s in age for s in ("0_4", "5_9", "10_14", "15_17")):
        return _pick_category(axis, ("Non_worker",))

    # 18-22 -> Student attractor (high). Boost rates to hit 6% marginal.
    if age == "18_22":
        if edu and any(k in edu for k in ("Secondary", "Higher_Secondary",
                                            "Graduate", "Postgraduate")):
            if rng.random() < 0.85:
                return _pick_category(axis, ("Student",))
        elif rng.random() < 0.30:
            return _pick_category(axis, ("Student",))
    # 23-27 with Graduate+ -> some still studying
    if age == "23_27" and edu in ("Graduate", "Postgraduate"):
        if rng.random() < 0.20:
            return _pick_category(axis, ("Student",))

    # 63+ -> mostly retired (~50%)
    if any(s in age for s in ("63_67", "68")):
        if rng.random() < 0.50:
            return _pick_category(axis, ("Non_worker",))
    # 58-62 -> leaning retired (~15%)
    if age == "58_62" and rng.random() < 0.15:
        return _pick_category(axis, ("Non_worker",))

    # Female 23-57 -> housewife (very low for tea-belt — 0% extra inflation;
    # rely entirely on workforce_status marginal sampling below)
    # No housewife inflation -- tea-belt women are predominantly workers.

    # Now sample directly from workforce_status marginal, excluding Student
    # (already handled). The marginal's split (34/6/8/38/8) handles main_tea
    # vs main_non_tea correctly without us needing to manually split.
    cats = [c for c in (axis.categories or []) if c != "Student"]
    weights = [(axis.marginal or {}).get(c, 0.0) for c in cats]
    if sum(weights) <= 0:
        return _pick_category(axis, ("Non_worker",))
    return rng.choices(cats, weights=weights, k=1)[0]
