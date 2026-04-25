# Per-Constituency Normalized Dataset — Target Schema & Source Coverage

## Design principle

**Spec first, pull second.** We commit to a target schema for what each AC row must contain, then prove — field by field — that a concrete source exists at a known granularity. Any field without a source is either (a) dropped, (b) marked as a documented proxy with uncertainty, or (c) synthesized with a flagged model.

The output is **one row per AC × one persona table per AC**. The AC row holds marginal distributions; the persona table (~1000–10,000 synthetic voters per AC) holds joint samples.

---

## Target schema — AC-level marginals

For each of 294 ACs we want these distributions:

| # | Field | Sub-breakdown |
|---|---|---|
| 1 | Population (total, rural, urban, M, F) | counts |
| 2 | Age | 5-year bins 0-4, 5-9, …, 80+ × sex |
| 3 | Religion | Hindu, Muslim, Christian, Sikh, Buddhist, Jain, Other, Not-stated |
| 4 | Religion × age × sex | joint, 3-way |
| 5 | Caste | SC, ST, OBC, General (SC/ST categorical by sub-caste where available) |
| 6 | Mother tongue / language | Bengali, Hindi, Urdu, Santali, Nepali, others |
| 7 | Education level | 7 categories (illiterate → graduate+) × sex |
| 8 | Literacy rate | by sex |
| 9 | Occupation (worker type) | main / marginal / non-worker × sex |
| 10 | Industry (workers) | NIC-1998 9 sections × sex (cultivator / agri-labour / HH industry / other) |
| 11 | Household size | 1, 2, 3, 4, 5, 6, 7, 8, 9+ |
| 12 | Household economic status | SECC deprivation / automatic-inclusion bands |
| 13 | Names (first, last, gender-tagged) | frequency table sampled from SIR 2026 roll |
| 14 | Current electorate | post-SIR voter count, by booth |
| 15 | Historical voting | party vote share by year 2011/2016/2021 |
| 16 | 2026 candidates | name, party, age, education, wealth, criminal record |
| 17 | Health / family planning | NFHS-5 district indicators (TFR, IMR, wealth quintiles) |

---

## Source coverage matrix

| Field | Primary source | Native geography | Aggregation to AC | Completeness |
|---|---|---|---|---|
| 1. Population | Census 2011 PCA | Village / Town / Ward | Sum via crosswalk | **100%** |
| 2. Age × sex | Census C-13 / C-14 | Sub-district | Population-weighted | **100%** |
| 3. Religion | Census C-01 | Sub-district (tehsil/CD-block) | Pop-weighted | **100%** |
| 4. Religion × age × sex | Census C-15 | Sub-district | Pop-weighted | **100%** |
| 5a. SC / ST | Census PCA + C-05 | Village | Direct sum | **100%** |
| 5b. OBC / sub-caste | SECC 2011 | Village / household | Aggregate | **SECC has OBC gaps** — use NSS rounds + district averages as fill |
| 6. Language | Census C-16 | Sub-district | Pop-weighted | **100%** |
| 7. Education | Census C-08 / C-11 | Village / sub-district | Sum / pop-weighted | **100%** |
| 8. Literacy | Census PCA | Village | Direct | **100%** |
| 9. Worker type | Census PCA + B-1 | Village | Direct | **100%** |
| 10. Industry (NIC) | Census B-4 / B-5 | Sub-district | Pop-weighted | **100%** for 9 broad sections; finer NIC codes only at district |
| 11. Household size | Census HH-1 | Sub-district | Pop-weighted | **100%** |
| 12. SECC deprivation | SECC 2011 household file | Household | Aggregate by village → AC | **100%** but dated |
| 13a. First names | SIR 2026 electoral roll PDFs | Booth-level | Direct count | **100%** if we parse all 294 PDFs |
| 13b. Last-name → community map | Ashoka `in-rolls` name corpora | N/A | Classifier | Probabilistic, not ground truth |
| 14. Current electorate | CEO WB SIR Final Roll Rev-2 | Booth | Direct | **100%** |
| 15. Historical vote | LokDhaba + dataful.in + ECI | AC | Direct | **100%** 1962–2021 |
| 16. 2026 candidates | ECI affidavit + MyNeta | Candidate | Direct | **100%** after scrape |
| 17. Health / NFHS | NFHS-5 | District | Attribute district value to AC | **Proxy** — district-level only |

