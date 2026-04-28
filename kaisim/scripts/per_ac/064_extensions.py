"""AC 064 (Murshidabad) — Muslim-majority Ganga belt.

Murshidabad is one of the few WB seats with a Hindu-minority composition
(~40% Hindu / ~60% Muslim). The local Muslim sub-caste structure is
explicit in this MD's D.2 (Sheikh / Ansari-Jolaha / Syed-Pathan-Mughal /
Other) — a richer fine-grain than most other ACs which collapse Muslim
into one bucket.

⚠ Known MD-level data issue (gate 1 hard-fail):
   The C.2 caste rows currently sum to 93.9% (off by 6.1pp). Root cause:
   the `UC bhadralok` row stores 10.0 (= % of Hindu) instead of 5.5 (=
   % of total population). The MD's own arithmetic-check row inside
   §C.2 acknowledges this. **Fix at the MD level before sampling.**

This extension:
  - Tags caste + religion axes as Muslim-majority + sub-caste-rich.
  - Marks `caste` axis with `audit_blocker: caste_sum_off_by_6pp` so any
    downstream sampling step sees a hard signal to fix-the-MD-first.
  - Adds `muslim_subcaste` derived axis usable by LLM persona narratives
    (Sheikh/Ansari/Syed structure is load-bearing for political behavior
    in this AC — silk-weaving Ansaris vs cultivator Sheikhs).
"""
from __future__ import annotations


def extend(axes, joints, aggregates):
    for axis in axes:
        if axis["name"] == "caste":
            axis["notes"] = ((axis.get("notes") or "")
                              + " [AC 064: Muslim sub-caste structure is "
                                "fine-grained (Sheikh/Ansari/Syed) — load-"
                                "bearing for political modeling]").strip()
            axis["audit_blocker"] = (
                "MD §C.2 caste rows sum to ≈93.9% (UC bhadralok stored as "
                "10.0=%-of-Hindu rather than 5.5=%-of-total). Fix MD before "
                "running population sampler."
            )
        if axis["name"] == "religion":
            axis["notes"] = ((axis.get("notes") or "")
                              + " [AC 064: Muslim-majority AC (~60%); "
                                "Hindu-minority dynamics distinct from rest "
                                "of WB]").strip()

    axes.append({
        "name": "muslim_subcaste",
        "kind": "derived",
        "parents": ["religion", "caste"],
        "module": "derived.muslim_subcaste",
        "function": "compute",
        "categories": ["sheikh", "ansari_jolaha_weaver", "syed_pathan_mughal",
                        "obc_muslim_other", "not_muslim"],
        "tier": "D",
        "needs_review": True,
        "notes": "AC 064 specific. Murshidabad silk-weaver belt dynamics. "
                  "Tier D throughout per MD §G.",
    })
    return axes, joints, aggregates
