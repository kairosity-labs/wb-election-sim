# Lessons from AC 222 (Jhargram)

Calibration: 6398.58 → 776.24 in 4 iterations.

## New pattern: 4th-religion (Sarna_ORP) parent expansion in conditional joints

**Symptom:** FINAL.md showed `caste_given_religion`, `lang_given_religion`,
`vote_given_religion`, `migration_given_religion`, `asset_given_religion`,
`religion_given_gp` all missing rows for `Sarna_ORP` and/or
`Other_not_stated`.  The auto-builder produced `Hindu / Muslim / Other`
parent keys but the religion axis declares 5 categories.  As a result,
personas of religion `Sarna_ORP` got *no* migration/lang/asset/caste
draw and fell back to defaults — and `Other_not_stated` was never
emitted at all (religion_given_gp had no row for it, so the conditional
sampler couldn't produce it).

**Cause:** D.2/D.4 source CSVs only enumerate Hindu/Muslim/Other or
similar 3-religion buckets; the auto-builder's religion-keyed wrapper
doesn't auto-expand to the AC's full religion axis when the AC has 4+
religions.

**Fix:** in `222_curate.py`, completely rebuild every religion-keyed
joint table to enumerate all 5 religion rows (Hindu, Muslim, Sarna_ORP,
Christian, Other_not_stated) using values *re-derived from the marginals*.
For a religion-mass solver:

```python
# caste_given_religion: solve P(X | Hindu) so weighted marginal hits
# target.  E.g. ST_total target 22.92, Sarna→ST 92, Hindu mass 84.04:
#   P(ST | Hindu) = (22.92 − 92*0.109) / 84.04 = 12.4
new_table["Hindu"] = {
    "ST_total": 12.4, "SC_total": 23.2, "UC_bhadralok": 7.7,
    "OBC": 13.6, "Other_Hindu_middle_castes": 43.1,
}
new_table["Sarna_ORP"] = {"ST_total": 92.0, "OBC": 5.0,
                            "Other_Hindu_middle_castes": 3.0}
new_table["Other_not_stated"] = {"Christian_Other": 100.0}
```

For `religion_given_gp`, add an `Other_not_stated` cell to every gp
parent row.  Without this, the religion axis can't hit its
Other_not_stated marginal target since the conditional sampler only
emits children listed in the joint.

**Suggested skill section:** NEW (call it H.1 "Multi-religion ACs:
expand conditional joint rows to cover full axis").

## New pattern: "ever-married" joint values vs "currently-married" axis target

**Symptom:** marital_status.Currently_married observed +11.6pp over
target (76.6 vs 65); Widowed -3.4pp (4.6 vs 8).

**Cause:** the `married_given_age_gender` joint values (e.g. F 33-47=90%,
F 28-32=93%) reflect "ever married" rates from the MD, not "currently
married".  The generic marital_sample plugin treats them as P(currently
married | age, gender), which over-counts because it never deducts
widows from the married pool.

**Fix:** in AC-specific `derived/marital_sampling.py`, treat the joint
as P(ever-married | age, gender) and split into currently-married /
widowed / separated using age-conditional widow probabilities:

```python
p_ever_married = float(row[key]) / 100.0
p_widow_given_ever = 0.65 if (age_60plus and gender == "Female") else ...
p_currently_married = p_ever_married * (1 - p_widow_given_ever - 0.02)
p_widowed = p_ever_married * p_widow_given_ever
# Use cumulative-threshold sampling: r < CM → CM; r < CM+W → W; ...
```

This matches the marginal target *and* keeps Widowed concentrated at
older cohorts.

**Suggested skill section:** G (extend the "broaden marital plugin
widow rates" guidance with the ever→currently split pattern).

## New pattern: Tribal-belt FLFPR is HIGH (not low)

**Symptom:** Non_worker observed +10pp over target (44 vs 34) when
using the generic plugin's 75% female-housewife rate.

**Cause:** the generic plugin's 75% female-housewife inflation was
calibrated to AC 095's WB-rural FLFPR ≈ 23%.  Tribal-belt women lead
forest-produce collection, ag-labour, and MGNREGA — district FLFPR ≈
50%+.  Inflating Female 23-57 to 75% Non_worker drops 10pp into
Non_worker that should have been Marginal_worker.

**Fix:** in AC-specific `derived/workforce_sampling.py`, drop the
female-housewife gate entirely (or set it ≤ 15%).  Combined with
modest senior gates (63+ at 70%, 58-62 at 30%) and a marginal
sampler, Non_worker lands within ~3pp of target.

**Suggested skill section:** B (extend "tune housewife" with the
*tribal-belt* counter-example: drop, don't broaden).

## New pattern: Workforce residual sampler over-emits Non_worker

**Symptom:** even after removing the housewife gate, Non_worker still
+6pp over target.

**Cause:** when `_sample_from_marginal_excluding(rng, axis, exclude=
{"Student"})` strips Student (10%) and renormalizes, Non_worker's
*share within the residual marginal* is 34/(100−10) = 37.8%.  Plus the
seniors gate adds ~5pp Non_worker from age-65+ retired cohort.  Total
≈ 43% Non_worker — observed.

**Fix:** down-weight Non_worker in the residual sampler with an
explicit reweight dict (e.g. {"Non_worker": 0.75}).  This exactly
compensates for the additive senior contribution and brings observed
Non_worker to ~34% target.

```python
def _sample_from_marginal_excluding(rng, axis, exclude, reweights=None):
    cats = [c for c in (axis.categories or []) if c not in exclude]
    weights = []
    for c in cats:
        w = (axis.marginal or {}).get(c, 0.0)
        if reweights and c in reweights:
            w *= reweights[c]
        weights.append(w)
    return rng.choices(cats, weights=weights, k=1)[0]

return _sample_from_marginal_excluding(rng, axis, exclude={"Student"},
                                          reweights={"Non_worker": 0.75})
```

**Suggested skill section:** B / NEW (a sub-section on residual-sampler
reweighting to balance additive rule contributions).

## Confirmed checklist patterns applied

- §A asset-flag renames (TV→Television etc.)
- §A migration child renames (WB_other_dist→WB_other_district etc.)
- §A gp_location parent renames (Jhargram_Muni→U1_Jhargram_Municipality
  including the "_share" suffix on U2)
- §A caste_given_gp child realignment (UC→UC_bhadralok, ST→ST_total,
  SC→SC_total, Other_Hindu→Other_Hindu_middle_castes)
- §B drop child cohorts from age_cohort (15→11 categories)
- §C verify_condition for occupation/class_of_worker
- §D expand 33_47/48_62/63 compound buckets to 5-yr cohorts
- §F drop bilingual_given_media + vote_given_welfare joints
- §H boost Student rate at 18-22 to 95% for educated cohort
