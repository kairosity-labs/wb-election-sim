"""AC-agnostic baseline plugins for the rule_based sampler.

Each function here implements the 095-style plugin contract:

    fn(rng, ctx, axis, persona, persona_config=None, **kwargs) -> Any

but reads everything from the SimulationContext (axes + joints) and the
prior persona fields — never hardcoding AC-specific category codes. This
lets a fresh AC produce a sensible baseline population without authoring
six per-axis Python files.

Per-AC simulations re-export these from `simulations/wb_2021_ac<NN>/derived/`
so the rule_based sampler's plugin loader can resolve them via the standard
import path `simulations.<sim>.derived.<module>.<function>`.

For ACs that need richer per-AC logic (welfare-take-up rules indexed to
local schemes, tea-garden workforce categories, etc.), override individual
modules per AC. AC 095 already does this in `simulations/wb_2021_ac095/derived/`.
"""
from __future__ import annotations

import math

_EPS = 1e-4


def _logit(p_pct: float) -> float:
    p = max(_EPS, min(1.0 - _EPS, p_pct / 100.0))
    return math.log(p / (1.0 - p))


def _sigmoid(x: float) -> float:
    return 1.0 / (1.0 + math.exp(-x))


def _try_joint(ctx, name):
    try:
        return ctx.joint(name)
    except KeyError:
        return None


def _row_for(joint, parent_value):
    if joint is None or parent_value is None:
        return {}
    return joint.table.get(parent_value, {}) or {}


def _categorical(rng, dist):
    """Sample a key from a {key: weight} dict; return None if all weights ≤ 0."""
    if not dist:
        return None
    keys = list(dist.keys())
    weights = [float(v) for v in dist.values()]
    total = sum(weights)
    if total <= 0:
        return None
    return rng.choices(keys, weights=weights, k=1)[0]


def _restrict_to_axis(dist, axis):
    legal = set(axis.categories or [])
    if not legal:
        return dist
    return {k: v for k, v in dist.items() if k in legal}


# ---------------------------------------------------------------------------
# Marital — use married_given_age_gender if present
# ---------------------------------------------------------------------------

def marital_sample(rng, ctx, axis, persona, persona_config=None, **kwargs):
    age = persona.get("age_cohort")
    gender = persona.get("gender")

    # Children → Never_married whatever the axis calls it
    if age and any(s in (age or "") for s in ("0_4", "5_9", "10_14", "15_17")):
        return _pick_category(axis, ("Never", "never_married"))

    joint = _try_joint(ctx, "married_given_age_gender")
    p_married = None
    if joint is not None:
        # Try (age, gender) tuple key, then age key with gender column.
        row = joint.table.get((age, gender)) or joint.table.get(age) or {}
        # Look for "Male"/"Female" column or "Currently_married" indicator
        if isinstance(row, dict):
            if "Male" in row or "Female" in row:
                key = "Male" if gender == "Male" else "Female"
                v = row.get(key)
                if v is not None:
                    try:
                        p_married = float(v) / 100.0
                    except (ValueError, TypeError):
                        pass
            else:
                v = row.get("Currently_married") or row.get("Currently_married_Male" if gender == "Male" else "Currently_married_Female")
                if v is not None:
                    try:
                        p_married = float(v) / 100.0
                    except (ValueError, TypeError):
                        pass

    if p_married is None:
        # Fall back to marginal "Currently married" rate or 60%
        marg = axis.marginal or {}
        p_married = float(marg.get(_pick_category(axis, ("Currently_married",)), 60.0)) / 100.0

    if rng.random() < p_married:
        return _pick_category(axis, ("Currently_married",))

    # Residual: widow concentrates older + female; never_married for younger.
    if age and any(s in age for s in ("63_67", "68plus", "58_62")):
        if gender == "Female" and rng.random() < 0.55:
            return _pick_category(axis, ("Widowed",))
        if gender == "Male" and rng.random() < 0.20:
            return _pick_category(axis, ("Widowed",))
    if age and any(s in age for s in ("28_32", "33_37", "38_42", "43_47", "48_52")):
        if rng.random() < 0.04:
            return _pick_category(axis, ("Separated",))
    return _pick_category(axis, ("Never",))


