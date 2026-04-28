# Verifier report (n=100)

- composite chi-square: **1101.3** (max allowed: 800.0)
- within tolerance: **False**
- max axis |z|: 4.66  · max joint cell |z|: 6.32  · aggregate vote max |z|: 0.82
- max axis gap: 23.0 pp  · max joint cell gap: 100.0 pp  · aggregate max gap: 4.08 pp
- cell tolerance: |z| ≤ 2.5

## Axes (sorted by max |z|)
| axis | tier | max |z| | max_gap_pp | chisq_sum | n_out |
|---|---|---|---|---|---|
| workforce_status | E | 4.66 | 23.00 | 36.3 | 2 |
| education | E | 4.59 | 19.00 | 45.3 | 2 |
| asset_media | C | 4.36 | 20.00 | 43.1 | 2 |
| age_cohort | E | 2.64 | 8.84 | 18.1 | 1 |
| class_of_worker | E | 2.60 | 8.67 | 12.1 | 1 |
| marital_status | E | 2.40 | 11.00 | 12.9 | 0 |
| migration | D | 2.40 | 12.00 | 18.0 | 0 |
| household_composition | E | 2.35 | 6.00 | 6.7 | 0 |
| economic_status | E | 2.21 | 7.00 | 10.3 | 0 |
| gp_location | E | 2.00 | 10.00 | 8.0 | 0 |
| mother_tongue | D | 1.96 | 5.00 | 11.7 | 0 |
| caste | D | 1.93 | 5.00 | 16.6 | 0 |
| occupation | E | 1.93 | 9.82 | 16.6 | 0 |
| amenities | C | 1.76 | 4.00 | 10.7 | 0 |
| gender | E | 1.69 | 8.47 | 5.7 | 0 |
| religion | D | 1.35 | 4.00 | 4.5 | 0 |
| linguistic_community | D | 0.00 | 0.00 | 0.0 | 0 |

## Top 10 category gaps (by |z|)
| axis | category | target | observed | gap_pp | z |
|---|---|---|---|---|---|
| workforce_status | Main_worker | 42.0 | 65.0 | +23.00 | +4.66 |
| education | Graduate | 22.0 | 41.0 | +19.00 | +4.59 |
| asset_media | Two_wheeler | 30.0 | 50.0 | +20.00 | +4.36 |
| asset_media | Cable_satellite_TV_subscription | 85.0 | 72.0 | -13.00 | -3.64 |
| education | Illiterate | 7.0 | 0.0 | -7.00 | -2.74 |
| age_cohort | 18_22 | 12.84 | 4.0 | -8.84 | -2.64 |
| class_of_worker | Employer | 8.0 | 16.67 | +8.67 | +2.60 |
| workforce_status | Unemployed | 8.0 | 1.0 | -7.00 | -2.58 |
| marital_status | Never_married | 30.0 | 19.0 | -11.00 | -2.40 |
| migration | Native_Kolkata_born | 50.0 | 62.0 | +12.00 | +2.40 |

## Joints (sorted by max cell |z|)
| joint | tier | max |z| | max_cell_gap_pp | chisq_sum | n_out | skipped |
|---|---|---|---|---|---|---|
| workforce_given_education | E | 6.32 | 55.00 | 64.4 | 1 |  |
| asset_given_occupation | C | 4.68 | 96.00 | 42.8 | 1 |  |
| education_given_caste | E | 3.75 | 59.50 | 111.3 | 6 |  |
| religion_given_gp | D | 3.69 | 24.39 | 45.1 | 4 |  |
| caste_given_gp | D | 3.69 | 21.63 | 52.2 | 3 |  |
| vote_given_caste | C | 3.04 | 42.00 | 81.7 | 5 |  |
| asset_given_gp | NFHS-4/5 WB urban gradient; constituency-adjusted | 2.60 | 19.84 | 17.0 | 1 |  |
| migration_given_religion | E | 2.58 | 65.00 | 29.0 | 1 |  |
| vote_given_religion | E | 2.58 | 50.00 | 22.4 | 1 |  |
| amenities_given_gp | C | 2.16 | 7.00 | 10.3 | 0 |  |
| caste_given_religion | D | 1.97 | 100.00 | 12.3 | 0 |  |
| lang_given_religion | E | 1.69 | 50.00 | 19.7 | 0 |  |
| asset_given_religion | C | 1.63 | 98.00 | 11.6 | 0 |  |
| vote_given_gender | C | 1.36 | 8.00 | 9.3 | 0 |  |
| education_given_age_gender | E | 0.00 | 0.00 | 0.0 | 0 | unknown semantics 'verifier_only' |
| married_given_age_gender | E (widow concentration) | 0.00 | 0.00 | 0.0 | 0 | unknown semantics 'verifier_only' |

## Aggregate vote share
### vote_2019_LS_share (tier A)  max |z| = 0.82
| bucket | target | observed | gap_pp | z | in_tol |
|---|---|---|---|---|---|
| AITC | 44.92 | 49.0 | +4.08 | +0.82 | True |
| BJP | 42.6 | 39.0 | -3.60 | -0.73 | True |
| CPI | 6.39 | 7.0 | +0.61 | +0.25 | True |
| INC | 3.43 | 3.0 | -0.43 | -0.24 | True |
| Others_SHS_7_IND | 1.35 | 1.0 | -0.35 | -0.30 | True |
| NOTA | 1.31 | 1.0 | -0.31 | -0.27 | True |


## Partial-coverage telemetry

All joints fully covered.

All aggregate buckets recoverable.