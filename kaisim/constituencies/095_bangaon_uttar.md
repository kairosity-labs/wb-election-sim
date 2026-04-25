# AC 095 — Bangaon Uttar (SC)

**District:** North 24 Parganas · **Region:** Presidency / Matua Belt · **2026 Phase:** Phase 2 (29 April 2026) · **Lok Sabha:** 14 Bangaon (SC) · **Total electors:** 241,337 (post-SIR, Jan 2026 qualifying date)

> Pilot profile #1 — the SCM test bed for the **Matua × SIR × CAA** axis. Every cell below carries a confidence tier (A–E per `/data/methodology.md` §1). Tier-D/E values are flagged inline; do not treat them as measurements.

## 1. Demographic snapshot

| Metric | Value | Tier | Source |
|---|---|---|---|
| AC number | 95 | A | ECI / Delimitation Commission WB 2008 |
| Reservation | SC | A | Delimitation Commission WB 2008 |
| Blocks / GPs covered | Bangaon municipality + 7 GPs of Bangaon CD Block (Akaipur, Chhaigheria, Dharma Pukuria, Ganganandapur, Ghatbore, Gopalnagar-I, Gopalnagar-II) | A | [Wikipedia — Bangaon Uttar AC](https://en.wikipedia.org/wiki/Bangaon_Uttar_(Vidhan_Sabha_constituency)) citing Delimitation Commission |
| 2026 total electors | 241,337 | A | [CEO WB SIR 2026 AC-wise draft roll](https://ceowestbengal.wb.gov.in/Downloads/SIR2026/AC%20wise%20Draft%20Elector%20SIR%202026.pdf) |
| Male / Female / Third-gender | 124,052 / 117,260 / 25 | A | CEO WB SIR 2026 |
| Polling stations | 276 | A | CEO WB |
| 2021 AE electorate (baseline) | 251,387 | A | ECI / [Wikipedia](https://en.wikipedia.org/wiki/Bangaon_Uttar_(Vidhan_Sabha_constituency)) |
| Net shrinkage vs 2021 | −3.98% | E | derived 251,387 → 241,337 |
| SIR deletions in AC 95 | ~34,109 (Phase 1 alone: 26,183) | **D** | [Outlook — Panic/anger in Matua belt](https://www.outlookindia.com/national/panic-anger-ripple-across-matua-belt-as-sir-deletions-reopen-citizenship-faultlines-before-wb-polls) — single journalistic source, validate via CEO WB roll-revision summary |
| SIR deletion % (of pre-SIR roll) | ~12.4% | E | computed 34,109 / (241,337 + 34,109) |
| Unmapped-voter share (Bongaon North) | 11.3% | D | [ETV Bharat / The Week](https://www.theweek.in/news/india/2025/12/16/this-community-in-west-bengal-has-the-highest-number-of-unmapped-voters-matua-sc-sir-election-commission.html) |

## 2. Caste composition

Census 2011 tables C-08 do not publish AC-level SC sub-group breakdowns; all sub-group numbers below are **tier E imputations** anchored on Bangaon CD Block + Bangaon LS-level shares.

| Group | AC 95 estimate (%) | Tier | Source / basis |
|---|---|---|---|
| **SC total** | ~46 | E | Bangaon CD Block 46.60% (Census 2011, tier A); municipality slightly lowers AC share |
| **Namasudra / Matua** | ~40 | **E (headline tier-E)** | [Outlook — Matua Mahasangha](https://www.outlookindia.com/elections/matua-mahasangha-maelstrom-family-feud-fuels-political-powerplay-in-matua-bastion) claims ~40% of ~19L Bangaon LS electorate are Matua; Bangaon Uttar is the LS core (Thakurbari seat) so share ≥ LS mean |
| Rajbanshi | <1 | E | Rajbanshis concentrated in North Bengal; negligible here |
| Bagdi | ~2 | E | Residual SC distribution inference |
| Poundra | ~1 | E | Residual SC distribution inference |
| Other SC | ~2 | E | |
| **ST total** | 3.6 | E | Bangaon CD Block 3.61% (Census 2011); small tribal pockets |
| **UC bhadralok** (Brahmin+Kayastha+Baidya) | ~10 | **E** | Very low in SC-reserved refugee AC; [Outlook — Bhadralok](https://www.outlookindia.com/national/opinion-political-collapse-of-bengals-upper-caste-bhadralok-hegemony-and-bjps-prize-news-357287) state baseline 20%, heavily down-weighted here |
| OBC (Mahishya / Kurmi / Teli / specific) | ~2 combined | E | Not a salient bloc in Bangaon |
| Other Hindu + Muslim OBC (residual) | ~22 | E | Residual by subtraction; includes non-bhadralok non-SC refugee Hindu middle castes + Muslim OBC fraction |

**Headline:** Matua / Namasudra concentration is the single heaviest causal weight in this AC. The Thakurbari split (Shantanu Thakur BJP / Mamatabala Thakur TMC) runs directly through this electorate (§7).

## 3. Language & ethnicity

Language distribution from Bangaon CD Block Census 2011 C-16 (Mother Tongue, tier A for block); AC 95 imputed (tier E).

| Language | AC 95 estimate (%) | Tier |
|---|---|---|
| Bengali | ≥98 | E (Bangaon CDB: 99.19% A) |
| Hindi | ~0.5 | E (Bangaon municipality trader fringe) |
| Urdu | <0.3 | E |
| Santhali / Rajbanshi / Nepali | ~0 | E |
| Other | ~0.2 | E |

Near-monolingual Bengali — reflects the refugee-Bengali-Hindu origin of the electorate.

## 4. Economic profile

Nearly all cells are **tier D/E** because SECC 2011 / MGNREGA / scheme dashboards publish at block-or-above, not AC. Explicit scrape TODOs are listed below in §8.

| Metric | AC 95 estimate | Tier | Source / imputation |
|---|---|---|---|
| BPL household % (SECC 2011) | _pending_ | — | Scrape `secc.gov.in` block=Bangaon, then weight to AC by population. Census-2001 CDB baseline: 27.70% ([Wikipedia — Bangaon CDB](https://en.wikipedia.org/wiki/Bangaon_(Community_development_block))) |
| MGNREGA worker share (% of households) | _pending_ | — | Scrape `nrega.nic.in` MIS block=Bangaon, scale to AC |
| Per-capita income band (ordinal 1–5, 5 = highest) | 3 (mid-rural) | D | N24P rural Bangaon sub-div below state mean, above tribal-belt ACs |
| Agri household % | ~55 | E | Cultivator+Ag-labourer main-worker share 61.89% in CDB (Census 2011 A); household scale ~55% |
| Out-migrant worker % of working-age males | 8–15 | D/E | Documented Matua migration to Kerala (construction), TN/Karnataka (textile), Gulf (masonry); no AC-level survey. [PMC-Springer — WB migrants to Kerala](https://pmc.ncbi.nlm.nih.gov/articles/PMC9208344/) |

SIR interaction: Bangaon Uttar's out-migrant males are a heavy over-representation in the "absent at time of SIR" deletion category — one reason the 11.3% unmapped-voter figure is so concentrated here (see §1).

## 5. Education

Census 2011 Bangaon CD Block / sub-division (tier A); AC 95 imputed (tier E).

| Metric | AC 95 estimate (%) | Tier | Source |
|---|---|---|---|
| Literacy (overall) | 80.6 | E | Bangaon sub-div 80.57% A; municipality pulls up |
| Literacy (male) | 84.3 | E | Bangaon CDB male 84.27% A |
| Literacy (female) | 74.8 | E | Bangaon CDB female 74.84% A |
| Graduate+ | ~8 | E | N24P district ~9–11% (Census C-08); AC slightly below |
| Unemployed-educated-youth salience (% of educated youth jobless) | ~18 | D | Adjacent to WBSSC 2016-panel scrap narrative; Matua aspirant-class exposure ([ThePrint — Matua SIR](https://theprint.in/india/bengals-matua-factor-fuming-over-sir-slow-citizenship-drive-matuas-say-being-used-as-pawns/2910251/)) |

## 6. Welfare scheme footprint

**All AC-level figures here are tier E.** Public dashboards for LB / Krishak Bandhu / Swasthya Sathi / Khadya Sathi / Kanyashree / pensions publish at block or district, never AC. The numbers below are population-weighted scaled from Bangaon block or N24P district totals — useful as priors, not measurements. Scrape scripts are queued (§8).

| Scheme | AC 95 estimate | Tier | Basis |
|---|---|---|---|
| Lakshmir Bhandar (women beneficiaries) | ~60,000 | E | State ~2.2 crore B; N24P ~22–24 lakh E; AC 95 ≈ 2.5% of N24P pop |
| Krishak Bandhu (farmer + bargadar beneficiaries) | ~17,500 | E | State ~1.05 crore B; scaled by CDB cultivator count 32,922 A × AC share of CDB |
| Swasthya Sathi coverage (% of families) | ≥90 | E | Near-universal scheme; state coverage >95% B |
| Khadya Sathi coverage (% of population) | ~87 | E | State coverage ~90% B |
| Kanyashree (active girl students) | ~12–15k | E | State ~81 lakh enrolled B; scaled by school-age girl population in AC |
| Old-age / widow / Manabik pensioners | ~8–12k | E | Scaled from district; SC/ST recipients eligible for ₹1,200/mo, others ₹1,000 |

Welfare footprint is heavy on the **women + cultivator** axes (the TMC's core patronage channels). Shantanu Thakur's BJP counter-channel is the CAA help-desk network at Thakurnagar (reported ₹800/application) — [The Wire — CAA help-desks](https://m.thewire.in/article/rights/rs-800-for-citizenship-at-union-ministers-camp-bjp-caa-applications).

## 7. Political dynamics

Vote history — all tier A (ECI).

| Year | Contest | Winner | % | Runner-up | % | Margin |
|---|---|---|---|---|---|---|
| 2011 AE | AC 95 | Biswajit Das (AITC) | 54.55 | Dr. Biswajit Biswas (CPI(M)) | 40.12 | 23,620 |
| 2016 AE | AC 95 | Biswajit Das (AITC) | 50.59 | Sushanta Baowali (AIFB) | 33.07 | 33,192 |
| 2019 LS | Bangaon (overall) | Shantanu Thakur (BJP) | 48.85 | Mamata Thakur (AITC) | 40.92 | 111,594 |
| **2021 AE** | **AC 95** | **Ashok Kirtania (BJP)** | **47.65** | Shyamal Roy (AITC) | 42.54 | **10,488** |
| 2024 LS | Bangaon (overall) | Shantanu Thakur (BJP) | 48.19 | Biswajit Das (AITC) | 43.25 | 73,693 (compressed 34% vs 2019) |
| **2024 LS AC-95 segment lead** | — | BJP (est.) | — | — | — | ~8–12k lead (E — needs ECI Form-20) |

### 2026 contest (declared candidates)

| Party | Candidate | Confidence |
|---|---|---|
| BJP | **Ashok Kirtania** (incumbent MLA) | D ([AajTak](https://www.aajtak.in/elections/assembly-chunav/west-bengal/bangaon-uttar-assembly-result-19095) / [Oneindia](https://www.oneindia.com/bongaon-uttar-assembly-elections-wb-95/)) |
| CPI(M) — Left-Cong-ISF morcha (Left Front seat) | Pijush Kanti Saha | D |
| INC (dual-contest signal) | Nilanjan "Bapi" Saha | D — suggests morcha seat-share not fully enforced |
| AITC | **Unconfirmed** — aggregators auto-fill "Biswajit Das" but this conflicts with his LS role; needs validation against TMC 291-list PDF (17 Mar 2026) | D |
| BSP | Subrata Biswas | D |
| SUCI(C) | Shyamsundar Haldar | D |
| ISF (independent run) | Not surfaced | — |

### Causal forces running through AC 95

1. **Thakurbari split** — Shantanu Thakur (BJP, Union MoS, Bangaon MP) controls Matua Mahasangha patronage through the CAA help-desk channel; Mamatabala Thakur (TMC, RS MP) controls state-welfare patronage (Lakshmir Bhandar, Swasthya Sathi, Namasudra Development Board). AC 95 is the Thakurbari seat itself — the contest is functionally a proxy for the family feud. ([Outlook — Matua Mahasangha](https://www.outlookindia.com/elections/matua-mahasangha-maelstrom-family-feud-fuels-political-powerplay-in-matua-bastion))
2. **CAA 2024 rollout disappointment** — CAA rules notified 11 Mar 2024; of ~1.12 lakh state-wide applications, only ~15,000 citizenships granted by late 2025. Gaighata (AC 97, same LS) reports ~100 grants against 4,000+ applicants. Slow processing + documentation catch-22 has produced measurable Matua drift back toward TMC at the margin. ([ThePrint — Matua disappointment](https://theprint.in/india/bengals-matua-factor-fuming-over-sir-slow-citizenship-drive-matuas-say-being-used-as-pawns/2910251/); [The Wire — CAA process](https://m.thewire.in/article/rights/matua-west-bengal-caa-citizenship-process))
3. **SIR "unmapped voter" panic** — Matua Mahasangha GS Mahitosh Baidya claims >50% of Matuas omitted from draft roll. Shantanu: "don't worry, CAA will grant citizenship." Mamatabala: "post-2002 arrivals will lose voting rights." The frame itself is the contest. ([Outlook](https://www.outlookindia.com/national/panic-anger-ripple-across-matua-belt-as-sir-deletions-reopen-citizenship-faultlines-before-wb-polls))
4. **Women-voter welfare stack** — 117,260 female electors of 241,337 (48.6%); near-universal Lakshmir Bhandar reach; TMC's floor in this AC rests on this bloc irrespective of Matua factionalism.

### SCM linkage (cross-reference to [`../DemographicParameters.md`](../DemographicParameters.md) top-15 nodes)

| DP top-15 node | Activation in AC 95 |
|---|---|
| 1. SIR deletions | Very high — 34k deletions, 11.3% unmapped-voter share |
| 2. Muslim consolidation | Low — ~14% Muslim |
| 3. Women / LB beneficiaries | High — 117k female electors, near-universal LB |
| 4. Matua / Namasudra | **Highest** — ~40% of electorate, Thakurbari seat |
| 8. OBC (Mahishya / Kurmi) | Low — not an OBC-dominant AC |
| 9. UC bhadralok | Low — SC-reserved, refugee-dominated |
| 10. Out-migrant workers | High — notable Matua out-migration; SIR-absent deletion over-representation |
| 11. Welfare stack | High — TMC floor |
| 12. CAA beneficiaries | **Highest** — epicenter of rollout disappointment |
| 13. SSC-scam youth | Moderate — adjacent narrative |

## 8. Sources & caveats

### Primary sources consulted (full URL list)

- [Wikipedia — Bangaon Uttar AC](https://en.wikipedia.org/wiki/Bangaon_Uttar_(Vidhan_Sabha_constituency))
- [Wikipedia — Bangaon LS constituency](https://en.wikipedia.org/wiki/Bangaon_Lok_Sabha_constituency)
- [Wikipedia — Bangaon CD Block](https://en.wikipedia.org/wiki/Bangaon_(Community_development_block))
- [Wikipedia — Bangaon subdivision](https://en.wikipedia.org/wiki/Bangaon_subdivision)
- [Wikipedia — North 24 Parganas district](https://en.wikipedia.org/wiki/North_24_Parganas_district)
- [Wikipedia — Special Intensive Revision](https://en.wikipedia.org/wiki/Special_Intensive_Revision)
- [ECI Bangaon LS 2024 result](https://results.eci.gov.in/PcResultGenJune2024/ConstituencywiseS2514.htm)
- [CEO WB — SIR 2026 AC-wise Draft Elector PDF](https://ceowestbengal.wb.gov.in/Downloads/SIR2026/AC%20wise%20Draft%20Elector%20SIR%202026.pdf)
- [N24P district — SIR 2026 page](https://north24parganas.gov.in/special-intensive-revision-sir-2026/)
- [Outlook — SIR panic in Matua belt](https://www.outlookindia.com/national/panic-anger-ripple-across-matua-belt-as-sir-deletions-reopen-citizenship-faultlines-before-wb-polls)
- [Outlook — Matua Mahasangha family feud](https://www.outlookindia.com/elections/matua-mahasangha-maelstrom-family-feud-fuels-political-powerplay-in-matua-bastion)
- [ETV Bharat — Matua unmapped voters](https://www.etvbharat.com/en/state/matua-community-in-panic-over-unmapped-voters-in-west-bengal-draft-electoral-rolls-enn25122002312)
- [ThePrint — Matua SIR + citizenship](https://theprint.in/india/bengals-matua-factor-fuming-over-sir-slow-citizenship-drive-matuas-say-being-used-as-pawns/2910251/)
- [ThePrint — BJP CAA help-desks](https://theprint.in/india/bjp-rolls-out-caa-help-desks-to-blunt-mamatas-bengali-asmita-pitch-in-crucial-matua-belt/2711222/)
- [The Quint — Bengal Matua ground report](https://www.thequint.com/news/politics/bengal-elections-matua-vote-sir-deletions-bjp-votebank-ground-report)
- [The Wire — Matua CAA process](https://m.thewire.in/article/rights/matua-west-bengal-caa-citizenship-process)
- [The Wire — CAA welfare split among Matuas](https://m.thewire.in/article/caste/how-caa-and-welfare-schemes-have-divided-the-matuas-in-bengal)
- [The Wire — ₹800 for citizenship at BJP camps](https://m.thewire.in/article/rights/rs-800-for-citizenship-at-union-ministers-camp-bjp-caa-applications)
- [The Week — Unmapped voters analysis](https://www.theweek.in/news/india/2025/12/16/this-community-in-west-bengal-has-the-highest-number-of-unmapped-voters-matua-sc-sir-election-commission.html)
- [The Squirrels — WB voter deletion algorithm analysis](https://thesquirrels.in/policy/west-bengal-voter-deletion-eci-algorithmic-deduplication-11758463)
- [MyNeta WB 2021 AC 95](https://www.myneta.info/WestBengal2021/index.php?action=show_candidates&constituency_id=95)
- [MyNeta WB 2026](https://www.myneta.info/WestBengal2026/)
- [AajTak — AC 95 result page](https://www.aajtak.in/elections/assembly-chunav/west-bengal/bangaon-uttar-assembly-result-19095)
- [Oneindia — AC 95 profile](https://www.oneindia.com/bongaon-uttar-assembly-elections-wb-95/)
- [Voterlist.co.in — Bangaon Uttar](https://voterlist.co.in/bangaon-uttar/)
- [WBXpress — AC schedule](https://wbxpress.com/assembly-constituencies-west-bengal-2026/)
- [PIB — WB poll schedule](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2253728&reg=3&lang=1)
- [N24P district profile PDF](https://wbmsmeefc.wb.gov.in/documents/district_profiles/district_profile_north_24_paragnas.pdf)

### Validation to-dos before production use

1. **CEO WB roll diff** — download `AC wise Draft Elector SIR 2026.pdf` + confirm 241,337 / TG=25 / 276 PS; cross-check 34,109 deletion count against CEO WB revision summary tables.
2. **ECI Form-20 2024 LS** — pull polling-station-level BJP / TMC split for AC 95 inside Bangaon LS to replace the tier-E "~8–12k BJP lead" with a measured value.
3. **Census 2011 DCHB N24P Part-A** — use GP-level religion / language / SC tables to compute a weighted AC rollup (7 rural GPs + Bangaon municipality) replacing the CDB-level tier-A values with AC-level tier-A values.
4. **TMC candidate confirmation** — pull AITC 291-list PDF (release date 17 Mar 2026) to resolve the TMC candidate identity — aggregator auto-fill is unreliable.
5. **SECC 2011 scrape** — run `scripts/scrape_secc2011.py` block=Bangaon to replace the blank `bpl_household_pct_secc` cell.
6. **MGNREGA scrape** — `scripts/scrape_mgnrega.py` block=Bangaon.
7. **Swasthya Sathi scrape** — `scripts/scrape_swasthya_sathi.py` block=Bangaon + Bangaon municipality for actual coverage %.
8. **Outlook 34,109 deletion count** — try to independently corroborate via ECI Form 7 / CEO WB roll-revision tables; currently single-source tier D.

### Tier-D/E reliance flags (what to distrust)

- All caste sub-group shares (§2) are tier E; the Matua ~40% figure has a journalistic anchor but is not a measurement.
- All welfare scheme counts at AC level (§6) are tier E population-scaled district figures — use as priors only.
- 2024 LS AC-95 segment lead (§7) is tier E; needs Form-20.
- Out-migrant worker % (§4) is a tier D/E inference from migration literature.
- UC bhadralok % (§2) is a qualitative down-weighted state estimate, not a measured number.
- The SIR deletion count (34,109) rests on a single Outlook source — retain tier D until corroborated.
