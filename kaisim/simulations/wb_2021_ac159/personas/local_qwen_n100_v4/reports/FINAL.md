# Verifier report (n=100)

- composite chi-square: **629.0** (max allowed: 800.0)
- within tolerance: **False**
- max axis |z|: 2.85  · max joint cell |z|: 5.75  · aggregate vote max |z|: 0.62
- max axis gap: 8.51 pp  · max joint cell gap: 100.0 pp  · aggregate max gap: 3.08 pp
- cell tolerance: |z| ≤ 2.5

## Axes (sorted by max |z|)
| axis | tier | max |z| | max_gap_pp | chisq_sum | n_out |
|---|---|---|---|---|---|
| marital_status | E | 2.85 | 7.50 | 10.4 | 1 |
| class_of_worker | E | 2.05 | 8.27 | 7.5 | 0 |
| religion | D | 1.87 | 8.00 | 6.8 | 0 |
| workforce_status | E | 1.84 | 8.00 | 11.5 | 0 |
| occupation | E | 1.76 | 8.51 | 16.2 | 0 |
| mother_tongue | D | 1.76 | 3.00 | 6.3 | 0 |
| asset_media | C | 1.76 | 8.00 | 12.7 | 0 |
| amenities | C | 1.76 | 3.00 | 8.2 | 0 |
| caste | D | 1.64 | 7.00 | 12.9 | 0 |
| migration | D | 1.60 | 8.00 | 7.7 | 0 |
| education | E | 1.57 | 5.00 | 8.6 | 0 |
| economic_status | E | 1.56 | 7.00 | 8.9 | 0 |
| household_composition | E | 1.30 | 5.00 | 3.3 | 0 |
| age_cohort | E | 1.29 | 4.19 | 7.9 | 0 |
| gp_location | E | 1.20 | 6.00 | 2.9 | 0 |
| gender | E | 0.09 | 0.47 | 0.0 | 0 |
| linguistic_community | D | 0.00 | 0.00 | 0.0 | 0 |

## Top 10 category gaps (by |z|)
| axis | category | target | observed | gap_pp | z |
|---|---|---|---|---|---|
| marital_status | Widowed | 7.5 | 15.0 | +7.50 | +2.85 |
| class_of_worker | Employer | 8.0 | 15.25 | +7.25 | +2.05 |
| religion | Muslim | 24.0 | 16.0 | -8.00 | -1.87 |
| workforce_status | Marginal_worker | 5.0 | 9.0 | +4.00 | +1.84 |
| workforce_status | Unemployed | 8.0 | 3.0 | -5.00 | -1.84 |
| mother_tongue | Other | 3.0 | 0.0 | -3.00 | -1.76 |
| occupation | Domestic_workers | 5.0 | 0.0 | -5.00 | -1.76 |
| asset_media | Mobile_phone | 97.0 | 100.0 | +3.00 | +1.76 |
| amenities | Improved_sanitation | 97.0 | 100.0 | +3.00 | +1.76 |
| religion | Hindu | 73.5 | 81.0 | +7.50 | +1.70 |

## Joints (sorted by max cell |z|)
| joint | tier | max |z| | max_cell_gap_pp | chisq_sum | n_out | skipped |
|---|---|---|---|---|---|---|
| workforce_given_education | E | 5.75 | 52.62 | 52.1 | 1 |  |
| religion_given_gp | D | 3.57 | 18.00 | 25.8 | 2 |  |
| caste_given_gp | D | 3.57 | 18.00 | 39.1 | 1 |  |
| asset_given_gp | NFHS-4/5 WB urban gradient; constituency-adjusted | 3.56 | 25.86 | 22.4 | 1 |  |
| education_given_caste | E | 3.28 | 90.00 | 65.2 | 2 |  |
| vote_given_caste | C | 2.38 | 58.00 | 41.3 | 0 |  |
| vote_given_religion | E | 2.31 | 50.00 | 14.4 | 0 |  |
| asset_given_occupation | C | 2.21 | 80.00 | 15.9 | 0 |  |
| lang_given_religion | E | 1.96 | 50.00 | 15.3 | 0 |  |
| migration_given_religion | E | 1.73 | 65.00 | 15.4 | 0 |  |
| asset_given_religion | C | 1.60 | 98.00 | 13.0 | 0 |  |
| caste_given_religion | D | 1.53 | 100.00 | 6.9 | 0 |  |
| amenities_given_gp | C | 1.49 | 5.00 | 5.7 | 0 |  |
| vote_given_gender | C | 1.34 | 4.92 | 5.6 | 0 |  |
| education_given_age_gender | E | 0.00 | 0.00 | 0.0 | 0 | unknown semantics 'verifier_only' |
| married_given_age_gender | E (widow concentration) | 0.00 | 0.00 | 0.0 | 0 | unknown semantics 'verifier_only' |

## Aggregate vote share
### vote_2019_LS_share (tier A)  max |z| = 0.62
| bucket | target | observed | gap_pp | z | in_tol |
|---|---|---|---|---|---|
| AITC | 44.92 | 48.0 | +3.08 | +0.62 | True |
| BJP | 42.6 | 42.0 | -0.60 | -0.12 | True |
| CPI | 6.39 | 5.0 | -1.39 | -0.57 | True |
| INC | 3.43 | 3.0 | -0.43 | -0.24 | True |
| Others_SHS_7_IND | 1.35 | 1.0 | -0.35 | -0.30 | True |
| NOTA | 1.31 | 1.0 | -0.31 | -0.27 | True |


## Partial-coverage telemetry

All joints fully covered.

All aggregate buckets recoverable.