"""AC 159 (Bhabanipur) — marital status sampler.

Target marginal (% of adults 18+):
    Never_married 30, Currently_married 61, Widowed 7.5, Separated_divorced 1.5

Strategy:
  1. married_given_age_gender joint stores Male_married/Female_married rates
     by 5-yr cohort (post-curate.py expansion).
  2. Sample Currently_married Bernoulli per persona.
  3. For non-married: weight Never/Widowed/Separated by age × gender.
"""
from __future__ import annotations

from pipeline.persona_generation.generic_plugins import (_pick_category,
                                                            _try_joint)


def sample(rng, ctx, axis, persona, persona_config=None, **kwargs):
    age = persona.get("age_cohort") or ""
    gender = persona.get("gender")

    # Children defensive → Never_married
    if any(s in age for s in ("0_4", "5_9", "10_14", "15_17")):
        return _pick_category(axis, ("Never_married",))

    # P(currently married | age × gender)
    # Use joint values but down-scale: CSV gives "ever married" rates
    # which include widow/separated; target marginal is Currently_married
    # only. Apply a 0.85 scale to align pop-weighted aggregate with the
    # 61% target (vs ~72% raw from joint).
    p_married = None
    joint = _try_joint(ctx, "married_given_age_gender")
    if joint is not None:
        row = joint.table.get(age, {})
        if isinstance(row, dict):
            key = "Male_married" if gender == "Male" else "Female_married"
            v = row.get(key)
            try:
                p_married = float(v) / 100.0 * 0.92
            except (TypeError, ValueError):
                pass
    if p_married is None:
        # Default urban Kolkata rate by age (scaled)
        defaults = {
            "18_22": (0.04, 0.15),
            "23_27": (0.26, 0.55),
            "28_32": (0.61, 0.72),
            "33_37": (0.75, 0.71),
            "38_42": (0.75, 0.71),
            "43_47": (0.75, 0.71),
            "48_52": (0.72, 0.58),
            "53_57": (0.72, 0.58),
            "58_62": (0.72, 0.58),
            "63_67": (0.61, 0.24),
            "68": (0.61, 0.24),
        }
        m, f = defaults.get(age, (0.50, 0.40))
        p_married = m if gender == "Male" else f

    if rng.random() < p_married:
        return _pick_category(axis, ("Currently_married",))

    # Non-married allocation:
    age_60plus = any(s in age for s in ("63_67", "68"))
    age_58_62 = age == "58_62"
    age_50plus = any(s in age for s in ("48_52", "53_57", "58_62", "63_67", "68"))
    age_33_47 = any(s in age for s in ("33_37", "38_42", "43_47"))

    if age_60plus:
        if gender == "Female" and rng.random() < 0.92:
            return _pick_category(axis, ("Widowed",))
        if gender == "Male" and rng.random() < 0.55:
            return _pick_category(axis, ("Widowed",))
    elif age_58_62:
        if gender == "Female" and rng.random() < 0.85:
            return _pick_category(axis, ("Widowed",))
        if gender == "Male" and rng.random() < 0.35:
            return _pick_category(axis, ("Widowed",))
    elif age_50plus:
        if gender == "Female" and rng.random() < 0.55:
            return _pick_category(axis, ("Widowed",))
        if gender == "Male" and rng.random() < 0.18:
            return _pick_category(axis, ("Widowed",))
    elif age_33_47:
        if gender == "Female" and rng.random() < 0.18:
            return _pick_category(axis, ("Widowed",))
        if rng.random() < 0.16:
            return _pick_category(axis, ("Separated_divorced", "Separated"))
    elif any(s in age for s in ("23_27", "28_32")):
        if rng.random() < 0.10:
            return _pick_category(axis, ("Separated_divorced", "Separated"))

    # Default: Never_married
    return _pick_category(axis, ("Never_married",))
