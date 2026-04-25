# Source catalog — WB 2026 Constituency-Level Demographic Dataset

Every URL consumed during research, with access date and which data columns it fed. See [`methodology.md`](methodology.md) for confidence-tier definitions; sources marked "probed" have been checked for scrape viability but not yet ingested.

## Conventions

- **Access date** is when the URL was last fetched for this dataset.
- **Tier** is the confidence tier we assign to values derived from this source (per `methodology.md` §1); a source can yield different tiers depending on which column it feeds.
- **Status:** `ingested` (in `data/raw/`) · `probed` (viability-checked, pending script) · `referenced` (quoted in prose only) · `planned` (next to pull).

---

## A. Canonical identity & electoral-roll sources (tier A)

| Source | URL | Fed columns | Status | Access date |
|---|---|---|---|---|
| Wikipedia — List of constituencies of the WB Legislative Assembly | https://en.wikipedia.org/wiki/List_of_constituencies_of_the_West_Bengal_Legislative_Assembly | `ac_no, ac_name, district, reservation` (all 294) | ✓ ingested → `data/raw/ac_list.csv` | 2026-04-24 |
| **CEO WB — AC-wise Draft Elector SIR 2026** | https://ceowestbengal.wb.gov.in/Downloads/SIR2026/AC%20wise%20Draft%20Elector%20SIR%202026.pdf | `total_electors_2026, male_electors, female_electors` (all 294, tier A) + polling_stations | ✓ ingested → `data/raw/pdfs/ceo_wb_sir2026_ac_wise.pdf` → `data/raw/ceo_wb_sir2026_electorate.csv` via `scripts/parse_ceo_wb_sir_pdf.py` | 2026-04-24 |
| Delimitation Commission of India 2008 — full order | https://upload.indiacode.nic.in/showfile?actid=AC_CEN_3_20_00030_200233_1517807324510&type=order&filename=Delimitation+Order,2008.pdf | AC ↔ block/GP/ward mapping (WB section ~50-70 pages of 572) | ✓ downloaded (1.3 MB, 572 pages) → `data/raw/pdfs/delimitation_order_2008.pdf` · parser pending | 2026-04-24 |
| CEO WB — Form 20 Part II 2024 LS (AC-segment vote breakdowns) | https://ceowestbengal.wb.gov.in/Downloads/Election/GE2024/Form%2020_Part-II_West%20Bengal.pdf | 2024 LS AC-segment vote share (political — future scope) | ✓ downloaded (18 MB) → `data/raw/pdfs/ceo_wb_form20_2024ls_part2.pdf` · parser pending | 2026-04-24 |
| CEO WB — Phase-wise PC elector / polling-station (2024 LS) | https://ceowestbengal.wb.gov.in/Downloads/Election/GE2024/Phasewise_PCwise_Elector_Polling%20Station_PE2024.pdf | Historical electorate / PS counts | ✓ downloaded (523 KB, 14 pages) → `data/raw/pdfs/ceo_wb_phasewise_pc_elector_ps_2024.pdf` | 2026-04-24 |
| Wikipedia — 2026 West Bengal Legislative Assembly election | https://en.wikipedia.org/wiki/2026_West_Bengal_Legislative_Assembly_election | Electorate totals, phase schedule | referenced | 2026-04-24 |

## B. Census 2011 + Delimitation 2008 (tier A-E)

### Probe findings (2026-04-24)

