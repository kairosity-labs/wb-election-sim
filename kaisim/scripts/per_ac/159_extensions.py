"""AC 159 (Bhabanipur) — Mamata's home seat, urban Kolkata, multilingual.

Bhabanipur is a unique AC: it's Mamata Banerjee's home base + one of the
most ethnically diverse seats in WB. The local linguistic palette is
load-bearing:
  - **Marwari + Gujarati** trader community (Burrabazar-adjacent) ~10-12%
  - **Bihari/UP Hindi-belt** migrants ~15-18%
  - **Punjabi + Odia + South Indian** smaller pockets
  - The MD's D.1 has Bengali/Hindi/Gujarati/Urdu/Punjabi/Odia/Other (vs
    095's collapsed Bengali/Hindi/Urdu/Other)

Sub-units are wards (KMC) rather than GPs. C.11 / D.11-D.14 use
"Ward cluster / zone" instead of "GP / Municipality".

This extension:
  - Tags caste with the multi-linguistic-community palette.
  - Tags mother_tongue + migration as multilingual.
  - Adds `linguistic_community` derived axis: trader-class identity
    is a major political-behavior signal in this AC.
"""
from __future__ import annotations


def extend(axes, joints, aggregates):
    for axis in axes:
        if axis["name"] == "caste":
            axis["notes"] = ((axis.get("notes") or "")
                              + " [AC 159: caste palette includes trader "
                                "communities (Marwari/Gujarati/Bihari) as "
                                "leaf cats; do NOT cross-map to non-Kolkata "
                                "ACs]").strip()
        if axis["name"] == "mother_tongue":
            axis["notes"] = ((axis.get("notes") or "")
                              + " [AC 159: 6+ language palette — "
                                "Bengali/Hindi/Gujarati/Urdu/Punjabi/Odia. "
                                "Bilingualism rate ~25% (vs 6% in 095)]"
                              ).strip()
        if axis["name"] == "migration":
            axis["notes"] = ((axis.get("notes") or "")
                              + " [AC 159: distinct Hindi-belt + other-state "
                                "in-migration cohorts — load-bearing for "
                                "trader-class persona narratives]").strip()
        if axis["name"] == "gp_location":
            axis["notes"] = ((axis.get("notes") or "")
                              + " [AC 159: sub-units are KMC ward clusters, "
                                "not GPs — see MD §A for ward composition]"
                              ).strip()

    axes.append({
        "name": "linguistic_community",
        "kind": "derived",
        "parents": ["mother_tongue", "caste", "migration"],
        "module": "derived.linguistic_community",
        "function": "compute",
        "categories": ["bengali_native", "marwari_gujarati_trader",
                        "bihari_hindi_belt", "punjabi_other_minority",
                        "muslim_urdu_speaking"],
        "tier": "D",
        "needs_review": True,
        "notes": "AC 159 specific. Bhabanipur trader-class identity is a "
                  "major political-behavior signal. Marwari-Gujarati BJP "
                  "leaning, Bengali-bhadralok TMC leaning is well-documented.",
    })
    return axes, joints, aggregates
