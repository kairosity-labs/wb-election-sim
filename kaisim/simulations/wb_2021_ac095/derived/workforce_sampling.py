"""Workforce status — combines education-conditional indicators with age/gender rules.

Inputs:
    education-conditional rates (from joint workforce_indicators_given_education):
        Main_worker_rate     Bernoulli base for "is a main worker"
        Unemployed_seeking   Bernoulli base for "actively seeking job"
    age/gender rules:
        18-22 educated → Student is a strong attractor
        60+            → Non_worker (retired) is dominant
        adult Female   → Non_worker (housewife) inflated for 23-57

Output: one of the 5 workforce_status partition codes.

Note: the marginal calibration target (Main 31, Marginal 11, Non-worker 38,
Student 12, Unemployed 8) won't be exactly hit — verifier reports the gap.
v1 accepts mismatch; v2 may add a global rejection-resampling pass.
"""
from __future__ import annotations


def sample(rng, ctx, axis, persona, persona_config=None, **kwargs):
    age = persona.get("age_cohort")
    gender = persona.get("gender")
    edu = persona.get("education")

    # Children: Non_worker bucket (we don't have a separate child category).
    if age in {"0_4", "5_9", "10_14", "15_17"}:
        return "Non_worker"

    # 18-22 educated → student attractor
    if age == "18_22" and edu in {"Higher_Secondary", "Graduate", "Postgraduate"}:
        if rng.random() < 0.55:
            return "Student"

    # 63+ → mostly retired
    if age in {"63_67", "68plus"}:
        if rng.random() < 0.85:
            return "Non_worker"

    # 58-62 → leaning retired
    if age == "58_62" and rng.random() < 0.55:
        return "Non_worker"

    # Edu-conditional rates
    joint = ctx.joint("workforce_indicators_given_education")
    rates = joint.table.get(edu, {})
    p_main = float(rates.get("Main_worker_rate", 30.0)) / 100.0
    p_unemp = float(rates.get("Unemployed_seeking", 5.0)) / 100.0

    # Female housewife inflation in working-age (23-57).
    # PLFS 2017-18 WB female LFPR = 23.0% overall (rural 19.8%) — meaning
    # ~77-80% of working-age women are non-LFPR. v0 used 0.55 which
    # under-counted housewives; bumped to 0.75 to approach the published
    # FLFPR after edu-conditional Main_worker Bernoulli below.
    # Source: https://iwwage.org/wp-content/uploads/2021/04/WB-Factsheet.pdf
    female_housewife_age = age in {"23_27", "28_32", "33_37", "38_42", "43_47", "48_52", "53_57"}
    if gender == "Female" and female_housewife_age:
        if rng.random() < 0.75:
            return "Non_worker"

    r = rng.random()
    if r < p_main:
        return "Main_worker"
    if r < p_main + p_unemp:
        return "Unemployed"
    # Residual: marginal vs non-worker (50/50)
    if rng.random() < 0.45:
        return "Marginal_worker"
    return "Non_worker"
