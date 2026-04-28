# Verifier report (n=500)

- composite chi-square: **590.54** (max allowed: 800.0)
- within tolerance: **False**
- max axis |z|: 2.64  · max joint cell |z|: 4.69  · aggregate vote max |z|: 1.15
- max axis gap: 4.32 pp  · max joint cell gap: 95.0 pp  · aggregate max gap: 1.69 pp
- cell tolerance: |z| ≤ 2.5

## Axes (sorted by max |z|)
| axis | tier | max |z| | max_gap_pp | chisq_sum | n_out |
|---|---|---|---|---|---|
| migration | D | 2.64 | 3.20 | 11.9 | 1 |
| marital_status | E | 2.31 | 3.60 | 12.0 | 0 |
| occupation | E | 1.90 | 4.32 | 9.2 | 0 |
| asset_media | C | 1.86 | 3.60 | 10.5 | 0 |
| education | E | 1.83 | 3.30 | 5.9 | 0 |
| amenities | C | 1.65 | 3.40 | 8.0 | 0 |
| religion | B | 1.40 | 3.09 | 5.0 | 0 |
| caste | E | 1.35 | 2.97 | 3.6 | 0 |
| workforce_status | E | 1.29 | 1.80 | 2.6 | 0 |
| class_of_worker | E | 1.09 | 3.07 | 1.8 | 0 |
| age_cohort | E | 1.06 | 1.51 | 3.9 | 0 |
| gp_location | E | 0.87 | 1.90 | 1.5 | 0 |
| economic_status | E | 0.86 | 1.20 | 1.7 | 0 |
| gender | E | 0.66 | 1.47 | 0.9 | 0 |
| mother_tongue | E | 0.42 | 0.10 | 0.4 | 0 |
| household_composition | E | 0.31 | 0.60 | 0.2 | 0 |
| abhishek_loyalty | E | 0.00 | 0.00 | 0.0 | 0 |

## Top 10 category gaps (by |z|)
| axis | category | target | observed | gap_pp | z |
|---|---|---|---|---|---|
| migration | WB_other_district | 6.0 | 8.8 | +2.80 | +2.64 |
| marital_status | Widowed | 8.0 | 5.2 | -2.80 | -2.31 |
| occupation | Out_migrant | 13.0 | 8.68 | -4.32 | -1.90 |
| marital_status | Never_married | 25.0 | 28.6 | +3.60 | +1.86 |
| asset_media | Two_wheeler | 25.0 | 28.6 | +3.60 | +1.86 |
| education | Illiterate | 20.5 | 17.2 | -3.30 | -1.83 |
| occupation | Services | 10.0 | 13.7 | +3.70 | +1.82 |
| asset_media | Computer | 8.0 | 5.8 | -2.20 | -1.81 |
| marital_status | Separated_divorced | 1.0 | 0.2 | -0.80 | -1.80 |
| migration | Native | 80.0 | 76.8 | -3.20 | -1.79 |

## Joints (sorted by max cell |z|)
| joint | tier | max |z| | max_cell_gap_pp | chisq_sum | n_out | skipped |
|---|---|---|---|---|---|---|
| caste_given_gp | B/A | 4.69 | 19.13 | 44.4 | 3 |  |
| vote_given_religion | — | 4.36 | 95.00 | 42.9 | 2 |  |
| asset_given_occupation | D | 3.50 | 36.42 | 53.4 | 2 |  |
| vote_given_caste | C | 3.16 | 13.82 | 27.7 | 1 |  |
| asset_given_gp | C | 2.95 | 10.02 | 32.9 | 2 |  |
| workforce_given_education | E | 2.72 | 45.00 | 38.0 | 2 |  |
| asset_given_religion | E | 2.48 | 90.00 | 17.6 | 0 |  |
| migration_given_religion | E | 2.43 | 80.00 | 24.8 | 0 |  |
| vote_given_gender | C | 2.36 | 7.34 | 18.3 | 0 |  |
| education_given_caste | E | 2.00 | 16.00 | 27.7 | 0 |  |
| amenities_given_gp | C | 1.96 | 7.13 | 7.1 | 0 |  |
| lang_given_religion | E | 0.98 | 92.00 | 2.9 | 0 |  |
| religion_given_gp | A | 0.92 | 3.34 | 3.4 | 0 |  |
| caste_given_religion | E | 0.55 | 0.86 | 0.7 | 0 |  |
| education_given_age_gender | E | 0.00 | 13.00 | 0.0 | 0 |  |
| married_given_age_gender | E (widows concentrate; fishing hazard; higher widow share) | 0.00 | 93.00 | 0.0 | 0 |  |

## Aggregate vote share
### vote_2019_LS_share (tier A)  max |z| = 1.15
| bucket | target | observed | gap_pp | z | in_tol |
|---|---|---|---|---|---|
| AITC | 52.86 | 53.6 | +0.74 | +0.33 | True |
| BJP | 35.69 | 34.0 | -1.69 | -0.79 | True |
| CPI | 8.19 | 9.6 | +1.41 | +1.15 | True |
| INC | 0.99 | 1.4 | +0.41 | +0.93 | True |
| Others | 1.21 | 1.4 | +0.19 | +0.39 | True |


## Partial-coverage telemetry

All joints fully covered.

All aggregate buckets recoverable.