"""AC 123 (Sandeshkhali) — Sundarbans / bheri-economy / Aila-displacement.

Sandeshkhali is the Sundarbans-edge constituency where:
  - Cyclone Aila (2009) displaced thousands of households from the
    embankment zone — they appear as a distinct migration cohort in C.16.
  - The local economy is dominated by **bheri** (brackish-water fish-farm)
    capture by TMC strongmen, which in 2024 became the Sandeshkhali
    women's protest scandal — but in 2019 (frozen) it was just a normal
    rural-coastal pocket.
  - SC composition is mixed: Bagdi + Namasudra-Matua + smaller sub-groups.

This extension:
  - Adds a `aila_displacement_status` derived axis: an Aila-displaced
    household is a salient narrative anchor for LLM persona generation.
  - Adds a `bheri_economy_dependent` flag for the fish-farm-economy cohort.
  - Tags migration axis as having an unusual displacement-origin row.
"""
from __future__ import annotations


def extend(axes, joints, aggregates):
    for axis in axes:
        if axis["name"] == "migration":
            axis["notes"] = ((axis.get("notes") or "")
                              + " [AC 123: includes Cyclone-Aila-displacement "
                                "(2009) cohort as a distinct origin — tier D, "
                                "anchored to embankment-rebuild rosters]"
                              ).strip()
        if axis["name"] == "occupation":
            axis["notes"] = ((axis.get("notes") or "")
                              + " [AC 123: bheri (brackish fish-farm) economy "
                                "concentrated in eastern blocks; not a "
                                "separate occupation row in C.8 but flagged "
                                "via bheri_economy_dependent]").strip()

    axes.append({
        "name": "aila_displacement_status",
        "kind": "derived",
        "parents": ["migration"],
        "module": "derived.aila_displacement",
        "function": "compute",
        "categories": ["aila_displaced_2009", "non_displaced"],
        "tier": "D",
        "needs_review": True,
        "notes": "AC 123 specific. Aila-2009 is a load-bearing "
                  "narrative anchor for embankment-zone personas.",
    })
    axes.append({
        "name": "bheri_economy_dependent",
        "kind": "derived",
        "parents": ["occupation", "gp_location"],
        "module": "derived.bheri_economy",
        "function": "compute",
        "categories": ["bheri_dependent", "non_bheri"],
        "tier": "E",
        "needs_review": True,
        "notes": "AC 123 specific. True iff agri/fishery occupation in "
                  "eastern bheri-zone blocks (per MD §A spatial notes).",
    })
    return axes, joints, aggregates
