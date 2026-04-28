"""AC 222 (Jhargram) — Jangalmahal tribal belt / Sarna religion.

Jhargram is the heart of WB's Jangalmahal — a tribal-majority Adivasi
region with:
  - **Sarna/ORP** as a distinct religion (~10-11% of population) —
    a tribal nature-worship tradition that Census 2011 records under
    "Other religions". The MD's C.1 disaggregates this from "Hindu"
    explicitly.
  - **Santali, Mundari, Kurmali** as significant mother tongues
    alongside Bengali (D.1 has 5+ language columns).
  - **Mahato (OBC)** is a large local caste with cross-Jharkhand
    political linkage; **Bhumij** semi-Hinduised tribal community
    appears under Hindu umbrella but with Sarna roots.
  - Christian Adivasis (mostly Santhal + Munda evangelized in colonial
    period) form a small but distinct cohort.
  - **JKP(N)** (Jharkhand Party Naren) appears in §E vote target —
    a regional party not present in non-tribal-belt ACs.

This extension:
  - Tags religion + caste + mother_tongue with Sarna/Adivasi specifics.
  - Adds a `tribal_subgroup` derived axis covering Santhal/Munda/Bhumij/
    Mahato/non-tribal — load-bearing for LLM persona narratives.
  - Notes that JKP(N) bucket in §E is a regional party.
"""
from __future__ import annotations


def extend(axes, joints, aggregates):
    for axis in axes:
        if axis["name"] == "religion":
            axis["notes"] = ((axis.get("notes") or "")
                              + " [AC 222: Sarna/ORP is disaggregated from "
                                "Hindu (~10.9% of pop) — a tribal nature-"
                                "worship tradition; Census 2011 buckets it "
                                "as 'Other religions']").strip()
        if axis["name"] == "caste":
            axis["notes"] = ((axis.get("notes") or "")
                              + " [AC 222: tribal sub-castes (Santhal/Munda/"
                                "Bhumij) + Mahato (OBC) are load-bearing. "
                                "Bhumij appears under Hindu umbrella but has "
                                "Sarna roots — not the same as 'generic ST']"
                              ).strip()
        if axis["name"] == "mother_tongue":
            axis["notes"] = ((axis.get("notes") or "")
                              + " [AC 222: 5-language palette — Bengali / "
                                "Santali (Ol Chiki script) / Mundari / "
                                "Kurmali / Other. Bilingualism rate ~30% "
                                "(tribal languages + Bengali)]").strip()

    if aggregates and aggregates.get("aggregate_targets"):
        for tgt in aggregates["aggregate_targets"]:
            tgt["notes"] = ((tgt.get("notes") or "")
                             + " [AC 222: §E includes JKP(N) (Jharkhand Party "
                               "Naren) bucket — regional party absent from "
                               "most non-tribal ACs]").strip()

    axes.append({
        "name": "tribal_subgroup",
        "kind": "derived",
        "parents": ["religion", "caste"],
        "module": "derived.tribal_subgroup",
        "function": "compute",
        "categories": ["santhal", "munda_oraon", "bhumij_semihindu",
                        "mahato_obc", "non_tribal"],
        "tier": "D",
        "needs_review": True,
        "notes": "AC 222 specific. Jangalmahal tribal political identity. "
                  "Santhal/Munda/Mahato have distinct vote-share patterns.",
    })
    return axes, joints, aggregates
