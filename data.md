# Data Collection Rules — kaisim / WB Election Simulation

Rules to follow whenever collecting or authoring data in this repo. Applies
to structured (CSV/JSON), unstructured (PDFs, scraped pages, manifestos),
and news-event (YAML) layers.

## A. Cross-cutting rules (apply to all data)

1. **Real sources only.** Every datum must be traceable to a real, citable
   source: ECI, Census of India, Wikipedia (English), mainstream press
   (Hindu, Wire, Indian Express, Telegraph India, Anandabazar Patrika),
   myneta.info, or an official party manifesto PDF. **Never fabricate URLs
   or invent sources.**
2. **Primary > secondary > tertiary.** Prefer ECI/Census raw data over
   Wikipedia summaries. Use Wikipedia only when primary is unavailable or
   when consolidating cross-references.
3. **Scrape sub-AC first.** If sub-AC (booth/segment) data exists, attempt
   the scrape before falling back to district rollup. Document the
   fallback when used.
4. **Stay upstream.** This repo produces upstream MD/YAML/CSV per
   constituency. Do **not** write population samplers or narrative engines
   here — that lives in the co-founder's simulation code.
5. **Absolute dates only.** Convert "Thursday", "next month", "after the
   poll" to ISO `YYYY-MM-DD` at write time. Relative dates rot.
6. **Reproducible scripts.** Every generated CSV/JSON must have its
   producing script committed alongside it under
   `kaisim/pipeline/...`. No artisanal one-off CSVs.
7. **Calibrated layers are frozen.** `calibrated_2019` reflects the state
   of knowledge as of 2019. Do **not** backport 2021+ findings into it.
   Same rule for any future calibrated_<year> layer.
8. **Note source discrepancies, don't silently reconcile.** When two
   sources disagree (e.g., AC numbers across delimitations, candidate
   names across press reports), record both and annotate which is used
   downstream and why.
9. **Verify before claiming complete.** Run a validation pass (cutoff
   compliance, tag vocabulary, file existence) before reporting work done.

## A.1 Required electoral data sources (per constituency)

For every constituency under study, the following must be collected and
joined at the AC level. These are **mandatory inputs** before any
event-layer or simulation work.

1. **2019 Lok Sabha — assembly-segment-level voting data.**
   File: `2019_AssemblySegmentLevelVotingData.csv` (repo root).
   Granularity: per AC segment, per party, per candidate, with absolute
   vote counts. Use this to derive 2019 LS-projection-onto-AC vote
   shares.
2. **2024 Lok Sabha — assembly-segment-level voting data.**
   File: `2024_AssemblySegmentLevelVotingData.csv` (repo root).
   Same granularity as 2019. Use to compute the 2019→2024 swing per AC.
3. **2021 WB Assembly Election — detailed results PDF.**
   File: `2021-detailed-results.pdf` (repo root). This is the primary
   source for AC-level 2021 vote counts. Per AC, extract:
   - Winner name + party (cross-check by web-searching the seat name +
     "2021 winner" if the PDF entry is ambiguous or partially scanned)
   - **Per-candidate vote counts** for all candidates listed on the seat
   - **Per-party total** (sum across that party's candidates if multiple,
     usually one)
   - **Per-vote totals** (NOTA, postal ballots, total valid votes, total
     electors, turnout %)
4. **Mandatory fields per AC × election.** For 2019 LS-segment, 2021 AE,
   2024 LS-segment — record at minimum:
   - `ac_number`, `ac_name`, `election_year`, `election_type`
   - `candidate_name`, `party`, `votes` (one row per candidate)
   - `total_valid_votes`, `nota_votes`, `postal_votes`, `total_electors`,
     `turnout_pct`
   - `winner_name`, `winner_party`, `margin_votes`, `margin_pct`
5. **Cross-checking rule.** If the 2021 PDF page for an AC is illegible,
   partially OCR'd, or missing a candidate row, **search online** for the
   winner and the second-place candidate (Wikipedia AE-2021 page,
   ECI archives, or mainstream press recap), and reconcile. Annotate
   the source of any reconciled row.
6. **Per-vote / per-party / per-candidate granularity is non-negotiable.**
   Do not collapse to "BJP got X%, TMC got Y%". The simulation needs
   the full candidate slate (incl. small parties + independents) because
   defections, candidate-swaps, and minor-party transfers are signals
   the narrative engine uses.
7. **Output canonical CSVs.** For each constituency under study, produce:
   - `ac<NNN>_results_2019_ls.csv`
   - `ac<NNN>_results_2021_ae.csv`
   - `ac<NNN>_results_2024_ls.csv`
   one row per candidate, with the mandatory fields above. Commit the
   extraction script alongside.

## B. Structured data (CSVs, JSON)

1. **Header attribution.** Either embed source in the column header
   (`turnout_2019_eci`) or document it in a sibling `.README.md` /
   `metadata.json`.
2. **Versioning by year.** Election-year data must include the year in the
   filename: `2019_AssemblySegmentLevelVotingData.csv`,
   `2024_AssemblySegmentLevelVotingData.csv`. Never overwrite.
3. **Delimitation awareness.** AC serial numbers changed in the 2008
   delimitation. When mixing pre-2008 and post-2008 data, annotate which
   delimitation each row uses. WB 2026 ECI numbering may also differ from
   internal/reference numbering — note both when they diverge.
4. **Census vintage.** State which Census round (2011, 2021 if released)
   any demographic figure comes from. Do not chain estimates.
5. **No silent units.** Percent vs share, vote count vs vote share, INR
   lakh vs crore — always state units in the header or metadata.
6. **Missing != zero.** Use `NA` / empty, never `0`, for missing data.