| Source | URL | Probe result | Status |
|---|---|---|---|
| Census 2011 — WB state home (C-01, C-08, C-09, C-16, B-series at village/town) | https://censusindia.gov.in/ | Public state home but per-district DCHB PDF files; slow manual fetch | Deferred |
| **data.gov.in — WB village/town Primary Census Abstract 2011** | https://www.data.gov.in/catalog/villagetown-wise-primary-census-abstract-2011-west-bengal | ✗ Catalog loads (961KB HTML) but download URLs are JS-rendered; requires Janparichay auth | Deferred — would give tier-A village→AC rollup |
| westbengal.census.gov.in/pca_2011_wb.php | | ✗ **ECONNREFUSED** | Deferred |
| **Wikipedia — 23 WB district pages** (Census 2011 demographics sections) | e.g. https://en.wikipedia.org/wiki/North_24_Parganas_district | ✓ All 23 pages accessible with consistent Census 2011 tables | ingested → `data/raw/census2011_wb_district.csv` |
| **Delimitation Commission 2008 — full order** | https://upload.indiacode.nic.in/showfile?actid=AC_CEN_3_20_00030_200233_1517807324510&type=order&filename=Delimitation+Order,2008.pdf | ✓ 1.3 MB PDF, 572 pages; WB is Schedule XXX pages 517-539 | ingested → `data/raw/pdfs/delimitation_order_2008.pdf` → `data/raw/delimitation_ac_components.csv` via `scripts/parse_delimitation_wb.py` (625 component rows, 294/294 ACs) |

### Source → column mapping

| Source | Fed columns | Tier | Notes |
|---|---|---|---|
| Census 2011 WB district rollup (Wikipedia) | `hindu_pct, muslim_pct, christian_pct, other_religion_pct, sc_total_pct, st_total_pct, literacy_overall_pct, literacy_male_pct, literacy_female_pct, bengali_pct, hindi_pct, santhali_pct, urdu_pct, nepali_pct` (all 294 ACs) | **E** | District→AC via uniform within-district distribution. Coarse but captures cross-district variation (Murshidabad 66% Muslim vs Purba Medinipur 15%). Pilot ACs (e.g. AC 95) with CDB-level tier-E values are preserved (tier_beats rule). |
| Delimitation Order 2008 WB Table A | AC ↔ CDB / Municipality / Notified-Area components (625 rows) | A | Enables future block→AC aggregation when CDB-level Census data becomes accessible. |
| CPS India — WB Religion Census 2011 analysis | https://blog.cpsindia.org/2016/04/religion-data-of-census-2011-xix-west.html | C | Referenced via DemographicParameters.md |
| Census2011.co.in WB religion demography | https://www.census2011.co.in/data/religion/state/19-west-bengal.html | C | Referenced |

## C. Poverty / income (tier B → falling back to D/E)

### Probe findings (2026-04-24)

| Source | URL | Probe result | Fallback |
|---|---|---|---|
| **SECC 2011 dashboard** | `https://secc.gov.in/` | ✗ **DNS dead** (connection refused) | Use MGNREGA IPPE-2 list (mnregaweb2) which exposes SECC-derived BPL; if blocked, Census 2001 CDB BPL baselines (tier C, 15-year-old) |
| **MGNREGA MIS** (old) | `https://nrega.nic.in/` | Redirects to `nrega.dord.gov.in` | Use new URL |
| **MGNREGA MIS** (new) | `https://mnregaweb2.dord.gov.in/netnrega/homestciti.aspx?state_code=32` | ✗ **HTTP 401 Unauthorized** — state drill-down needs session/login | Data.gov.in MGNREGA district-wise CSV (tier B, district granularity only) |
| **MGNREGA public data portal (dynamic report)** | `https://mnregaweb4.nic.in/netnrega/dynamic2/dynamicreport_new4.aspx` | Public drill-down allegedly supports State/Dist/Block/GP — needs Playwright (stateful ASPX session), deferred | Tier C from Dataful.in block-wise persondays dataset |
| Data.gov.in — District-wise MGNREGA at a glance | https://www.data.gov.in/resource/district-wise-mgnrega-data-glance | Not yet fetched — tier B if it lists WB by district | Planned (Step 4 merge via `scripts/download_mgnrega_ogd.py`) |
| Dataful.in — MNREGA block-wise 2023-24 | https://dataful.in/datasets/20073/ | Paywalled / account-gated | Deferred |
| PLFS 2022-23 — WB annual report (NSS) | https://mospi.gov.in/ | Not yet fetched; tier C for occupation/income bands | Planned |
| NITI Aayog — Macro and Fiscal Landscape of WB | https://niti.gov.in/sites/default/files/2025-07/Macro-and-Fiscal-Landscape-of-the-State-of-West-Bengal-1.pdf | Macro context, LFPR, sector shares | referenced | 2026-04-24 |
| **Decision**: for Step 4 Pass A, populate `bpl_household_pct_secc` from Census 2001 CDB (tier C) + MGNREGA district job-card saturation proxy (tier C) pending a future scraper session with Playwright to tackle the live ASPX portals. |

