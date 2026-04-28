# Verifier report (n=100)

- composite chi-square: **1818.59** (max allowed: 800.0)
- within tolerance: **False**
- max axis |z|: 6.31  · max joint cell |z|: 8.0  · aggregate vote max |z|: 1.08
- max axis gap: 25.0 pp  · max joint cell gap: 100.0 pp  · aggregate max gap: 5.38 pp
- cell tolerance: |z| ≤ 2.5

## Axes (sorted by max |z|)
| axis | tier | max |z| | max_gap_pp | chisq_sum | n_out |
|---|---|---|---|---|---|
| mother_tongue | A | 6.31 | 24.50 | 84.3 | 3 |
| education | E | 5.47 | 15.50 | 68.6 | 4 |
| caste | E | 5.25 | 22.08 | 49.5 | 2 |
| workforce_status | E | 5.24 | 25.00 | 40.6 | 2 |
| occupation | E | 4.65 | 15.19 | 62.8 | 3 |
| asset_media | C | 3.64 | 15.00 | 46.7 | 3 |
| amenities | C | 3.39 | 13.00 | 27.9 | 2 |
| migration | D | 3.27 | 12.00 | 20.9 | 1 |
| gender | A | 2.49 | 12.44 | 12.4 | 0 |
| gp_location | E | 2.39 | 11.80 | 10.9 | 0 |
| age_cohort | E | 1.88 | 4.15 | 7.0 | 0 |
| class_of_worker | E | 1.58 | 5.65 | 5.3 | 0 |
| economic_status | E | 1.43 | 5.00 | 4.9 | 0 |
| marital_status | E | 1.37 | 6.00 | 4.5 | 0 |
| religion | E | 1.34 | 2.96 | 4.4 | 0 |
| household_composition | E | 1.24 | 6.00 | 2.9 | 0 |
| tribal_subgroup | D | 0.00 | 0.00 | 0.0 | 0 |

## Top 10 category gaps (by |z|)
| axis | category | target | observed | gap_pp | z |
|---|---|---|---|---|---|
| mother_tongue | Bengali | 81.5 | 57.0 | -24.50 | -6.31 |
| education | Graduate | 6.0 | 19.0 | +13.00 | +5.47 |
| mother_tongue | Santali | 16.0 | 36.0 | +20.00 | +5.46 |
| caste | ST_total | 22.92 | 45.0 | +22.08 | +5.25 |
| workforce_status | Main_worker | 35.0 | 60.0 | +25.00 | +5.24 |
| occupation | Forest_produce_collection | 8.0 | 23.19 | +15.19 | +4.65 |
| occupation | Government_services_teachers_health_workers | 5.0 | 15.94 | +10.94 | +4.17 |
| mother_tongue | Mundari | 1.5 | 6.0 | +4.50 | +3.70 |
| asset_media | Two_wheeler | 18.0 | 32.0 | +14.00 | +3.64 |
| education | Illiterate | 24.5 | 9.0 | -15.50 | -3.60 |

## Joints (sorted by max cell |z|)
| joint | tier | max |z| | max_cell_gap_pp | chisq_sum | n_out | skipped |
|---|---|---|---|---|---|---|
| lang_given_religion | E | 8.00 | 92.00 | 171.6 | 3 |  |
| caste_given_religion | E | 7.55 | 100.00 | 86.3 | 3 |  |
| workforce_given_education | E | 5.66 | 60.00 | 62.1 | 2 |  |
| caste_given_gp | A/E | 5.26 | 34.89 | 84.4 | 5 |  |
| education_given_caste | E | 5.04 | 78.00 | 114.8 | 6 |  |
| migration_given_religion | E | 4.36 | 95.00 | 48.2 | 2 |  |
| amenities_given_gp | C | 3.70 | 25.48 | 60.1 | 3 |  |
| asset_given_religion | None | 3.62 | 84.00 | 25.0 | 1 |  |
| vote_given_gender | D | 3.29 | 26.97 | 26.6 | 1 |  |
| vote_given_caste | C | 2.86 | 59.25 | 36.2 | 3 |  |
| asset_given_gp | C | 2.83 | 25.00 | 24.8 | 1 |  |
| vote_given_religion | E | 2.78 | 65.00 | 20.7 | 1 |  |
| asset_given_occupation | D | 2.39 | 72.00 | 25.4 | 0 |  |
| religion_given_gp | A | 2.09 | 8.98 | 13.0 | 0 |  |
| education_given_age_gender | E | 0.00 | 10.00 | 0.0 | 0 |  |
| married_given_age_gender | E (widows concentrate here; higher female mortality risk) | 0.00 | 93.00 | 0.0 | 0 |  |

## Aggregate vote share
### vote_2019_LS_share (tier A)  max |z| = 1.08
| bucket | target | observed | gap_pp | z | in_tol |
|---|---|---|---|---|---|
| BJP | 44.49 | 45.0 | +0.51 | +0.10 | True |
| AITC | 43.62 | 49.0 | +5.38 | +1.08 | True |


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