# Verifier report (n=100)

- composite chi-square: **396.58** (max allowed: 800.0)
- within tolerance: **False**
- max axis |z|: 2.95  · max joint cell |z|: 3.23  · aggregate vote max |z|: 0.8
- max axis gap: 8.0 pp  · max joint cell gap: 100.0 pp  · aggregate max gap: 3.86 pp
- cell tolerance: |z| ≤ 2.5

## Axes (sorted by max |z|)
| axis | tier | max |z| | max_gap_pp | chisq_sum | n_out |
|---|---|---|---|---|---|
| household_composition | E | 2.95 | 7.00 | 10.1 | 1 |
| asset_media | C | 2.11 | 6.00 | 12.1 | 0 |
| education | E | 2.10 | 6.00 | 9.1 | 0 |
| economic_status | E | 2.00 | 8.00 | 7.8 | 0 |
| marital_status | E | 1.96 | 5.00 | 5.7 | 0 |
| occupation | E | 1.50 | 6.29 | 5.4 | 0 |
| migration | D | 1.43 | 3.00 | 5.3 | 0 |
| caste | E | 1.38 | 5.35 | 5.7 | 0 |
| amenities | C | 1.38 | 4.00 | 4.6 | 0 |
| religion | A/E | 1.24 | 5.49 | 3.2 | 0 |
| class_of_worker | E | 1.21 | 7.71 | 2.3 | 0 |
| age_cohort | E | 1.13 | 3.77 | 4.6 | 0 |
| workforce_status | E | 0.74 | 3.00 | 1.1 | 0 |
| gender | A | 0.52 | 2.60 | 0.5 | 0 |
| mother_tongue | A | 0.16 | 0.05 | 0.1 | 0 |
| gp_location | A | 0.05 | 0.22 | 0.0 | 0 |
| land_acq_displaced_2007 | D | 0.00 | 0.00 | 0.0 | 0 |

## Top 10 category gaps (by |z|)
| axis | category | target | observed | gap_pp | z |
|---|---|---|---|---|---|
| household_composition | Extended_multi_generation | 6.0 | 13.0 | +7.00 | +2.95 |
| asset_media | Radio | 6.0 | 11.0 | +5.00 | +2.11 |
| education | Graduate | 9.0 | 15.0 | +6.00 | +2.10 |
| economic_status | BPL_household | 20.0 | 28.0 | +8.00 | +2.00 |
| marital_status | Widowed | 7.0 | 12.0 | +5.00 | +1.96 |
| occupation | Trade_retail | 8.0 | 14.29 | +6.29 | +1.50 |
| economic_status | Middle | 13.0 | 8.0 | -5.00 | -1.49 |
| migration | Bangladesh_origin | 2.0 | 0.0 | -2.00 | -1.43 |
| caste | Kayastha_Brahmin_UC_bhadralok | 5.0 | 8.0 | +3.00 | +1.38 |
| asset_media | Four_wheeler | 5.0 | 2.0 | -3.00 | -1.38 |

## Joints (sorted by max cell |z|)
| joint | tier | max |z| | max_cell_gap_pp | chisq_sum | n_out | skipped |
|---|---|---|---|---|---|---|
| caste_given_gp | A/D | 3.23 | 23.13 | 29.7 | 1 |  |
| vote_given_religion | E | 2.76 | 50.00 | 21.5 | 1 |  |
| asset_given_gp | C | 2.67 | 16.60 | 15.9 | 1 |  |
| workforce_given_education | E | 2.54 | 40.00 | 24.3 | 1 |  |
| education_given_caste | E | 2.35 | 36.50 | 34.6 | 0 |  |
| religion_given_gp | A | 2.28 | 12.29 | 10.5 | 0 |  |
| asset_given_religion | E | 2.21 | 92.00 | 9.8 | 0 |  |
| asset_given_occupation | C | 1.96 | 35.00 | 16.6 | 0 |  |
| amenities_given_gp | C | 1.86 | 11.19 | 8.7 | 0 |  |
| vote_given_caste | C | 1.61 | 59.00 | 16.0 | 0 |  |
| migration_given_religion | E | 1.42 | 60.00 | 5.0 | 0 |  |
| caste_given_religion | E | 1.27 | 100.00 | 4.1 | 0 |  |
| vote_given_gender | C | 1.19 | 3.00 | 4.8 | 0 |  |
| lang_given_religion | A | 0.14 | 0.10 | 0.1 | 0 |  |
| education_given_age_gender | E | 0.00 | 17.00 | 0.0 | 0 |  |
| married_given_age_gender | E (widows concentrate here) | 0.00 | 93.00 | 0.0 | 0 |  |

## Aggregate vote share
### vote_2019_LS_share (tier A)  max |z| = 0.80
| bucket | target | observed | gap_pp | z | in_tol |
|---|---|---|---|---|---|
| AITC | 63.14 | 67.0 | +3.86 | +0.80 | True |
| BJP | 30.09 | 31.0 | +0.91 | +0.20 | True |
| INC | 0.86 | 1.0 | +0.14 | +0.15 | True |


## Partial-coverage telemetry

All joints fully covered.

### Skipped aggregate buckets
| aggregate | bucket | reason |
|---|---|---|
| vote_2019_LS_share | CPI | vote_values=['CPI'] not present in sampled population (field=vote_2019_LS) |
| vote_2019_LS_share | BSP | vote_values=['BSP'] not present in sampled population (field=vote_2019_LS) |
| vote_2019_LS_share | NOTA | vote_values=['NOTA'] not present in sampled population (field=vote_2019_LS) |