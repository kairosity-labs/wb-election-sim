# Verifier report (n=100)

- composite chi-square: **662.48** (max allowed: 800.0)
- within tolerance: **False**
- max axis |z|: 2.64  · max joint cell |z|: 4.42  · aggregate vote max |z|: 1.29
- max axis gap: 10.8 pp  · max joint cell gap: 100.0 pp  · aggregate max gap: 6.38 pp
- cell tolerance: |z| ≤ 2.5

## Axes (sorted by max |z|)
| axis | tier | max |z| | max_gap_pp | chisq_sum | n_out |
|---|---|---|---|---|---|
| caste | E | 2.64 | 6.52 | 19.4 | 1 |
| gp_location | E | 2.19 | 10.80 | 9.8 | 0 |
| religion | E | 2.17 | 7.96 | 10.8 | 0 |
| education | E | 2.11 | 7.00 | 13.2 | 0 |
| amenities | C | 1.96 | 7.00 | 12.0 | 0 |
| class_of_worker | E | 1.83 | 7.92 | 4.4 | 0 |
| asset_media | C | 1.82 | 7.00 | 7.5 | 0 |
| occupation | E | 1.72 | 5.42 | 10.4 | 0 |
| household_composition | E | 1.67 | 5.00 | 4.0 | 0 |
| economic_status | E | 1.62 | 8.00 | 5.9 | 0 |
| migration | D | 1.53 | 4.00 | 3.9 | 0 |
| gender | A | 1.29 | 6.44 | 3.3 | 0 |
| workforce_status | E | 1.27 | 6.00 | 4.7 | 0 |
| age_cohort | E | 1.16 | 4.03 | 4.3 | 0 |
| marital_status | E | 1.14 | 5.00 | 3.9 | 0 |
| mother_tongue | A | 0.90 | 3.50 | 2.7 | 0 |
| tribal_subgroup | D | 0.00 | 0.00 | 0.0 | 0 |

## Top 10 category gaps (by |z|)
| axis | category | target | observed | gap_pp | z |
|---|---|---|---|---|---|
| caste | UC_bhadralok | 6.5 | 13.0 | +6.50 | +2.64 |
| gp_location | U3_Binpur_I_CD_Block | 57.8 | 47.0 | -10.80 | -2.19 |
| religion | Hindu | 84.04 | 92.0 | +7.96 | +2.17 |
| gp_location | U2_Jhargram_CDB_4GP_rural_share | 19.4 | 28.0 | +8.60 | +2.17 |
| education | Graduate | 6.0 | 11.0 | +5.00 | +2.11 |
| education | Secondary | 14.0 | 21.0 | +7.00 | +2.02 |
| amenities | Other_fuel | 7.0 | 2.0 | -5.00 | -1.96 |
| religion | Muslim | 3.44 | 0.0 | -3.44 | -1.89 |
| caste | Muslim | 3.44 | 0.0 | -3.44 | -1.89 |
| caste | OBC | 12.0 | 18.0 | +6.00 | +1.85 |

## Joints (sorted by max cell |z|)
| joint | tier | max |z| | max_cell_gap_pp | chisq_sum | n_out | skipped |
|---|---|---|---|---|---|---|
| caste_given_gp | A/E | 4.42 | 32.90 | 58.4 | 4 |  |
| vote_given_religion | E | 3.65 | 80.00 | 28.9 | 1 |  |
| education_given_caste | E | 3.43 | 26.00 | 44.2 | 2 |  |
| vote_given_caste | C | 3.07 | 80.00 | 33.9 | 2 |  |
| asset_given_gp | C | 2.93 | 21.29 | 17.7 | 1 |  |
| vote_given_gender | D | 2.82 | 21.44 | 25.1 | 1 |  |
| workforce_given_education | E | 2.78 | 60.00 | 27.6 | 1 |  |
| amenities_given_gp | C | 2.77 | 25.00 | 39.4 | 2 |  |
| asset_given_religion | None | 2.64 | 84.00 | 8.4 | 1 |  |
| caste_given_religion | E | 2.45 | 100.00 | 25.5 | 0 |  |
| lang_given_religion | E | 2.16 | 95.50 | 14.7 | 0 |  |
| migration_given_religion | E | 1.81 | 88.00 | 9.7 | 0 |  |
| asset_given_occupation | D | 1.57 | 72.00 | 12.2 | 0 |  |
| religion_given_gp | A | 1.38 | 7.64 | 10.0 | 0 |  |
| education_given_age_gender | E | 0.00 | 10.00 | 0.0 | 0 |  |
| married_given_age_gender | E (widows concentrate here; higher female mortality risk) | 0.00 | 93.00 | 0.0 | 0 |  |

## Aggregate vote share
### vote_2019_LS_share (tier A)  max |z| = 1.29
| bucket | target | observed | gap_pp | z | in_tol |
|---|---|---|---|---|---|
| BJP | 44.49 | 42.0 | -2.49 | -0.50 | True |
| AITC | 43.62 | 50.0 | +6.38 | +1.29 | True |


## Partial-coverage telemetry

All joints fully covered.

### Skipped aggregate buckets
| aggregate | bucket | reason |
|---|---|---|
| vote_2019_LS_share | CPI | vote_values=['CPI'] not present in sampled population (field=vote_2019_LS) |
| vote_2019_LS_share | JKP | vote_values=['JKP'] not present in sampled population (field=vote_2019_LS) |
| vote_2019_LS_share | INC | vote_values=['INC'] not present in sampled population (field=vote_2019_LS) |
| vote_2019_LS_share | BSP | vote_values=['BSP'] not present in sampled population (field=vote_2019_LS) |
| vote_2019_LS_share | AKBJHP | vote_values=['AKBJHP'] not present in sampled population (field=vote_2019_LS) |
| vote_2019_LS_share | SUCI | vote_values=['SUCI'] not present in sampled population (field=vote_2019_LS) |
| vote_2019_LS_share | IND | vote_values=['IND'] not present in sampled population (field=vote_2019_LS) |
| vote_2019_LS_share | NOTA | vote_values=['NOTA'] not present in sampled population (field=vote_2019_LS) |