## D. Welfare schemes (tier B/C/D)

### Probe findings (2026-04-24)

| Source | URL | Probe result | Fallback |
|---|---|---|---|
| **Swasthya Sathi** state dashboard | `https://swasthyasathi.gov.in/` | ✗ **HTTP 403 Forbidden** to WebFetch (likely UA-based block or bot protection) | State-level coverage narrative (~95% universal, tier C); Playwright retry with full browser headers planned |
| Khadya Sathi — state food dept | `https://food.wb.gov.in/` | Not yet probed; state-level only expected | tier C state-level ~90% |
| Krishak Bandhu — state agri dept portal | `https://matirkatha.net/` | Not yet probed | tier C state-level ~1.05 crore beneficiaries |
| Kanyashree — WB state portal | `https://wbkanyashree.gov.in/` | Not yet probed | tier C state-level ~81 lakh enrolled |
| Lakshmir Bhandar — state press releases (no AC-level dashboard known) | https://services.india.gov.in/service/detail/west-bengal-lakshmir-bhandar-scheme | `lakshmir_bhandar_beneficiaries_est` (state/district only → AC imputed) | referenced | 2026-04-24 |
| Subhadra Yojana comparison — LB beneficiary counts | https://subhadrayojanaa.com/lakshmir-bhandar-scheme/ | LB total beneficiaries state-wide | referenced | 2026-04-24 |
| **Decision**: welfare-scheme AC columns remain tier C/D/E (district-to-AC population weighting). A future session with Playwright can attempt the JS-dashboards, but given the uniformity of welfare coverage (>85–95% for all schemes state-wide), the SCM signal from within-AC variation is small. Prefer district-level heterogeneity over fake AC-level precision. |

## E. Caste / community (tier C/D)

| Source | URL | Fed columns | Status | Access date |
|---|---|---|---|---|
| Adibasikalyan, WB — Scheduled Tribes of West Bengal | https://adibasikalyan.gov.in/scheduled-tribes-of-west-bengal | ST sub-group state shares | referenced | 2026-04-24 |
| Wikipedia — List of Scheduled Tribes in West Bengal | https://en.wikipedia.org/wiki/List_of_Scheduled_Tribes_in_West_Bengal | ST sub-group state shares | referenced | 2026-04-24 |
| The Mooknayak — SC/ST & CAA 2024 analysis | https://en.themooknayak.com/politics/lok-sabha-elections-2024-after-caa-notification-all-eyes-are-set-on-the-dalit-and-tribal-votes-in-bengal | SC sub-group shares, geography | referenced | 2026-04-24 |
| Joshua Project — Mahishya of India | https://joshuaproject.net/people_groups/17411/IN | Mahishya population distribution | referenced | 2026-04-24 |
| Outlook — Political collapse of Bengal's UC Bhadralok hegemony | https://www.outlookindia.com/national/opinion-political-collapse-of-bengals-upper-caste-bhadralok-hegemony-and-bjps-prize-news-357287 | UC Bhadralok ~20% state estimate | referenced | 2026-04-24 |
| WB OBC category list (A/B) | https://www.scribd.com/document/875260718/New-OBC-List-Category-Wise-Up-to-03-06-2025 | OBC sub-castes (state list) | referenced | 2026-04-24 |
| Testbook — Matua community | https://testbook.com/ias-preparation/matua-community | Matua influence 30–45 AC estimate | referenced | 2026-04-24 |
| ETV Bharat — Matua unmapped voters (SIR) | https://www.etvbharat.com/en/state/matua-community-in-panic-over-unmapped-voters-in-west-bengal-draft-electoral-rolls-enn25122002312 | Matua / SIR interaction | referenced | 2026-04-24 |
| The Indian Tribal — Kurmi ST-status agitation | https://theindiantribal.com/2024/03/31/west-bengal-kurmis-contest-lok-sabha-elections/ | Kurmi concentration Jangalmahal | referenced | 2026-04-24 |

