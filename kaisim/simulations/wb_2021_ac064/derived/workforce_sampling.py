"""AC 064 (Murshidabad) — workforce sampler.

Marginal-respecting design: rule-driven gates for children/seniors/
female-housewife/students cover the structural Non_worker mass; the
remainder samples directly from the workforce marginal (Main/Marginal/
Unemp/Non) so the population marginal lands close to target by
construction. Tuned for AC 064 (Muslim-majority Ganga-belt, low FLFPR
~15-20%, high household-industry/silk-weaver share).
"""
from __future__ import annotations

import random as _r
from pipeline.persona_generation.generic_plugins import _pick_category


def _sample_from_marginal_excluding(rng: _r.Random, axis, exclude: set):
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

    # 18-22 → Student. Target Student = 11% population. With 18-22 cohort
    # ~14.7% of adult pop, need ~75% of 18-22 to be students.
    if age == "18_22":
        if edu and any(k in edu for k in ("Secondary", "Higher_Secondary",
                                            "Graduate", "Postgraduate")):
            if rng.random() < 0.85:
                return _pick_category(axis, ("Student",))
        elif rng.random() < 0.50:
            return _pick_category(axis, ("Student",))
    # 23-27 with Graduate+ → small share still in PG/professional school
    if age == "23_27" and edu in ("Graduate", "Postgraduate"):
        if rng.random() < 0.18:
            return _pick_category(axis, ("Student",))

    # 63+ → mostly retired (~80%).
    if any(s in age for s in ("63_67", "68")):
        if rng.random() < 0.80:
            return _pick_category(axis, ("Non_worker",))
    # 58-62 → leaning retired (~50%).
    if age == "58_62" and rng.random() < 0.50:
        return _pick_category(axis, ("Non_worker",))

    # Female 23-57 → housewife. Murshidabad target Non_worker=37%, so
    # housewife rate moderated to land marginal at target.
    female_housewife_age = age in {"23_27", "28_32", "33_37", "38_42",
                                     "43_47", "48_52", "53_57"}
    if gender == "Female" and female_housewife_age and rng.random() < 0.18:
        return _pick_category(axis, ("Non_worker",))

    # Residual: sample directly from workforce marginal, excluding Student
    # and Non_worker (already handled above).
    return _sample_from_marginal_excluding(rng, axis,
                                            exclude={"Student"})
