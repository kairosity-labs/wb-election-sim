"""AC 143 (Diamond Harbour) — marital status sampler.

Tuned to hit the AC 143 marital marginal:
  Never_married 25, Currently_married 66, Widowed 8, Separated_divorced 1.

Strategy:
  1. Use married_given_age_gender joint (post-curation it has 5-yr cohort
     keys like '33_37' and Male_married/Female_married flag rates).
  2. For non-married personas, allocate to Widowed / Separated / Never
     based on age + gender. Diamond Harbour has fishing-related widow risk;
     widows over-concentrate in older female cohorts.
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

    # P(currently married | age × gender) from the joint
    p_married = None
    joint = _try_joint(ctx, "married_given_age_gender")
    if joint is not None:
        row = joint.table.get(age, {})
        if isinstance(row, dict):
            key = "Male_married" if gender == "Male" else "Female_married"
            v = row.get(key)
            try:
                p_married = float(v) / 100.0
            except (TypeError, ValueError):
                pass
    if p_married is None:
        p_married = 0.66
    # Dampen — joint's compound-bucket means over-marry the population once
    # expanded onto adult-only (no-kids) axis. Multiply by 0.88 to land near
    # the 66% Currently_married target.
    p_married *= 0.88

    if rng.random() < p_married:
        return _pick_category(axis, ("Currently_married",))

    # Residual: ~34% non-married. Target distribution within residual:
    #   Never 25/34 = 73%  Widowed 8/34 = 24%  Separated 1/34 = 3%
    age_50plus = any(s in age for s in ("48_52", "53_57", "58_62", "63_67", "68"))
    age_60plus = any(s in age for s in ("63_67", "68"))
    age_60to62 = age == "58_62"

    if age_60plus:
        # Female 85% widow; Male 45% widow (fishing community: higher male
        # widower share than typical, women still over-represented).
        if gender == "Female" and rng.random() < 0.85:
            return _pick_category(axis, ("Widowed",))
        if gender == "Male" and rng.random() < 0.45:
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
        if rng.random() < 0.05:
            return _pick_category(axis, ("Separated",))

    # Default: Never_married
    return _pick_category(axis, ("Never_married",))