## F. Political-survey / academic (tier C)

| Source | URL | Fed columns | Status | Access date |
|---|---|---|---|---|
| CSDS-Lokniti — 2021 WB Post-Poll Survey Report | https://lokniti.org/media/PDF-upload/1622695848_3736100_download_report.pdf | Regional voting correlates, gender gap, caste × vote | planned (full extract) | — |
| Swarajya — CSDS 2021 WB/TN summary | https://swarajyamag.com/politics/explained-what-lokniti-csds-post-poll-survey-tells-us-about-recent-elections-in-tamil-nadu-and-bengal | UC/OBC/SC voting shares | referenced | 2026-04-24 |
| ISAS-NUS — Mamata beats Modi in WB (2024) | https://www.isas.nus.edu.sg/papers/indian-election-results-2024-mamata-beats-modi-in-west-bengal/ | 2024 LS gender swing (+11 pts) | referenced | 2026-04-24 |
| Shethepeople / CSDS — Women voters for Mamata | https://www.shethepeople.tv/news/women-voters-for-mamata-banerjee-post-poll-survey-by-lokniti-csds/ | Women × caste voting | referenced | 2026-04-24 |
| IWWAGE — NFHS-5 women's economic resources | https://iwwage.org/womens-control-over-their-economic-resources-evidence-from-nfhs-5/ | 61% WB women control money (NFHS-5) | referenced | 2026-04-24 |
| Trivedi Centre for Political Data (TCPD), Ashoka Univ. | https://tcpd.ashoka.edu.in/ | AC-level political covariates | planned | — |
| EAC-PM — Female LFPR working paper | https://eacpm.gov.in/wp-content/uploads/2024/12/EACPM-WP-Female-LFPR-India.pdf | Female LFPR national/state | referenced | 2026-04-24 |

## G. SIR / citizenship (tier D)

| Source | URL | Fed columns | Status | Access date |
|---|---|---|---|---|
| Free Press Journal — WB SIR row, myths, data | https://www.freepressjournal.in/analysis/west-bengal-sir-row-myths-data-and-the-voter-deletions-that-could-reshape-2026-elections | 91 lakh deleted, religion/gender breakdowns | referenced | 2026-04-24 |
| Outlook — SIR impact on Bengal's Muslim-majority constituencies | https://www.outlookindia.com/elections/how-does-sir-impact-bengals-muslim-majority-constituencies | Muslim-AC SIR concentration | referenced | 2026-04-24 |
| Outlook — Testing TMC's grip in Bengal's BJP bastion (north) | https://www.outlookindia.com/elections/assembly-elections-2026-testing-tmcs-grip-in-bjp-bastion-northern-bengal | District SIR deletion counts | referenced | 2026-04-24 |
| TheQuint — WB 7 lakh new voters | https://www.thequint.com/news/breaking-news/west-bengal-adds-seven-lakh-new-voters-assembly-elections | 2026 supplementary additions | referenced | 2026-04-24 |
| New Kerala — Women/third-gender deletion rates | https://www.newkerala.com/news/a/bengal-polls-women-voters-decline-slightly-higher-than-658.htm | Deletion rate by gender | referenced | 2026-04-24 |
| Millennium Post — Women outnumber men in 16 Phase 1 seats | https://www.millenniumpost.in/bengal/women-voters-outnumber-men-in-16-seats-in-phase-i-polls-656800 | Phase 1 gender split | referenced | 2026-04-24 |
| Zee News — Reserved seats kingmaker analysis | https://zeenews.india.com/india/the-power-of-84-why-reserved-seats-are-the-ultimate-kingmakers-in-bengal-3039842.html | 68 SC + 16 ST reserved seats | referenced | 2026-04-24 |

