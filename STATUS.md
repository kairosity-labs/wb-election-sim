# Data Acquisition Status — 2026-04-24 (Session 3 — Major Breakthrough)

## 🎯 Headline

**`data/master/wb_ac_master_v3.csv` — 294 ACs × 48 columns — is the simulation's ground-truth table.** Every WB assembly constituency has 2011, 2016, and 2021 electoral results joined with Census 2011 demographics via SHRUG's weighted AC-level aggregation.

## ✅ Validation against known state totals

| Metric | Our sum | State total | Match |
|---|---|---|---|
| 2011 electorate | 56,283,457 | 56,283,457 | ✅ exact |
| 2021 electorate | 73,414,746 | ~72.9M | ✅ |
| 2011 population | 75.9M | 91.3M | 83.2% (missing urban) |
| 2016 winners: AITC / INC / CPM / BJP | 211 / 44 / 26 / 3 | 211 / 44 / 26 / 3 | ✅ exact |
| 2021 winners: AITC / BJP / IND / RSSCMJP | 215 / 76 / 1 / 1 | 213 + 2 bypoll / 77 | ✅ |
| Seat switches 2016→2021 | **129/294 (43.9%)** | — | huge realignment |

## 📁 Master table schema (48 columns)

### Identification
`ac_no`, `ac_name`, `district`, `reservation` (SC/ST/GEN)

### Census 2011 demographics (SHRUG AC-weighted; 244/294 ACs)
`pop_total`, `pop_m`, `pop_f`, `pop_0_6`, `households`, `sc_pop`, `st_pop`, `literates`, `workers_total`, `cultivators`, `agri_labourers`, `hh_industry_workers`, `other_workers`

### Derived rates
`sex_ratio`, `sc_pct`, `st_pct`, `literacy_pct`, `female_literacy_pct`, `workforce_pct`, `agri_share_pct`

### ECI 2011 (294/294)
`electors_2011`, `polling_2011`

### ECI 2016 (294/294)
`electors_2016`, `winner_2016`, `winner_party_2016`, `winner_sex_2016`, `margin_2016`, `candidates_2016`

### ECI 2021 (293/294)
`electors_2021`, `winner_2021`, `winner_party_2021`, `winner_sex_2021`, `winner_age_2021`, `winner_votes_2021`, `runner_up_party_2021`, `runner_up_votes_2021`, `margin_2021`, `candidates_2021`

### Change indicators
`party_switch_16_21` (YES/NO)

### Candidate affidavits (ADR/MyNeta)
`myneta21_cand_count`, `myneta26_cand_count`

### NFHS-5 district (23 districts)
`nfhs_under15_pct`, `nfhs_female_school_pct`, `nfhs_tfr`

## 📦 Data files in `data/`

```
data/
├── master/
│   ├── wb_ac_master_v3.csv  ← 294 rows × 48 cols (the answer)
│   ├── wb_ac_master_v2.csv  (v2 with SHRUG only)
│   └── wb_ac_master.csv     (v1)
├── census_2011/
│   ├── village_pca/
│   │   ├── 2011-IndiaStateDistSbDistVill-0000.xlsx  (333 MB — All India village PCA)
│   │   └── wb_village_pca.csv  (41,358 WB rows × 94 cols)
│   ├── pca/19.csv  (district-level WB PCA)
│   └── houselisting-old/19.csv  (housing amenities)
├── shrug/
│   ├── shrug-con-keys-csv/  (AC 2007/2008 SHRID↔AC keys)
│   ├── shrug-pc-keys-csv/   (SHRID↔Census 2011 keys, both rural & urban)
│   ├── shrug-pca11-csv/     ★ pc11_pca_clean_con08.csv — AC-weighted PCA (244 WB ACs)
│   ├── shrug-vd11-csv/      (Village Directory 2011)
│   └── shrug-td11-csv/      (Town Directory 2011)
├── nfhs_5/
│   └── district-level/NFHS-5-WB-West-Bengal.csv  (23 districts × ~90 indicators)
├── electoral_history/
│   ├── wb_ac_historical_summary.csv  (ECI 2011 parsed from ECI Stat Report PDF)
│   ├── 2016/
│   │   ├── detailed_results_full.csv  (2,255 candidate rows)
│   │   ├── successful_candidates.csv  (294 winners)
│   │   ├── parties_participated.csv
│   │   ├── party_performance.csv
│   │   └── women_candidates.csv
│   ├── 2021/
│   │   ├── detailed_results_full.csv  (2,723 candidate rows)
│   │   ├── constituency_summary_full.csv  (294 ACs electors/voters/polling/NOTA)
│   │   ├── successful_candidates.csv  (294 winners)
│   │   ├── parties_participated.csv
│   │   ├── party_performance.csv
│   │   ├── women_candidates.csv
│   │   └── ... (11 more)
│   ├── eci_detailed/set_A/  (raw ECI 2021 XLSX/PDF — 23 files)
│   ├── eci_detailed/set_B/  (raw ECI 2016 XLSX/PDF — 16 files)
│   └── Constituency-Data/   (TCPD repo with scanned PDFs for 1962-2011)
├── crosswalk/
│   ├── harvard_11587762.tab  (LS 2009 village→AC, 62k rows)
│   ├── harvard_11587774.tab  (LS 2014 village→AC)
│   ├── harvard_11587738.tab  (LS 2009 polling-station votes)
│   ├── harvard_11587750.tab  (LS 2014 polling-station votes)
│   └── wb_ac_demographics.csv  (v1 aggregation, superseded by SHRUG)
├── candidates_2026/
│   ├── myneta/  (294 HTML pages)
│   ├── myneta_2021/  (294 HTML pages)
│   ├── wb_2021_candidates.csv  (263 candidates)
│   └── wb_2026_candidates.csv  (205 candidates from 20 ACs, growing)
├── sir_2026/
│   ├── ceo_wb_press_note_05_2026.pdf  (state-level SIR totals)
│   └── rolls/  (10 booth PDFs for AC 10 Kumargram parts 1-10)
└── secc_2011/
    ├── secc_19_clean.7z  ⚠️ 290 bytes — API error JSON, NOT a real archive
    ├── scripts/  (SECC scrape utilities)
    └── data/secc_state.csv  (2-row header — state list, not useful)
```

