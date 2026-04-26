"""Amenity flags — gp-conditional Bernoulli + cooking-fuel partition.

Cooking fuel (LPG / Wood / Other_fuel) is conceptually a partition (sums to
~100%); the others (Sanitation, Water, Electricity) are independent flags.

Algorithm:
    1. LPG: gp-conditional Bernoulli from amenity_given_gp.
    2. If !LPG: split residual between Wood and Other_fuel using marginal ratio
       (Wood ≫ Other in marginal: 45 / 5 → 90% / 10%).
    3. Sanitation, Water, Electricity: independent gp-conditional Bernoulli.
"""
from __future__ import annotations


def sample(rng, ctx, axis, persona, persona_config=None, **kwargs):
    gp = persona.get("gp_location")
    j = ctx.joint("amenity_given_gp")
    rates = j.table.get(gp, {})

    out: dict[str, bool] = {f: False for f in axis.flags}

    p_lpg = float(rates.get("LPG", axis.rates.get("LPG", 50.0))) / 100.0
    out["LPG"] = rng.random() < p_lpg
    if not out["LPG"]:
        wood_share = float(axis.rates.get("Wood", 45.0))
        other_share = float(axis.rates.get("Other_fuel", 5.0))
        total = wood_share + other_share
        if total > 0 and rng.random() < (wood_share / total):
            out["Wood"] = True
        else:
            out["Other_fuel"] = True

    for flag in ("Improved_sanitation_latrine",
                 "Improved_drinking_water_source",
                 "Electricity"):
        if flag in axis.flags:
            p = float(rates.get(flag, axis.rates.get(flag, 70.0))) / 100.0
            out[flag] = rng.random() < p

    return out