## H. Per-constituency / regional journalism (tier D)

| Source | URL | Fed columns | Status | Access date |
|---|---|---|---|---|
| Deccan Herald — North Bengal 54 seats battleground | https://www.deccanherald.com/elections/west-bengal/west-bengal-assembly-elections-2026-north-bengals-54-seats-emerge-as-key-battleground-bjp-seeks-to-retain-edge-tmc-eyes-gains-3975291 | N Bengal regional dynamics | referenced | 2026-04-24 |
| The Print — RSS growth in WB | https://theprint.in/opinion/from-nowhere-to-everywhere-how-rss-grew-in-west-bengal-to-benefit-bjp/645542/ | Shakha density, 2020 baseline | referenced | 2026-04-24 |
| Organiser — WB RSS 500 new shakhas (2023-25) | https://organiser.org/2025/03/28/284836/bharat/west-bengal-rss-expands-with-500-new-shakhas-focuses-on-hindu-unity-amid-demographic-concerns/ | RSS growth rate | referenced | 2026-04-24 |
| Business Standard — WB Assembly 2026 preview | https://www.business-standard.com/elections/west-bengal-elections/west-bengal-assembly-election-2026-can-mamata-banerjee-s-tmc-hold-off-bjp-126040201061_1.html | Campaign context, region-level | referenced | 2026-04-24 |
| The Print — Tea gardens in North Bengal | https://theprint.in/politics/how-tea-gardens-in-north-bengal-key-to-poll-fortunes-of-bjp-tmc-have-kept-both-guessing/641016/ | Tea-garden workforce, 408 gardens | referenced | 2026-04-24 |
| Outlook — Matua Mahasangha power play | https://www.outlookindia.com/elections/matua-mahasangha-maelstrom-family-feud-fuels-political-powerplay-in-matua-bastion | Thakurbari split, Bangaon Matua share | referenced | 2026-04-24 |
| Prabhat Khabar — Rajbanshi vote bank | https://www.prabhatkhabar.com/state/west-bengal/kolkata/assembly-election-2026-rajbanshi-community-vote-bank-politics-tmc-vs-bjp-north-bengal | Rajbanshi concentration, politics | referenced | 2026-04-24 |
| The Federal — Revival of tribal identity in Jangalmahal | https://thefederal.com/category/elections-2024//revival-of-tribal-identity-dominates-poll-mood-in-bengals-jangalmahal | "Ajodhya vs Ayodhya", ASA | referenced | 2026-04-24 |
| The Print — Furfura Sharif cleric launches party | https://theprint.in/politics/mamata-deceived-bengal-muslims-furfura-sharif-cleric-launches-party-ahead-of-polls/589871/ | Furfura / ISF influence, 30-40 seats | referenced | 2026-04-24 |

## I. Additional references (DemographicParameters.md already cites)

The ~60 URLs already catalogued in [`../DemographicParameters.md`](../DemographicParameters.md) are implicitly part of this dataset's source base. When a per-AC profile quotes a number from that document, it inherits the citation from there rather than re-listing here.

---

## Maintenance

- When a new scraper is added, list it in the **Fed columns** rows above with status `ingested` and an access date.
- When a URL 404s or the underlying data changes, mark the row with a ⚠ and add a note pointing to an archive.org snapshot if available.
- No cell in `constituencies.csv` should have a non-null value without at least one corresponding entry in `sources_json` traceable to this catalog.