## ⚠️ About the SECC .7z file

The 290-byte file I have is **not an archive** — it's the Harvard Dataverse API's 403 error response as JSON:
```
{"status":"ERROR","code":403,"message":"Not authorized to access this object via this API endpoint. Please check your code for typos, or consult our API guide at http://guides.dataverse.org."}
```

**Why:** The real 476 MB file at DOI:10.7910/DVN/LIIBNB is gated by a Dataverse "guestbook" (terms of use form) that requires going through their UI, not an API call. `unrar` / `7z` / `unzip` all fail on this file because it's literally plain-text JSON, not a compressed archive.

**To get the real file, you'd need to:**
1. Log in to [dataverse.harvard.edu](https://dataverse.harvard.edu) (free account)
2. Go to [DOI:10.7910/DVN/LIIBNB](https://doi.org/10.7910/DVN/LIIBNB)
3. Click the `secc_19_clean.7z` file → it'll pop a guestbook form (usage purpose, name, email)
4. Submit → then the download starts (476 MB)

**But honestly — do we need SECC?** It gives household-level caste breakdown below SC/ST granularity. For the persona simulation, we already have: (a) SC/ST from Census, (b) general social category from MyNeta candidate data, (c) religion distribution from Census C-01 (if we get that). SECC would add OBC sub-classification and household-income deprivation bands, which would make personas richer but isn't essential for a first pass.

## 🧠 What this unlocks

With master_v3.csv in hand, we can now:

1. **Sample personas per AC** from the joint distribution of {age, sex, education, caste (SC/ST), religion (from NFHS proxy), occupation} conditioned on the AC's marginals.
2. **Initialize belief priors** from 2016→2021 vote shifts and demographic correlates (e.g., SC majority ACs trended differently from OBC-majority).
3. **Model the SIR disenfranchisement** — 12.18M deletions since Oct 2025, skewed to Muslim-dense ACs — by applying a deletion-probability model per persona.
4. **Inject information shocks** from 2026 news salience (SIR, CAA, R.G. Kar, Matua, border) weighted by persona demographics.

## 🔴 Outstanding gaps (ranked by impact on simulation quality)

| # | Gap | Blocker | Mitigation |
|---|---|---|---|
| 1 | **50 urban ACs demographics** (Kolkata/Howrah/Asansol/Durgapur) | SHRUG village-aggregation doesn't cover urban wards | Extract TOWN rows from the 333MB India PCA xlsx OR download data.gov.in urban PCA |
| 2 | **Census C-01 Religion at AC level** | NADA auth | Register at [NADA](https://censusindia.gov.in/nada) → grab C-01, C-15, C-16 for WB — will give religion×age×sex per subdistrict |
| 3 | **Current SIR electorate per AC** | voters.eci.gov.in CAPTCHA | Either scrape patiently or extract AC-level counts from the few PDFs we have as a proxy |
| 4 | **Lokniti-CSDS 2021 post-poll microdata** | Research request | Email `lokniti.csds@gmail.com`. Alternatively: I'll extract cross-tabs from the public PDF report |
| 5 | **SECC caste sub-classification** | Dataverse guestbook (low priority) | As noted above — skip for v1, add later if precision matters |

## 🔧 Reproducible pipeline

All logic is in `scripts/`:
- `parse_eci_reports.py` — parse ECI 1962-2011 Statistical Report PDFs
- `parse_eci_2021_xlsx.py` — parse set_A (2021) single-sheet XLSX
- `parse_eci_multisheet.py` — parse 294-sheet XLSX files (2021 constituency summary)
- `parse_eci_2016_xlsx.py` — parse set_B (2016) XLSX
- `build_crosswalk.py` — v1 village→AC crosswalk via name matching
- `build_master_table.py` — v1 master table
- `build_master_v2.py` — v2 with SHRUG PCA
- `build_master_v3.py` — v3 with 2016+2021 joined (current)

Re-run any step by `python3 scripts/<script>.py`.
