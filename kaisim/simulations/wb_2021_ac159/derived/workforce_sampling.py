"""AC 159 (Bhabanipur) — workforce sampler.

Bhabanipur is fully urban Kolkata, dominated by trader/professional/services
workforce. Target marginals (% of total population):
    Main_worker 42, Marginal_worker 5, Non_worker 35, Student 10, Unemployed 8.

Strategy:
  1. Children → Non_worker (defensive; child cohorts dropped from axis).
  2. 18-22 with Secondary+ → Student at high rate (~85%) to hit 10% Student.
  3. 23-27 Graduate+ → small Student rate (PG students).
  4. 63+ → mostly retired (~85% Non_worker).
  5. 58-62 → leaning retired (~50%).
  6. Female 23-57 → housewife at 55% (urban Kolkata FLFPR ~35-40% on
     PLFS estimates, vs 23% rural; substantially below 75% generic).
  7. Residual: cumulative-threshold from workforce_given_education joint.
"""
from __future__ import annotations

import random as _r
from pipeline.persona_generation.generic_plugins import _pick_category, _try_joint


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
    edu = persona.get("education") or ""

    # Children → Non_worker (defensive)
    if any(s in age for s in ("0_4", "5_9", "10_14", "15_17")):
        return _pick_category(axis, ("Non_worker",))

    # 18-22 → Student high rate (Bhabanipur high-education AC).
    # Target 10% Student; 18-22 cohort is ~9.5% of population; ~85% Student
    # rate puts that cohort alone at ~8% Student. Add 23-27 PG layer.
    if age == "18_22":
        if any(k in edu for k in ("Secondary", "Higher_Secondary",
                                    "Graduate", "Postgraduate")):
            if rng.random() < 0.85:
                return _pick_category(axis, ("Student",))
        elif rng.random() < 0.30:
            return _pick_category(axis, ("Student",))
    if age == "23_27" and edu in ("Graduate", "Postgraduate"):
        if rng.random() < 0.20:
            return _pick_category(axis, ("Student",))

    # 63+ → retired
    if any(s in age for s in ("63_67", "68")):
        if rng.random() < 0.85:
            return _pick_category(axis, ("Non_worker",))
    if age == "58_62" and rng.random() < 0.50:
        return _pick_category(axis, ("Non_worker",))

    # Female 23-57 → housewife. Urban Kolkata FLFPR ~40%; rate 32%
    # housewife empirically lands Non_worker target with the boost
    # below.
    female_housewife_age = age in {"23_27", "28_32", "33_37", "38_42",
                                     "43_47", "48_52", "53_57"}
    if gender == "Female" and female_housewife_age and rng.random() < 0.32:
        return _pick_category(axis, ("Non_worker",))

    # Hard-coded per-education Main_worker / Unemployed rates,
    # tuned for AC 159. The plugin's pre-stage gates (housewife,
    # seniors, students) reduce the pool that p_main applies to —
    # so these rates are higher than the marginal-style targets to
    # land aggregate Main_worker on 42%.
    edu_rates = {
        "Illiterate":      (0.55, 0.03),
        "Primary":         (0.60, 0.04),
        "Middle":          (0.55, 0.05),
        "Secondary":       (0.55, 0.08),
        "Higher_Secondary":(0.55, 0.12),
        "Graduate":        (0.55, 0.16),
        "Postgraduate":    (0.78, 0.06),
    }
    p_main, p_unemp = edu_rates.get(edu, (0.55, 0.10))

    r = rng.random()
    if r < p_main:
        return _pick_category(axis, ("Main_worker", "Main worker"))
    if r < p_main + p_unemp:
        return _pick_category(axis, ("Unemployed",))
    # 22% of remaining → Marginal_worker; rest Non_worker.
    if rng.random() < 0.22:
        return _pick_category(axis, ("Marginal_worker", "Marginal worker"))
    return _pick_category(axis, ("Non_worker",))
