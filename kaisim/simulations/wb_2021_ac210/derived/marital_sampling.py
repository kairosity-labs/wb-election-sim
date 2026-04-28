"""AC 210 (Nandigram) — marital status sampler.

Tuned to hit AC 210 marital marginal:
  Never_married 27, Currently_married 65, Widowed 7, Separated_divorced 1.

Strategy:
  1. Use married_given_age_gender joint (post-curation it has 5-yr cohort
     keys + Male/Female columns).
  2. For non-married personas, broaden widow rates per age × gender so
     residual splits hit target.
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
            v = row.get("Male") if gender == "Male" else row.get("Female")
            try:
                p_married = float(v) / 100.0
            except (TypeError, ValueError):
                pass
    if p_married is None:
        p_married = 0.65

    if rng.random() < p_married:
        return _pick_category(axis, ("Currently_married",))

    # Residual: ~35% non-married. Target distribution:
    #   Never 27/35 = 77%  Widowed 7/35 = 20%  Separated 1/35 = 3%
    # Conditioned on age:
    #   - 18-32 mostly Never; tiny widow chance
    #   - 33-57 mix; some widow; slight separated
    #   - 58+ heavy widow (esp female)
    age_50plus = any(s in age for s in ("48_52", "53_57", "58_62", "63_67", "68"))
    age_60plus = any(s in age for s in ("63_67", "68"))
    age_60to62 = age == "58_62"

    if age_60plus:
        # Female 85% widow; Male 45% widow; rest Never
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
        if gender == "Male" and rng.random() < 0.10:
            return _pick_category(axis, ("Widowed",))
    elif any(s in age for s in ("33_37", "38_42", "43_47")):
        if rng.random() < 0.10:
            return _pick_category(axis, ("Widowed",))
        if rng.random() < 0.05:
            return _pick_category(axis, ("Separated",))

    # Default: Never_married
    return _pick_category(axis, ("Never_married",))
