"""AC 222 (Jhargram) — marital status sampler.

Tuned to hit the marginal:
  Never_married 26, Currently_married 65, Widowed 8, Separated_divorced 1.

Strategy:
  1. Use married_given_age_gender joint (post-curation it has 5-yr cohort
     keys like '33_37').  Note tribal-belt earlier female marriage:
     18-22 Female 45%; 23-27 Female 85%.
  2. For non-married personas, allocate to Widowed / Separated / Never
     based on age + gender; widows concentrate at 63+.
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

    # P(ever-married | age × gender) — joint table format:
    #   {age_cohort: {Male_married: pct, Female_married: pct}}
    # The MD values reflect "ever married" rather than "currently married"
    # (e.g. F 33-47=90% includes widowed mothers).  We split this into
    # currently_married vs widowed based on age below.
    p_ever_married = None
    joint = _try_joint(ctx, "married_given_age_gender")
    if joint is not None:
        row = joint.table.get(age, {})
        if isinstance(row, dict):
            key = "Male_married" if gender == "Male" else "Female_married"
            v = row.get(key)
            try: p_ever_married = float(v) / 100.0
            except (TypeError, ValueError): pass
    if p_ever_married is None:
        p_ever_married = 0.73

    # Age-conditional widow probability (within ever-married sub-pop)
    age_60plus = any(s in age for s in ("63_67", "68"))
    age_60to62 = age == "58_62"
    age_50plus = any(s in age for s in ("48_52", "53_57", "58_62", "63_67", "68"))

    p_widow_given_ever = 0.0
    if age_60plus:
        p_widow_given_ever = 0.65 if gender == "Female" else 0.25
    elif age_60to62:
        p_widow_given_ever = 0.45 if gender == "Female" else 0.10
    elif age_50plus:
        p_widow_given_ever = 0.20 if gender == "Female" else 0.05
    elif any(s in age for s in ("33_37", "38_42", "43_47")):
        p_widow_given_ever = 0.05 if gender == "Female" else 0.02

    p_separated_given_ever = 0.02

    p_currently_married = p_ever_married * (1 - p_widow_given_ever
                                                - p_separated_given_ever)
    p_widowed = p_ever_married * p_widow_given_ever
    p_separated = p_ever_married * p_separated_given_ever

    r = rng.random()
    if r < p_currently_married:
        return _pick_category(axis, ("Currently_married",))
    if r < p_currently_married + p_widowed:
        return _pick_category(axis, ("Widowed",))
    if r < p_currently_married + p_widowed + p_separated:
        return _pick_category(axis, ("Separated_divorced", "Separated"))

    # Default: Never_married
    return _pick_category(axis, ("Never_married",))
