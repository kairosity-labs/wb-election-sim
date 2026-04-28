# Verifier report (n=100)

- composite chi-square: **985.56** (max allowed: 800.0)
- within tolerance: **False**
- max axis |z|: 4.36  · max joint cell |z|: 4.54  · aggregate vote max |z|: 0.92
- max axis gap: 18.0 pp  · max joint cell gap: 100.0 pp  · aggregate max gap: 1.45 pp
- cell tolerance: |z| ≤ 2.5

## Axes (sorted by max |z|)
| axis | tier | max |z| | max_gap_pp | chisq_sum | n_out |
|---|---|---|---|---|---|
| class_of_worker | E | 4.36 | 6.08 | 21.4 | 1 |
| marital_status | E | 4.19 | 12.00 | 21.9 | 1 |
| caste | D | 3.67 | 18.00 | 37.2 | 3 |
| migration | D | 3.57 | 7.00 | 20.9 | 1 |
| mother_tongue | A | 3.49 | 16.00 | 40.4 | 2 |
| economic_status | E | 3.22 | 16.00 | 19.3 | 1 |
| workforce_status | E | 2.95 | 10.00 | 16.5 | 1 |
| household_composition | E | 2.67 | 11.00 | 13.2 | 1 |
| amenities | D | 2.54 | 11.00 | 18.4 | 1 |
| education | E | 2.45 | 10.00 | 25.0 | 0 |
| gender | E | 2.41 | 12.03 | 11.6 | 0 |
| occupation | A | 2.32 | 6.48 | 11.7 | 0 |
| asset_media | D | 2.24 | 8.00 | 16.8 | 0 |
| age_cohort | E | 1.74 | 3.85 | 9.4 | 0 |
| religion | E | 1.68 | 7.00 | 8.8 | 0 |
| gp_location | E | 0.50 | 1.20 | 0.5 | 0 |
| garden_status | E | 0.00 | 0.00 | 0.0 | 0 |

## Top 10 category gaps (by |z|)
| axis | category | target | observed | gap_pp | z |
|---|---|---|---|---|---|
| class_of_worker | Employer | 1.0 | 6.56 | +5.56 | +4.36 |
| marital_status | Widowed | 9.0 | 21.0 | +12.00 | +4.19 |
| caste | ST_total | 40.0 | 58.0 | +18.00 | +3.67 |
| migration | Nepal_origin | 4.0 | 11.0 | +7.00 | +3.57 |
| mother_tongue | Sadri_Nagpuri | 30.0 | 46.0 | +16.00 | +3.49 |
| economic_status | BPL_household | 45.0 | 61.0 | +16.00 | +3.22 |
| workforce_status | Unemployed | 8.0 | 0.0 | -8.00 | -2.95 |
| mother_tongue | Bengali | 14.0 | 24.0 | +10.00 | +2.88 |
| caste | Christian | 7.0 | 0.0 | -7.00 | -2.74 |
| caste | Other_Sarna_Buddhist | 7.0 | 0.0 | -7.00 | -2.74 |

## Joints (sorted by max cell |z|)
| joint | tier | max |z| | max_cell_gap_pp | chisq_sum | n_out | skipped |
|---|---|---|---|---|---|---|
| education_given_caste | E | 4.54 | 78.00 | 87.7 | 5 |  |
| lang_given_religion | E | 3.47 | 52.00 | 64.1 | 4 |  |
| caste_given_religion | E | 3.32 | 100.00 | 44.3 | 3 |  |
| vote_given_caste | D | 3.30 | 60.00 | 54.6 | 2 |  |
| migration_given_religion | D | 2.85 | 55.00 | 33.2 | 2 |  |
| asset_given_occupation | D | 2.72 | 50.00 | 16.8 | 1 |  |
| vote_given_gender | D | 2.71 | 11.56 | 17.6 | 1 |  |
| amenities_given_gp | E | 2.70 | 45.00 | 23.2 | 1 |  |
| vote_given_religion | D | 2.43 | 45.00 | 28.0 | 0 |  |
| asset_given_religion | None | 2.17 | 55.00 | 26.1 | 0 |  |
| religion_given_gp | E | 1.62 | 15.60 | 10.1 | 0 |  |
| asset_given_gp | E | 1.52 | 22.00 | 4.1 | 0 |  |
| education_given_age_gender | E | 0.00 | 8.00 | 0.0 | 0 |  |
| married_given_age_gender | E (high widowhood: occupational male premature mortality) | 0.00 | 85.56 | 0.0 | 0 |  |

## Aggregate vote share
### vote_2019_LS_share (tier A)  max |z| = 0.92
| bucket | target | observed | gap_pp | z | in_tol |
|---|---|---|---|---|---|
| BJP | 58.53 | 59.0 | +0.47 | +0.10 | True |
| AITC | 33.63 | 34.0 | +0.37 | +0.08 | True |
| INC | 2.55 | 4.0 | +1.45 | +0.92 | True |
| RSP | 2.2 | 3.0 | +0.80 | +0.55 | True |


## Partial-coverage telemetry

All joints fully covered.

### Skipped aggregate buckets
| aggregate | bucket | reason |
|---|---|---|
| vote_2019_LS_share | IND | vote_values=['IND'] not present in sampled population (field=vote_2019_LS) |
| vote_2019_LS_share | NOTA | vote_values=['NOTA'] not present in sampled population (field=vote_2019_LS) |
| vote_2019_LS_share | SUCI | vote_values=['SUCI'] not present in sampled population (field=vote_2019_LS) |
| vote_2019_LS_share | IND | vote_values=['IND'] not present in sampled population (field=vote_2019_LS) |