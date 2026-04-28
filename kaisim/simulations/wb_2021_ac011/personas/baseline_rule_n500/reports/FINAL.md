# Verifier report (n=500)

- composite chi-square: **696.84** (max allowed: 800.0)
- within tolerance: **False**
- max axis |z|: 3.01  · max joint cell |z|: 4.2  · aggregate vote max |z|: 2.13
- max axis gap: 5.04 pp  · max joint cell gap: 100.0 pp  · aggregate max gap: 2.33 pp
- cell tolerance: |z| ≤ 2.5

## Axes (sorted by max |z|)
| axis | tier | max |z| | max_gap_pp | chisq_sum | n_out |
|---|---|---|---|---|---|
| workforce_status | E | 3.01 | 3.20 | 15.5 | 1 |
| asset_media | D | 2.51 | 2.80 | 14.1 | 1 |
| mother_tongue | A | 2.25 | 1.00 | 7.9 | 0 |
| age_cohort | E | 2.23 | 3.30 | 14.0 | 0 |
| economic_status | E | 1.92 | 1.60 | 5.7 | 0 |
| marital_status | E | 1.88 | 2.40 | 8.2 | 0 |
| religion | E | 1.84 | 1.40 | 9.9 | 0 |
| occupation | A | 1.80 | 5.04 | 11.6 | 0 |
| migration | D | 1.76 | 3.60 | 13.4 | 0 |
| amenities | D | 1.55 | 3.00 | 6.0 | 0 |
| caste | D | 1.49 | 2.40 | 5.4 | 0 |
| household_composition | E | 1.10 | 2.40 | 2.5 | 0 |
| education | E | 0.94 | 1.20 | 1.4 | 0 |
| gender | E | 0.73 | 1.63 | 1.1 | 0 |
| class_of_worker | E | 0.56 | 1.60 | 0.7 | 0 |
| gp_location | E | 0.56 | 0.60 | 0.6 | 0 |
| garden_status | E | 0.00 | 0.00 | 0.0 | 0 |

## Top 10 category gaps (by |z|)
| axis | category | target | observed | gap_pp | z |
|---|---|---|---|---|---|
| workforce_status | Main_worker_non_tea | 6.0 | 9.2 | +3.20 | +3.01 |
| asset_media | Computer | 4.0 | 1.8 | -2.20 | -2.51 |
| workforce_status | Student | 6.0 | 3.4 | -2.60 | -2.45 |
| mother_tongue | Santali | 1.0 | 0.0 | -1.00 | -2.25 |
| age_cohort | 18_22 | 12.5 | 9.2 | -3.30 | -2.23 |
| asset_media | Two_wheeler | 12.0 | 9.2 | -2.80 | -1.93 |
| economic_status | Upper_middle_well_off | 2.0 | 0.8 | -1.20 | -1.92 |
| marital_status | Widowed | 9.0 | 6.6 | -2.40 | -1.88 |
| religion | Sarna_Tribal_ORP | 3.0 | 4.4 | +1.40 | +1.84 |
| occupation | Tea_garden_plucking_processing | 72.0 | 77.04 | +5.04 | +1.80 |

## Joints (sorted by max cell |z|)
| joint | tier | max |z| | max_cell_gap_pp | chisq_sum | n_out | skipped |
|---|---|---|---|---|---|---|
| asset_given_occupation | D | 4.20 | 55.00 | 65.1 | 4 |  |
| vote_given_caste | D | 3.50 | 24.50 | 68.8 | 1 |  |
| asset_given_religion | None | 3.21 | 8.64 | 23.4 | 1 |  |
| vote_given_gender | D | 2.98 | 7.40 | 25.2 | 1 |  |
| migration_given_religion | D | 2.80 | 14.12 | 30.7 | 2 |  |
| caste_given_religion | E | 2.79 | 100.00 | 14.6 | 1 |  |
| lang_given_religion | E | 2.67 | 10.00 | 43.7 | 1 |  |
| vote_given_religion | D | 2.06 | 16.43 | 35.5 | 0 |  |
| education_given_caste | E | 2.00 | 13.94 | 41.0 | 0 |  |
| religion_given_gp | E | 1.43 | 6.78 | 5.1 | 0 |  |
| amenities_given_gp | E | 1.01 | 7.41 | 3.3 | 0 |  |
| asset_given_gp | E | 0.64 | 2.71 | 0.9 | 0 |  |
| education_given_age_gender | E | 0.00 | 8.00 | 0.0 | 0 |  |
| married_given_age_gender | E (high widowhood: occupational male premature mortality) | 0.00 | 85.56 | 0.0 | 0 |  |

## Aggregate vote share
### vote_2019_LS_share (tier A)  max |z| = 2.13
| bucket | target | observed | gap_pp | z | in_tol |
|---|---|---|---|---|---|
| BJP | 58.53 | 56.2 | -2.33 | -1.06 | True |
| AITC | 33.63 | 32.0 | -1.63 | -0.77 | True |
| INC | 2.55 | 3.4 | +0.85 | +1.21 | True |
| RSP | 2.2 | 3.6 | +1.40 | +2.13 | True |


## Partial-coverage telemetry

All joints fully covered.

### Skipped aggregate buckets
| aggregate | bucket | reason |
|---|---|---|
| vote_2019_LS_share | IND | vote_values=['IND'] not present in sampled population (field=vote_2019_LS) |
| vote_2019_LS_share | NOTA | vote_values=['NOTA'] not present in sampled population (field=vote_2019_LS) |
| vote_2019_LS_share | SUCI | vote_values=['SUCI'] not present in sampled population (field=vote_2019_LS) |
| vote_2019_LS_share | IND | vote_values=['IND'] not present in sampled population (field=vote_2019_LS) |