# Verifier report (n=500)

- composite chi-square: **729.07** (max allowed: 800.0)
- within tolerance: **False**
- max axis |z|: 3.58  · max joint cell |z|: 4.82  · aggregate vote max |z|: 2.68
- max axis gap: 6.8 pp  · max joint cell gap: 93.0 pp  · aggregate max gap: 5.49 pp
- cell tolerance: |z| ≤ 2.5

## Axes (sorted by max |z|)
| axis | tier | max |z| | max_gap_pp | chisq_sum | n_out |
|---|---|---|---|---|---|
| workforce_status | E | 3.58 | 5.20 | 17.1 | 1 |
| marital_status | E | 3.19 | 6.80 | 24.8 | 2 |
| asset_media | C | 2.67 | 2.60 | 11.5 | 1 |
| caste | E | 2.46 | 4.80 | 15.7 | 0 |
| amenities | C | 2.28 | 2.00 | 6.0 | 0 |
| migration | D | 2.25 | 1.20 | 9.0 | 0 |
| occupation | E | 1.80 | 4.56 | 9.9 | 0 |
| class_of_worker | E | 1.76 | 5.02 | 5.2 | 0 |
| education | E | 1.56 | 2.60 | 9.2 | 0 |
| economic_status | E | 1.55 | 3.40 | 5.0 | 0 |
| age_cohort | E | 1.42 | 1.47 | 6.7 | 0 |
| household_composition | E | 0.47 | 1.00 | 0.5 | 0 |
| religion | A/E | 0.36 | 0.31 | 0.2 | 0 |
| mother_tongue | A | 0.35 | 0.05 | 0.3 | 0 |
| gender | A | 0.09 | 0.20 | 0.0 | 0 |
| gp_location | A | 0.01 | 0.02 | 0.0 | 0 |
| land_acq_displaced_2007 | D | 0.00 | 0.00 | 0.0 | 0 |

## Top 10 category gaps (by |z|)
| axis | category | target | observed | gap_pp | z |
|---|---|---|---|---|---|
| workforce_status | Student | 12.0 | 6.8 | -5.20 | -3.58 |
| marital_status | Currently_married | 65.0 | 71.8 | +6.80 | +3.19 |
| marital_status | Widowed | 7.0 | 3.8 | -3.20 | -2.80 |
| asset_media | Four_wheeler | 5.0 | 2.4 | -2.60 | -2.67 |
| caste | Other_Hindu_middle_castes | 21.95 | 17.4 | -4.55 | -2.46 |
| caste | Mahishya | 27.0 | 31.8 | +4.80 | +2.42 |
| amenities | Electricity | 96.0 | 94.0 | -2.00 | -2.28 |
| marital_status | Separated_divorced | 1.0 | 0.0 | -1.00 | -2.25 |
| migration | Out_migrant | 1.0 | 0.0 | -1.00 | -2.25 |
| workforce_status | Non_worker | 37.0 | 41.0 | +4.00 | +1.85 |

## Joints (sorted by max cell |z|)
| joint | tier | max |z| | max_cell_gap_pp | chisq_sum | n_out | skipped |
|---|---|---|---|---|---|---|
| vote_given_gender | C | 4.82 | 8.42 | 64.7 | 4 |  |
| vote_given_caste | C | 4.07 | 47.00 | 59.6 | 3 |  |
| workforce_given_education | E | 3.39 | 18.00 | 49.8 | 4 |  |
| asset_given_occupation | C | 3.18 | 38.33 | 41.1 | 4 |  |
| vote_given_religion | E | 2.81 | 50.00 | 21.5 | 1 |  |
| caste_given_religion | E | 2.68 | 6.74 | 10.4 | 1 |  |
| education_given_caste | E | 2.60 | 80.00 | 59.8 | 1 |  |
| caste_given_gp | A/D | 2.52 | 5.63 | 22.6 | 1 |  |
| asset_given_gp | C | 2.35 | 8.60 | 11.9 | 0 |  |
| migration_given_religion | E | 2.13 | 82.00 | 12.1 | 0 |  |
| asset_given_religion | E | 1.65 | 50.00 | 7.2 | 0 |  |
| amenities_given_gp | C | 1.46 | 2.41 | 4.1 | 0 |  |
| religion_given_gp | A | 0.85 | 1.81 | 2.1 | 0 |  |
| lang_given_religion | A | 0.36 | 0.10 | 0.3 | 0 |  |
| education_given_age_gender | E | 0.00 | 17.00 | 0.0 | 0 |  |
| married_given_age_gender | E (widows concentrate here) | 0.00 | 93.00 | 0.0 | 0 |  |

## Aggregate vote share
### vote_2019_LS_share (tier A)  max |z| = 2.68
| bucket | target | observed | gap_pp | z | in_tol |
|---|---|---|---|---|---|
| AITC | 63.14 | 63.4 | +0.26 | +0.12 | True |
| BJP | 30.09 | 24.6 | -5.49 | -2.68 | False |
| INC | 0.86 | 1.0 | +0.14 | +0.34 | True |


## Partial-coverage telemetry

All joints fully covered.

### Skipped aggregate buckets
| aggregate | bucket | reason |
|---|---|---|
| vote_2019_LS_share | CPI | vote_values=['CPI'] not present in sampled population (field=vote_2019_LS) |
| vote_2019_LS_share | BSP | vote_values=['BSP'] not present in sampled population (field=vote_2019_LS) |
| vote_2019_LS_share | NOTA | vote_values=['NOTA'] not present in sampled population (field=vote_2019_LS) |