def _pick_category(axis, hints):
    """Find an axis category whose snake_case starts with any hint substring."""
    cats = axis.categories or []
    for hint in hints:
        h = hint.lower()
        for c in cats:
            if c.lower().startswith(h) or h in c.lower():
                return c
    # Last resort: first marginal-largest category.
    if axis.marginal:
        return max(axis.marginal.items(), key=lambda kv: kv[1])[0]
    return cats[0] if cats else None


# ---------------------------------------------------------------------------
# Workforce — use workforce_given_education if available, with age/gender caps
# ---------------------------------------------------------------------------

def workforce_sample(rng, ctx, axis, persona, persona_config=None, **kwargs):
    """Generic workforce-status sampler. Logic mirrors AC 095's calibrated
    plugin: rule-driven children/seniors/female-housewife buckets, then
    education-conditional Bernoullis using the joint workforce_given_education
    if present (semantics two_indicator_rates: Main_worker_rate +
    Unemployed_seeking), with cumulative-threshold residual."""
    age = persona.get("age_cohort") or ""
    gender = persona.get("gender")
    edu = persona.get("education")

    # Children → Non_worker
    if any(s in age for s in ("0_4", "5_9", "10_14", "15_17")):
        return _pick_category(axis, ("Non_worker",))

    # 18-22 educated → Student attractor (~55%)
    if age == "18_22" and edu and ("Secondary" in edu or "Graduate" in edu
                                      or "Postgraduate" in edu):
        if rng.random() < 0.55:
            return _pick_category(axis, ("Student",))

    # 63+ → mostly retired (~85%)
    if any(s in age for s in ("63_67", "68plus")):
        if rng.random() < 0.85:
            return _pick_category(axis, ("Non_worker",))
    # 58-62 → leaning retired (~55%)
    if age == "58_62" and rng.random() < 0.55:
        return _pick_category(axis, ("Non_worker",))

    # Education-conditional rates (two_indicator_rates joint)
    p_main, p_unemp = 0.30, 0.05
    joint = _try_joint(ctx, "workforce_given_education")
    if joint is not None:
        row = joint.table.get(edu, {})
        if isinstance(row, dict):
            try: p_main = float(row.get("Main_worker_rate", p_main * 100)) / 100.0
            except (ValueError, TypeError): pass
            try: p_unemp = float(row.get("Unemployed_seeking",
                                           p_unemp * 100)) / 100.0
            except (ValueError, TypeError): pass

    # Female housewife inflation in working-age 23-57 (~75%, calibrated to
    # PLFS 2017-18 WB FLFPR ≈ 23%).
    female_housewife_age = age in {"23_27", "28_32", "33_37", "38_42",
                                     "43_47", "48_52", "53_57"}
    if gender == "Female" and female_housewife_age and rng.random() < 0.75:
        return _pick_category(axis, ("Non_worker",))

    # Cumulative-threshold (single-draw) residual to keep marginals balanced
    r = rng.random()
    if r < p_main:
        return _pick_category(axis, ("Main_worker", "Main worker"))
    if r < p_main + p_unemp:
        return _pick_category(axis, ("Unemployed",))
    # 45% chance the rest are Marginal_worker, else Non_worker
    if rng.random() < 0.45:
        return _pick_category(axis, ("Marginal_worker", "Marginal worker"))
    return _pick_category(axis, ("Non_worker",))


# ---------------------------------------------------------------------------
# Occupation — workers only; conditional on workforce_status
# ---------------------------------------------------------------------------

def occupation_sample(rng, ctx, axis, persona, persona_config=None, **kwargs):
    wf = persona.get("workforce_status") or ""
    if "Non_worker" in wf or "Student" in wf or "Unemployed" in wf:
        return None  # Not a worker → axis stays unset
    # Sample from axis marginal (we don't have a global occupation conditional)
    cats = axis.categories or []
    if not cats:
        return None
    weights = [axis.marginal.get(c, 0.0) for c in cats] if axis.marginal else [1.0] * len(cats)
    if sum(weights) <= 0:
        return cats[0]
    return rng.choices(cats, weights=weights, k=1)[0]


