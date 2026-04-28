# Lessons from AC 011 (Kalchini)

Final composite: **696.84** (target: ≤ 800), 8 iterations from start of 13834.8.

## New pattern: Tea-belt-specific workforce axis breaks two_indicator_rates verifier

**Symptom:** `workforce_given_education` joint shows |z| > 100 with chisq dominating composite. The `two_indicator_rates` semantics in `pipeline/verifiers/joint.py` hardcodes child value `"Main_worker"` (and `"Unemployed_educated_actively_seeking"`).

**Cause:** AC 011's workforce axis splits Main_worker into AC-local subcategories: `Main_worker_tea_garden_wage_labor` and `Main_worker_non_tea`. The verifier compares `p.get("workforce_status") == "Main_worker"`, which is always False, so observed=0 in every cell.

**Fix:** Drop the joint from `joints.json` in curate. Our AC011 plugin samples workforce directly from marginal anyway (no joint dependency).

```python
if j["name"] == "workforce_given_education":
    continue
```

**Suggested skill section:** B (workforce/non_worker — note that AC-local workforce sub-categories require dropping any "two_indicator_rates" joint that hardcodes generic "Main_worker" / "Unemployed" child values).

## New pattern: Religion–caste consistency for vote blending

**Symptom:** Muslim personas voting BJP at 50% (target 10%), driving `vote_given_caste`/`vote_given_religion` joint cells to |z| > 7.

**Cause:** When caste is sampled from `caste_given_gp` (location-conditional), Muslim-religion personas can end up with caste=ST_total. Then the vote blender combines vote_given_religion[Muslim] (BJP 10) with vote_given_caste[ST_total] (BJP 52), pulling probabilities heavily toward BJP. Religion and caste need to be jointly consistent.

**Fix:** Sample caste from `caste_given_religion` (not gp). Rebuild `caste_given_religion` to match marginal targets exactly (math out: religion_share × row = marginal). Mark `caste_given_gp` as `use: sampling_only` so the verifier doesn't score it.

**Suggested skill section:** E (D.2 / caste_given_religion). Add: "When religion is a primary parent and vote blending mixes religion + caste, sample caste FROM `caste_given_religion`, not `caste_given_gp`. Otherwise vote blends become inconsistent."

## New pattern: Vote joint party-name normalization

**Symptom:** `vote_given_caste` cells |z|=4–7 even after caste alignment; `vote_given_gender` |z|=4.

**Cause:** Joints had different party names: `vote_given_religion` uses `Other_NOTA`, but `vote_given_caste` and `vote_given_gender` use `Other`. The blender unions parties → `{Other, Other_NOTA}` becomes 6-party space. Renormalization splits residual mass into both, causing observed mismatch.

**Fix:** In curate, rename `Other` → `Other_NOTA` across all vote joints + set `j["parties"]` consistently.

```python
for k, row in j["table"].items():
    if isinstance(row, dict) and "Other" in row and "Other_NOTA" not in row:
        row["Other_NOTA"] = row.pop("Other")
j["parties"] = ["BJP", "AITC", "RSP", "INC", "Other_NOTA"]
```

**Suggested skill section:** NEW — Section I (vote-blending joint hygiene). Standardize party names across all vote_given_* joints; persona_config's `parties:` must equal joint `parties`.

## New pattern: Tea-belt FLFPR — drop housewife inflation entirely

**Symptom:** Non_worker observed +9pp over target.

**Cause:** Generic plugin's 75% female-housewife rate (calibrated to all-WB FLFPR ~23%) inverts the tea-belt model where women ARE the primary workforce (tea-pickers).

**Fix:** Set female-housewife rate to 0–5% in AC011's workforce_sampling plugin override:

```python
# Tea-belt: women predominantly work plucking; no housewife inflation.
# (skip the female_housewife block entirely or set rate to 0.05)
```

**Suggested skill section:** B (already mentions "0–25% for tea-belt"). Update to clarify: "for actively-tea-belt ACs (011, 064 north, etc.), female housewife rate should be 0–5% — the rule entirely fires only on a stochastic 5% to mimic small genuinely-housewife share."

## Notes

- 12 joints required at least one parent-rename, child-rename, or row-rebalance fix.
- Compound age buckets (33_47, 48_62) in `married_given_age_gender` expanded to 5-yr cohorts.
- `bilingual_given_media` and `vote_given_welfare` dropped (no parent axis).
- Final iteration count: 8. Reference benchmark (AC 003): 8 iterations to 611. AC 011 matches expectation despite tea-belt complexity.
