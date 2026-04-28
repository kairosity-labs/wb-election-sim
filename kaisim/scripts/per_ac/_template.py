"""Per-AC extension template.

Copy this file to `<NN>_extensions.py` (e.g. `011_extensions.py`) when an
AC needs custom post-processing the common scaffold doesn't capture
(tea-garden workforce buckets, Sarna sub-religion expansion, AC-local
ward-cluster sub-units, etc.).

The build_ac_verifier_configs.py script will detect and import the file
automatically and call `extend(axes, joints, aggregates)` as the final
post-processing step before writing JSON.

Inputs:
    axes        — list[dict], the auto-generated axis JSON entries
    joints      — list[dict], the auto-generated joint JSON entries
    aggregates  — dict | None, the auto-generated aggregate-targets JSON

Returns:
    (axes, joints, aggregates) — possibly modified

Common patterns:
    - patch a marginal pct (audit override)
    - add a derived axis (e.g., welfare_exposure with module/function)
    - declare a subgroup_rollup (e.g., SC_total = [Namasudra_Matua, Bagdi, ...])
    - inject an AC-specific joint missing from the common builder
    - rename an AC-local category to align with sim-wide vocabulary
"""
from __future__ import annotations


def extend(axes: list[dict], joints: list[dict],
           aggregates: dict | None) -> tuple[list[dict], list[dict], dict | None]:
    # Example skeleton — does nothing by default.
    #
    # for axis in axes:
    #     if axis["name"] == "religion":
    #         # audit override: re-weight from sub-AC composition
    #         axis["marginal"]["Hindu"] = 81.0
    #         axis["marginal"]["Muslim"] = 18.0
    #         axis["notes"] = "audit-overridden marginal (sub-unit re-weighted)"
    #         axis["needs_review"] = False
    #
    # axes.append({
    #     "name": "welfare_exposure",
    #     "kind": "derived",
    #     "parents": ["occupation", "age_cohort", "gender"],
    #     "module": "simulations.wb_2021_ac<NN>.derived.welfare_exposure",
    #     "function": "compute",
    #     "tier": "E",
    #     "needs_review": False,
    #     "notes": "Derived from rural/urban × scheme-eligibility rules.",
    # })

    return axes, joints, aggregates
