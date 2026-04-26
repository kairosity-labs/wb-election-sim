"""Occupation — only meaningful if the persona is a worker.

Returns:
    "None"   if workforce_status ∉ {Main_worker, Marginal_worker}
    sampled occupation from marginal otherwise

There is no joint conditioning occupation on caste/gp in v1. Occupation is
sampled from its marginal among workers.
"""
from __future__ import annotations


def sample(rng, ctx, axis, persona, persona_config=None, **kwargs):
    wf = persona.get("workforce_status")
    if wf not in {"Main_worker", "Marginal_worker"}:
        return "None"
    cats = axis.categories
    weights = [axis.marginal[c] for c in cats]
    return rng.choices(cats, weights=weights, k=1)[0]


def class_of_worker(rng, ctx, axis, persona, persona_config=None, **kwargs):
    wf = persona.get("workforce_status")
    if wf not in {"Main_worker", "Marginal_worker"}:
        return "None"
    cats = axis.categories
    weights = [axis.marginal[c] for c in cats]
    return rng.choices(cats, weights=weights, k=1)[0]
