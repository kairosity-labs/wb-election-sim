"""Joint verifier — per-cell pct gap on conditional / flag-rate / vote tables.

Uses the joint's `semantics` to dispatch:
    conditional             P(child | parents) — child-cat pcts in each row
    flag_rate_conditional   per-flag Bernoulli rate in each parent cell
    two_indicator_rates     same as flag_rate (treated as separate flag axes)
    vote_conditional        P(vote_field | parent) per row

Bucket maps:
    Some joints aggregate axis leaves into coarser buckets (e.g., the caste
    leaves Bagdi/Poundra/Other_SC collapse to "Bagdi_other_SC" in the
    education_given_caste table). The verifier maps persona leaf values to
    bucket keys before lookup.

Joints with no usable parent path on the persona (e.g., parent='asset_media_tier_derived')
are skipped with `skipped_reason`.
"""
from __future__ import annotations

from typing import Any

from ..core.joint import Joint
from ..core.persona import Persona
from .base import JointGap, standard_error_pp, z_from_gap


def _persona_parent_value(p: Persona, parent: str) -> Any:
    return p.get(parent)


def _map_bucket(value: Any, bucket_map: dict[str, list[str]] | None) -> Any:
    """Reverse-lookup: find bucket key whose leaf list contains this value."""
    if not bucket_map:
        return value
    for bucket, leaves in bucket_map.items():
        if value in leaves:
            return bucket
    return None


def _resolve_parent_for_joint(p: Persona, joint: Joint, parent: str) -> Any:
    raw = _persona_parent_value(p, parent)
    # Apply joint-specific bucket maps for caste / education parents.
    if parent == "caste" and joint.caste_bucket_map:
        return _map_bucket(raw, joint.caste_bucket_map)
    if parent == "education" and joint.education_bucket_map:
        # education_bucket_map is leaf -> bucket (1:1)
        return joint.education_bucket_map.get(raw, raw)
    return raw


def verify_joint(joint: Joint, personas: list[Persona], tolerance: dict[str, float]) -> JointGap:
    gap = JointGap(joint=joint.name, parents=joint.parents, child=joint.child,
                   semantics=joint.semantics, tier=joint.tier)
    n = len(personas)
    if n == 0:
        return gap

    # Skip joints whose parent isn't a direct persona field.
    parent_field_set = set(joint.parents)
    if any(p == "asset_media_tier_derived" for p in joint.parents):
        gap.skipped_reason = "parent 'asset_media_tier_derived' not implemented yet"
        return gap

    z_max = float(tolerance.get("cell_z_max", 2.5))

    def _record_cell(cell_meta: dict, observed_pct: float, target_pct: float, n_in: int):
        """Append a cell with z + chi-sq accounting; returns nothing."""
        g = observed_pct - target_pct
        se = standard_error_pp(target_pct, n_in)
        z = z_from_gap(observed_pct, target_pct, n_in)
        in_tol = abs(z) <= z_max
        cell = {
            **cell_meta,
            "target_pct": round(target_pct, 2),
            "observed_pct": round(observed_pct, 2),
            "gap_pp": round(g, 2),
            "se_pp": round(se, 3),
            "z": round(z, 2),
            "in_tol": in_tol,
            "n_in_cell": n_in,
        }
        gap.cells.append(cell)
        gap.max_abs_cell_gap_pp = max(gap.max_abs_cell_gap_pp, abs(g))
        gap.max_abs_z = max(gap.max_abs_z, abs(z))
        if n_in > 0:
            gap.chisq_sum += z * z
        if not in_tol:
            gap.n_out_of_tol += 1

    # Group personas by parent-value tuple.
    by_pv: dict[tuple, list[Persona]] = {}
    for p in personas:
        pv = tuple(_resolve_parent_for_joint(p, joint, par) for par in joint.parents)
        if any(v is None for v in pv):
            continue
        by_pv.setdefault(pv, []).append(p)

    # ----- Dispatch on semantics -----

    if joint.semantics == "conditional":
        child_bucket = (
            joint.caste_bucket_map
            if joint.child == "caste" and joint.caste_bucket_map
            else None
        )
        for pv_tuple, target_row in joint.table.items():
            pv = (pv_tuple,) if not isinstance(pv_tuple, tuple) else pv_tuple
            cell_personas = by_pv.get(pv, [])
            n_in = len(cell_personas)
            for child_cat, tgt in target_row.items():
                if n_in == 0:
                    obs = 0.0
                elif child_bucket is not None:
                    accepted = set(child_bucket.get(child_cat, [child_cat]))
                    obs = sum(1 for p in cell_personas if p.get(joint.child) in accepted) / n_in * 100
                else:
                    obs = sum(1 for p in cell_personas if p.get(joint.child) == child_cat) / n_in * 100
                _record_cell({"parent_values": list(pv), "child": child_cat}, obs, float(tgt), n_in)

    elif joint.semantics == "flag_rate_conditional":
        for pv_tuple, target_row in joint.table.items():
            pv = (pv_tuple,) if not isinstance(pv_tuple, tuple) else pv_tuple
            cell_personas = by_pv.get(pv, [])
            n_in = len(cell_personas)
            for flag, tgt in target_row.items():
                if n_in == 0:
                    obs = 0.0
                else:
                    obs_count = sum(
                        1 for p in cell_personas
                        if isinstance(p.get(joint.child), dict)
                        and p.get(joint.child, {}).get(flag)
                    )
                    obs = obs_count / n_in * 100
                _record_cell({"parent_values": list(pv), "child_flag": flag}, obs, float(tgt), n_in)

    elif joint.semantics == "two_indicator_rates":
        indicator_to_value = {
            "Main_worker_rate": "Main_worker",
            "Unemployed_seeking": "Unemployed_educated_actively_seeking",
        }
        for pv_key, target_row in joint.table.items():
            cell_personas = by_pv.get((pv_key,), [])
            n_in = len(cell_personas)
            for indicator, tgt in target_row.items():
                target_val = indicator_to_value.get(indicator)
                if target_val is None or n_in == 0:
                    obs = 0.0
                else:
                    obs = sum(1 for p in cell_personas if p.get(joint.child) == target_val) / n_in * 100
                _record_cell({"parent_values": [pv_key], "indicator": indicator}, obs, float(tgt), n_in)

    elif joint.semantics == "vote_conditional":
        for pv_key, target_row in joint.table.items():
            cell_personas = by_pv.get((pv_key,), [])
            n_in = len(cell_personas)
            for party, tgt in target_row.items():
                if n_in == 0:
                    obs = 0.0
                else:
                    obs = sum(1 for p in cell_personas if p.get(joint.child) == party) / n_in * 100
                _record_cell({"parent_values": [pv_key], "party": party}, obs, float(tgt), n_in)

    else:
        gap.skipped_reason = f"unknown semantics {joint.semantics!r}"

    return gap
