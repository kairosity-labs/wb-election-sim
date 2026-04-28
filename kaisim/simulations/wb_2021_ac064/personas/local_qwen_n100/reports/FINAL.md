# Verifier report (n=100)

- composite chi-square: **671.05** (max allowed: 800.0)
- within tolerance: **False**
- max axis |z|: 2.85  · max joint cell |z|: 3.83  · aggregate vote max |z|: 1.3
- max axis gap: 10.0 pp  · max joint cell gap: 100.0 pp  · aggregate max gap: 4.99 pp
- cell tolerance: |z| ≤ 2.5

## Axes (sorted by max |z|)
| axis | tier | max |z| | max_gap_pp | chisq_sum | n_out |
|---|---|---|---|---|---|
| marital_status | E | 2.85 | 7.50 | 12.3 | 1 |
| workforce_status | E | 2.67 | 8.00 | 17.3 | 1 |
| age_cohort | E | 2.41 | 5.77 | 11.0 | 0 |
| caste | E | 2.23 | 5.50 | 19.1 | 0 |
| amenities | C | 2.03 | 10.00 | 12.2 | 0 |
| education | E | 1.96 | 7.00 | 10.9 | 0 |
| mother_tongue | A | 1.90 | 3.50 | 7.2 | 0 |
| occupation | E | 1.90 | 9.59 | 18.2 | 0 |
| gender | E | 1.70 | 8.50 | 5.8 | 0 |
| gp_location | D | 1.62 | 6.10 | 4.4 | 0 |
| migration | D | 1.60 | 2.50 | 5.5 | 0 |
| class_of_worker | E | 1.55 | 9.31 | 5.0 | 0 |
| economic_status | E | 1.53 | 7.00 | 5.6 | 0 |
| household_composition | E | 1.47 | 4.00 | 2.7 | 0 |
| asset_media | C | 1.22 | 6.00 | 5.1 | 0 |
| religion | D | 0.95 | 1.50 | 1.6 | 0 |
| muslim_subcaste | D | 0.00 | 0.00 | 0.0 | 0 |

## Top 10 category gaps (by |z|)
| axis | category | target | observed | gap_pp | z |
|---|---|---|---|---|---|
| marital_status | Widowed | 7.5 | 15.0 | +7.50 | +2.85 |
| workforce_status | Marginal_worker | 10.0 | 18.0 | +8.00 | +2.67 |
| workforce_status | Unemployed | 9.0 | 2.0 | -7.00 | -2.45 |
| age_cohort | 63_67 | 3.55 | 8.0 | +4.45 | +2.41 |
| caste | Muslim_other_OBC_Muslim | 6.5 | 1.0 | -5.50 | -2.23 |
| amenities | LPG_clean_cooking_fuel | 42.0 | 32.0 | -10.00 | -2.03 |
| caste | UC_bhadralok | 5.5 | 10.0 | +4.50 | +1.97 |
| education | Graduate | 7.0 | 12.0 | +5.00 | +1.96 |
| mother_tongue | Bengali | 96.5 | 100.0 | +3.50 | +1.90 |
| occupation | Agricultural_labourer | 18.0 | 27.59 | +9.59 | +1.90 |

## Joints (sorted by max cell |z|)
| joint | tier | max |z| | max_cell_gap_pp | chisq_sum | n_out | skipped |
|---|---|---|---|---|---|---|
| amenities_given_gp | C | 3.83 | 16.18 | 31.0 | 1 |  |
| vote_given_caste | E | 3.62 | 45.00 | 40.7 | 1 |  |
| asset_given_gp | C | 3.31 | 27.11 | 42.4 | 2 |  |
| caste_given_gp | A (SC/ST tier A); E (internal Hindu split) | 3.14 | 19.03 | 51.4 | 2 |  |
| vote_given_religion | E | 3.11 | 45.00 | 20.1 | 1 |  |
| education_given_caste | E | 2.95 | 35.00 | 65.1 | 4 |  |
| workforce_given_education | E | 2.67 | 33.33 | 23.8 | 1 |  |
| asset_given_religion | E | 2.58 | 98.00 | 22.7 | 1 |  |
| migration_given_religion | E | 2.48 | 80.00 | 17.6 | 0 |  |
| caste_given_religion | E | 2.17 | 100.00 | 18.5 | 0 |  |
| vote_given_gender | C | 1.87 | 11.71 | 6.8 | 0 |  |
| asset_given_occupation | D | 1.60 | 78.00 | 18.6 | 0 |  |
| religion_given_gp | A | 1.45 | 14.38 | 6.4 | 0 |  |
| lang_given_religion | E | 1.41 | 90.00 | 7.5 | 0 |  |
| education_given_age_gender | E | 0.00 | 16.00 | 0.0 | 0 |  |
| married_given_age_gender | E (widows concentrate here) | 0.00 | 93.00 | 0.0 | 0 |  |

## Aggregate vote share
### vote_2019_LS_share (tier None)  max |z| = 1.30
| bucket | target | observed | gap_pp | z | in_tol |
|---|---|---|---|---|---|
| BJP | 37.1 | 35.0 | -2.10 | -0.43 | True |
| AITC | 35.54 | 36.0 | +0.46 | +0.10 | True |
| INC | 18.01 | 23.0 | +4.99 | +1.30 | True |
| CPI | 5.87 | 6.0 | +0.13 | +0.06 | True |


## Partial-coverage telemetry

All joints fully covered.

### Skipped aggregate buckets
| aggregate | bucket | reason |
|---|---|---|
| vote_2019_LS_share | IND | vote_values=['IND'] not present in sampled population (field=vote_2019_LS) |
| vote_2019_LS_share | JeSM | vote_values=['JeSM'] not present in sampled population (field=vote_2019_LS) |
| vote_2019_LS_share | SUCI | vote_values=['SUCI'] not present in sampled population (field=vote_2019_LS) |
| vote_2019_LS_share | BSP | vote_values=['BSP'] not present in sampled population (field=vote_2019_LS) |
| vote_2019_LS_share | IND | vote_values=['IND'] not present in sampled population (field=vote_2019_LS) |
| vote_2019_LS_share | IND | vote_values=['IND'] not present in sampled population (field=vote_2019_LS) |
| vote_2019_LS_share | BMUP | vote_values=['BMUP'] not present in sampled population (field=vote_2019_LS) |
| vote_2019_LS_share | NOTA | vote_values=['NOTA'] not present in sampled population (field=vote_2019_LS) |