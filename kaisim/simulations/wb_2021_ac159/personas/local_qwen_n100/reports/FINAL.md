# Verifier report (n=100)

- composite chi-square: **910.28** (max allowed: 800.0)
- within tolerance: **False**
- max axis |z|: 7.0  · max joint cell |z|: 6.19  · aggregate vote max |z|: 1.02
- max axis gap: 25.0 pp  · max joint cell gap: 100.0 pp  · aggregate max gap: 5.08 pp
- cell tolerance: |z| ≤ 2.5

## Axes (sorted by max |z|)
| axis | tier | max |z| | max_gap_pp | chisq_sum | n_out |
|---|---|---|---|---|---|
| asset_media | C | 7.00 | 25.00 | 64.5 | 1 |
| caste | D | 3.59 | 8.00 | 27.1 | 1 |
| economic_status | E | 2.90 | 13.00 | 16.1 | 1 |
| household_composition | E | 2.74 | 7.00 | 9.4 | 1 |
| workforce_status | E | 2.43 | 12.00 | 13.5 | 0 |
| class_of_worker | E | 2.29 | 10.18 | 10.1 | 0 |
| migration | D | 2.21 | 8.00 | 15.4 | 0 |
| education | E | 2.17 | 9.00 | 14.5 | 0 |
| age_cohort | E | 2.04 | 6.84 | 16.6 | 0 |
| marital_status | E | 1.96 | 9.00 | 9.8 | 0 |
| religion | D | 1.93 | 8.50 | 7.6 | 0 |
| occupation | E | 1.92 | 10.73 | 13.6 | 0 |
| amenities | C | 1.84 | 5.00 | 10.8 | 0 |
| mother_tongue | D | 1.76 | 4.00 | 7.3 | 0 |
| gender | E | 1.29 | 6.47 | 3.3 | 0 |
| gp_location | E | 0.20 | 1.00 | 0.1 | 0 |
| linguistic_community | D | 0.00 | 0.00 | 0.0 | 0 |

## Top 10 category gaps (by |z|)
| axis | category | target | observed | gap_pp | z |
|---|---|---|---|---|---|
| asset_media | Cable_satellite_TV_subscription | 85.0 | 60.0 | -25.00 | -7.00 |
| caste | Jain | 0.8 | 4.0 | +3.20 | +3.59 |
| economic_status | Lower_middle | 28.0 | 41.0 | +13.00 | +2.90 |
| household_composition | Extended_multi_generation | 7.0 | 14.0 | +7.00 | +2.74 |
| workforce_status | Main_worker | 42.0 | 54.0 | +12.00 | +2.43 |
| class_of_worker | Employer | 8.0 | 16.36 | +8.36 | +2.29 |
| caste | Bengali_OBC_middle_caste_Hindu | 15.0 | 23.0 | +8.00 | +2.24 |
| migration | Other_Indian_state | 8.0 | 2.0 | -6.00 | -2.21 |
| education | Graduate | 22.0 | 31.0 | +9.00 | +2.17 |
| age_cohort | 18_22 | 12.84 | 6.0 | -6.84 | -2.04 |

## Joints (sorted by max cell |z|)
| joint | tier | max |z| | max_cell_gap_pp | chisq_sum | n_out | skipped |
|---|---|---|---|---|---|---|
| workforce_given_education | E | 6.19 | 51.87 | 62.1 | 2 |  |
| asset_given_occupation | C | 4.24 | 96.00 | 38.3 | 1 |  |
| lang_given_religion | E | 3.49 | 55.00 | 24.5 | 1 |  |
| religion_given_gp | D | 3.35 | 19.04 | 24.9 | 2 |  |
| caste_given_gp | D | 3.35 | 18.00 | 44.8 | 3 |  |
| education_given_caste | E | 3.16 | 90.00 | 74.7 | 4 |  |
| vote_given_caste | C | 2.51 | 58.00 | 49.2 | 1 |  |
| asset_given_gp | NFHS-4/5 WB urban gradient; constituency-adjusted | 2.48 | 16.67 | 12.0 | 0 |  |
| migration_given_religion | E | 2.40 | 70.00 | 21.3 | 0 |  |
| vote_given_religion | E | 2.38 | 70.00 | 13.6 | 0 |  |
| caste_given_religion | D | 2.06 | 100.00 | 10.4 | 0 |  |
| amenities_given_gp | C | 1.61 | 5.04 | 8.7 | 0 |  |
| asset_given_religion | C | 1.37 | 100.00 | 9.8 | 0 |  |
| vote_given_gender | C | 1.37 | 9.43 | 8.8 | 0 |  |
| education_given_age_gender | E | 0.00 | 0.00 | 0.0 | 0 | unknown semantics 'verifier_only' |
| married_given_age_gender | E (widow concentration) | 0.00 | 0.00 | 0.0 | 0 | unknown semantics 'verifier_only' |

## Aggregate vote share
### vote_2019_LS_share (tier A)  max |z| = 1.02
| bucket | target | observed | gap_pp | z | in_tol |
|---|---|---|---|---|---|
| AITC | 44.92 | 50.0 | +5.08 | +1.02 | True |
| BJP | 42.6 | 42.0 | -0.60 | -0.12 | True |
| CPI | 6.39 | 4.0 | -2.39 | -0.98 | True |
| INC | 3.43 | 3.0 | -0.43 | -0.24 | True |
| NOTA | 1.31 | 1.0 | -0.31 | -0.27 | True |


## Partial-coverage telemetry

All joints fully covered.

### Skipped aggregate buckets
| aggregate | bucket | reason |
|---|---|---|
| vote_2019_LS_share | Others_SHS_7_IND | vote_values=['Others_SHS_7_IND'] not present in sampled population (field=vote_2019_LS) |