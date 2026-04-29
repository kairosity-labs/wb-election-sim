# Verifier report (n=100)

- composite chi-square: **437.01** (max allowed: 800.0)
- within tolerance: **False**
- max axis |z|: 2.32  · max joint cell |z|: 4.06  · aggregate vote max |z|: 0.55
- max axis gap: 11.0 pp  · max joint cell gap: 100.0 pp  · aggregate max gap: 2.37 pp
- cell tolerance: |z| ≤ 2.5

## Axes (sorted by max |z|)
| axis | tier | max |z| | max_gap_pp | chisq_sum | n_out |
|---|---|---|---|---|---|
| religion | E | 2.32 | 11.00 | 11.4 | 0 |
| mother_tongue | A | 2.10 | 6.00 | 8.6 | 0 |
| education | E | 1.97 | 5.00 | 8.7 | 0 |
| class_of_worker | E | 1.93 | 5.64 | 6.0 | 0 |
| migration | D | 1.85 | 8.00 | 9.9 | 0 |
| workforce_status | E | 1.84 | 8.00 | 13.0 | 0 |
| age_cohort | E | 1.81 | 3.24 | 5.5 | 0 |
| marital_status | E | 1.75 | 5.00 | 5.2 | 0 |
| caste | D | 1.63 | 8.00 | 6.1 | 0 |
| asset_media | D | 1.53 | 5.00 | 6.6 | 0 |
| occupation | A | 1.53 | 4.00 | 4.8 | 0 |
| household_composition | E | 1.53 | 7.00 | 4.5 | 0 |
| gp_location | E | 1.33 | 3.20 | 3.5 | 0 |
| amenities | D | 1.25 | 5.00 | 4.0 | 0 |
| economic_status | E | 0.71 | 2.00 | 0.8 | 0 |
| gender | E | 0.41 | 2.03 | 0.3 | 0 |
| garden_status | E | 0.00 | 0.00 | 0.0 | 0 |

## Top 10 category gaps (by |z|)
| axis | category | target | observed | gap_pp | z |
|---|---|---|---|---|---|
| religion | Hindu | 66.0 | 77.0 | +11.00 | +2.32 |
| mother_tongue | Other | 9.0 | 3.0 | -6.00 | -2.10 |
| education | Graduate | 5.5 | 10.0 | +4.50 | +1.97 |
| class_of_worker | Employer | 1.0 | 3.57 | +2.57 | +1.93 |
| migration | Jharkhand_Chhattisgarh_Odisha_origin | 25.0 | 17.0 | -8.00 | -1.85 |
| workforce_status | Unemployed | 8.0 | 3.0 | -5.00 | -1.84 |
| age_cohort | 63_67 | 2.94 | 6.0 | +3.06 | +1.81 |
| religion | Sarna_Tribal_ORP | 3.0 | 0.0 | -3.00 | -1.76 |
| marital_status | Widowed | 9.0 | 14.0 | +5.00 | +1.75 |
| workforce_status | Main_worker_tea_garden_wage_labor | 34.0 | 42.0 | +8.00 | +1.69 |

## Joints (sorted by max cell |z|)
| joint | tier | max |z| | max_cell_gap_pp | chisq_sum | n_out | skipped |
|---|---|---|---|---|---|---|
| vote_given_caste | D | 4.06 | 35.33 | 60.6 | 1 |  |
| education_given_caste | E | 2.59 | 32.00 | 55.3 | 1 |  |
| religion_given_gp | E | 2.45 | 26.83 | 16.4 | 0 |  |
| lang_given_religion | E | 2.42 | 60.00 | 23.8 | 0 |  |
| asset_given_religion | None | 1.80 | 55.00 | 10.7 | 0 |  |
| vote_given_religion | D | 1.80 | 55.00 | 15.1 | 0 |  |
| caste_given_religion | E | 1.77 | 100.00 | 11.0 | 0 |  |
| asset_given_occupation | D | 1.56 | 55.00 | 8.5 | 0 |  |
| amenities_given_gp | E | 1.55 | 31.67 | 7.8 | 0 |  |
| vote_given_gender | D | 1.50 | 5.19 | 7.0 | 0 |  |
| migration_given_religion | D | 1.46 | 50.00 | 10.4 | 0 |  |
| asset_given_gp | E | 1.36 | 38.00 | 4.2 | 0 |  |
| education_given_age_gender | E | 0.00 | 8.00 | 0.0 | 0 |  |
| married_given_age_gender | E (high widowhood: occupational male premature mortality) | 0.00 | 85.56 | 0.0 | 0 |  |

## Aggregate vote share
### vote_2019_LS_share (tier A)  max |z| = 0.55
| bucket | target | observed | gap_pp | z | in_tol |
|---|---|---|---|---|---|
| BJP | 58.53 | 59.0 | +0.47 | +0.10 | True |
| AITC | 33.63 | 36.0 | +2.37 | +0.50 | True |
| INC | 2.55 | 2.0 | -0.55 | -0.35 | True |
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