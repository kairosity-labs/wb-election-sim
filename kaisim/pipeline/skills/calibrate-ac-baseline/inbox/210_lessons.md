# Lessons from AC 210 (Nandigram)

## New pattern: Vote-conditional macro reconciliation

**Symptom:** `aggregate vote_2019_LS_share` shows e.g. INC z=10.99 (target 0.86%, observed 5.4%); axis-level agg max_z dominates composite even after all joint/axis fixes are clean.

**Cause:** The vote-conditional joints (`vote_given_religion`, `vote_given_caste`, `vote_given_gender`) carry CSDS state-level rates (e.g. INC 3% Hindu / 8% Muslim) that DON'T reconcile to the AC-level macro outcome (INC at 0.86% in Nandigram). The vote_blending step blends these joints in log-odds, so all the joint INC values feed through and the AC-level macro is over-shot.

This isn't a name-mismatch — it's a substantive rate inconsistency between the conditional source (CSDS state pattern) and the macro target (AC-level ECI result). For AC's where the macro target diverges sharply from the state CSDS pattern (e.g. tiny party shares like INC, BSP, NOTA at <2% AC-wide), the joint must be rescaled to the AC outcome.

**Fix:** In curate.py, scale down party rates in vote-conditional joints to be consistent with the AC macro target. The simple recipe: identify any party with macro target <1.5% and clamp its joint values to ~1%, redistributing the excess to the locally-dominant party (here AITC):

```python
if j["name"] == "vote_given_caste":
    for caste_key, row in new_table.items():
        if not isinstance(row, dict):
            continue
        inc = row.get("INC", 0)
        if inc > 1.5:
            excess = inc - 1.0
            row["INC"] = 1.0
            if "AITC" in row:
                row["AITC"] = row["AITC"] + excess
```

For vote_given_religion in particular, a more principled fix is to back-solve the Hindu/Muslim row to satisfy the macro share equations directly:

```python
# Macro: AITC 63.14, BJP 30.09, INC 0.86 with Hindu mass 73.5% / Muslim 26.4%
# Solve Hindu row from AC target: 0.7351*h_aitc + 0.2635*82 = 63.14 → h_aitc = 56.5
j["table"]["Hindu"] = {"AITC": 56.5, "BJP": 30.0, "LF": 4.0,
                        "INC": 0.7, "Other": 8.8}
j["table"]["Muslim"] = {"AITC": 82.0, "BJP": 3.0, "LF": 6.0,
                         "INC": 1.0, "Other": 8.0}
```

This single change (in iteration 4) dropped composite from 1208 to 707 — i.e. the vote aggregate was contributing ~500 chisq purely from this rate inconsistency.

**Suggested skill section:** Add as **section I** (vote-conditional reconciliation), or fold into **section F** as a sibling pattern to "drop joints with non-existent parents" — this is "fix joints whose rate values don't reconcile to the AC's macro target."

---

## Minor pattern: Sub-block CDB names vs U1/U2 prefix

**Symptom:** `caste_given_gp`, `asset_given_gp`, `amenities_given_gp` joints all skip with `"all parent values absent from axes (dropped: ['Nandigram_I', 'Nandigram_II'])"`.

**Cause:** Sub-units in this AC are CDB blocks (Nandigram-I, Nandigram-II), not GPs, but the gp_location axis adds U1_/U2_ prefixes (`U1_Nandigram_I_CDB`, `U2_Nandigram_II_CDB`). Joint tables emit raw block names.

**Fix:** Same as AC 003's `gp_location` rename pattern — rename joint parent keys (or strip axis prefix). Here we renamed joint keys via a `GP_PARENT_RENAMES` map in curate.py rather than dropping the axis prefix, since the prefix carries semantic value (CDB-block sentinel) for downstream personas.

**Suggested skill section:** Already covered by section A (joint cell key vs axis cat alignment). Add a row to the table: "Sub-block axis cats have U1_/U2_/CDB- prefix but joint keys are bare → rename joint keys." (Same pattern as 003 with U1_/U2_ but with different rationale for keeping the prefix.)
