"""AC 210 (Nandigram) — workforce sampler.

Tuned to hit the AC 210 marginal:
  Main_worker 33, Marginal_worker 8, Non_worker 37, Student 12, Unemployed 10.

Coastal Purba Medinipur is a heavily agrarian belt — Mahishya cultivator/
agricultural-labourer dominant. Female farm-labour participation is real
but most working-age women still report as Non_worker (housewife) in
Census workforce-status — so we use a moderate housewife rate to hit the
37% Non_worker target.

Strategy:
  1. Children → Non_worker (defensive)
  2. 18-22 educated → mostly Student (~85%); 18-22 illit/primary → some Student
  3. 23-27 grad+ → some Student (PG cohort)
  4. 63+ → mostly retired (Non_worker)
  5. 58-62 → leaning retired
  6. Female 23-57 → housewife (~55%) — calibrated for AC 210
  7. Prime-working-age males 23-57 → distribute over Main/Marginal/Unemp
     proportional to non-Non marginal (excludes Non_worker)
  8. Everyone else → marginal sample (excluding Student)
"""
from __future__ import annotations

import random as _r
from pipeline.persona_generation.generic_plugins import _pick_category


def _sample_from_marginal_subset(rng: _r.Random, axis, include: set):
    """Sample from axis.marginal restricted to a subset of categories
    (renormalized). Returns one of the included cats or None if no mass."""
    cats = [c for c in (axis.categories or []) if c in include]
    weights = [(axis.marginal or {}).get(c, 0.0) for c in cats]
    if sum(weights) <= 0:
        return None
    return rng.choices(cats, weights=weights, k=1)[0]


def sample(rng, ctx, axis, persona, persona_config=None, **kwargs):
    age = persona.get("age_cohort") or ""
    gender = persona.get("gender")
    edu = persona.get("education")

    # Children → Non_worker (defensive; child cohorts dropped from axis).
    if any(s in age for s in ("0_4", "5_9", "10_14", "15_17")):
        return _pick_category(axis, ("Non_worker",))

    # 18-22 → Student.
    if age == "18_22":
        if edu and any(k in edu for k in ("Secondary", "Higher_Secondary",
                                            "Graduate", "Postgraduate")):
            if rng.random() < 0.85:
                return _pick_category(axis, ("Student",))
        elif rng.random() < 0.30:
            return _pick_category(axis, ("Student",))
    # 23-27 with Graduate+ → still in PG/professional school
    if age == "23_27" and edu in ("Graduate", "Postgraduate"):
        if rng.random() < 0.20:
            return _pick_category(axis, ("Student",))

    # 63+ → mostly retired (~85%).
    if any(s in age for s in ("63_67", "68")):
        if rng.random() < 0.85:
            return _pick_category(axis, ("Non_worker",))
    # 58-62 → leaning retired (~50%).
    if age == "58_62" and rng.random() < 0.50:
        return _pick_category(axis, ("Non_worker",))

    # Female 23-57 → housewife. Coastal Medinipur ag-labour belt has some
    # female farm participation but Census-style workforce reporting still
    # marks most as Non_worker (housewife). 55% balances the marginal.
    female_housewife_age = age in {"23_27", "28_32", "33_37", "38_42",
                                     "43_47", "48_52", "53_57"}
    if gender == "Female" and female_housewife_age and rng.random() < 0.55:
        return _pick_category(axis, ("Non_worker",))

    # Prime working-age males (23-57): exclude Non_worker — distribute over
    # Main/Marginal/Unemp by their marginal weights. This prevents the
    # "fall back to Non_worker" sink that inflates Non_worker beyond target.
    male_working_age = age in {"23_27", "28_32", "33_37", "38_42",
                                  "43_47", "48_52", "53_57"}
    if gender == "Male" and male_working_age:
        pick = _sample_from_marginal_subset(
            rng, axis, include={"Main_worker", "Marginal_worker",
                                  "Unemployed"})
        if pick is not None:
            return pick

    # Residual: sample directly from workforce marginal, excluding Student
    # (already handled above; including would double-count).
    cats = [c for c in (axis.categories or []) if c != "Student"]
    weights = [(axis.marginal or {}).get(c, 0.0) for c in cats]
    if sum(weights) <= 0:
        return _pick_category(axis, ("Non_worker",))
    return rng.choices(cats, weights=weights, k=1)[0]
