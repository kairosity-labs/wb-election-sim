"""Marital status sampler — currently_married Bernoulli (joint) + age residual rules.

The married_given_age_gender joint uses compound age cohorts (33-47, 48-62,
63+); we map our finer age cohorts (5-yr) onto these buckets.

After Bernoulli for Currently_married, the residual {Never, Widowed,
Separated} is filled by age pattern:
    age <= 17:           Never_married
    18-32:               Never (mostly), tiny widow rate
    33-57:               small Never, small widow, small separated
    58+:                 high widow rate (especially female), some never
"""
from __future__ import annotations


_AGE_TO_MARITAL_BUCKET = {
    "0_4": None, "5_9": None, "10_14": None, "15_17": None,  # children
    "18_22": "18_22", "23_27": "23_27", "28_32": "28_32",
    "33_37": "33_47_compound", "38_42": "33_47_compound", "43_47": "33_47_compound",
    "48_52": "48_62_compound", "53_57": "48_62_compound", "58_62": "48_62_compound",
    "63_67": "63plus_compound", "68plus": "63plus_compound",
}


def sample(rng, ctx, axis, persona, persona_config=None, **kwargs):
    age = persona.get("age_cohort")
    gender = persona.get("gender")
    bucket = _AGE_TO_MARITAL_BUCKET.get(age)
    if bucket is None:
        return "Never_married"

    joint = ctx.joint("married_given_age_gender")
    row = joint.table.get(bucket, {})
    g_key = "Male" if gender == "Male" else "Female"
    p_married = float(row.get(g_key, 50.0)) / 100.0

    if rng.random() < p_married:
        return "Currently_married"

    # Residual: Never / Widowed / Separated_divorced
    # Widowed concentrates at older ages, especially female.
    if age in {"63_67", "68plus"}:
        if gender == "Female" and rng.random() < 0.75:
            return "Widowed"
        if gender == "Male" and rng.random() < 0.30:
            return "Widowed"
    elif age in {"58_62", "53_57"}:
        if gender == "Female" and rng.random() < 0.40:
            return "Widowed"
    # Small chance of separated for 28-57.
    if age in {"28_32", "33_37", "38_42", "43_47", "48_52"}:
        if rng.random() < 0.04:
            return "Separated_divorced"
    return "Never_married"
