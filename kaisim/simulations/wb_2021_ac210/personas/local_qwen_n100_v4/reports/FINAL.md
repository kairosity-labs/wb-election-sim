# Verifier report (n=100)

- composite chi-square: **494.28** (max allowed: 800.0)
- within tolerance: **False**
- max axis |z|: 3.53  · max joint cell |z|: 3.36  · aggregate vote max |z|: 1.21
- max axis gap: 11.0 pp  · max joint cell gap: 100.0 pp  · aggregate max gap: 5.86 pp
- cell tolerance: |z| ≤ 2.5

## Axes (sorted by max |z|)
| axis | tier | max |z| | max_gap_pp | chisq_sum | n_out |
|---|---|---|---|---|---|
| marital_status | E | 3.53 | 9.00 | 16.3 | 1 |
| economic_status | E | 2.75 | 11.00 | 14.3 | 1 |
| asset_media | C | 2.53 | 8.00 | 12.1 | 1 |
| education | E | 2.45 | 7.00 | 11.1 | 0 |
| amenities | C | 2.24 | 8.00 | 11.0 | 0 |
| household_composition | E | 2.11 | 5.00 | 5.3 | 0 |
| workforce_status | E | 1.84 | 5.00 | 5.3 | 0 |
| migration | D | 1.54 | 5.00 | 5.5 | 0 |
| religion | A/E | 1.47 | 6.49 | 4.4 | 0 |
| occupation | E | 1.38 | 4.00 | 4.6 | 0 |
| caste | E | 1.35 | 6.00 | 4.3 | 0 |
| age_cohort | E | 1.33 | 3.48 | 6.1 | 0 |
| gender | A | 1.32 | 6.60 | 3.5 | 0 |
| class_of_worker | E | 0.84 | 2.43 | 0.9 | 0 |
| gp_location | A | 0.16 | 0.78 | 0.1 | 0 |
| mother_tongue | A | 0.16 | 0.05 | 0.1 | 0 |
| land_acq_displaced_2007 | D | 0.00 | 0.00 | 0.0 | 0 |

## Top 10 category gaps (by |z|)
| axis | category | target | observed | gap_pp | z |
|---|---|---|---|---|---|
| marital_status | Widowed | 7.0 | 16.0 | +9.00 | +3.53 |
| economic_status | BPL_household | 20.0 | 31.0 | +11.00 | +2.75 |
| asset_media | Radio | 6.0 | 12.0 | +6.00 | +2.53 |
| education | Graduate | 9.0 | 16.0 | +7.00 | +2.45 |
| amenities | Improved_drinking_water_source | 85.0 | 93.0 | +8.00 | +2.24 |
| household_composition | Extended_multi_generation | 6.0 | 11.0 | +5.00 | +2.11 |
| amenities | Electricity | 96.0 | 100.0 | +4.00 | +2.04 |
| workforce_status | Marginal_worker | 8.0 | 13.0 | +5.00 | +1.84 |
| education | Postgraduate | 3.0 | 0.0 | -3.00 | -1.76 |
| economic_status | Upper_middle_well_off | 3.0 | 0.0 | -3.00 | -1.76 |

## Joints (sorted by max cell |z|)
| joint | tier | max |z| | max_cell_gap_pp | chisq_sum | n_out | skipped |
|---|---|---|---|---|---|---|
| asset_given_gp | C | 3.36 | 21.03 | 18.1 | 1 |  |
| workforce_given_education | E | 2.94 | 40.00 | 37.7 | 2 |  |
| vote_given_religion | E | 2.78 | 50.00 | 22.5 | 1 |  |
| education_given_caste | E | 2.73 | 49.00 | 34.7 | 1 |  |
| religion_given_gp | A | 2.31 | 12.29 | 10.9 | 0 |  |
| caste_given_gp | A/D | 2.29 | 12.12 | 14.8 | 0 |  |
| amenities_given_gp | C | 2.28 | 16.42 | 20.8 | 0 |  |
| asset_given_religion | E | 2.12 | 92.00 | 10.8 | 0 |  |
| asset_given_occupation | C | 1.80 | 86.00 | 15.5 | 0 |  |
| vote_given_gender | C | 1.67 | 11.95 | 11.6 | 0 |  |
| vote_given_caste | C | 1.61 | 59.00 | 20.2 | 0 |  |
| migration_given_religion | E | 1.46 | 60.00 | 7.4 | 0 |  |
| caste_given_religion | E | 1.20 | 100.00 | 2.8 | 0 |  |
| lang_given_religion | A | 0.14 | 0.10 | 0.1 | 0 |  |
| education_given_age_gender | E | 0.00 | 17.00 | 0.0 | 0 |  |
| married_given_age_gender | E (widows concentrate here) | 0.00 | 93.00 | 0.0 | 0 |  |

## Aggregate vote share
### vote_2019_LS_share (tier A)  max |z| = 1.21
| bucket | target | observed | gap_pp | z | in_tol |
|---|---|---|---|---|---|
| AITC | 63.14 | 69.0 | +5.86 | +1.21 | True |
| BJP | 30.09 | 30.0 | -0.09 | -0.02 | True |
| INC | 0.86 | 1.0 | +0.14 | +0.15 | True |


## Partial-coverage telemetry

All joints fully covered.

### Skipped aggregate buckets
| aggregate | bucket | reason |
|---|---|---|
| vote_2019_LS_share | CPI | vote_values=['CPI'] not present in sampled population (field=vote_2019_LS) |
| vote_2019_LS_share | BSP | vote_values=['BSP'] not present in sampled population (field=vote_2019_LS) |
| vote_2019_LS_share | NOTA | vote_values=['NOTA'] not present in sampled population (field=vote_2019_LS) |