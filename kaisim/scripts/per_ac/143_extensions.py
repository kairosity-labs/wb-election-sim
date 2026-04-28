"""AC 143 (Diamond Harbour) — South 24 Parganas estuarine / Abhishek's seat.

Diamond Harbour is Abhishek Banerjee's parliamentary base. AC 143 is one
of seven LS segments. The seat is:
  - Hindu-majority but with a notable Muslim cohort (~22-25%)
  - Bagdi/Mahishya OBC mix on the Hindu side; SC pool more diverse than
    Bangaon's Matua-monoculture
  - Bangladesh-origin migration is small (tier D throughout — methodology
    note documents the cohort as long-resident rather than recent refugee)
  - Has a distinct **CPI(M)+LF combined** vote bucket in §E (vs. 095's
    CPI(M)+INC). Reflects the Left's residual 2019 strength here.

This extension:
  - Tags vote axes about the combined CPI(M)+LF bucket so downstream
    samplers know the bucket is a *combination*, not a single party.
  - Adds `abhishek_loyalty` derived axis as a candidate-effect anchor
    (modelled E-tier, salient for LLM narratives).
"""
from __future__ import annotations


def extend(axes, joints, aggregates):
    for axis in axes:
        if axis["name"] == "caste":
            axis["notes"] = ((axis.get("notes") or "")
                              + " [AC 143: SC pool diverse — Bagdi-led but "
                                "Mahishya-Bagdi-Pod-Poundra mix, not Matua-"
                                "monoculture]").strip()

    if aggregates and aggregates.get("aggregate_targets"):
        for tgt in aggregates["aggregate_targets"]:
            tgt["notes"] = ((tgt.get("notes") or "")
                             + " [AC 143: §E uses combined CPI(M)+LF bucket — "
                               "reflects 2019 LF residual strength here]"
                            ).strip()

    axes.append({
        "name": "abhishek_loyalty",
        "kind": "derived",
        "parents": ["religion", "caste"],
        "module": "derived.abhishek_loyalty",
        "function": "compute",
        "categories": ["high", "medium", "low"],
        "tier": "E",
        "needs_review": True,
        "notes": "AC 143 specific. Anchors candidate-effect: Abhishek's "
                  "2019 Diamond Harbour LS margin was the highest in WB. "
                  "TMC ground-game saturation here is uniquely strong.",
    })
    return axes, joints, aggregates
