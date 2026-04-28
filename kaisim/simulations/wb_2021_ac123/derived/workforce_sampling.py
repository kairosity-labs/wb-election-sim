"""AC 123 (Sandeshkhali) — workforce-status sampler.

Sundarbans delta workforce distribution (per 123_marginals.csv):
  Main_worker 28, Marginal_worker 14, Non_worker 42, Student 10, Unemployed 6.

Strategy:
  1. Children → Non_worker (defensive)
  2. 18-22 with secondary+ → Student at high rate (delta has limited college
     access but secondary-level enrollment is rising). Target Student=10%
     among adults.
  3. 23-27 with Graduate+ → some still in PG/professional school
  4. 63+ → mostly retired
  5. 58-62 → leaning retired
  6. Female 23-57 → housewife at moderate rate (rural delta FLFPR ~30%,
     so housewife 70% of working-age women — but we also need ~24% main
     workers and ~18% marginal workers which competes).
  7. Residual: sample directly from workforce marginal.
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

    # Children → Non_worker (defensive; child cohorts dropped)
    if any(s in age for s in ("0_4", "5_9", "10_14", "15_17")):
        return _pick_category(axis, ("Non_worker",))

    # 18-22 → Student attractor. Target Student=10% (over all 11 adult
    # cohorts ≈ 110% Student in 18-22 alone → impossible). Need 18-22
    # cohort (9% of pop, ~13% of adults) to be 70% Student to hit 10%.
    # Add some 23-27 grad-school overflow.
    if age == "18_22":
        if edu and any(k in (edu or "") for k in ("Secondary", "Higher",
                                                    "Graduate", "Postgraduate")):
            if rng.random() < 0.90:
                return _pick_category(axis, ("Student",))
        elif rng.random() < 0.40:
            return _pick_category(axis, ("Student",))
    if age == "23_27" and edu in ("Graduate", "Postgraduate"):
        if rng.random() < 0.20:
            return _pick_category(axis, ("Student",))

    # 63+ → mostly retired
    if any(s in age for s in ("63_67", "68")):
        if rng.random() < 0.85:
            return _pick_category(axis, ("Non_worker",))
    # 58-62 → leaning retired
    if age == "58_62" and rng.random() < 0.55:
        return _pick_category(axis, ("Non_worker",))

    # Female 23-57 → housewife. Reduced rate (0.30) so the marginal
    # sampler can emit Main/Marginal workers to hit target Non_worker=42.
    female_housewife_age = age in {"23_27", "28_32", "33_37", "38_42",
                                     "43_47", "48_52", "53_57"}
    if gender == "Female" and female_housewife_age and rng.random() < 0.30:
        return _pick_category(axis, ("Non_worker",))

    # Residual: sample directly from workforce marginal, excluding Student.
    return _sample_from_marginal_excluding(rng, axis, exclude={"Student"})
