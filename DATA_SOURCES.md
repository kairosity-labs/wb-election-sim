# WB 2026 Election Simulation — Data Sources

Polling: **Phase I** 2026-04-23 (AC 1–76, 203–258, 275–294, ~152 seats) · **Phase II** 2026-04-29 (AC 77–202, 259–274, ~142 seats) · **Results** 2026-05-04. 294 assembly constituencies.

---

## Layer 1 — Demographics (ground truth for persona generation)

### Census 2011 (most granular available; 2021 census is delayed)

| Table | What it gives us | URL |
|---|---|---|
| PCA (Primary Census Abstract) | Village/town-level: population, SC/ST, workers, literacy, age | [data.gov.in PCA WB](https://www.data.gov.in/catalog/villagetown-wise-primary-census-abstract-2011-west-bengal) · [WB census portal](https://westbengal.census.gov.in/pca_2011_wb.php) |
| C-01 | Population by religious community | [censusindia NADA C-01 WB](https://censusindia.gov.in/nada/index.php/catalog/11396) |
| C-15 | Religion × age × sex | [censusindia NADA C-15 WB](https://censusindia.gov.in/nada/index.php/catalog/11435) |
| C-16 | Mother tongue / language | censusindia.gov.in NADA |
| B-series | Workers by industry/occupation | censusindia.gov.in |
| HH-series | Household composition, size | censusindia.gov.in |
| DCHB | District Census Handbooks — rich per-district tables | [WB DCHBs](https://westbengal.census.gov.in/) |

### SECC 2011 — Socio-Economic Caste Census
- [secc.dord.gov.in — WB (state code 19)](https://secc.dord.gov.in/getSeccDataSummaryStateReport.htm/19)
- [GitHub: in-rolls/secc](https://github.com/in-rolls/secc) — community-cleaned
- Gives: caste (within SC/ST/Other), income bands, deprivation indicators, occupation categories at household level

### NFHS-5 (2019-21) — District-level health & family
- [GitHub: pratapvardhan/NFHS-5](https://github.com/pratapvardhan/NFHS-5) — CSVs, CC-BY 4.0, `NFHS-5-WB-West-Bengal.csv` per-district, 131 indicators
- [DHS WB state report (FR374)](https://dhsprogram.com/pubs/pdf/FR374/FR374_WestBengal.pdf)
- [NFHS-5 on data.gov.in](https://www.data.gov.in/catalog/national-family-health-survey-5-nfhs-5-india-districts-factsheet-data)

---

## Layer 2 — Electoral history & candidates

### Historical results (constituency-level)
- **LokDhaba (Ashoka TCPD)** — [lokdhaba.ashoka.edu.in](https://lokdhaba.ashoka.edu.in/) · structured 1962-onwards, includes candidate caste/gender where known
- **dataful.in** — [WB AC results 1951–2021](https://dataful.in/datasets/14457/) · 23 columns, 26,087 rows, CSV/XLSX/Parquet
- **TCPD project** — [tcpd.ashoka.edu.in](https://tcpd.ashoka.edu.in/lok-dhaba/)

### Polling-station ↔ village crosswalk (critical for census merge)
- **Harvard Dataverse DOI [10.7910/DVN/KKOWNJ](https://doi.org/10.7910/DVN/KKOWNJ)** — Lok Sabha 2009/2014 for 11 states including WB (66k–76k booths), 2019 UP only. Includes links to census village codes via merge files.
- [Nature Scientific Data paper](https://www.nature.com/articles/s41597-025-05418-6) · [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12214517/) — the methodology paper. **Caveat: LS-booth geography ≠ AC-booth geography**, but overlap is high and it's the best crosswalk available.

### 2026 candidates & affidavits
- **Official ECI** — [affidavit.eci.gov.in](https://affidavit.eci.gov.in/) · [voters.eci.gov.in](https://voters.eci.gov.in/download-eroll?stateCode=S25)
- **MyNeta (ADR)** — [myneta.info WB](https://www.myneta.info/state_assembly.php?state=West+Bengal) · criminal + wealth + education, scraped from ECI
- **OpenCity partial** — [WB 2026 affidavits (Kolkata only so far)](https://data.opencity.in/dataset/west-bengal-assembly-elections-2026-affidavits)
- **CEO WB** — [ceowestbengal.wb.gov.in](https://ceowestbengal.wb.gov.in/) · notifications, voter lists, SIR data
- **WB State EC** — [wbsec.gov.in](https://wbsec.gov.in/)

### SIR 2026 — ⚠️ the elephant in the room
- ~9.1M voters deleted (11.88% of October 2025 electorate), ~65% of contested deletions are Muslim
- [CEO WB SIR page](https://ceowestbengal.wb.gov.in/SIR) · [ASD list](https://ceowestbengal.wb.gov.in/asd_sir)
- Any simulation must model the SIR-modified electorate, not pre-SIR demographics.

---

## Layer 3 — Opinion / attitudinal signal

### Academic surveys
- **Lokniti-CSDS** — [State Election Studies](https://www.lokniti.org/state-election-studies) · [lokniti.org](https://www.lokniti.org/) · [csds.in/lokniti](https://www.csds.in/lokniti)
- 2021 WB post-poll: [PDF findings](https://lokniti.org/media/PDF-upload/1622695848_3736100_download_report.pdf) — 4,223 voters across 40 ACs; cross-tabs by religion/caste/class/age/gender. **Raw microdata is not public — request from Data Unit.** Extract cross-tabs from PDF.
- 2024 Social & Political Barometer: [PDF](https://lokniti.org/media/PDF-upload/1718435207_67606300_download_report.pdf)

### Commercial pollsters (2026 cycle)
- **CVoter** — [IndiaTV aggregation](https://www.indiatvnews.com/news/india/assembly-election-opinion-poll-live-updates-of-west-bengal-assam-tamil-nadu-kerala-puducherry-bjp-congress-left-tmc-aiudf-dmk-ldf-udf-2026-04-06-1036492) · [YouTube release](https://www.youtube.com/watch?v=wvt6CfDywos)
- **Axis My India** — [axismyindia.org](https://www.axismyindia.org/perform-rec.php)
- **Aggregators** — [opinionsandratings.com](https://www.opinionsandratings.com/india-polls/general-stories/westbengal2026electionopinionpoll) · [mywestbengal.com](https://mywestbengal.com/west-bengal-election/)

---

## Layer 4 — News & information environment

### Bengali media (most important — most voters consume in Bengali)
- **ABP Ananda** — [YouTube channel](https://www.youtube.com/channel/UCv3rFzn-GHGtqzXiaq3sWNg) · [Election playlist](https://www.youtube.com/playlist?list=PL0TFwRh-mFhGLxsBIzTSvfgC-D013YoFI) — scrape with `yt-dlp`, transcribe with Whisper
- **Anandabazar Patrika** — [anandabazar.com](https://www.anandabazar.com/) · archive section
- Zee 24 Ghanta, News18 Bangla, R Plus News — all have YouTube archives

### English coverage of WB
- [The Hindu](https://www.thehindu.com/), [Scroll.in](https://scroll.in/), [The Wire](https://thewire.in/), [The Federal](https://thefederal.com/), [Al Jazeera](https://www.aljazeera.com/news/2026/4/16/muslims-the-target-fury-as-millions-lose-voting-rights-in-indias-bengal), [Deccan Herald](https://www.deccanherald.com/)
- ThePrint sociology-of-elections pieces: good for cross-tab intuition

### Campaign issues to model for 2026 (from news scan)
1. **SIR voter deletion** — dominant issue; disproportionate Muslim impact
2. **CAA implementation** — polarization vector
3. **Matua community** — swing bloc in 40-50 seats
4. **Bengali asmita vs Hindu consolidation** — identity cleavage
5. **Border / infiltration / Siliguri corridor** — BJP security frame
6. **R.G. Kar case (2024)** — women's safety
7. **School recruitment scam** — corruption / anti-incumbency
8. **15-year TMC anti-incumbency**
9. **Jobs and delayed exams**

---

## Layer 5 — Geography (shapefiles)

- **Datameet India** — open shapefiles for AC/PC boundaries (2008 delimitation, still current)
- ECI delimitation orders: [eci.gov.in/delimitation](https://www.eci.gov.in/delimitation)

---

## Known gaps & caveats

1. **Census is 15 years old.** Must age-forward using NFHS-5 deltas and projected growth. Religious composition has likely shifted; sub-district economic base definitely has.
2. **Village boundaries ≠ AC boundaries.** Need the Harvard crosswalk (LS-based) + manual correction for AC boundaries. This is the hardest engineering step.
3. **No public raw microdata for Lokniti surveys.** Only published cross-tabs in PDF reports. Will need OCR + careful extraction of religion × vote, caste × vote, age × vote joint distributions.
4. **SIR invalidates pre-2025 electorate assumptions** in directionally important ways. Treat the ASD (Additions/Shifts/Deletions) list as a first-class input.
5. **Commercial opinion polls report state-level not AC-level.** Use them for priors, but AC-level movement has to come from historical patterns + local signals.
