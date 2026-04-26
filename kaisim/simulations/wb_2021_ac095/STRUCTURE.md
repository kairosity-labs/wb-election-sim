# Bangaon Uttar (AC 095) — STRUCTURE notes

This document records the design choices that shaped this simulation's
`structures/axes.json` + `structures/joints.json`. Read it alongside
[`build_structures.py`](build_structures.py) (the script that produces the
JSON) and the framework's
[`HOWTO_AXES_AND_JOINTS.md`](../../pipeline/HOWTO_AXES_AND_JOINTS.md).

The numbers cited (e.g. "Hindu 85.45%") are from the calibrated 2019 CSVs
under [`../../data/calibrated_2019/csv/`](../../data/calibrated_2019/csv/).

---

## 1. Axes — what we model

19 axes total: 16 marginal + 1 scalar (household_size_avg) + 2 derived
(welfare_exposure, welfare_dominant).

Special handling per axis:

  - **age_cohort** — filtered to voter ages (18+) and renormalized. Children
    (0-17, ~30% of population) excluded because the workforce / education /
    welfare marginals all use voter-population denominators.
  - **religion** — collapsed from 5 → 3 categories (Hindu / Muslim / Other).
    Christian, Sarna, and minor others sum to ~1% of the AC and have noisy
    joint coverage; collapsing them to "Other" matches the dominant joint
    structure (`joint_gp_religion` only has 3 cells).
  - **caste** — partition over leaves with subgroup roll-up `SC_total`
    (Namasudra + Bagdi + Poundra + Other_SC). Verifier reports both leaves
    and the roll-up.
  - **occupation, class_of_worker** — declared with `verify_condition` so
    the verifier only considers personas whose `workforce_status` ∈
    {Main_worker, Marginal_worker}. The marginal targets are
    worker-conditional in the source data.
  - **welfare_exposure** (derived) — multi-flag exposure to {Krishak_Bandhu,
    Kanyashree, Sabuj_Sathi, Swasthya_Sathi, Khadya_Sathi}. Plugin uses
    occupation/gender/age/economic_status to set each Bernoulli flag.
  - **welfare_dominant** (derived) — single label from welfare_exposure via
    the configured WelfareOverlapReducer. Composite labels (from "mean"
    method) are bucketed as "None" so the joint vote_given_welfare check
    can match a row.

---

## 2. The 4 overlap resolutions

These were judgment calls during structure design. Documented here so a
reader can understand why the joints don't precisely mirror the source CSVs.

### 2.1 Religion ↔ caste partition redundancy

**Problem:** the source `095_marginals.csv` caste rows include "Muslim" and
"Christian + Sarna + Other" — i.e., caste was a *full social-strat
partition* including non-Hindu rows. Religion is also a partition. Sampling
both independently double-counts.

**Resolution:** sample religion first; sample caste from
`caste_given_religion` joint:
  - Hindu → 8 sub-categories (UC_bhadralok, Namasudra_Matua, Bagdi,
    Poundra, Other_SC, ST_total, OBC_specific, Other_Hindu_middle_castes)
    via `joint_religion_caste.csv`
  - Muslim → caste = "Muslim" (single leaf)
  - Other → caste = "Christian_plus_Sarna_plus_Other" (single leaf)

### 2.2 GP-religion 3-cell expansion

**Problem:** `joint_gp_religion.csv` has only 3 columns (Hindu / Muslim /
Other) but the source religion marginal had 5 (Hindu / Muslim / Christian /
Sarna_ORP / Other_minor).

**Resolution:** religion axis collapsed to 3 categories matching the joint
columns (see §1). This makes the joint a 1:1 conditional with no expansion
needed.

### 2.3 GP-caste edge: dropped from sampling DAG

**Problem:** `joint_gp_caste.csv` collapses "OBC + Other Hindu" into a
single bucket that doesn't disaggregate cleanly to the leaf castes. Using
this joint for sampling caste would lose information.

**Resolution:** the DAG samples caste via gp → religion → caste (chain), not
gp → caste. The `joint_gp_caste.csv` joint is marked `use:
"verifier_only"` — kept as a sanity check but ignored by the sampler.

### 2.4 age × gender × education only constrains Grad+ share

**Problem:** `joint_age_gender_education.csv` only provides P(Grad+ | age,
gender), not a full P(education | age, gender). The full education
distribution comes from `joint_caste_education.csv`.

**Resolution (v1):** sample education from caste→education conditional
only. The age×gender Grad+ joint is marked `use: "sampling_only"` and not
verified. v2 should add an IPF reweight pass to match the Grad+ marginal
within (age, gender) cells.

---

## 3. Welfare exposure derivation (calibrated to end-2019)

