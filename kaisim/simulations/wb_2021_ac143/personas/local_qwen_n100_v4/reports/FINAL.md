# Verifier report (n=100)

- composite chi-square: **617.05** (max allowed: 800.0)
- within tolerance: **False**
- max axis |z|: 3.32  · max joint cell |z|: 3.29  · aggregate vote max |z|: 1.02
- max axis gap: 14.33 pp  · max joint cell gap: 100.0 pp  · aggregate max gap: 3.14 pp
- cell tolerance: |z| ≤ 2.5

## Axes (sorted by max |z|)
| axis | tier | max |z| | max_gap_pp | chisq_sum | n_out |
|---|---|---|---|---|---|
| marital_status | E | 3.32 | 9.00 | 13.7 | 1 |
| economic_status | E | 2.88 | 10.00 | 18.8 | 1 |
| occupation | E | 2.68 | 14.33 | 28.4 | 1 |
| workforce_status | E | 2.62 | 12.00 | 11.9 | 1 |
| asset_media | C | 2.29 | 6.00 | 15.2 | 0 |
| household_composition | E | 2.10 | 6.00 | 5.7 | 0 |
| religion | B | 2.00 | 9.89 | 8.1 | 0 |
| caste | E | 1.94 | 9.57 | 8.5 | 0 |
| amenities | C | 1.47 | 5.00 | 4.9 | 0 |
| migration | D | 1.43 | 5.00 | 5.7 | 0 |
| education | E | 1.36 | 5.50 | 5.9 | 0 |
| age_cohort | E | 1.25 | 3.67 | 5.0 | 0 |
| gp_location | E | 1.19 | 4.10 | 1.8 | 0 |
| class_of_worker | E | 0.91 | 1.57 | 0.9 | 0 |
| gender | E | 0.79 | 3.94 | 1.2 | 0 |
| mother_tongue | E | 0.75 | 0.56 | 1.1 | 0 |
| abhishek_loyalty | E | 0.00 | 0.00 | 0.0 | 0 |

## Top 10 category gaps (by |z|)
| axis | category | target | observed | gap_pp | z |
|---|---|---|---|---|---|
| marital_status | Widowed | 8.0 | 17.0 | +9.00 | +3.32 |
| economic_status | Middle | 11.0 | 2.0 | -9.00 | -2.88 |
| occupation | Agricultural_labourer | 19.0 | 33.33 | +14.33 | +2.68 |
| workforce_status | Main_worker | 30.0 | 42.0 | +12.00 | +2.62 |
| asset_media | Four_wheeler | 5.0 | 0.0 | -5.00 | -2.29 |
| economic_status | BPL_household | 28.0 | 38.0 | +10.00 | +2.23 |
| asset_media | Computer | 8.0 | 2.0 | -6.00 | -2.21 |
| occupation | Trade_retail | 11.0 | 1.85 | -9.15 | -2.15 |
| household_composition | Extended_multi_generation | 9.0 | 15.0 | +6.00 | +2.10 |
| occupation | Out_migrant | 13.0 | 3.7 | -9.30 | -2.03 |

## Joints (sorted by max cell |z|)
| joint | tier | max |z| | max_cell_gap_pp | chisq_sum | n_out | skipped |
|---|---|---|---|---|---|---|
| religion_given_gp | A | 3.29 | 24.32 | 22.8 | 2 |  |
| workforce_given_education | E | 3.25 | 35.00 | 21.7 | 1 |  |
| caste_given_gp | B/A | 3.22 | 23.77 | 24.5 | 1 |  |
| asset_given_gp | C | 3.04 | 28.89 | 35.4 | 2 |  |
| amenities_given_gp | C | 2.88 | 28.00 | 42.6 | 3 |  |
| vote_given_religion | — | 2.65 | 45.00 | 18.7 | 1 |  |
| vote_given_caste | C | 2.65 | 39.67 | 21.5 | 1 |  |
| education_given_caste | E | 2.12 | 40.67 | 30.3 | 0 |  |
| asset_given_occupation | D | 1.87 | 88.00 | 15.8 | 0 |  |
| asset_given_religion | E | 1.50 | 95.00 | 5.0 | 0 |  |
| migration_given_religion | E | 1.39 | 80.00 | 9.1 | 0 |  |
| caste_given_religion | E | 1.23 | 100.00 | 2.0 | 0 |  |
| vote_given_gender | C | 1.12 | 5.73 | 3.2 | 0 |  |
| lang_given_religion | E | 0.70 | 92.00 | 1.4 | 0 |  |
| education_given_age_gender | E | 0.00 | 13.00 | 0.0 | 0 |  |
| married_given_age_gender | E (widows concentrate; fishing hazard; higher widow share) | 0.00 | 93.00 | 0.0 | 0 |  |

## Aggregate vote share
### vote_2019_LS_share (tier A)  max |z| = 1.02
| bucket | target | observed | gap_pp | z | in_tol |
|---|---|---|---|---|---|
| AITC | 52.86 | 56.0 | +3.14 | +0.63 | True |
| BJP | 35.69 | 36.0 | +0.31 | +0.06 | True |
| CPI | 8.19 | 6.0 | -2.19 | -0.80 | True |
| INC | 0.99 | 2.0 | +1.01 | +1.02 | True |


## Partial-coverage telemetry

All joints fully covered.

### Skipped aggregate buckets
| aggregate | bucket | reason |
|---|---|---|
| vote_2019_LS_share | Others | vote_values=['Other'] not present in sampled population (field=vote_2019_LS) |