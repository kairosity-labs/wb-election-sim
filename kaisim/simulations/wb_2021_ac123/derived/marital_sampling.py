"""AC 123 (Sandeshkhali) — marital status sampler.

Tuned to hit AC 123 marital marginal:
  Never_married 26, Currently_married 65, Widowed 8, Separated 1.

The Sundarbans delta has elevated widow rates (target 8% vs WB rural ~6%)
because of male mortality from sea/river fishing accidents and Aila-cyclone
disaster aftermath. Widows concentrate in 60+ female cohort.
"""
from __future__ import annotations

from pipeline.persona_generation.generic_plugins import (_pick_category,
                                                            _try_joint)


def sample(rng, ctx, axis, persona, persona_config=None, **kwargs):
    age = persona.get("age_cohort") or ""
    gender = persona.get("gender")

    # Children → Never_married (defensive; child cohorts dropped from axis)
    if any(s in age for s in ("0_4", "5_9", "10_14", "15_17")):
        return _pick_category(axis, ("Never_married",))

    # P(currently married | age × gender) from joint
    p_married = None
    joint = _try_joint(ctx, "married_given_age_gender")
    if joint is not None:
        row = joint.table.get(age, {})
        if isinstance(row, dict):
            v = row.get("Male") if gender == "Male" else row.get("Female")
            try: p_married = float(v) / 100.0
            except (TypeError, ValueError): pass
    if p_married is None:
        p_married = 0.65

    if rng.random() < p_married:
        return _pick_category(axis, ("Currently_married",))

    # Residual: 35% non-married. Target: Never 26, Widowed 8, Separated 1.
    # Non-married dist: Never 74.3%, Widowed 22.9%, Separated 2.9%.
    age_50plus = any(s in age for s in ("48_52", "53_57", "58_62", "63_67", "68"))
    age_60plus = any(s in age for s in ("63_67", "68"))
    age_60to62 = age == "58_62"

    if age_60plus:
        # Female 80% widow; Male 40% widow (delta-AC fishing-mortality bump)
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
        if gender == "Female" and rng.random() < 0.45:
            return _pick_category(axis, ("Widowed",))
        if gender == "Male" and rng.random() < 0.12:
            return _pick_category(axis, ("Widowed",))
    elif any(s in age for s in ("33_37", "38_42", "43_47")):
        if rng.random() < 0.12:
            return _pick_category(axis, ("Widowed",))
        if rng.random() < 0.05:
            return _pick_category(axis, ("Separated",))

    # Default: Never_married
    return _pick_category(axis, ("Never_married",))
