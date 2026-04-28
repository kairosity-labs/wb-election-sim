"""AC 011 (Kalchini) — marital status sampler.

Tea-belt notes:
  - Marital target: Never 24, Married 66, Widowed 9, Separated 1.
  - High occupational male premature mortality in tea-garden -> elevated
    female widow rates.
  - Uses married_given_age_gender post-curation (5-yr cohort keys).
"""
from __future__ import annotations

from pipeline.persona_generation.generic_plugins import (_pick_category,
                                                            _try_joint)


def sample(rng, ctx, axis, persona, persona_config=None, **kwargs):
    age = persona.get("age_cohort") or ""
    gender = persona.get("gender")

    # Children -> Never_married (defensive)
    if any(s in age for s in ("0_4", "5_9", "10_14", "15_17")):
        return _pick_category(axis, ("Never_married",))

    # P(currently married | age x gender) from curated joint
    p_married = None
    joint = _try_joint(ctx, "married_given_age_gender")
    if joint is not None:
        row = joint.table.get(age, {})
        if isinstance(row, dict):
            v = row.get("Male") if gender == "Male" else row.get("Female")
            try: p_married = float(v) / 100.0
            except (TypeError, ValueError): pass
    if p_married is None:
        p_married = 0.66

    if rng.random() < p_married:
        return _pick_category(axis, ("Currently_married",))

    # Residual: 34% non-married. Target = 24 Never + 9 Widow + 1 Sep.
    age_50plus = any(s in age for s in ("48_52", "53_57", "58_62", "63_67", "68"))
    age_60plus = any(s in age for s in ("63_67", "68"))
    age_60to62 = age == "58_62"

    if age_60plus:
        # Tea-belt: very high female widow rate
        if gender == "Female" and rng.random() < 0.95:
            return _pick_category(axis, ("Widowed",))
        if gender == "Male" and rng.random() < 0.55:
            return _pick_category(axis, ("Widowed",))
    elif age_60to62:
        if gender == "Female" and rng.random() < 0.85:
            return _pick_category(axis, ("Widowed",))
        if gender == "Male" and rng.random() < 0.35:
            return _pick_category(axis, ("Widowed",))
    elif age_50plus:
        if gender == "Female" and rng.random() < 0.65:
            return _pick_category(axis, ("Widowed",))
        if gender == "Male" and rng.random() < 0.20:
            return _pick_category(axis, ("Widowed",))
    elif any(s in age for s in ("33_37", "38_42", "43_47")):
        if gender == "Female" and rng.random() < 0.30:
            return _pick_category(axis, ("Widowed",))
        if rng.random() < 0.06:
            return _pick_category(axis, ("Separated",))
    elif any(s in age for s in ("28_32",)):
        if gender == "Female" and rng.random() < 0.10:
            return _pick_category(axis, ("Widowed",))

    return _pick_category(axis, ("Never_married",))
