# Lessons from AC 064 (Murshidabad)

AC 064 went 8166 → 756 in 8 iterations.

## New pattern: Hindu-minority AC has incomplete Hindu sub-caste row in `caste_given_religion`

**Symptom:** After running auto-builder, `caste_given_religion`'s Hindu row sums to ~81% rather than 100% — the verifier sees `caste` axis marginal heavily under-weighted on Other_Hindu_middle.

**Cause:** The MD §C.2 lists the Hindu sub-castes as % of total population. The CSV-derivation gets `% of Hindu` correctly for the dominant SC/ST/UC/OBC leaves but drops some sub-buckets (e.g. "Kumbhakar/Subarnabanik/Tanti", "Jain religious minority") because they don't prefix-match any axis leaf via `_map_subcat_to_axis_leaf`. That dropped mass leaves Hindu summing to ~81%.

**Fix:** In `<NN>_curate.py`, rebuild the `caste_given_religion` Hindu row directly from MD §C.2 % of total values divided by religion marginal, and ALSO add explicit rows for each non-Hindu, non-Muslim religion key:

```python
if j["name"] == "caste_given_religion":
    hindu_dist = {
        "SC_total":           19.5 / 56.5 * 100,
        "ST_total":            2.2 / 56.5 * 100,
        "UC_bhadralok":        5.5 / 56.5 * 100,
        "OBC_Hindu":           8.0 / 56.5 * 100,
        "Other_Hindu_middle": 21.4 / 56.5 * 100,
    }
    j["table"] = {
        "Hindu": hindu_dist,
        "Muslim": dict(MUSLIM_SUBCASTE_SHARES),
        "Christian": {"Christian_Jain_Other": 100.0},
        "Jain": {"Christian_Jain_Other": 100.0},
        "Sikh_Other_Buddhist": {"Christian_Jain_Other": 100.0},
        "Not_stated": {"Other_Hindu_middle": 100.0},
    }
```

**Suggested skill section:** E (D.2 sub-castes treated as religions) — extend to handle case where Hindu row has DROPPED rather than RELABELED sub-castes.

## New pattern: Muslim-majority AC needs explicit `Muslim` row distribution across multiple Muslim sub-caste leaves

**Symptom:** AC 064's caste axis has 4 Muslim sub-caste leaves (Sheikh / Ansari-Jolaha / Syed-Pathan-Mughal / OBC-Muslim-other). Auto-builder collapses Muslim into a single lexical leaf (the first axis leaf with "muslim" in its name, e.g. `Muslim_other_OBC_Muslim`), distributing 100% of Muslim mass to that one leaf. Result: 42% population shows up as `Muslim_other_OBC_Muslim` (target 6.5%), and the other 3 Muslim leaves are empty.

**Cause:** `_build_caste_given_religion` in `build_ac_verifier_configs.py` uses `next((c for c in axis_leaves if "muslim" in c.lower()), "Muslim")` — picks first Muslim leaf only.

**Fix:** In `<NN>_curate.py`, declare the Muslim sub-caste shares (sum 100) directly, e.g.:

```python
MUSLIM_SUBCASTE_SHARES = {
    "Muslim_Sheikh":              48.0,
    "Muslim_Ansari_Jolaha":       30.0,
    "Muslim_Syed_Pathan_Mughal":   8.0,
    "Muslim_other_OBC_Muslim":    14.0,
}
# in patch_joints:
if j["name"] == "caste_given_religion":
    j["table"]["Muslim"] = dict(MUSLIM_SUBCASTE_SHARES)
```

**Suggested skill section:** NEW — Muslim-majority ACs with fine-grained Muslim sub-caste structure (Murshidabad / Malda / N24P border belt). Generalize: any AC where the religion has K>1 sub-caste leaves needs a per-AC distribution declaration.

## New pattern: `religion_given_gp` parent uses different prefix scheme than `caste_given_gp`

**Symptom:** After applying `GP_PARENT_RENAMES` for AC 064 ({Murshidabad_Muni → U1_Murshidabad_municipality, ...}), the `religion_given_gp` joint's `U3_CDB_rural` parent value didn't get renamed and was reported as a dropped parent value — observed Muslim share fell ~10pp below target.

**Cause:** Auto-builder uses the raw CSV column header as the joint parent key. Two different CSVs (`064_joint_gp_religion.csv` vs `064_joint_gp_caste.csv`) used different prefix conventions: `U3_CDB_rural` vs `CDB_rural`. The axis leaf is `U3_Murshidabad_Jiaganj_CDB_rural`. So both parent forms must be aliased.

**Fix:** Include both forms in the GP parent rename map:

```python
GP_PARENT_RENAMES = {
    "Murshidabad_Muni":      "U1_Murshidabad_municipality",
    "Jiaganj_Azimganj_Muni": "U2_Jiaganj_Azimganj_municipality",
    "CDB_rural":             "U3_Murshidabad_Jiaganj_CDB_rural",
    "U3_CDB_rural":          "U3_Murshidabad_Jiaganj_CDB_rural",
}
```

**Suggested skill section:** A — extend with example of "two CSVs use different prefix schemes for the same gp leaf".

## Small note: `caste_given_gp` is redundant in DAG but high-chisq

The DAG samples religion ← gp, then caste ← religion (via `caste_given_religion`). So `caste_given_gp` is verifier-only. But its chisq stays ~50-90 even in a well-tuned run because the implicit P(caste|gp) from chained sampling = Σ_religion P(caste|religion)·P(religion|gp) doesn't exactly equal the directly-quoted joint values in `caste_given_gp`. Marking it `verify_condition: workers` doesn't help since it's all-population. Setting `use: "verifier_only"` plus a tighter or matched joint table is the right answer; for v0 we accept the residual.

**Suggested skill section:** D / NEW — note that joints used only as verifier targets (not in DAG) often run higher cell-z than DAG-driven joints; consider lowering their tier weight or rebuilding from chained P(.) for v1.
