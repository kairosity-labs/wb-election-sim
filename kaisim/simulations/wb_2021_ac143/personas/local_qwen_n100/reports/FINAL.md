# Verifier report (n=100)

- composite chi-square: **404.9** (max allowed: 800.0)
- within tolerance: **False**
- max axis |z|: 2.56  · max joint cell |z|: 2.71  · aggregate vote max |z|: 0.83
- max axis gap: 11.64 pp  · max joint cell gap: 100.0 pp  · aggregate max gap: 4.14 pp
- cell tolerance: |z| ≤ 2.5

## Axes (sorted by max |z|)
| axis | tier | max |z| | max_gap_pp | chisq_sum | n_out |
|---|---|---|---|---|---|
| workforce_status | E | 2.56 | 8.00 | 10.1 | 1 |
| asset_media | C | 1.96 | 7.00 | 11.7 | 0 |
| household_composition | E | 1.82 | 8.00 | 6.1 | 0 |
| economic_status | E | 1.78 | 8.00 | 12.3 | 0 |
| migration | D | 1.75 | 7.00 | 7.5 | 0 |
| age_cohort | E | 1.72 | 5.49 | 9.3 | 0 |
| occupation | E | 1.67 | 8.45 | 10.3 | 0 |
| class_of_worker | E | 1.54 | 11.64 | 5.3 | 0 |
| education | E | 1.54 | 4.50 | 4.6 | 0 |
| amenities | C | 1.40 | 7.00 | 5.0 | 0 |
| religion | B | 1.19 | 5.89 | 3.0 | 0 |
| caste | E | 1.13 | 5.57 | 3.0 | 0 |
| marital_status | E | 1.11 | 3.00 | 2.7 | 0 |
| mother_tongue | E | 0.75 | 0.56 | 1.1 | 0 |
| gp_location | E | 0.52 | 2.60 | 0.5 | 0 |
| gender | E | 0.39 | 1.94 | 0.3 | 0 |
| abhishek_loyalty | E | 0.00 | 0.00 | 0.0 | 0 |

## Top 10 category gaps (by |z|)
| axis | category | target | observed | gap_pp | z |
|---|---|---|---|---|---|
| workforce_status | Student | 11.0 | 19.0 | +8.00 | +2.56 |
| asset_media | Mobile_phone | 85.0 | 92.0 | +7.00 | +1.96 |
| asset_media | Radio | 5.0 | 9.0 | +4.00 | +1.84 |
| household_composition | Joint_HH | 26.0 | 18.0 | -8.00 | -1.82 |
| economic_status | BPL_household | 28.0 | 36.0 | +8.00 | +1.78 |
| economic_status | Upper_middle_well_off | 3.0 | 0.0 | -3.00 | -1.76 |
| migration | Native | 80.0 | 87.0 | +7.00 | +1.75 |
| age_cohort | 33_37 | 11.51 | 17.0 | +5.49 | +1.72 |
| economic_status | Lower_middle | 22.0 | 15.0 | -7.00 | -1.69 |
| household_composition | Nuclear_HH | 65.0 | 73.0 | +8.00 | +1.68 |

## Joints (sorted by max cell |z|)
| joint | tier | max |z| | max_cell_gap_pp | chisq_sum | n_out | skipped |
|---|---|---|---|---|---|---|
| vote_given_religion | — | 2.71 | 45.00 | 20.1 | 1 |  |
| vote_given_caste | C | 2.71 | 15.86 | 29.2 | 1 |  |
| caste_given_gp | B/A | 2.43 | 12.00 | 12.8 | 0 |  |
| amenities_given_gp | C | 2.40 | 21.33 | 29.6 | 0 |  |
| asset_given_gp | C | 2.32 | 20.00 | 15.7 | 0 |  |
| education_given_caste | E | 1.88 | 31.14 | 22.5 | 0 |  |
| migration_given_religion | E | 1.70 | 80.00 | 10.6 | 0 |  |
| asset_given_religion | E | 1.61 | 95.00 | 5.2 | 0 |  |
| workforce_given_education | E | 1.54 | 65.00 | 14.2 | 0 |  |
| asset_given_occupation | D | 1.50 | 88.00 | 14.1 | 0 |  |
| vote_given_gender | C | 1.05 | 4.83 | 4.5 | 0 |  |
| religion_given_gp | A | 0.82 | 7.35 | 3.3 | 0 |  |
| lang_given_religion | E | 0.74 | 92.00 | 1.5 | 0 |  |
| caste_given_religion | E | 0.67 | 100.00 | 0.8 | 0 |  |
| education_given_age_gender | E | 0.00 | 13.00 | 0.0 | 0 |  |
| married_given_age_gender | E (widows concentrate; fishing hazard; higher widow share) | 0.00 | 93.00 | 0.0 | 0 |  |

## Aggregate vote share
### vote_2019_LS_share (tier A)  max |z| = 0.83
| bucket | target | observed | gap_pp | z | in_tol |
|---|---|---|---|---|---|
| AITC | 52.86 | 57.0 | +4.14 | +0.83 | True |
| BJP | 35.69 | 36.0 | +0.31 | +0.06 | True |
| CPI | 8.19 | 6.0 | -2.19 | -0.80 | True |
| INC | 0.99 | 1.0 | +0.01 | +0.01 | True |


## Partial-coverage telemetry

All joints fully covered.

### Skipped aggregate buckets
| aggregate | bucket | reason |
|---|---|---|
| vote_2019_LS_share | Others | vote_values=['Other'] not present in sampled population (field=vote_2019_LS) |