**Coverage summary:** All 17 fields have a concrete primary source. 13 of 17 are truly at or below AC granularity; 4 (NFHS-5, some NIC, OBC detail, SECC caste strings) are district-level proxies, which is standard practice in Indian electoral sociology.

---

## The critical dependency — the village→AC crosswalk

Census tables are indexed by Location Code Directory (LGD) village codes. ACs are indexed by delimitation boundaries. To aggregate Census from village to AC we need a mapping:

`village_LGD_code → polling_booth → AC_number`

**Sources for this mapping (ranked):**
1. **Harvard Dataverse [DOI 10.7910/DVN/KKOWNJ](https://doi.org/10.7910/DVN/KKOWNJ)** — Lok Sabha 2009/2014/2019 polling-station-to-village linkage for West Bengal (66k–76k booths). LS boundaries differ from AC but overlap is high; AC is a subset of LS so the village-to-AC mapping can be derived.
2. **LGD — [lgdirectory.gov.in](https://lgdirectory.gov.in/)** — official administrative crosswalk (village → CD block → district).
3. **CEO WB SIR Rev-2 polling-station list** — each booth has a named catchment locality. Fuzzy-match to village names.
4. **Datameet shapefiles + Census village shapefiles** — spatial join.

**Engineering plan for the crosswalk:**
- Start with Harvard's booth→village file (WB is covered) and the ECI booth→AC mapping. Compose them: village → LS booth → AC.
- Validate: every WB village in Census PCA should hit exactly one AC. Expect ~2–5% unresolved (renames, splits). Manually resolve the long tail.
- Cache the final crosswalk as `data/crosswalk/village_to_ac.parquet`.

---

## Staleness & freshness corrections

Census 2011 is 15 years old. Adjustments:

1. **Re-anchor population to 2026 electorate.** CEO WB SIR Rev-2 gives us the current adult electorate per AC. Rescale Census adult population to match.
2. **SIR deletion model.** ~9.1M deletions, 65% Muslim in contested cases. Overlay a deletion model on the Census-projected electorate so post-SIR religion proportions differ (meaningfully) from raw Census.
3. **NFHS-5 deltas.** Where NFHS-5 (2019-21) reports district-level religion/TFR/literacy, compare to Census 2011 district totals and apply a ratio adjustment to Census.
4. **Economic Census 2013 / MSME register / PLFS** for occupation drift since 2011 (coarser; use at district level only).

**What we do NOT claim:** we do not manufacture 2026 village-level data we don't have. We acknowledge that between-census drift at sub-district level is estimated, not measured.

---

## Validation checks (run after build)

These guarantee the dataset is internally consistent and externally plausible:

- [ ] Every AC has non-null values for all 17 fields.
- [ ] AC-level population sums to the WB state total within ±1% (after re-anchoring, exactly).
- [ ] Religion shares at state level match Census state totals (Hindu 70.54%, Muslim 27.01%, others 2.45%) within 0.5 pp before SIR adjustment.
- [ ] Age pyramid median in each AC falls in 20–35 (sanity).
- [ ] Literacy rate per AC in 60–90% range (WB state avg ≈77%).
- [ ] Historical vote shares per AC sum to 100% ± 0.1%.
- [ ] Every AC-row joins back to ≥1 booth in SIR Rev-2.
- [ ] SECC deprivation categories sum to total households per village.
- [ ] Name corpus per AC ≥ 10k unique names (large enough to sample without collisions).
- [ ] Spot-check 5 ACs manually against published DCHBs.

---

## What goes into each persona (synthesized from the AC marginals)

Each synthetic voter in an AC gets:
- Age, sex, religion, caste, language, education, occupation, household size — **sampled from the joint distribution** built from Census cross-tabs. We'll use IPF (iterative proportional fitting) to reconcile marginals when joint is unavailable.
- Name — sampled from AC's empirical SIR name distribution, conditioned on sex and community.
- Economic status — SECC deprivation band.
- Past-vote prior — from historical AC results + Lokniti cross-tabs by demographic.
- Information diet — constituency × literacy × age drives a weighting on Bengali TV, Bengali print, Hindi TV, WhatsApp groups, X.

This is the full demographic scaffold before any belief modeling kicks in.
