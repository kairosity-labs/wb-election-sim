"""AC 198 (Tarakeswar) — caste sampler.

Samples caste conditional on (gp_location, religion):
  - Muslim → Muslim
  - Hindu → caste_given_gp row, restricted to Hindu sub-castes
            (UC_bhadralok / OBC_Hindu / Other_Hindu / SC_total / ST_total)
  - Sarna_Tribal_religion / Christian / Other → Christian_Sarna_only_Other

This makes the population's GP×caste cross-tab match `caste_given_gp` while
keeping Hindu/Muslim caste consistent with religion.
"""
from __future__ import annotations

from pipeline.persona_generation.generic_plugins import _try_joint, _pick_category


HINDU_CASTES = ("UC_bhadralok", "OBC_Hindu", "Other_Hindu", "SC_total", "ST_total")


def sample(rng, ctx, axis, persona, persona_config=None, **kwargs):
    religion = persona.get("religion")
    gp = persona.get("gp_location")

    if religion == "Muslim":
        return _pick_category(axis, ("Muslim",))
    if religion in ("Sarna_Tribal_religion", "Christian", "Other"):
        return _pick_category(axis, ("Christian_Sarna_only_Other",))

    # Hindu — use caste_given_gp restricted to Hindu sub-castes.
    joint = _try_joint(ctx, "caste_given_gp")
    if joint is not None:
        row = joint.table.get(gp, {})
        if isinstance(row, dict):
            cats = [c for c in HINDU_CASTES if c in row and row[c] > 0]
            weights = [row[c] for c in cats]
            if sum(weights) > 0:
                return rng.choices(cats, weights=weights, k=1)[0]

    # Fallback — Hindu axis marginal, restricted to Hindu cats.
    cats = [c for c in HINDU_CASTES if (axis.marginal or {}).get(c, 0) > 0]
    weights = [axis.marginal[c] for c in cats]
    if sum(weights) > 0:
        return rng.choices(cats, weights=weights, k=1)[0]
    return _pick_category(axis, ("OBC_Hindu",))
