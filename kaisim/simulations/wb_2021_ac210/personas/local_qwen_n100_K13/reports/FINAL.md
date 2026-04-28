# Verifier report (n=100)

- composite chi-square: **671.13** (max allowed: 800.0)
- within tolerance: **False**
- max axis |z|: 5.49  · max joint cell |z|: 4.13  · aggregate vote max |z|: 0.39
- max axis gap: 14.0 pp  · max joint cell gap: 100.0 pp  · aggregate max gap: 1.86 pp
- cell tolerance: |z| ≤ 2.5

## Axes (sorted by max |z|)
| axis | tier | max |z| | max_gap_pp | chisq_sum | n_out |
|---|---|---|---|---|---|
| marital_status | E | 5.49 | 14.00 | 35.3 | 1 |
| occupation | E | 3.05 | 9.52 | 24.2 | 2 |
| workforce_status | E | 2.98 | 14.00 | 17.5 | 1 |
| age_cohort | E | 2.95 | 5.48 | 24.7 | 1 |
| household_composition | E | 2.95 | 10.00 | 14.0 | 1 |
| economic_status | E | 2.50 | 10.00 | 12.8 | 0 |
| class_of_worker | E | 2.30 | 4.26 | 6.5 | 0 |
| amenities | C | 2.29 | 9.00 | 19.4 | 0 |
| education | E | 2.27 | 9.00 | 23.8 | 0 |
| gender | A | 2.12 | 10.60 | 9.0 | 0 |
| asset_media | C | 2.08 | 9.00 | 11.1 | 0 |
| caste | E | 1.76 | 4.95 | 6.4 | 0 |
| migration | D | 1.01 | 2.00 | 2.3 | 0 |
| gp_location | A | 0.87 | 4.22 | 1.5 | 0 |
| religion | A/E | 0.79 | 3.49 | 1.3 | 0 |
| mother_tongue | A | 0.16 | 0.05 | 0.1 | 0 |
| land_acq_displaced_2007 | D | 0.00 | 0.00 | 0.0 | 0 |

## Top 10 category gaps (by |z|)
| axis | category | target | observed | gap_pp | z |
|---|---|---|---|---|---|
| marital_status | Widowed | 7.0 | 21.0 | +14.00 | +5.49 |
| occupation | Transport_fishing | 6.0 | 15.52 | +9.52 | +3.05 |
| workforce_status | Main_worker | 33.0 | 47.0 | +14.00 | +2.98 |
| age_cohort | 63_67 | 3.55 | 9.0 | +5.45 | +2.95 |
| household_composition | Extended_multi_generation | 6.0 | 13.0 | +7.00 | +2.95 |
| occupation | Trade_retail | 8.0 | 17.24 | +9.24 | +2.59 |
| economic_status | BPL_household | 20.0 | 30.0 | +10.00 | +2.50 |
| class_of_worker | Employer | 1.5 | 5.17 | +3.67 | +2.30 |
| amenities | Other_fuel | 5.0 | 0.0 | -5.00 | -2.29 |
| education | Higher_Secondary | 12.5 | 20.0 | +7.50 | +2.27 |

## Joints (sorted by max cell |z|)
| joint | tier | max |z| | max_cell_gap_pp | chisq_sum | n_out | skipped |
|---|---|---|---|---|---|---|
| education_given_caste | E | 4.13 | 74.00 | 64.5 | 1 |  |
| workforce_given_education | E | 3.66 | 43.33 | 41.7 | 2 |  |
| vote_given_religion | E | 2.73 | 50.00 | 21.7 | 1 |  |
| caste_given_gp | A/D | 2.71 | 12.12 | 15.9 | 1 |  |
| asset_given_occupation | C | 2.65 | 74.00 | 21.1 | 1 |  |
| amenities_given_gp | C | 2.44 | 14.67 | 21.4 | 0 |  |
| asset_given_religion | E | 2.40 | 92.00 | 11.0 | 0 |  |
| vote_given_caste | C | 2.39 | 59.00 | 26.0 | 0 |  |
| asset_given_gp | C | 2.26 | 13.64 | 13.4 | 0 |  |
| vote_given_gender | C | 2.17 | 15.47 | 15.9 | 0 |  |
| religion_given_gp | A | 2.15 | 12.29 | 9.3 | 0 |  |
| migration_given_religion | E | 1.77 | 60.00 | 5.1 | 0 |  |
| caste_given_religion | E | 1.63 | 100.00 | 4.0 | 0 |  |
| lang_given_religion | A | 0.15 | 0.10 | 0.1 | 0 |  |
| education_given_age_gender | E | 0.00 | 17.00 | 0.0 | 0 |  |
| married_given_age_gender | E (widows concentrate here) | 0.00 | 93.00 | 0.0 | 0 |  |

## Aggregate vote share
### vote_2019_LS_share (tier A)  max |z| = 0.39
| bucket | target | observed | gap_pp | z | in_tol |
|---|---|---|---|---|---|
| AITC | 63.14 | 65.0 | +1.86 | +0.39 | True |
| BJP | 30.09 | 31.0 | +0.91 | +0.20 | True |


## Partial-coverage telemetry

All joints fully covered.

### Skipped aggregate buckets
| aggregate | bucket | reason |
|---|---|---|
| vote_2019_LS_share | CPI | vote_values=['CPI'] not present in sampled population (field=vote_2019_LS) |
| vote_2019_LS_share | INC | vote_values=['INC'] not present in sampled population (field=vote_2019_LS) |
| vote_2019_LS_share | BSP | vote_values=['BSP'] not present in sampled population (field=vote_2019_LS) |
| vote_2019_LS_share | NOTA | vote_values=['NOTA'] not present in sampled population (field=vote_2019_LS) |