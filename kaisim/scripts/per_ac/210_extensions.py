"""AC 210 (Nandigram) — 2007 land-acquisition / Suvendu's seat.

Nandigram is the constituency where Mamata won her dramatic 2007 anti-
land-acquisition mobilization, and where Suvendu Adhikari (defected to
BJP in Dec 2020) defeated Mamata in the 2021 AE — though that's frozen
out in our 2019-state file. Key features in 2019:
  - **Land-acquisition-displaced cohort** from the 2007 SEZ confrontation
    is still partly identifiable — though the displacement registry is
    incomplete (tier D throughout per MD §G).
  - Hindu-majority + Mahishya/Bagdi mix (similar to but distinct from
    Tarakeswar's pure-Mahishya pattern).
  - Sub-units are CDB blocks (Nandigram-I + Nandigram-II), not GPs.

⚠ Known MD-level data issue (gate 1 hard-fail):
   The C.2 caste rows currently sum to 98.34% (off by 1.7pp). Smaller
   gap than AC 064 but still requires review. **Inspect §C.2 before
   sampling.**

This extension:
  - Tags caste as Mahishya/Bagdi mix.
  - Tags migration / occupation with land-acquisition-cohort note.
  - Adds `land_acq_displaced_2007` derived axis as a salient persona
    narrative anchor for the 2007 movement legacy.
"""
from __future__ import annotations


def extend(axes, joints, aggregates):
    for axis in axes:
        if axis["name"] == "caste":
            axis["notes"] = ((axis.get("notes") or "")
                              + " [AC 210: Mahishya + Bagdi mix; some Mahato "
                                "near Nandigram-II border. Distinct from "
                                "Matua belts]").strip()
            axis["audit_blocker"] = (
                "MD §C.2 caste rows sum to ≈98.3% (off by 1.7pp). "
                "Inspect leaf row pcts before running population sampler."
            )
        if axis["name"] == "migration":
            axis["notes"] = ((axis.get("notes") or "")
                              + " [AC 210: 2007 land-acquisition-displaced "
                                "cohort partly identifiable but registry is "
                                "incomplete; tier D]").strip()
        if axis["name"] == "gp_location":
            axis["notes"] = ((axis.get("notes") or "")
                              + " [AC 210: sub-units are CDB blocks "
                                "(Nandigram-I + Nandigram-II), not GPs]"
                              ).strip()

    axes.append({
        "name": "land_acq_displaced_2007",
        "kind": "derived",
        "parents": ["migration", "gp_location"],
        "module": "derived.land_acq_displaced",
        "function": "compute",
        "categories": ["displaced_2007", "non_displaced"],
        "tier": "D",
        "needs_review": True,
        "notes": "AC 210 specific. Anchors 2007 land-acquisition movement "
                  "legacy — load-bearing for political behavior in older "
                  "personas (cohort ≥35y in 2019).",
    })
    return axes, joints, aggregates
