# Verifier report (n=500)

- composite chi-square: **778.48** (max allowed: 800.0)
- within tolerance: **False**
- max axis |z|: 4.56  · max joint cell |z|: 3.61  · aggregate vote max |z|: 1.69
- max axis gap: 8.0 pp  · max joint cell gap: 93.0 pp  · aggregate max gap: 3.73 pp
- cell tolerance: |z| ≤ 2.5

## Axes (sorted by max |z|)
| axis | tier | max |z| | max_gap_pp | chisq_sum | n_out |
|---|---|---|---|---|---|
| mother_tongue | E | 4.56 | 1.70 | 24.8 | 1 |
| economic_status | E | 3.69 | 8.00 | 22.2 | 1 |
| caste | E | 3.24 | 4.60 | 32.5 | 1 |
| education | E | 3.19 | 5.60 | 21.9 | 1 |
| religion | E | 2.60 | 2.34 | 14.0 | 1 |
| occupation | E | 2.43 | 4.29 | 9.7 | 0 |
| marital_status | E | 2.25 | 1.80 | 6.5 | 0 |
| migration | D | 2.25 | 1.80 | 13.4 | 0 |
| household_composition | E | 2.21 | 4.60 | 9.3 | 0 |
| workforce_status | E | 2.14 | 3.00 | 8.0 | 0 |
| gender | E | 1.92 | 4.29 | 7.4 | 0 |
| asset_media | C | 1.81 | 2.80 | 7.8 | 0 |
| age_cohort | E | 1.77 | 2.44 | 8.6 | 0 |
| amenities | C | 1.61 | 3.60 | 7.0 | 0 |
| class_of_worker | E | 0.78 | 2.03 | 1.0 | 0 |
| gp_location | E | 0.39 | 0.80 | 0.3 | 0 |
| obc_subgroup | D | 0.00 | 0.00 | 0.0 | 0 |

## Top 10 category gaps (by |z|)
| axis | category | target | observed | gap_pp | z |
|---|---|---|---|---|---|
| mother_tongue | Other | 0.7 | 2.4 | +1.70 | +4.56 |
| economic_status | Above_Poverty_Line_low_income | 38.0 | 46.0 | +8.00 | +3.69 |
| caste | Christian_Sarna_only_Other | 1.46 | 3.2 | +1.74 | +3.24 |
| education | Secondary | 19.0 | 13.4 | -5.60 | -3.19 |
| religion | Sarna_Tribal_religion | 0.9 | 2.0 | +1.10 | +2.60 |
| education | Middle | 21.5 | 26.0 | +4.50 | +2.45 |
| occupation | Services | 8.0 | 12.29 | +4.29 | +2.43 |
| marital_status | Separated_divorced | 1.0 | 0.0 | -1.00 | -2.25 |
| migration | Out_migrant | 1.0 | 0.0 | -1.00 | -2.25 |
| caste | OBC_Hindu | 30.0 | 25.4 | -4.60 | -2.24 |

## Joints (sorted by max cell |z|)
| joint | tier | max |z| | max_cell_gap_pp | chisq_sum | n_out | skipped |
|---|---|---|---|---|---|---|
| asset_given_gp | C | 3.61 | 14.31 | 27.6 | 1 |  |
| vote_given_religion | E | 3.19 | 65.00 | 33.7 | 1 |  |
| vote_given_caste | C | 3.19 | 18.06 | 57.9 | 2 |  |
| vote_given_gender | C | 2.75 | 8.43 | 23.2 | 1 |  |
| caste_given_gp | D | 2.56 | 13.52 | 33.4 | 1 |  |
| caste_given_religion | E | 2.39 | 5.44 | 17.3 | 0 |  |
| religion_given_gp | A | 2.33 | 6.68 | 24.2 | 0 |  |
| amenities_given_gp | C | 2.31 | 13.96 | 15.2 | 0 |  |
| asset_given_religion | E | 2.28 | 18.00 | 14.0 | 0 |  |
| lang_given_religion | E | 2.11 | 20.00 | 17.6 | 0 |  |
| migration_given_religion | E | 1.96 | 40.00 | 17.2 | 0 |  |
| education_given_caste | E | 1.90 | 11.04 | 46.4 | 0 |  |
| education_given_age_gender | E | 0.00 | 17.00 | 0.0 | 0 |  |
| married_given_age_gender | E (widows concentrate here) | 0.00 | 93.00 | 0.0 | 0 |  |

## Aggregate vote share
### vote_2019_LS_share (tier A)  max |z| = 1.69
| bucket | target | observed | gap_pp | z | in_tol |
|---|---|---|---|---|---|
| AITC | 44.67 | 42.2 | -2.47 | -1.11 | True |
| BJP | 42.47 | 46.2 | +3.73 | +1.69 | True |
| INC | 1.71 | 2.4 | +0.69 | +1.19 | True |


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