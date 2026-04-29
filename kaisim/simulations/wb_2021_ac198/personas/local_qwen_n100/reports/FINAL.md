# Verifier report (n=100)

- composite chi-square: **625.86** (max allowed: 800.0)
- within tolerance: **False**
- max axis |z|: 3.27  · max joint cell |z|: 3.55  · aggregate vote max |z|: 1.88
- max axis gap: 15.0 pp  · max joint cell gap: 100.0 pp  · aggregate max gap: 9.33 pp
- cell tolerance: |z| ≤ 2.5

## Axes (sorted by max |z|)
| axis | tier | max |z| | max_gap_pp | chisq_sum | n_out |
|---|---|---|---|---|---|
| caste | E | 3.27 | 15.00 | 19.6 | 1 |
| occupation | E | 3.20 | 13.06 | 26.4 | 1 |
| gender | E | 2.22 | 11.11 | 9.9 | 0 |
| migration | D | 2.04 | 4.00 | 7.7 | 0 |
| gp_location | E | 2.02 | 9.90 | 7.4 | 0 |
| economic_status | E | 2.00 | 8.00 | 7.6 | 0 |
| education | E | 1.97 | 5.50 | 10.7 | 0 |
| religion | E | 1.84 | 6.22 | 7.0 | 0 |
| asset_media | C | 1.84 | 7.00 | 12.6 | 0 |
| amenities | C | 1.84 | 9.00 | 10.0 | 0 |
| age_cohort | E | 1.73 | 5.77 | 7.0 | 0 |
| class_of_worker | E | 1.44 | 10.27 | 5.5 | 0 |
| mother_tongue | E | 1.36 | 3.50 | 5.2 | 0 |
| workforce_status | E | 1.28 | 6.00 | 4.2 | 0 |
| marital_status | E | 1.14 | 5.00 | 3.9 | 0 |
| household_composition | E | 0.86 | 4.00 | 1.7 | 0 |
| obc_subgroup | D | 0.00 | 0.00 | 0.0 | 0 |

## Top 10 category gaps (by |z|)
| axis | category | target | observed | gap_pp | z |
|---|---|---|---|---|---|
| caste | OBC_Hindu | 30.0 | 45.0 | +15.00 | +3.27 |
| occupation | Services | 8.0 | 20.41 | +12.41 | +3.20 |
| gender | Male | 50.89 | 62.0 | +11.11 | +2.22 |
| gender | Female | 49.11 | 38.0 | -11.11 | -2.22 |
| migration | Bangladesh_origin | 4.0 | 0.0 | -4.00 | -2.04 |
| gp_location | Tarakeswar_CDB | 59.9 | 50.0 | -9.90 | -2.02 |
| economic_status | BPL_household | 20.0 | 28.0 | +8.00 | +2.00 |
| education | Graduate | 8.5 | 14.0 | +5.50 | +1.97 |
| occupation | Agricultural_labourer | 40.0 | 53.06 | +13.06 | +1.87 |
| religion | Hindu | 86.78 | 93.0 | +6.22 | +1.84 |

## Joints (sorted by max cell |z|)
| joint | tier | max |z| | max_cell_gap_pp | chisq_sum | n_out | skipped |
|---|---|---|---|---|---|---|
| asset_given_gp | C | 3.55 | 22.00 | 27.2 | 1 |  |
| amenities_given_gp | C | 3.45 | 26.94 | 22.2 | 1 |  |
| vote_given_caste | C | 3.40 | 55.00 | 42.5 | 1 |  |
| education_given_caste | E | 2.85 | 37.64 | 44.5 | 2 |  |
| caste_given_religion | E | 2.82 | 100.00 | 16.3 | 1 |  |
| caste_given_gp | D | 2.74 | 24.68 | 43.5 | 3 |  |
| religion_given_gp | A | 2.49 | 11.06 | 15.6 | 0 |  |
| vote_given_religion | E | 2.36 | 51.60 | 14.6 | 0 |  |
| vote_given_gender | C | 2.27 | 18.42 | 12.0 | 0 |  |
| migration_given_religion | E | 2.21 | 90.00 | 8.3 | 0 |  |
| asset_given_religion | E | 1.94 | 92.00 | 8.4 | 0 |  |
| lang_given_religion | E | 1.37 | 90.00 | 6.1 | 0 |  |
| education_given_age_gender | E | 0.00 | 17.00 | 0.0 | 0 |  |
| married_given_age_gender | E (widows concentrate here) | 0.00 | 93.00 | 0.0 | 0 |  |

## Aggregate vote share
### vote_2019_LS_share (tier A)  max |z| = 1.88
| bucket | target | observed | gap_pp | z | in_tol |
|---|---|---|---|---|---|
| AITC | 44.67 | 54.0 | +9.33 | +1.88 | True |
| BJP | 42.47 | 40.0 | -2.47 | -0.50 | True |
| INC | 1.71 | 3.0 | +1.29 | +1.00 | True |


## Partial-coverage telemetry

All joints fully covered.

### Skipped aggregate buckets
| aggregate | bucket | reason |
|---|---|---|
| vote_2019_LS_share | CPI | vote_values=['CPI'] not present in sampled population (field=vote_2019_LS) |
| vote_2019_LS_share | NOTA | vote_values=['NOTA'] not present in sampled population (field=vote_2019_LS) |
| vote_2019_LS_share | BSP | vote_values=['BSP'] not present in sampled population (field=vote_2019_LS) |
| vote_2019_LS_share | RaJSP | vote_values=['RaJSP'] not present in sampled population (field=vote_2019_LS) |
| vote_2019_LS_share | SUCI | vote_values=['SUCI'] not present in sampled population (field=vote_2019_LS) |
| vote_2019_LS_share | BNARP | vote_values=['BNARP'] not present in sampled population (field=vote_2019_LS) |
| vote_2019_LS_share | IND | vote_values=['IND'] not present in sampled population (field=vote_2019_LS) |