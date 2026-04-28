# Verifier report (n=500)

- composite chi-square: **651.15** (max allowed: 800.0)
- within tolerance: **False**
- max axis |z|: 2.8  · max joint cell |z|: 4.35  · aggregate vote max |z|: 1.9
- max axis gap: 4.4 pp  · max joint cell gap: 50.0 pp  · aggregate max gap: 4.2 pp
- cell tolerance: |z| ≤ 2.5

## Axes (sorted by max |z|)
| axis | tier | max |z| | max_gap_pp | chisq_sum | n_out |
|---|---|---|---|---|---|
| household_composition | E | 2.80 | 3.60 | 11.4 | 1 |
| marital_status | E | 2.29 | 3.60 | 8.5 | 0 |
| mother_tongue | D | 2.24 | 2.00 | 14.2 | 0 |
| asset_media | C | 2.15 | 4.40 | 15.5 | 0 |
| education | E | 1.88 | 2.40 | 6.3 | 0 |
| amenities | C | 1.84 | 1.40 | 7.8 | 0 |
| class_of_worker | E | 1.78 | 3.46 | 4.4 | 0 |
| age_cohort | E | 1.59 | 1.81 | 7.5 | 0 |
| caste | D | 1.56 | 1.03 | 6.6 | 0 |
| migration | D | 1.43 | 3.20 | 5.0 | 0 |
| economic_status | E | 1.20 | 2.40 | 2.7 | 0 |
| workforce_status | E | 1.19 | 1.60 | 3.7 | 0 |
| religion | D | 1.00 | 1.30 | 2.1 | 0 |
| occupation | E | 0.78 | 1.58 | 2.6 | 0 |
| gp_location | E | 0.45 | 1.00 | 0.4 | 0 |
| gender | E | 0.42 | 0.94 | 0.4 | 0 |
| linguistic_community | D | 0.00 | 0.00 | 0.0 | 0 |

## Top 10 category gaps (by |z|)
| axis | category | target | observed | gap_pp | z |
|---|---|---|---|---|---|
| household_composition | Extended_multi_generation | 7.0 | 10.2 | +3.20 | +2.80 |
| marital_status | Widowed | 7.5 | 4.8 | -2.70 | -2.29 |
| mother_tongue | Odia | 2.0 | 3.4 | +1.40 | +2.24 |
| asset_media | Two_wheeler | 30.0 | 34.4 | +4.40 | +2.15 |
| mother_tongue | Other | 3.0 | 1.4 | -1.60 | -2.10 |
| asset_media | Four_wheeler | 20.0 | 16.4 | -3.60 | -2.01 |
| education | Postgraduate | 9.0 | 6.6 | -2.40 | -1.88 |
| household_composition | Nuclear_HH | 75.0 | 71.4 | -3.60 | -1.86 |
| asset_media | Television | 95.0 | 96.8 | +1.80 | +1.85 |
| amenities | Improved_sanitation | 97.0 | 95.6 | -1.40 | -1.84 |

## Joints (sorted by max cell |z|)
| joint | tier | max |z| | max_cell_gap_pp | chisq_sum | n_out | skipped |
|---|---|---|---|---|---|---|
| vote_given_religion | E | 4.35 | 50.00 | 47.2 | 1 |  |
| workforce_given_education | E | 3.98 | 15.62 | 50.2 | 3 |  |
| lang_given_religion | E | 2.92 | 45.00 | 24.2 | 1 |  |
| vote_given_caste | C | 2.72 | 36.67 | 46.2 | 1 |  |
| asset_given_gp | NFHS-4/5 WB urban gradient; constituency-adjusted | 2.67 | 7.14 | 14.5 | 1 |  |
| caste_given_gp | D | 2.44 | 5.06 | 24.8 | 0 |  |
| education_given_caste | E | 2.33 | 28.00 | 56.8 | 0 |  |
| asset_given_religion | C | 2.18 | 40.00 | 23.7 | 0 |  |
| amenities_given_gp | C | 2.17 | 3.39 | 11.3 | 0 |  |
| asset_given_occupation | C | 2.15 | 17.73 | 21.3 | 0 |  |
| vote_given_gender | C | 1.92 | 4.25 | 11.8 | 0 |  |
| migration_given_religion | E | 1.54 | 35.00 | 13.4 | 0 |  |
| caste_given_religion | D | 1.49 | 1.34 | 4.4 | 0 |  |
| religion_given_gp | D | 1.24 | 1.61 | 4.1 | 0 |  |
| education_given_age_gender | E | 0.00 | 0.00 | 0.0 | 0 | unknown semantics 'verifier_only' |
| married_given_age_gender | E (widow concentration) | 0.00 | 0.00 | 0.0 | 0 | unknown semantics 'verifier_only' |

## Aggregate vote share
### vote_2019_LS_share (tier A)  max |z| = 1.90
| bucket | target | observed | gap_pp | z | in_tol |
|---|---|---|---|---|---|
| AITC | 44.92 | 48.2 | +3.28 | +1.47 | True |
| BJP | 42.6 | 38.4 | -4.20 | -1.90 | True |
| CPI | 6.39 | 7.6 | +1.21 | +1.11 | True |
| INC | 3.43 | 3.6 | +0.17 | +0.21 | True |
| Others_SHS_7_IND | 1.35 | 1.0 | -0.35 | -0.68 | True |
| NOTA | 1.31 | 1.2 | -0.11 | -0.22 | True |


## Partial-coverage telemetry

All joints fully covered.

All aggregate buckets recoverable.