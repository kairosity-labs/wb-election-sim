"""AC 064 (Murshidabad) — marital status sampler.

Tuned to hit the AC 064 marital marginal:
  Never_married 25, Currently_married 66, Widowed 7.5, Separated_divorced 1.5.

Uses married_given_age_gender joint (post-curation has 5-yr cohort keys);
allocates non-married to Widowed / Separated / Never by age+gender.
"""
from __future__ import annotations

from pipeline.persona_generation.generic_plugins import (_pick_category,
                                                            _try_joint)


def sample(rng, ctx, axis, persona, persona_config=None, **kwargs):
    age = persona.get("age_cohort") or ""
    gender = persona.get("gender")

    # Children → Never_married (defensive)
    if any(s in age for s in ("0_4", "5_9", "10_14", "15_17")):
        return _pick_category(axis, ("Never_married",))

    # P(currently married | age × gender) from joint
    p_married = None
    joint = _try_joint(ctx, "married_given_age_gender")
    if joint is not None:
        row = joint.table.get(age, {})
        if isinstance(row, dict):
            v = (row.get("Male_married") if gender == "Male"
                 else row.get("Female_married"))
            try:
                p_married = float(v) / 100.0
            except (TypeError, ValueError):
                pass
    if p_married is None:
        p_married = 0.66

    # Joint married_given_age_gender has per-cohort rates that integrate to
    # ~74.7% population Currently_married, vs marginal target 66%. Apply a
    # uniform shrinkage factor so the population marginal lands close to
    # target. (66/74.7 ≈ 0.884.)
    p_married = p_married * 0.88

    if rng.random() < p_married:
        return _pick_category(axis, ("Currently_married",))

    # Residual: ~34% non-married. Target distribution among non-married:
    #   Never 25/34 = 73%  Widowed 7.5/34 = 22%  Separated 1.5/34 = 4%
    # Conditional on age:
    age_50plus = any(s in age for s in ("48_52", "53_57", "58_62", "63_67", "68"))
    age_60plus = any(s in age for s in ("63_67", "68"))
    age_60to62 = age == "58_62"

    if age_60plus:
        if gender == "Female" and rng.random() < 0.85:
            return _pick_category(axis, ("Widowed",))
        if gender == "Male" and rng.random() < 0.40:
            return _pick_category(axis, ("Widowed",))
    elif age_60to62:
        if gender == "Female" and rng.random() < 0.65:
            return _pick_category(axis, ("Widowed",))
        if gender == "Male" and rng.random() < 0.20:
            return _pick_category(axis, ("Widowed",))
    elif age_50plus:
        if gender == "Female" and rng.random() < 0.40:
            return _pick_category(axis, ("Widowed",))
        if gender == "Male" and rng.random() < 0.10:
            return _pick_category(axis, ("Widowed",))
    elif any(s in age for s in ("33_37", "38_42", "43_47")):
        if rng.random() < 0.10:
            return _pick_category(axis, ("Widowed",))
        if rng.random() < 0.06:
            return _pick_category(axis, ("Separated_divorced",))

    # Default: Never_married
    return _pick_category(axis, ("Never_married",))
