"""AC 003 (Cooch Behar Uttar) — Rajbanshi-belt specifics.

Cooch Behar Uttar is a Rajbanshi/Koch (SC) and Muslim border seat in north
WB. The local caste palette is dominated by **Rajbanshi (Koch)** as the
single largest SC sub-group — a configuration distinct from the
Namasudra-Matua belts of the south. The MD's C.5 also lists **Rajbongshi**
as a distinct mother-tongue (a Bengali register written either in Bengali
or Eastern Nagari script).

This extension:
  - Tags the local caste/language palette as do-NOT-cross-map to other ACs.
  - Adds a `rajbanshi_status` derived axis: present-vs-absent indicator
    that downstream LLM persona narratives can key on.
  - Notes the Greater Cooch Behar / KPP regional-party angle (D.15-D.18
    sometimes lists AIFB as a distinct vote bucket).
"""
from __future__ import annotations


def extend(axes, joints, aggregates):
    for axis in axes:
        if axis["name"] == "caste":
            axis["notes"] = ((axis.get("notes") or "")
                              + " [AC 003: Rajbanshi (Koch) is dominant SC; "
                                "do NOT cross-map to Namasudra-Matua belts]"
                              ).strip()
        if axis["name"] == "mother_tongue":
            axis["notes"] = ((axis.get("notes") or "")
                              + " [AC 003: Rajbongshi listed as distinct MT — "
                                "a Bengali register, not a separate language]"
                              ).strip()
        if axis["name"] == "migration":
            axis["notes"] = ((axis.get("notes") or "")
                              + " [AC 003: Bangladesh-origin + Nepal/Bhutan-origin "
                                "are both salient — border with both countries]"
                              ).strip()

    axes.append({
        "name": "rajbanshi_status",
        "kind": "derived",
        "parents": ["caste"],
        "module": "derived.rajbanshi_status",
        "function": "compute",
        "categories": ["rajbanshi_sc", "non_rajbanshi"],
        "tier": "E",
        "needs_review": True,
        "notes": "AC 003 specific. True iff caste ∈ {Rajbanshi, Koch}. "
                  "Used by LLM persona narratives for Cooch Behar identity.",
    })
    return axes, joints, aggregates
