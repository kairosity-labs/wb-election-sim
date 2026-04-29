# Verifier report (n=100)

- composite chi-square: **514.38** (max allowed: 800.0)
- within tolerance: **False**
- max axis |z|: 2.9  · max joint cell |z|: 3.39  · aggregate vote max |z|: 1.29
- max axis gap: 16.18 pp  · max joint cell gap: 100.0 pp  · aggregate max gap: 6.38 pp
- cell tolerance: |z| ≤ 2.5

## Axes (sorted by max |z|)
| axis | tier | max |z| | max_gap_pp | chisq_sum | n_out |
|---|---|---|---|---|---|
| class_of_worker | E | 2.90 | 16.18 | 13.2 | 1 |
| asset_media | C | 2.08 | 8.00 | 13.2 | 0 |
| gp_location | E | 1.98 | 9.80 | 7.3 | 0 |
| religion | E | 1.90 | 6.96 | 7.4 | 0 |
| workforce_status | E | 1.90 | 9.00 | 6.4 | 0 |
| age_cohort | E | 1.88 | 4.15 | 9.4 | 0 |
| caste | E | 1.83 | 5.00 | 8.9 | 0 |
| education | E | 1.75 | 5.00 | 8.9 | 0 |
| occupation | E | 1.53 | 5.45 | 9.4 | 0 |
| migration | D | 1.53 | 3.00 | 5.4 | 0 |
| economic_status | E | 1.43 | 5.00 | 4.4 | 0 |
| mother_tongue | A | 1.36 | 5.00 | 4.4 | 0 |
| household_composition | E | 1.34 | 6.00 | 3.2 | 0 |
| gender | A | 1.29 | 6.44 | 3.3 | 0 |
| marital_status | E | 1.11 | 5.00 | 3.8 | 0 |
| amenities | C | 1.07 | 5.00 | 3.0 | 0 |
| tribal_subgroup | D | 0.00 | 0.00 | 0.0 | 0 |

## Top 10 category gaps (by |z|)
| axis | category | target | observed | gap_pp | z |
|---|---|---|---|---|---|
| class_of_worker | Family_worker | 22.0 | 38.18 | +16.18 | +2.90 |
| asset_media | Two_wheeler | 18.0 | 26.0 | +8.00 | +2.08 |
| gp_location | U3_Binpur_I_CD_Block | 57.8 | 48.0 | -9.80 | -1.98 |
| religion | Hindu | 84.04 | 91.0 | +6.96 | +1.90 |
| workforce_status | Non_worker | 34.0 | 25.0 | -9.00 | -1.90 |
| age_cohort | 68 | 5.15 | 1.0 | -4.15 | -1.88 |
| asset_media | Radio | 8.0 | 13.0 | +5.00 | +1.84 |
| caste | UC_bhadralok | 6.5 | 11.0 | +4.50 | +1.83 |
| education | Higher_Secondary | 9.0 | 14.0 | +5.00 | +1.75 |
| gp_location | U1_Jhargram_Municipality | 22.8 | 30.0 | +7.20 | +1.72 |

## Joints (sorted by max cell |z|)
| joint | tier | max |z| | max_cell_gap_pp | chisq_sum | n_out | skipped |
|---|---|---|---|---|---|---|
| vote_given_gender | D | 3.39 | 11.63 | 23.1 | 1 |  |
| migration_given_religion | E | 2.92 | 82.00 | 17.4 | 1 |  |
| vote_given_religion | E | 2.62 | 50.00 | 20.9 | 1 |  |
| amenities_given_gp | C | 2.39 | 21.67 | 29.9 | 0 |  |
| vote_given_caste | C | 2.25 | 48.75 | 20.3 | 0 |  |
| caste_given_gp | A/E | 2.24 | 16.99 | 30.6 | 0 |  |
| lang_given_religion | E | 2.20 | 92.00 | 17.8 | 0 |  |
| caste_given_religion | E | 2.16 | 100.00 | 14.5 | 0 |  |
| workforce_given_education | E | 1.93 | 40.00 | 13.7 | 0 |  |
| asset_given_occupation | D | 1.70 | 72.00 | 13.4 | 0 |  |
| religion_given_gp | A | 1.66 | 10.03 | 7.1 | 0 |  |
| education_given_caste | E | 1.60 | 22.00 | 20.3 | 0 |  |
| asset_given_religion | None | 1.58 | 84.00 | 5.8 | 0 |  |
| asset_given_gp | C | 1.39 | 14.55 | 12.3 | 0 |  |
| education_given_age_gender | E | 0.00 | 10.00 | 0.0 | 0 |  |
| married_given_age_gender | E (widows concentrate here; higher female mortality risk) | 0.00 | 93.00 | 0.0 | 0 |  |

## Aggregate vote share
### vote_2019_LS_share (tier A)  max |z| = 1.29
| bucket | target | observed | gap_pp | z | in_tol |
|---|---|---|---|---|---|
| BJP | 44.49 | 39.0 | -5.49 | -1.10 | True |
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