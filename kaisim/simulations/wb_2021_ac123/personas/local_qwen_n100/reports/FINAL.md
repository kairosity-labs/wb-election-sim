# Verifier report (n=100)

- composite chi-square: **708.09** (max allowed: 800.0)
- within tolerance: **False**
- max axis |z|: 3.14  · max joint cell |z|: 3.82  · aggregate vote max |z|: 2.71
- max axis gap: 17.23 pp  · max joint cell gap: 100.0 pp  · aggregate max gap: 13.54 pp
- cell tolerance: |z| ≤ 2.5

## Axes (sorted by max |z|)
| axis | tier | max |z| | max_gap_pp | chisq_sum | n_out |
|---|---|---|---|---|---|
| occupation | E | 3.14 | 13.08 | 29.6 | 2 |
| caste | E | 2.97 | 14.36 | 23.0 | 2 |
| education | E | 2.85 | 12.00 | 23.5 | 2 |
| household_composition | E | 2.66 | 11.00 | 12.3 | 1 |
| amenities | C | 2.63 | 13.00 | 20.7 | 1 |
| mother_tongue | E | 2.53 | 1.60 | 7.2 | 1 |
| workforce_status | E | 2.53 | 9.00 | 11.6 | 1 |
| class_of_worker | E | 2.49 | 17.23 | 12.6 | 0 |
| economic_status | E | 2.36 | 11.00 | 10.1 | 0 |
| migration | D | 2.17 | 9.00 | 13.3 | 0 |
| asset_media | C | 2.08 | 8.00 | 14.0 | 0 |
| gp_location | E | 1.62 | 8.10 | 5.3 | 0 |
| marital_status | E | 1.47 | 4.00 | 3.4 | 0 |
| age_cohort | E | 1.28 | 3.86 | 6.1 | 0 |
| gender | A/E | 1.21 | 6.04 | 2.9 | 0 |
| religion | A/E | 1.02 | 4.58 | 2.3 | 0 |
| aila_displacement_status | D | 0.00 | 0.00 | 0.0 | 0 |
| bheri_economy_dependent | E | 0.00 | 0.00 | 0.0 | 0 |

## Top 10 category gaps (by |z|)
| axis | category | target | observed | gap_pp | z |
|---|---|---|---|---|---|
| occupation | Fishing_prawn_bheri | 10.0 | 23.08 | +13.08 | +3.14 |
| caste | SC_total | 37.36 | 23.0 | -14.36 | -2.97 |
| education | Graduate | 5.5 | 12.0 | +6.50 | +2.85 |
| occupation | Construction_building_labour | 5.0 | 13.46 | +8.46 | +2.80 |
| education | Illiterate | 25.0 | 13.0 | -12.00 | -2.77 |
| caste | OBC_specific | 5.0 | 11.0 | +6.00 | +2.75 |
| household_composition | Joint_HH | 22.0 | 11.0 | -11.00 | -2.66 |
| amenities | Wood_biomass_fuel | 58.0 | 71.0 | +13.00 | +2.63 |
| mother_tongue | Santali | 0.4 | 2.0 | +1.60 | +2.53 |
| workforce_status | Unemployed | 6.0 | 0.0 | -6.00 | -2.53 |

## Joints (sorted by max cell |z|)
| joint | tier | max |z| | max_cell_gap_pp | chisq_sum | n_out | skipped |
|---|---|---|---|---|---|---|
| caste_given_religion | E | 3.82 | 100.00 | 25.7 | 2 |  |
| education_given_caste | E | 3.81 | 60.00 | 70.3 | 3 |  |
| asset_given_occupation | D | 3.38 | 65.00 | 35.3 | 1 |  |
| asset_given_gp | C | 3.15 | 24.84 | 20.0 | 2 |  |
| vote_given_caste | C | 3.11 | 62.00 | 39.9 | 1 |  |
| vote_given_religion | E | 2.88 | 55.00 | 22.2 | 1 |  |
| vote_given_gender | C | 2.62 | 19.74 | 18.4 | 1 |  |
| caste_given_gp | A/E | 2.58 | 15.96 | 27.6 | 1 |  |
| asset_given_religion | E | 2.55 | 85.00 | 13.1 | 1 |  |
| migration_given_religion | E | 2.54 | 85.00 | 21.0 | 1 |  |
| lang_given_religion | E | 2.43 | 95.00 | 6.8 | 0 |  |
| amenities_given_gp | C | 2.29 | 14.52 | 14.7 | 0 |  |
| workforce_given_education | E | 1.95 | 28.00 | 20.5 | 0 |  |
| religion_given_gp | A | 1.13 | 6.62 | 3.0 | 0 |  |
| education_given_age_gender | E | 0.00 | 10.00 | 0.0 | 0 |  |
| married_given_age_gender | E (widows concentrate here) | 0.00 | 79.98 | 0.0 | 0 |  |

## Aggregate vote share
### vote_2019_LS_share (tier None)  max |z| = 2.71
| bucket | target | observed | gap_pp | z | in_tol |
|---|---|---|---|---|---|
| AITC | 52.46 | 66.0 | +13.54 | +2.71 | False |
| BJP | 38.83 | 32.0 | -6.83 | -1.40 | True |
| CPI | 2.81 | 1.0 | -1.81 | -1.10 | True |
| INC | 1.43 | 1.0 | -0.43 | -0.36 | True |


## Partial-coverage telemetry

All joints fully covered.

### Skipped aggregate buckets
| aggregate | bucket | reason |
|---|---|---|
| vote_2019_LS_share | Others | vote_values=['Others'] not present in sampled population (field=vote_2019_LS) |