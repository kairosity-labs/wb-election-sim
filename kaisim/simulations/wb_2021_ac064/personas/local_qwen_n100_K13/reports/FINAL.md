# Verifier report (n=100)

- composite chi-square: **1127.73** (max allowed: 800.0)
- within tolerance: **False**
- max axis |z|: 4.31  · max joint cell |z|: 6.27  · aggregate vote max |z|: 1.35
- max axis gap: 20.0 pp  · max joint cell gap: 100.0 pp  · aggregate max gap: 6.46 pp
- cell tolerance: |z| ≤ 2.5

## Axes (sorted by max |z|)
| axis | tier | max |z| | max_gap_pp | chisq_sum | n_out |
|---|---|---|---|---|---|
| education | E | 4.31 | 12.00 | 36.6 | 2 |
| amenities | C | 4.12 | 20.00 | 43.4 | 3 |
| gp_location | D | 3.48 | 13.10 | 18.9 | 1 |
| occupation | E | 3.24 | 12.91 | 36.8 | 1 |
| marital_status | E | 3.23 | 8.50 | 13.9 | 1 |
| workforce_status | E | 3.19 | 15.00 | 19.7 | 1 |
| household_composition | E | 2.95 | 8.00 | 11.5 | 1 |
| gender | E | 2.70 | 13.50 | 14.6 | 2 |
| caste | E | 2.64 | 9.00 | 38.4 | 2 |
| migration | D | 2.46 | 8.00 | 12.4 | 0 |
| age_cohort | E | 2.30 | 5.91 | 9.2 | 0 |
| economic_status | E | 2.18 | 10.00 | 12.5 | 0 |
| asset_media | C | 2.11 | 6.00 | 14.7 | 0 |
| class_of_worker | E | 1.69 | 10.00 | 6.7 | 0 |
| religion | D | 1.42 | 7.00 | 4.8 | 0 |
| mother_tongue | A | 1.36 | 2.50 | 4.6 | 0 |
| muslim_subcaste | D | 0.00 | 0.00 | 0.0 | 0 |

## Top 10 category gaps (by |z|)
| axis | category | target | observed | gap_pp | z |
|---|---|---|---|---|---|
| education | Graduate | 7.0 | 18.0 | +11.00 | +4.31 |
| amenities | Improved_sanitation | 62.0 | 42.0 | -20.00 | -4.12 |
| gp_location | U2_Jiaganj_Azimganj_municipality | 17.1 | 4.0 | -13.10 | -3.48 |
| occupation | Government_services_teachers | 6.0 | 16.36 | +10.36 | +3.24 |
| marital_status | Widowed | 7.5 | 16.0 | +8.50 | +3.23 |
| workforce_status | Main_worker | 33.0 | 48.0 | +15.00 | +3.19 |
| household_composition | Extended_multi_generation | 8.0 | 16.0 | +8.00 | +2.95 |
| education | Illiterate | 22.0 | 10.0 | -12.00 | -2.90 |
| gender | Male | 50.5 | 64.0 | +13.50 | +2.70 |
| gender | Female | 49.49 | 36.0 | -13.49 | -2.70 |

## Joints (sorted by max cell |z|)
| joint | tier | max |z| | max_cell_gap_pp | chisq_sum | n_out | skipped |
|---|---|---|---|---|---|---|
| caste_given_gp | A (SC/ST tier A); E (internal Hindu split) | 6.27 | 35.48 | 124.5 | 7 |  |
| workforce_given_education | E | 4.68 | 47.22 | 62.8 | 2 |  |
| amenities_given_gp | C | 4.53 | 30.00 | 64.4 | 3 |  |
| education_given_caste | E | 4.35 | 56.82 | 96.4 | 5 |  |
| caste_given_religion | E | 3.12 | 100.00 | 37.2 | 3 |  |
| asset_given_gp | C | 3.08 | 42.00 | 39.3 | 2 |  |
| vote_given_caste | E | 2.73 | 45.00 | 49.9 | 2 |  |
| asset_given_occupation | D | 2.50 | 80.00 | 31.5 | 1 |  |
| religion_given_gp | A | 2.21 | 19.62 | 12.3 | 0 |  |
| asset_given_religion | E | 2.21 | 98.00 | 12.8 | 0 |  |
| migration_given_religion | E | 1.97 | 80.00 | 13.0 | 0 |  |
| vote_given_gender | C | 1.83 | 14.78 | 11.8 | 0 |  |
| lang_given_religion | E | 1.26 | 90.00 | 4.7 | 0 |  |
| vote_given_religion | E | 1.23 | 45.00 | 6.5 | 0 |  |
| education_given_age_gender | E | 0.00 | 16.00 | 0.0 | 0 |  |
| married_given_age_gender | E (widows concentrate here) | 0.00 | 93.00 | 0.0 | 0 |  |

## Aggregate vote share
### vote_2019_LS_share (tier None)  max |z| = 1.35
| bucket | target | observed | gap_pp | z | in_tol |
|---|---|---|---|---|---|
| BJP | 37.1 | 32.0 | -5.10 | -1.06 | True |
| AITC | 35.54 | 42.0 | +6.46 | +1.35 | True |
| INC | 18.01 | 21.0 | +2.99 | +0.78 | True |
| CPI | 5.87 | 5.0 | -0.87 | -0.37 | True |


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