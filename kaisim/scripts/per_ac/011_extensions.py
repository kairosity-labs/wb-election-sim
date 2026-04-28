"""AC 011 (Kalchini) — tea-garden specifics.

This AC's workforce and economic structure is dominated by the closed-/
operational-tea-garden axis, which the standard schema doesn't capture.
The MD already encodes this in C.7 / C.10 with AC-local categories like
"Main worker — non-tea", "Marginal worker (seasonal / casual tea picking)",
"Unemployed (closed-garden / displaced)" and "BPL household (tea-garden
wages-dependent)".

The base build_ac_verifier_configs.py auto-generates these as their own
partition categories (snake-cased), which is the correct mechanical
result. This extension does light cleanup:

- Adds a `garden_status` derived axis for downstream simulator use.
- Notes that the SC/ST rollup pattern from 095 doesn't apply here
  (Kalchini's caste partition uses a different parent — `tribal_total`).
"""
from __future__ import annotations


def extend(axes: list[dict], joints: list[dict],
           aggregates: dict | None) -> tuple[list[dict], list[dict], dict | None]:
    # Mark workforce_status as AC-local (it has tea-garden-specific buckets
    # not present in other ACs).
    for axis in axes:
        if axis["name"] == "workforce_status":
            axis["notes"] = ((axis.get("notes") or "")
                              + " [AC 011: includes tea-garden-specific "
                                "categories (closed-garden displaced, seasonal "
                                "picking) — do NOT cross-map to other ACs]").strip()
        if axis["name"] == "economic_status":
            axis["notes"] = ((axis.get("notes") or "")
                              + " [AC 011: BPL is tea-garden-wage indexed; "
                                "₹176/day × ~275 work-days baseline]").strip()

    # Add a derived axis: garden_status. Useful for downstream LLM persona
    # narratives ("you live in a closed garden") even though it's mechanically
    # derivable from workforce_status + occupation. Marked needs_review so
    # the sim author can decide whether to keep it or compute on the fly.
    axes.append({
        "name": "garden_status",
        "kind": "derived",
        "parents": ["workforce_status", "occupation"],
        "module": "derived.garden_status",
        "function": "compute",
        "categories": ["operational_garden", "closed_displaced",
                        "non_garden", "outside_workforce"],
        "tier": "E",
        "needs_review": True,
        "notes": "AC 011 specific. Derived from workforce_status × occupation.",
    })

    return axes, joints, aggregates
