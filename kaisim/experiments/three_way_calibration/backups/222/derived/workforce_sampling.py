"""AC 222 (Jhargram) — workforce sampler.

Jangalmahal tribal belt has *higher* female labour participation than
typical WB rural ACs because tribal women lead forest-produce collection
and ag-labour (women overrepresented per MD §F). FLFPR ~50%+ vs WB
average ~23%.

Marginal targets (adults-only, after child-cohort drop):
  Main_worker 35, Marginal_worker 15, Non_worker 34, Student 10,
  Unemployed 6 (in original % of all).
"""
from __future__ import annotations

import random as _r
from pipeline.persona_generation.generic_plugins import (_pick_category,
                                                            _try_joint)


def _sample_from_marginal_excluding(rng: _r.Random, axis, exclude: set,
                                       reweights: dict | None = None):
    """Sample from marginal excluding categories; optionally reweight."""
    cats = [c for c in (axis.categories or []) if c not in exclude]
    weights = []
    for c in cats:
        w = (axis.marginal or {}).get(c, 0.0)
        if reweights and c in reweights:
            w *= reweights[c]
        weights.append(w)
    if sum(weights) <= 0:
        return _pick_category(axis, ("Non_worker",))
    return rng.choices(cats, weights=weights, k=1)[0]


def sample(rng, ctx, axis, persona, persona_config=None, **kwargs):
    age = persona.get("age_cohort") or ""
    gender = persona.get("gender")
    edu = persona.get("education") or ""

    # Children → Non_worker (defensive; child cohorts dropped from axis).
    if any(s in age for s in ("0_4", "5_9", "10_14", "15_17")):
        return _pick_category(axis, ("Non_worker",))

    # 18-22 → Student.  Need 10% pop Student; 18-22 is ~9% of pop, so
    # nearly all 18-22 must be Student (or pull some 23-27 too).
    if age == "18_22":
        if any(k in edu for k in ("Middle", "Secondary", "Higher_Secondary",
                                    "Graduate", "Postgraduate")):
            if rng.random() < 0.95:
                return _pick_category(axis, ("Student",))
        elif rng.random() < 0.50:
            return _pick_category(axis, ("Student",))

    # 23-27 with Graduate+ → PG/professional school still
    if age == "23_27" and edu in ("Graduate", "Postgraduate"):
        if rng.random() < 0.30:
            return _pick_category(axis, ("Student",))

    # 63+ → mostly retired (~70%) — slightly lighter than urban WB ACs
    # because tribal seniors continue forest-produce labour.
    if any(s in age for s in ("63_67", "68")):
        if rng.random() < 0.70:
            return _pick_category(axis, ("Non_worker",))
    # 58-62 → leaning retired (~30%).
    if age == "58_62" and rng.random() < 0.30:
        return _pick_category(axis, ("Non_worker",))

    # Tribal-belt FLFPR is HIGH; do NOT inflate Female → Non_worker as the
    # generic plugin does.  No extra housewife gate — the marginal
    # sampler will pick Non_worker at its native 34% rate.

    # Residual: sample from marginal excluding Student.  Down-weight
    # Non_worker (already inflated by senior gates above) so total
    # Non_worker mass lands ≈ 34%.
    return _sample_from_marginal_excluding(rng, axis, exclude={"Student"},
                                              reweights={"Non_worker": 0.75})
