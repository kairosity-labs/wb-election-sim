"""AC 003 (Cooch Behar Uttar) — workforce sampler.

Marginal-respecting design: rule-driven gates for children/seniors/
female-housewife/students cover the structural Non_worker mass; the
remainder samples directly from the workforce marginal (Main/Marginal/
Unemp/Non) so the population marginal lands close to target by
construction. Tuned for AC 003's adult age distribution.
"""
from __future__ import annotations

import random as _r
from pipeline.persona_generation.generic_plugins import _pick_category


def _sample_from_marginal_excluding(rng: _r.Random, axis, exclude: set):
    """Sample from axis.marginal excluding given categories (renormalized)."""
    cats = [c for c in (axis.categories or []) if c not in exclude]
    weights = [(axis.marginal or {}).get(c, 0.0) for c in cats]
    if sum(weights) <= 0:
        return _pick_category(axis, ("Non_worker",))
    return rng.choices(cats, weights=weights, k=1)[0]


def sample(rng, ctx, axis, persona, persona_config=None, **kwargs):
    age = persona.get("age_cohort") or ""
    gender = persona.get("gender")
    edu = persona.get("education")

    # Children → Non_worker (defensive; child cohorts dropped from axis).
    if any(s in age for s in ("0_4", "5_9", "10_14", "15_17")):
        return _pick_category(axis, ("Non_worker",))

    # 18-22 → Student (high rate; even non-secondary may be in school given
    # AC 003's Cooch Behar HE expansion).
    if age == "18_22":
        if edu and any(k in edu for k in ("Secondary", "Graduate", "Postgraduate")):
            if rng.random() < 0.85:
                return _pick_category(axis, ("Student",))
        elif rng.random() < 0.30:
            return _pick_category(axis, ("Student",))
    # 23-27 with Graduate+ → still in PG/professional school for some
    if age == "23_27" and edu in ("Graduate", "Postgraduate"):
        if rng.random() < 0.18:
            return _pick_category(axis, ("Student",))

    # 63+ → mostly retired (~85%).
    if any(s in age for s in ("63_67", "68")):
        if rng.random() < 0.85:
            return _pick_category(axis, ("Non_worker",))
    # 58-62 → leaning retired (~50%).
    if age == "58_62" and rng.random() < 0.50:
        return _pick_category(axis, ("Non_worker",))

    # Female 23-57 → housewife (25%) — Cooch Behar adult FLFPR ~32% so
    # ~70% of working-age women in workforce; but most are Marginal_worker
    # (ag-labourer cohort) which we let the marginal pick.
    female_housewife_age = age in {"23_27", "28_32", "33_37", "38_42",
                                     "43_47", "48_52", "53_57"}
    # AC 003 Non_worker target is 36% (low for WB) — let the marginal
    # sampler do its work without extra housewife inflation. Empirically
    # the seniors gate already handles much of the structural Non_worker.

    # Residual: sample directly from workforce marginal, excluding Student
    # (already handled above; including it here would double-count).
    return _sample_from_marginal_excluding(rng, axis, exclude={"Student"})