def class_of_worker_sample(rng, ctx, axis, persona, persona_config=None, **kwargs):
    wf = persona.get("workforce_status") or ""
    if "Non_worker" in wf or "Student" in wf or "Unemployed" in wf:
        return None
    cats = axis.categories or []
    if not cats:
        return None
    weights = [axis.marginal.get(c, 0.0) for c in cats] if axis.marginal else [1.0] * len(cats)
    if sum(weights) <= 0:
        return cats[0]
    return rng.choices(cats, weights=weights, k=1)[0]


# ---------------------------------------------------------------------------
# Asset — log-odds blend across multiple parent joints + marginal fallback
# ---------------------------------------------------------------------------

def asset_sample(rng, ctx, axis, persona, persona_config=None, **kwargs):
    gp = persona.get("gp_location")
    religion = persona.get("religion")
    occ = persona.get("occupation")

    j_gp = _try_joint(ctx, "asset_given_gp")
    j_rel = _try_joint(ctx, "asset_given_religion")
    j_occ = _try_joint(ctx, "asset_given_occupation")

    out: dict[str, bool] = {}
    for flag in (axis.flags or []):
        rates = []
        if j_gp is not None:
            v = j_gp.table.get(gp, {}).get(flag)
            if v is not None:
                try: rates.append(float(v))
                except (ValueError, TypeError): pass
        if j_rel is not None:
            v = j_rel.table.get(religion, {}).get(flag)
            if v is not None:
                try: rates.append(float(v))
                except (ValueError, TypeError): pass
        if j_occ is not None and occ is not None:
            v = j_occ.table.get(occ, {}).get(flag)
            if v is not None:
                try: rates.append(float(v))
                except (ValueError, TypeError): pass
        if rates:
            mean_logit = sum(_logit(r) for r in rates) / len(rates)
            p = _sigmoid(mean_logit)
        else:
            # Fall back to axis marginal rate
            try:
                p = float((axis.rates or {}).get(flag, 0.0)) / 100.0
            except (ValueError, TypeError):
                p = 0.0
        out[flag] = rng.random() < p
    return out


# ---------------------------------------------------------------------------
# Amenities — use amenities_given_gp if available
# ---------------------------------------------------------------------------

def amenity_sample(rng, ctx, axis, persona, persona_config=None, **kwargs):
    gp = persona.get("gp_location")
    j = _try_joint(ctx, "amenities_given_gp")
    out: dict[str, bool] = {}
    for flag in (axis.flags or []):
        rate = None
        if j is not None:
            v = j.table.get(gp, {}).get(flag)
            if v is not None:
                try:
                    rate = float(v) / 100.0
                except (ValueError, TypeError):
                    pass
        if rate is None:
            try:
                rate = float((axis.rates or {}).get(flag, 0.0)) / 100.0
            except (ValueError, TypeError):
                rate = 0.0
        out[flag] = rng.random() < rate
    return out


# ---------------------------------------------------------------------------
# Welfare — independent Bernoulli per flag from axis.rates (no scheme rules)
# ---------------------------------------------------------------------------

def welfare_derive(rng, ctx, axis, persona, persona_config=None, **kwargs):
    """Generic welfare derivation — independent Bernoulli per flag from axis.rates.
    Per-AC overrides should replace this for production runs."""
    out: dict[str, bool] = {}
    for flag in (axis.flags or []):
        try:
            rate = float((axis.rates or {}).get(flag, 0.0)) / 100.0
        except (ValueError, TypeError):
            rate = 0.0
        out[flag] = rng.random() < rate
    return out


def welfare_dominant(rng, ctx, axis, persona, persona_config=None, **kwargs):
    """Dominant scheme by precedence over flags currently True. Returns 'None'
    if no flag is True or precedence list is empty."""
    flags = persona.get("welfare_exposure", {}) or {}
    precedence = []
    if persona_config is not None:
        precedence = persona_config.get("vote.welfare_overlap.precedence") or []
    if not precedence:
        # Use axis flag declaration order
        precedence = list(flags.keys())
    for f in precedence:
        if flags.get(f):
            return f
    return _pick_category(axis, ("None", "none")) or "None"
