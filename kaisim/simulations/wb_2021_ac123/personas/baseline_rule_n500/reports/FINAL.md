# Verifier report (n=500)

- composite chi-square: **642.54** (max allowed: 800.0)
- within tolerance: **False**
- max axis |z|: 3.28  · max joint cell |z|: 4.7  · aggregate vote max |z|: 2.58
- max axis gap: 6.6 pp  · max joint cell gap: 100.0 pp  · aggregate max gap: 5.63 pp
- cell tolerance: |z| ≤ 2.5

## Axes (sorted by max |z|)
| axis | tier | max |z| | max_gap_pp | chisq_sum | n_out |
|---|---|---|---|---|---|
| education | E | 3.28 | 4.40 | 24.4 | 1 |
| workforce_status | E | 3.13 | 6.60 | 24.6 | 2 |
| marital_status | E | 2.34 | 4.60 | 14.3 | 0 |
| religion | A/E | 2.26 | 3.25 | 12.1 | 0 |
| occupation | E | 2.24 | 3.72 | 19.9 | 0 |
| age_cohort | E | 2.11 | 3.23 | 10.9 | 0 |
| amenities | C | 1.88 | 4.00 | 6.5 | 0 |
| gp_location | E | 1.84 | 4.10 | 6.8 | 0 |
| economic_status | E | 1.73 | 3.20 | 4.1 | 0 |
| caste | E | 1.63 | 3.25 | 7.3 | 0 |
| asset_media | C | 1.60 | 1.40 | 4.4 | 0 |
| class_of_worker | E | 1.59 | 5.29 | 5.8 | 0 |
| migration | D | 1.35 | 2.40 | 4.6 | 0 |
| household_composition | E | 1.32 | 1.40 | 2.1 | 0 |
| gender | A/E | 1.27 | 2.84 | 3.2 | 0 |
| mother_tongue | E | 1.00 | 0.30 | 1.8 | 0 |
| aila_displacement_status | D | 0.00 | 0.00 | 0.0 | 0 |
| bheri_economy_dependent | E | 0.00 | 0.00 | 0.0 | 0 |

## Top 10 category gaps (by |z|)
| axis | category | target | observed | gap_pp | z |
|---|---|---|---|---|---|
| education | Higher_Secondary | 9.0 | 4.8 | -4.20 | -3.28 |
| workforce_status | Student | 10.0 | 5.8 | -4.20 | -3.13 |
| workforce_status | Non_worker | 42.0 | 48.6 | +6.60 | +2.99 |
| education | Middle | 20.0 | 24.4 | +4.40 | +2.46 |
| marital_status | Never_married | 26.0 | 30.6 | +4.60 | +2.34 |
| religion | Other | 0.08 | 0.4 | +0.32 | +2.26 |
| marital_status | Separated_divorced | 1.0 | 0.0 | -1.00 | -2.25 |
| occupation | Trade_retail | 6.0 | 9.71 | +3.71 | +2.24 |
| age_cohort | 28_32 | 13.57 | 16.8 | +3.23 | +2.11 |
| education | Illiterate | 25.0 | 21.2 | -3.80 | -1.96 |

## Joints (sorted by max cell |z|)
| joint | tier | max |z| | max_cell_gap_pp | chisq_sum | n_out | skipped |
|---|---|---|---|---|---|---|
| workforce_given_education | E | 4.70 | 20.00 | 75.9 | 3 |  |
| caste_given_gp | A/E | 3.31 | 6.53 | 36.2 | 1 |  |
| vote_given_gender | C | 3.16 | 9.54 | 33.0 | 2 |  |
| asset_given_occupation | D | 3.01 | 40.00 | 28.5 | 1 |  |
| education_given_caste | E | 2.98 | 33.00 | 69.4 | 2 |  |
| vote_given_caste | C | 2.24 | 20.00 | 29.8 | 0 |  |
| religion_given_gp | A | 2.24 | 6.53 | 11.5 | 0 |  |
| amenities_given_gp | C | 2.14 | 6.61 | 14.5 | 0 |  |
| vote_given_religion | E | 2.02 | 30.00 | 15.0 | 0 |  |
| migration_given_religion | E | 1.98 | 85.00 | 9.5 | 0 |  |
| asset_given_religion | E | 1.81 | 85.00 | 6.6 | 0 |  |
| caste_given_religion | E | 1.72 | 100.00 | 3.7 | 0 |  |
| asset_given_gp | C | 0.98 | 2.49 | 1.4 | 0 |  |
| lang_given_religion | E | 0.87 | 95.00 | 2.9 | 0 |  |
| education_given_age_gender | E | 0.00 | 10.00 | 0.0 | 0 |  |
| married_given_age_gender | E (widows concentrate here) | 0.00 | 79.98 | 0.0 | 0 |  |

## Aggregate vote share
### vote_2019_LS_share (tier None)  max |z| = 2.58
| bucket | target | observed | gap_pp | z | in_tol |
|---|---|---|---|---|---|
| AITC | 52.46 | 54.6 | +2.14 | +0.96 | True |
| BJP | 38.83 | 33.2 | -5.63 | -2.58 | False |
| CPI | 2.81 | 3.6 | +0.79 | +1.07 | True |
| INC | 1.43 | 2.2 | +0.77 | +1.45 | True |


## Partial-coverage telemetry

All joints fully covered.

### Skipped aggregate buckets
| aggregate | bucket | reason |
|---|---|---|
| vote_2019_LS_share | Others | vote_values=['Others'] not present in sampled population (field=vote_2019_LS) |