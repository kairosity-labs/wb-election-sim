# Verifier report (n=100)

- composite chi-square: **1409.6** (max allowed: 800.0)
- within tolerance: **False**
- max axis |z|: 6.59  · max joint cell |z|: 5.36  · aggregate vote max |z|: 4.49
- max axis gap: 31.0 pp  · max joint cell gap: 100.0 pp  · aggregate max gap: 22.33 pp
- cell tolerance: |z| ≤ 2.5

## Axes (sorted by max |z|)
| axis | tier | max |z| | max_gap_pp | chisq_sum | n_out |
|---|---|---|---|---|---|
| workforce_status | E | 6.59 | 31.00 | 65.9 | 3 |
| education | E | 5.92 | 16.50 | 64.4 | 4 |
| amenities | C | 4.09 | 15.00 | 31.2 | 1 |
| gp_location | E | 3.85 | 11.70 | 17.9 | 1 |
| migration | D | 3.38 | 13.00 | 22.2 | 1 |
| occupation | E | 3.38 | 11.12 | 22.4 | 1 |
| gender | E | 3.02 | 15.11 | 18.3 | 2 |
| caste | E | 2.84 | 13.00 | 28.4 | 3 |
| economic_status | E | 2.75 | 11.00 | 12.3 | 1 |
| marital_status | E | 2.73 | 13.00 | 14.9 | 2 |
| class_of_worker | E | 2.66 | 16.12 | 13.2 | 1 |
| age_cohort | E | 2.03 | 6.77 | 15.0 | 0 |
| asset_media | C | 1.96 | 7.00 | 15.4 | 0 |
| household_composition | E | 1.82 | 8.00 | 5.7 | 0 |
| mother_tongue | E | 1.60 | 2.50 | 6.3 | 0 |
| religion | E | 1.25 | 4.22 | 3.5 | 0 |
| obc_subgroup | D | 0.00 | 0.00 | 0.0 | 0 |

## Top 10 category gaps (by |z|)
| axis | category | target | observed | gap_pp | z |
|---|---|---|---|---|---|
| workforce_status | Main_worker | 33.0 | 64.0 | +31.00 | +6.59 |
| education | Graduate | 8.5 | 25.0 | +16.50 | +5.92 |
| amenities | Improved_drinking_water_source | 84.0 | 99.0 | +15.00 | +4.09 |
| gp_location | Tarakeswar_Muni | 10.3 | 22.0 | +11.70 | +3.85 |
| occupation | Services | 8.0 | 19.12 | +11.12 | +3.38 |
| migration | Native | 82.0 | 95.0 | +13.00 | +3.38 |
| gender | Male | 50.89 | 66.0 | +15.11 | +3.02 |
| gender | Female | 49.11 | 34.0 | -15.11 | -3.02 |
| workforce_status | Non_worker | 37.0 | 23.0 | -14.00 | -2.90 |
| caste | OBC_Hindu | 30.0 | 43.0 | +13.00 | +2.84 |

## Joints (sorted by max cell |z|)
| joint | tier | max |z| | max_cell_gap_pp | chisq_sum | n_out | skipped |
|---|---|---|---|---|---|---|
| education_given_caste | E | 5.36 | 85.50 | 151.7 | 8 |  |
| caste_given_gp | D | 5.29 | 40.91 | 84.9 | 3 |  |
| vote_given_religion | E | 4.93 | 59.40 | 50.6 | 2 |  |
| vote_given_caste | C | 4.03 | 68.20 | 75.6 | 3 |  |
| vote_given_gender | C | 3.77 | 32.35 | 42.2 | 3 |  |
| migration_given_religion | E | 3.46 | 40.00 | 22.7 | 1 |  |
| caste_given_religion | E | 3.09 | 100.00 | 27.0 | 2 |  |
| amenities_given_gp | C | 3.04 | 28.50 | 41.3 | 3 |  |
| asset_given_gp | C | 3.00 | 28.00 | 44.9 | 4 |  |
| lang_given_religion | E | 2.27 | 90.00 | 10.0 | 0 |  |
| religion_given_gp | A | 2.13 | 12.85 | 18.3 | 0 |  |
| asset_given_religion | E | 2.08 | 92.00 | 14.6 | 0 |  |
| education_given_age_gender | E | 0.00 | 17.00 | 0.0 | 0 |  |
| married_given_age_gender | E (widows concentrate here) | 0.00 | 93.00 | 0.0 | 0 |  |

## Aggregate vote share
### vote_2019_LS_share (tier A)  max |z| = 4.49
| bucket | target | observed | gap_pp | z | in_tol |
|---|---|---|---|---|---|
| AITC | 44.67 | 67.0 | +22.33 | +4.49 | False |
| BJP | 42.47 | 30.0 | -12.47 | -2.52 | False |
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