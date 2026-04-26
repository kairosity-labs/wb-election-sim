"""Asset flags — log-odds blend across (gp, religion, occupation) + marginal fallback.

For each flag in asset_media:
    1. Collect all available conditional rates from joints whose parent the
       persona has a value for:
          asset_given_gp[gp][flag]
          asset_given_religion[religion][flag]
          asset_given_occupation[occupation][flag]   (only if occupation != None)
    2. Average the available rates in log-odds space (uniform weights).
    3. Bernoulli sample.

Flags with no joint coverage (Radio, Mobile, TwoWheeler, FourWheeler) fall
back to the marginal axis rate.
"""
from __future__ import annotations

import math

_EPS = 1e-4


def _logit(p: float) -> float:
    p = max(_EPS, min(1.0 - _EPS, p / 100.0))
    return math.log(p / (1.0 - p))


def _sigmoid(x: float) -> float:
    return 1.0 / (1.0 + math.exp(-x))


def sample(rng, ctx, axis, persona, persona_config=None, **kwargs):
    gp = persona.get("gp_location")
    religion = persona.get("religion")
    occ = persona.get("occupation")

    j_gp = ctx.joint("asset_given_gp")
    j_rel = ctx.joint("asset_given_religion")
    j_occ = ctx.joint("asset_given_occupation")

    out: dict[str, bool] = {}
    for flag in axis.flags:
        rates: list[float] = []
        gp_row = j_gp.table.get(gp, {}) if gp else {}
        if flag in gp_row:
            rates.append(float(gp_row[flag]))
        rel_row = j_rel.table.get(religion, {}) if religion else {}
        if flag in rel_row:
            rates.append(float(rel_row[flag]))
        if occ and occ != "None":
            occ_row = j_occ.table.get(occ, {})
            if flag in occ_row:
                rates.append(float(occ_row[flag]))

        if rates:
            mean_logit = sum(_logit(r) for r in rates) / len(rates)
            p = _sigmoid(mean_logit)
        else:
            # No joint coverage → marginal fallback.
            p = float(axis.rates.get(flag, 0.0)) / 100.0

        out[flag] = rng.random() < p
    return out
