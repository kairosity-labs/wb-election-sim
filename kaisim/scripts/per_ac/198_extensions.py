"""AC 198 (Tarakeswar) — Hooghly Mahishya/Sadgop OBC belt + temple economy.

Tarakeswar's caste palette is dominated by OBC sub-groups absent from the
simpler 095 schema:
  - **Mahishya** — single largest caste group in this AC; agriculture-
    rooted OBC, distinct political behavior from SC/ST blocs
  - **Sadgop** — second largest OBC; dairy + small-trade economy
  - **Kurmi / Tili** — smaller OBCs with cross-state migration links

The seat also has a Shiva-temple-pilgrimage economy (the Tarakeswar
Mandir) that sustains a distinct trader/service occupation cohort in §C.8.

Notes for v0:
  - **PM-Kisan exposure was 0% in 2019** — WB government declined the
    scheme until FY2021-22. The MD documents this with a forward-looking
    note that triggers the leakage gate (allow-listed in validate_calibrated).
  - The §E §H also tracks an unusual TMC-vs-BJP 2024 swing that 095's
    Bangaon doesn't have.

This extension:
  - Tags caste as Mahishya/Sadgop OBC dominated (do-NOT-cross-map).
  - Adds `obc_subgroup` derived axis with the local OBC palette.
"""
from __future__ import annotations


def extend(axes, joints, aggregates):
    for axis in axes:
        if axis["name"] == "caste":
            axis["notes"] = ((axis.get("notes") or "")
                              + " [AC 198: Mahishya + Sadgop OBC dominated "
                                "(~30-40% of pop). Distinct from generic "
                                "'OBC' bucket in other ACs]").strip()
        if axis["name"] == "occupation":
            axis["notes"] = ((axis.get("notes") or "")
                              + " [AC 198: includes temple-economy service "
                                "workers (~3-5% pop, Tarakeswar Mandir "
                                "pilgrimage) — folded into Trade/retail and "
                                "Services in C.8]").strip()
        if axis["name"] == "economic_status":
            axis["notes"] = ((axis.get("notes") or "")
                              + " [AC 198: PM-Kisan exposure = 0 in 2019 "
                                "(WB declined scheme until FY2021-22)]"
                              ).strip()

    axes.append({
        "name": "obc_subgroup",
        "kind": "derived",
        "parents": ["caste"],
        "module": "derived.obc_subgroup",
        "function": "compute",
        "categories": ["mahishya", "sadgop", "kurmi_tili", "other_obc",
                        "non_obc"],
        "tier": "D",
        "needs_review": True,
        "notes": "AC 198 specific. Mahishya political identity is a "
                  "long-running theme in WB politics (Sandeep Pandey's "
                  "sub-caste-mobilization framework).",
    })
    return axes, joints, aggregates
