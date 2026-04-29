# Verifier report (n=100)

- composite chi-square: **647.03** (max allowed: 800.0)
- within tolerance: **False**
- max axis |z|: 3.06  · max joint cell |z|: 3.74  · aggregate vote max |z|: 0.55
- max axis gap: 15.0 pp  · max joint cell gap: 100.0 pp  · aggregate max gap: 1.37 pp
- cell tolerance: |z| ≤ 2.5

## Axes (sorted by max |z|)
| axis | tier | max |z| | max_gap_pp | chisq_sum | n_out |
|---|---|---|---|---|---|
| caste | D | 3.06 | 15.00 | 19.0 | 1 |
| education | E | 2.80 | 8.00 | 22.0 | 1 |
| migration | D | 2.55 | 5.00 | 12.0 | 1 |
| religion | E | 2.53 | 12.00 | 13.1 | 1 |
| mother_tongue | A | 2.45 | 9.00 | 22.9 | 0 |
| amenities | D | 2.29 | 10.00 | 12.6 | 0 |
| workforce_status | E | 2.21 | 8.00 | 14.4 | 0 |
| economic_status | E | 2.21 | 11.00 | 13.1 | 0 |
| age_cohort | E | 2.17 | 5.38 | 6.7 | 0 |
| class_of_worker | E | 1.97 | 7.36 | 7.4 | 0 |
| gender | E | 1.81 | 9.03 | 6.5 | 0 |
| marital_status | E | 1.75 | 6.00 | 6.2 | 0 |
| household_composition | E | 1.75 | 8.00 | 5.5 | 0 |
| asset_media | D | 1.53 | 4.00 | 6.2 | 0 |
| gp_location | E | 1.33 | 3.20 | 3.5 | 0 |
| occupation | A | 1.06 | 4.36 | 3.6 | 0 |
| garden_status | E | 0.00 | 0.00 | 0.0 | 0 |

## Top 10 category gaps (by |z|)
| axis | category | target | observed | gap_pp | z |
|---|---|---|---|---|---|
| caste | ST_total | 40.0 | 55.0 | +15.00 | +3.06 |
| education | Higher_Secondary | 9.0 | 17.0 | +8.00 | +2.80 |
| migration | Nepal_origin | 4.0 | 9.0 | +5.00 | +2.55 |
| religion | Hindu | 66.0 | 78.0 | +12.00 | +2.53 |
| mother_tongue | Other | 9.0 | 2.0 | -7.00 | -2.45 |
| mother_tongue | Bengali | 14.0 | 22.0 | +8.00 | +2.31 |
| amenities | Other_fuel | 5.0 | 0.0 | -5.00 | -2.29 |
| workforce_status | Marginal_worker | 8.0 | 2.0 | -6.00 | -2.21 |
| economic_status | BPL_household | 45.0 | 56.0 | +11.00 | +2.21 |
| age_cohort | 53_57 | 6.62 | 12.0 | +5.38 | +2.17 |

## Joints (sorted by max cell |z|)
| joint | tier | max |z| | max_cell_gap_pp | chisq_sum | n_out | skipped |
|---|---|---|---|---|---|---|
| lang_given_religion | E | 3.74 | 60.00 | 51.4 | 2 |  |
| education_given_caste | E | 3.37 | 43.00 | 75.7 | 3 |  |
| asset_given_religion | None | 3.15 | 55.00 | 37.1 | 2 |  |
| vote_given_caste | D | 2.81 | 60.00 | 52.7 | 3 |  |
| religion_given_gp | E | 2.45 | 15.60 | 13.1 | 0 |  |
| caste_given_religion | E | 2.44 | 100.00 | 19.1 | 0 |  |
| amenities_given_gp | E | 2.42 | 31.67 | 13.3 | 0 |  |
| migration_given_religion | D | 2.24 | 50.00 | 13.9 | 0 |  |
| vote_given_religion | D | 1.80 | 55.00 | 10.2 | 0 |  |
| vote_given_gender | D | 1.71 | 13.28 | 15.4 | 0 |  |
| asset_given_occupation | D | 1.64 | 50.00 | 9.3 | 0 |  |
| asset_given_gp | E | 1.19 | 28.67 | 3.7 | 0 |  |
| education_given_age_gender | E | 0.00 | 8.00 | 0.0 | 0 |  |
| married_given_age_gender | E (high widowhood: occupational male premature mortality) | 0.00 | 85.56 | 0.0 | 0 |  |

## Aggregate vote share
### vote_2019_LS_share (tier A)  max |z| = 0.55
| bucket | target | observed | gap_pp | z | in_tol |
|---|---|---|---|---|---|
| BJP | 58.53 | 59.0 | +0.47 | +0.10 | True |
| AITC | 33.63 | 35.0 | +1.37 | +0.29 | True |
| INC | 2.55 | 3.0 | +0.45 | +0.29 | True |
| RSP | 2.2 | 3.0 | +0.80 | +0.55 | True |


## Partial-coverage telemetry

All joints fully covered.

### Skipped aggregate buckets
| aggregate | bucket | reason |
|---|---|---|
| vote_2019_LS_share | IND | vote_values=['IND'] not present in sampled population (field=vote_2019_LS) |
| vote_2019_LS_share | NOTA | vote_values=['NOTA'] not present in sampled population (field=vote_2019_LS) |
| vote_2019_LS_share | SUCI | vote_values=['SUCI'] not present in sampled population (field=vote_2019_LS) |
| vote_2019_LS_share | IND | vote_values=['IND'] not present in sampled population (field=vote_2019_LS) |