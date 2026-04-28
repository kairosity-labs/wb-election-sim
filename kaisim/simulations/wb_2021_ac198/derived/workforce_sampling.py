"""AC 198 (Tarakeswar) — workforce sampler.

Tuned for Hooghly rural-OBC AC. Targets:
  Main_worker 33  Marginal_worker 12  Non_worker 37  Student 11  Unemployed 7

Strategy: gate-driven for structural Non_worker (seniors, female housewife)
and Student; the residual samples from workforce marginal directly so the
overall distribution lands near target by construction.
"""
from __future__ import annotations

import random as _r
from pipeline.persona_generation.generic_plugins import _pick_category


def _sample_from_workers(rng: _r.Random, axis):
    """Sample from {Main_worker, Marginal_worker, Unemployed} weighted by
    target marginal proportions. Excludes Student (gate-only) and Non_worker
    (gate-only)."""
    worker_cats = ("Main_worker", "Marginal_worker", "Unemployed")
    cats = [c for c in (axis.categories or []) if c in worker_cats]
    weights = [(axis.marginal or {}).get(c, 0.0) for c in cats]
    if sum(weights) <= 0:
        return _pick_category(axis, ("Main_worker",))
    return rng.choices(cats, weights=weights, k=1)[0]


def sample(rng, ctx, axis, persona, persona_config=None, **kwargs):
    age = persona.get("age_cohort") or ""
    gender = persona.get("gender")
    edu = persona.get("education")

    # Defensive: children → Non_worker (already dropped from axis though)
    if any(s in age for s in ("0_4", "5_9", "10_14", "15_17")):
        return _pick_category(axis, ("Non_worker",))

    # 18-22 → very high Student rate (95% if secondary+, 50% otherwise)
    if age == "18_22":
        if edu and any(k in edu for k in ("Secondary", "Graduate", "Postgraduate")):
            if rng.random() < 0.95:
                return _pick_category(axis, ("Student",))
        elif rng.random() < 0.50:
            return _pick_category(axis, ("Student",))
    # 23-27 graduate+ → some still in PG/professional school
    if age == "23_27" and edu in ("Graduate", "Postgraduate"):
        if rng.random() < 0.30:
            return _pick_category(axis, ("Student",))

    # 63+ → mostly retired (~85%)
    if any(s in age for s in ("63_67", "68")):
        if rng.random() < 0.85:
            return _pick_category(axis, ("Non_worker",))
    # 58-62 → leaning retired (~50%)
    if age == "58_62" and rng.random() < 0.50:
        return _pick_category(axis, ("Non_worker",))

    # Female 23-57 → housewife (50% — drives most of Non_worker mass).
    # Target Non_worker=37%; subtract structural mass already gated:
    #   seniors gate: ~7% pop * 0.7 ≈ 5pp Non_worker
    #   female housewife at 50% of ~22% pop ≈ 11pp Non_worker
    #   children gate: 0 (children already removed)
    # Residual ~21pp Non_worker should come from Marginal_worker→Non_worker
    # which happens for males and non-housewife females in the worker pool.
    female_housewife_age = age in {"23_27", "28_32", "33_37", "38_42",
                                     "43_47", "48_52", "53_57"}
    if gender == "Female" and female_housewife_age and rng.random() < 0.45:
        return _pick_category(axis, ("Non_worker",))

    # Residual: sample with weights tuned to land marginal near target.
    # After student/senior/housewife gates, residual should be ~58% workers
    # (Main+Marginal), ~15% Non_worker, ~10% Unemployed.
    cats = ["Main_worker", "Marginal_worker", "Unemployed", "Non_worker"]
    cats = [c for c in cats if c in (axis.categories or [])]
    weights_map = {"Main_worker": 55, "Marginal_worker": 20,
                    "Unemployed": 12, "Non_worker": 13}
    weights = [weights_map.get(c, 1) for c in cats]
    return rng.choices(cats, weights=weights, k=1)[0]
