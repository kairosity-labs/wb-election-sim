"""AC 198 (Tarakeswar) — marital status sampler.

Tuned to hit AC 198 marital marginal:
  Never_married 26, Currently_married 65, Widowed 8, Separated_divorced 1.

Strategy:
  1. Use married_given_age_gender joint (post-curation expanded to 5-yr cohorts).
  2. For non-married, broaden Widowed by age+gender to hit 8% target.
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

    # P(currently married | age × gender) from joint, dampened so the
    # overall marginal Currently_married=65% is hit (joint values 90%+ in
    # 33-47 are local conditionals but pop avg should be 65 not 80+).
    p_married = None
    joint = _try_joint(ctx, "married_given_age_gender")
    if joint is not None:
        row = joint.table.get(age, {})
        if isinstance(row, dict):
            key = "Male_married" if gender == "Male" else "Female_married"
            v = row.get(key)
            try: p_married = float(v) / 100.0
            except (TypeError, ValueError): pass
    if p_married is None:
        p_married = 0.65

    # Dampen high p_married values to land marginal closer to 65% target.
    # Empirically the joint over-weights Currently_married for 33-62 cohorts.
    if p_married > 0.78:
        p_married = 0.78

    if rng.random() < p_married:
        return _pick_category(axis, ("Currently_married",))

    # Residual ~35%; target is 26% Never + 8% Widowed + 1% Sep ≈ 35%.
    age_50plus = any(s in age for s in ("48_52", "53_57", "58_62", "63_67", "68"))
    age_60plus = any(s in age for s in ("63_67", "68"))
    age_60to62 = age == "58_62"

    if age_60plus:
        if gender == "Female" and rng.random() < 0.92:
            return _pick_category(axis, ("Widowed",))
        if gender == "Male" and rng.random() < 0.55:
            return _pick_category(axis, ("Widowed",))
    elif age_60to62:
        if gender == "Female" and rng.random() < 0.80:
            return _pick_category(axis, ("Widowed",))
        if gender == "Male" and rng.random() < 0.30:
            return _pick_category(axis, ("Widowed",))
    elif age_50plus:
        if gender == "Female" and rng.random() < 0.55:
            return _pick_category(axis, ("Widowed",))
        if gender == "Male" and rng.random() < 0.15:
            return _pick_category(axis, ("Widowed",))
    elif any(s in age for s in ("33_37", "38_42", "43_47")):
        if rng.random() < 0.18:
            return _pick_category(axis, ("Widowed",))
        if rng.random() < 0.06:
            return _pick_category(axis, ("Separated_divorced",))

    # Default: Never_married
    return _pick_category(axis, ("Never_married",))
