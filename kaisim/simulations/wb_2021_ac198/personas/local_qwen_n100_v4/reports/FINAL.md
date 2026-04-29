# Verifier report (n=100)

- composite chi-square: **421.9** (max allowed: 800.0)
- within tolerance: **False**
- max axis |z|: 1.85  · max joint cell |z|: 2.94  · aggregate vote max |z|: 0.87
- max axis gap: 8.0 pp  · max joint cell gap: 100.0 pp  · aggregate max gap: 4.33 pp
- cell tolerance: |z| ≤ 2.5

## Axes (sorted by max |z|)
| axis | tier | max |z| | max_gap_pp | chisq_sum | n_out |
|---|---|---|---|---|---|
| education | E | 1.85 | 6.50 | 9.1 | 0 |
| amenities | C | 1.76 | 5.00 | 7.6 | 0 |
| workforce_status | E | 1.70 | 8.00 | 5.4 | 0 |
| migration | D | 1.53 | 3.00 | 5.5 | 0 |
| economic_status | E | 1.50 | 6.00 | 6.4 | 0 |
| occupation | E | 1.46 | 7.06 | 8.3 | 0 |
| asset_media | C | 1.38 | 3.00 | 4.2 | 0 |
| mother_tongue | E | 1.36 | 2.50 | 5.2 | 0 |
| gp_location | E | 1.20 | 5.90 | 2.7 | 0 |
| marital_status | E | 1.11 | 3.00 | 2.4 | 0 |
| religion | E | 0.95 | 3.22 | 2.2 | 0 |
| caste | E | 0.87 | 4.00 | 2.2 | 0 |
| age_cohort | E | 0.79 | 1.77 | 2.1 | 0 |
| class_of_worker | E | 0.63 | 3.53 | 0.7 | 0 |
| gender | E | 0.62 | 3.11 | 0.8 | 0 |
| household_composition | E | 0.42 | 1.00 | 0.2 | 0 |
| obc_subgroup | D | 0.00 | 0.00 | 0.0 | 0 |

## Top 10 category gaps (by |z|)
| axis | category | target | observed | gap_pp | z |
|---|---|---|---|---|---|
| education | Higher_Secondary | 12.0 | 18.0 | +6.00 | +1.85 |
| amenities | Electricity | 97.0 | 100.0 | +3.00 | +1.76 |
| workforce_status | Main_worker | 33.0 | 41.0 | +8.00 | +1.70 |
| education | Primary | 22.5 | 16.0 | -6.50 | -1.56 |
| migration | Bangladesh_origin | 4.0 | 1.0 | -3.00 | -1.53 |
| economic_status | BPL_household | 20.0 | 26.0 | +6.00 | +1.50 |
| economic_status | Middle | 13.0 | 8.0 | -5.00 | -1.49 |
| occupation | Government_services_teachers | 4.0 | 0.0 | -4.00 | -1.46 |
| asset_media | Four_wheeler | 5.0 | 2.0 | -3.00 | -1.38 |
| amenities | Other_fuel | 5.0 | 2.0 | -3.00 | -1.38 |

## Joints (sorted by max cell |z|)
| joint | tier | max |z| | max_cell_gap_pp | chisq_sum | n_out | skipped |
|---|---|---|---|---|---|---|
| education_given_caste | E | 2.94 | 82.00 | 53.4 | 1 |  |
| amenities_given_gp | C | 2.50 | 20.38 | 20.7 | 0 |  |
| caste_given_gp | D | 2.34 | 20.28 | 21.9 | 0 |  |
| vote_given_caste | C | 2.27 | 45.00 | 34.4 | 0 |  |
| asset_given_gp | C | 2.18 | 24.62 | 25.8 | 0 |  |
| religion_given_gp | A | 2.16 | 9.21 | 11.5 | 0 |  |
| asset_given_religion | E | 1.73 | 92.00 | 5.9 | 0 |  |
| migration_given_religion | E | 1.69 | 40.00 | 6.6 | 0 |  |
| lang_given_religion | E | 1.43 | 90.00 | 7.3 | 0 |  |
| vote_given_religion | E | 1.31 | 58.00 | 10.0 | 0 |  |
| vote_given_gender | C | 1.19 | 8.70 | 6.4 | 0 |  |
| caste_given_religion | E | 0.66 | 100.00 | 1.3 | 0 |  |
| education_given_age_gender | E | 0.00 | 17.00 | 0.0 | 0 |  |
| married_given_age_gender | E (widows concentrate here) | 0.00 | 93.00 | 0.0 | 0 |  |

## Aggregate vote share
### vote_2019_LS_share (tier A)  max |z| = 0.87
| bucket | target | observed | gap_pp | z | in_tol |
|---|---|---|---|---|---|
| AITC | 44.67 | 49.0 | +4.33 | +0.87 | True |
| BJP | 42.47 | 42.0 | -0.47 | -0.10 | True |
| INC | 1.71 | 1.0 | -0.71 | -0.55 | True |


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