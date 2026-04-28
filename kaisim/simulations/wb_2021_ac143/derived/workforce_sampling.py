"""AC 143 (Diamond Harbour) — workforce sampler.

Marginal-respecting design tuned for AC 143's adult age distribution:
  Main_worker 30, Marginal_worker 13, Non_worker 38, Student 11, Unemployed 8.

Strategy:
  - Children → Non_worker (defensive; child cohorts dropped from axis).
  - 18-22 with secondary+ → Student (~80%); some non-secondary too.
  - 23-27 with Graduate+ → still Student (~18%).
  - 63+ → ~85% retired (Non_worker); 58-62 → ~50% retired.
  - Female 23-57 → housewife at 60% (S24P FLFPR ≈ 30%; not as high as
    tea-belt but considerably higher than Non_worker mass forces).
  - Residual: sample from workforce marginal directly so it aligns by
    construction.
"""
from __future__ import annotations

import random as _r
from pipeline.persona_generation.generic_plugins import _pick_category


def _sample_from_marginal_excluding(rng: _r.Random, axis, exclude: set):
    """Sample from axis.marginal excluding given categories (renormalized)."""
    cats = [c for c in (axis.categories or []) if c not in exclude]
    weights = [(axis.marginal or {}).get(c, 0.0) for c in cats]
    if sum(weights) <= 0:
        return _pick_category(axis, ("Non_worker",))
    return rng.choices(cats, weights=weights, k=1)[0]


def sample(rng, ctx, axis, persona, persona_config=None, **kwargs):
    age = persona.get("age_cohort") or ""
    gender = persona.get("gender")
    edu = persona.get("education")

    # Children → Non_worker (defensive; child cohorts dropped from axis).
    if any(s in age for s in ("0_4", "5_9", "10_14", "15_17")):
        return _pick_category(axis, ("Non_worker",))

    # 18-22 → Student attractor (high rate to hit 11% Student target,
    # given 18-22 cohort is ~10.5% of adult population and only roughly half
    # have secondary+ in this AC).
    if age == "18_22":
        if edu and any(k in edu for k in ("Secondary", "Higher_Secondary",
                                          "Graduate", "Postgraduate")):
            if rng.random() < 0.92:
                return _pick_category(axis, ("Student",))
        elif rng.random() < 0.55:
            return _pick_category(axis, ("Student",))
    # 23-27 with secondary+ → some still in education
    if age == "23_27":
        if edu in ("Graduate", "Postgraduate"):
            if rng.random() < 0.25:
                return _pick_category(axis, ("Student",))
        elif edu == "Higher_Secondary":
            if rng.random() < 0.10:
                return _pick_category(axis, ("Student",))

    # 63+ → mostly retired (~85%).
    if any(s in age for s in ("63_67", "68")):
        if rng.random() < 0.85:
            return _pick_category(axis, ("Non_worker",))
    # 58-62 → leaning retired (~50%).
    if age == "58_62" and rng.random() < 0.50:
        return _pick_category(axis, ("Non_worker",))

    # Female 23-57 → housewife (~75%) — S24P FLFPR around 25%; most
    # working-age women are out of the formal labour force. Tuned upward
    # from 60% to land Non_worker at the 38% target.
    female_housewife_age = age in {"23_27", "28_32", "33_37", "38_42",
                                   "43_47", "48_52", "53_57"}
    if gender == "Female" and female_housewife_age and rng.random() < 0.75:
        return _pick_category(axis, ("Non_worker",))

    # Residual: sample directly from workforce marginal, excluding Student
    # (already handled above) and Non_worker (handled by gates).
    return _sample_from_marginal_excluding(
        rng, axis, exclude={"Student", "Non_worker"})