`derived/welfare_exposure.py:derive` applies these heuristic rules. Take-up
rates were **audited and re-calibrated** against end-2019 sources after the
v0 implementation overstated coverage and squeezed the "None" pool (the
unenrolled segment) to <2%, breaking aggregate vote calibration.

### Calibrated rates and sources

  - **Krishak_Bandhu**: if Cultivator → **10%**; if Agricultural_labourer
    → **5%**; else 0%.
    *Source: ~3 lakh enrolled at the Dec 2019 Duare Sarkar camps out of
    ~70 lakh WB farmers (~5%); scheme launched only Jan 2019 so end-2019
    take-up is still nascent.*
    [Krishi Jagran — 3 lakh enrolled by Dec 2019](https://krishijagran.com/news/krishak-bandhu-system-3-lakhs-farmers-enroll-in-west-bengal-important-details-inside/) ·
    [Wikipedia — Krishak Bandhu Scheme](https://en.wikipedia.org/wiki/Krishak_Bandhu_Scheme)

  - **Kanyashree**: girl-student-in-HH proxy. If gender=Female and
    age_cohort ∈ {15_17, 18_22} → **40%**; else 0%.
    *Source: ~18 lakh K1 + 3.5 lakh K2 active beneficiaries against ~50
    lakh eligible 13-18 girl population ≈ 43% of eligible.*
    [Wikipedia — Kanyashree Prakalpa](https://en.wikipedia.org/wiki/Kanyashree_Prakalpa)

  - **Sabuj_Sathi**: similar life-stage proxy. Female + 15_17/18_22 → **30%**.
    *Source: ~1 cr cycles distributed cumulatively by 2019; one-time
    distribution to Class 9-12 students.*

  - **Swasthya_Sathi** (the v0 bug): tier-skewed by gender + economic_status.
    Female + BPL/APL-low → **45%** (SHG/ASHA networks);
    male + BPL/APL-low → **30%**;
    Lower_middle → **20%**;
    other → **10%**.
    *Source: ~50 lakh families enrolled / 2.5 cr population coverage at
    2019-20 ≈ 28% of WB population. **Universal coverage was only declared
    1 December 2020.** Pre-2020 enrollment skewed to SHG members,
    ASHA/ICDS workers, civic volunteers.*
    [Down to Earth — universal coverage Dec 2020](https://www.downtoearth.org.in/health/swasthya-sathi-will-now-include-bengal-s-entire-population-mamata-74458) ·
    [Tata AIG — Swasthya Sathi summary](https://www.tataaig.com/knowledge-center/health-insurance/swasthya-sathi-scheme) ·
    [HDFC ERGO — Swasthya Sathi guide](https://www.hdfcergo.com/blogs/health-insurance/swasthya-sathi-scheme-west-bengal)

  - **Khadya_Sathi**: BPL/APL-low → **95%**; Lower_middle → **80%**;
    Middle → **40%**; Upper_middle → **10%**.
    *Source: ~7.49 cr / 10 cr WB population ≈ 80% overall coverage; steeply
    income-tilted (NFSA + RKSY income criteria).*
    [WBPDS official help portal](https://wbpds.gov.in/help.aspx)

### Why the "None" pool matters

The vote_welfare_2019 conditional table (`095_vote_welfare_2019.csv`)
includes a **"No state-scheme exposure"** row at tier C (CSDS-Lokniti
sourced) showing BJP 55% / AITC 30% — the unenrolled segment is the most
BJP-leaning bloc. If the persona generator squeezes this pool to near-zero
(as v0 did), the aggregate population can't reach the BJP=48% calibration
target.

After re-calibration: ~14% of personas now have **zero** scheme flags,
pulling the aggregate BJP share toward target. The implied target from the
calibration is closer to 20-25%; getting there requires further tuning of
Khadya_Sathi (currently still hits 83%) and Swasthya_Sathi for upper-middle
households.

### Dominant-label methods

`derived/welfare_exposure.py:dominant` collapses the multi-flag dict to a
single label using the configured WelfareOverlapReducer:
  - **precedence** (default): pick first flag from the configured order
    (Krishak_Bandhu > Kanyashree > Sabuj_Sathi > Swasthya_Sathi > Khadya_Sathi).
  - **mean**: returns a composite label "+a+b+c"; mapped to "None" for the
    joint verifier (this is a known fidelity loss; see verifier docs).
  - **dominant**: pick the row with max range across parties.

---

## 4. Vote-prior blending — defaults and rationale

The default config uses **log_odds_mean** with weights:

  - religion = 1.5
  - caste = 1.5
  - gender = 0.7
  - welfare_dominant = 1.0

Reasoning (CSDS-Lokniti tradition for Indian voting analysis):
  - Religion ≈ caste are the strongest predictors in WB
    (Matua/Namasudra is a subset of SC; both effects compound).
  - Welfare exposure is meaningful in WB (state-scheme state) but weaker than
    the identity axes.
  - Gender (3-9 pp) is the smallest modulator.

The blender combines per-table P(party | axis_value) into P(party | persona).
Override these in `persona_configs/<your_config>.yaml` to test alternatives:

```yaml
vote:
  blending:
    method: "naive_bayes"           # or "log_odds_mean"
    inputs:
      - {table: "vote_given_religion", parent: "religion", weight: 2.0}
      - ...
```

---

## 5. Verifier scoring — Pearson chi-square on z-scores

The verifier scores every cell (per-axis row, per-joint cell, per-aggregate
bucket) by a **z-score** = (observed_pct − target_pct) / SE, where SE is
the binomial standard error at that cell's effective n. This is the
principled successor to summing raw pp-gaps: small-n cells (large SE → small
z) automatically contribute less, so sampling noise on rare buckets no
longer dominates the score.

The composite is a **tier-weighted Pearson chi-square** — sum of (tier_weight
× z²) across all cells.

Defaults in [`persona_configs/baseline_rule.yaml`](persona_configs/baseline_rule.yaml)
and `pipeline/verifiers/composite.py`:

| Threshold                | Default | Meaning                                         |
|--------------------------|---------|-------------------------------------------------|
| `cell_z_max`             | 2.5     | Per-cell tolerance: \|z\| ≤ 2.5 ≈ 99% two-sided CI |
| `composite_chisq_max`    | 800.0   | Whole-population Pearson chi-square ceiling     |

Why 800: under the null hypothesis (population perfectly matches targets,
all gaps are pure sampling noise), each cell's z² has E[z²] = 1, so the
expected unweighted chi-square sum equals the cell count (~324 in the WB
sim). With average tier weight ~1.5 the noise expectation is ~486; 800
leaves ~64% headroom for a few small biases without false alarms.

The threshold is **n-stable**: at n=100 the same biases produce smaller z
(noise dominates), so the score scales naturally with sample size and the
threshold doesn't need to be retuned. Real biases that survive at n=1000
(z>2.5 means the bias is statistically significant given the sample size)
will fail tolerance at any n large enough to detect them — which is exactly
the principled behavior.

### Legacy pp tolerances (reported, not used in score)

The pp-based thresholds remain in the report for human readability but are
not used to compute the composite. They're useful when you want a "what
would a human flag as suspicious" view alongside the statistical view.

### Current baseline status

The baseline rule-based set scores ~1530 chi-square at n=1000 (above the
800 threshold) because:
  - **workforce_status max\|z\|=10.1** — Non_worker over by 11.6pp; the
    rule plugin's housewife/retiree heuristics over-fire. Fix: tune the
    `derived/workforce_sampling.py` rule probabilities or add a global
    rejection-resampling pass.
  - **marital_status max\|z\|=5.9** — Currently_married inflated, Widowed
    under-modelled. Fix: bump the widow-rate rules in
    `derived/marital_sampling.py` for 60+ female.
  - **asset_given_gp max\|z\|=6.6** — log-odds blend across (gp, religion,
    occupation) systematically biases asset rates within gp groups by a
    few pp. Fix: weight gp higher in the blend or use IPF.
  - **aggregate vote BJP max\|z\|=5.3** — BJP undershoots by 4pp. Fix:
    bump `vote_given_caste` / `vote_given_religion` weights in
    persona_config, or tune the welfare overlap method.

Small-n cells (Other religion n=12, OBC caste n=13) that previously
contributed +20pp to the old score now correctly score |z|<2.0 — they're
noise, not bias.

The framework works end-to-end; tightening the chi-square score is a v2
task (better plugin heuristics + IPF reweighting + vote-weight tuning).

---

## 6. Known v1 limitations

  - **No IPF reweighting** of education for age×gender Grad+. The joint
    target is recorded but unused at sample time.
  - **Bilingual axis dropped.** `joint_asset_bilingualism.csv` references a
    derived "media tier" that needed extra plumbing; deferred to v2.
  - **Workforce status heuristics are ad hoc.** Especially Student (under)
    and Non_worker (over). Tune by adjusting the rule probabilities in
    `derived/workforce_sampling.py` or by adding a global rejection-resampling
    pass.
  - **Out-migrant occupation share** is a marginal sample, not modeled as a
    Bernoulli outcome of male + working-age + Matua-belt. Refine when
    Census D-series migration data becomes available.
  - **No narrative.** Rule-based personas have demographics + vote prior but
    no `narrative` field. The LLM sampler (Phase 1.2) fills that in.