## C. Unstructured data (PDFs, scraped HTML, manifestos)

1. **Keep the raw artifact.** Commit the PDF / HTML snapshot alongside any
   extracted text. Future extractions may need to re-parse.
2. **Extraction script alongside output.** If text was extracted via
   pymupdf / BeautifulSoup / pdfplumber, commit the script. No "I ran
   pymupdf in my head" extractions.
3. **Quote manifestos verbatim.** Party promises ("Lakshmir Bhandar
   ₹1,000/mo for SC/ST, ₹500/mo general") must be quoted, not paraphrased.
   Paraphrasing introduces drift between what was promised and what is
   simulated.
4. **Cite page numbers.** When pulling from a multi-page PDF (manifesto,
   ECI affidavit, Wikipedia AE page export), record the page or section.
5. **Snapshot URL + access date.** Web sources can change. Record both the
   URL and the date it was accessed.

## D. News events (YAML — `events_<period>.yaml`)

Authoritative spec: `kaisim/pipeline/skills/add-news-event/SKILL.md`.
Operative rules I must always apply:

1. **Cutoff is hard.** No event's `date` or `date_start` may exceed
   `cutoff_date`. Post-election "for context" events go in the next
   period's file, not this one.
2. **Episodic vs chronic.**
   - `episodic` → single `date:` (cyclone landfall, court ruling, defection)
   - `chronic` → `date_start:` + `date_end:` (COVID era, scheme rollout,
     ongoing scandal)
3. **Scope by news cycle, not geography.** If a story got national TV
   coverage, scope is at least `state` even if it physically happened in
   one block (Sandeshkhali rule).
4. **Intensity 1–5 with anchors.** Calibrate against:
   - 5: top-of-mind for weeks (CAA Rules, LB launch, Partha arrest)
   - 4: major, days-long (Sandeshkhali, Cyclone Amphan)
   - 3: notable but displaced (cabinet reshuffle, BSF jurisdiction extension)
   - 2: narrow demographic only
   - 1: barely registers (procedural hearings)
5. **Controlled tag vocabulary only.** Identity (matua_refugee, woman,
   elderly, upper_caste_hindu, bhadralok, muslim_voter), economic
   (cultivator, ag_labourer, urban_trader, petrapole_economy,
   out_migrant_household, school_age_household), welfare-beneficiary
   (lakshmir_bhandar_beneficiary, krishak_bandhu_beneficiary,
   swasthya_sathi_beneficiary, khadya_sathi_beneficiary,
   kanyashree_household, sabuj_sathi_household), partisan
   (bjp_supporter, tmc_supporter). New tags require updating
   `derived/persona_tags.py` in the same change.
6. **Valence per tag.** `positive` / `negative` / `ambient`. Always
   include both `bjp_supporter` and `tmc_supporter` valence.
7. **Critical asymmetry.** The same event often has **opposite** valence
   across identities. CAA Rules: matua_refugee=positive,
   muslim_voter=negative. Don't forget the opposite-valence pair.
8. **Broadcast flag.** `true` for national/state scope at intensity ≥4
   (TV/radio reach). `false` for AC-scope identity-specific events
   (Mahasangha pamphlets, mosque networks, trader WhatsApp groups).
9. **At least one real URL in `sources:`.** Wikipedia, ECI, mainstream
   press, or reputable secondary. **No fabricated URLs.**
10. **Promise vs delivery are distinct events.** A manifesto guarantee
    ("BJP promises ₹2,000/mo to women, 2024") is one event; the actual
    rollout / payment ("LB amount hiked to ₹1,200, Apr 2024") is another.
    Voters update on both, asymmetrically.
11. **Multi-period replication.** When the same event is relevant in
    multiple period files (e.g., COVID hits both 2019_2021 and
    2019_2024), it must appear in each file the period covers. Keep slug
    and metadata identical across files.
12. **Slug is snake_case and unique within the file.** Re-use the same
    slug across period files for the same underlying event so cross-file
    joins work.
13. **Headline = one sentence. Summary = 2–3 sentences** explaining what
    happened and why it matters for voters in this constituency. Be
    specific about geographic + identity relevance.

## E. Per-constituency files (`news/<period>/ac<NNN>_<slug>/`)

1. **Directory naming.** `ac<3-digit-AC>_<snake_case_name>` using the
   internal/reference AC number. If the ECI/PDF AC number diverges (e.g.,
   post-delimitation), keep the directory name stable and annotate the
   discrepancy inside the YAML's candidate event headline + summary.
2. **National + state events go in every constituency file** for that
   period. AC-specific events go only in the relevant directory.
3. **Candidate events.** When candidate names come from a PDF/Wikipedia
   table, cite the table version (URL + access date). Update names if
   later sources correct earlier scrapes; note the supersession.

## F. What NOT to do

- Don't add post-election events to satisfy "for completeness."
- Don't paraphrase manifesto promises into your own wording.
- Don't introduce new tags without updating `persona_tags.py`.
- Don't omit the opposite-valence pair on polarizing events.
- Don't silently overwrite a CSV with new data — version it by year.
- Don't fabricate URLs, candidate names, vote shares, or affidavit
  details. If a source can't be found, leave the field empty and flag it.
- Don't write simulation/sampler/engine code in this repo.

## G. Reference

- Event schema: `kaisim/pipeline/skills/add-news-event/SKILL.md`
- Tag derivation: `kaisim/simulations/<sim>/derived/persona_tags.py`
- Targeting selector: `kaisim/pipeline/simulation/targeting/rule_based.py`
- Pilot seat reference: `kaisim/simulations/wb_2021_ac095/`
