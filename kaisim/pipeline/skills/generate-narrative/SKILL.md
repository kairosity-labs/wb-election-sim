---
name: generate-narrative
description: Research and write a constituency narrative.md — the frozen opinion-climate seed that LLM personas draw on during simulation. Use when the user says "write the narrative for AC NNN", "fill narrative.md for <constituency>", "seed the pre-<year> context for <name>", or "generate the persona context for <AC>".
---

# Kaisim — Generate a Constituency Narrative

You are writing a `narrative.md` for one constituency and one election year.
This file is the **primary LLM seed**: every persona generated for this AC
draws its psychological baseline, salience topics, and vote rationale from
what you write here.

**Output:** `constituency_data/constituencies/{id}_{name}/{year}/narrative.md`

---

## Step 1 — Confirm inputs

Before searching, confirm with the user:

| Input | Default if not stated |
|---|---|
| AC ID (3-digit) | Required — ask |
| AC name (folder slug) | Derive from `constituency_data/constituencies/` listing |
| Election year | Required — ask (typically `2019`) |
| Source election (for results) | Lok Sabha immediately preceding or containing the year |

Run:

```bash
ls constituency_data/constituencies/ | grep "^{AC_ID}"
```

to find the correct folder slug. The stub file should already exist at
`constituency_data/constituencies/{id}_{name}/{year}/narrative.md` — you
will overwrite it.

---

## Step 2 — Read the calibration data

Before web-searching, read what is already known about this AC from its
calibration layer. These files are the ground truth; do not contradict them.

```bash
# Read the calibration MD (the source-of-truth demographic profile)
cat constituency_data/constituencies/{id}_{name}/2019/{id}_{name}_2019.md | head -200

# Check which parties appear in the vote CSVs
head -3 constituency_data/constituencies/{id}_{name}/2019/csv/{id}_vote_religion_2019.csv
head -3 constituency_data/constituencies/{id}_{name}/2019/csv/{id}_vote_caste_2019.csv

# Read marginals for demographic anchors (religion, caste, migration)
head -60 constituency_data/constituencies/{id}_{name}/2019/csv/{id}_marginals.csv
```

Extract and note:
- Religion split (Hindu / Muslim / Sarna_ORP / Christian / Other)
- Caste top-5 categories + percentages
- Migration breakdown (native / refugee-origin / recent migrant)
- GP location names (urban / rural cluster labels)
- Economic status split

---

## Step 3 — Web research

Search for each topic below. Prioritize Wikipedia + Election Commission of
India + The Hindu / Indian Express / Wire / NDTV over blogs or thin sources.
Cross-verify vote percentages — do not guess them.

### 3a. Election results (required, verify numerically)

Search: `"{AC_NAME} assembly constituency 2019 election result"` AND
`"{LS_CONSTITUENCY_NAME} lok sabha 2019 result"` (the AC falls under an LS
seat — find the LS result too).

Note: Assembly constituency results from a LS year = AC-level breakdown of
the LS vote (Vidhan Sabha segment-wise). For a 2019 narrative, the relevant
vote is the **2019 Lok Sabha** and the **2016 Assembly** results.

Look up on: `results.eci.gov.in`, Wikipedia, `myneta.info`, `affidavit.eci.gov.in`.

Record:
- 2019 LS: winner party, winner %, runner-up party, runner-up %, turnout
- 2016 AC: winner party, winner %, runner-up party, margin
- LS constituency name that contains this AC

### 3b. Demographics and local identity

Search: `"{constituency_name} West Bengal demographics caste religion"`,
`"{district} district census 2011"`, `"scheduled tribe {constituency} West Bengal"`.

Focus on what is distinctive — what makes this AC's demographic mix
different from a generic WB rural AC.

### 3c. Political history and key events (year-frozen)

**STRICT TEMPORAL SCOPE: Only include events that were common knowledge
by 31 December of the target year. Anything that happened after that date
must be listed in the Out of Scope appendix.**

Search for:
- Major political events in the constituency in the 3 years before the target year
- Known local leaders and their affiliations **as of the target year** (people
  change parties — double-check the date of any defection, death, or win)
- Welfare schemes active in the state **as of the target year**
- Any significant local incidents (land acquisition disputes, communal
  incidents, cyclones / floods, industrial events)

### 3d. Economy and livelihood

Search: `"{constituency} economy livelihood agriculture industry"`,
`"{district} {primary crop OR industry} West Bengal"`.

Identify the 2-3 dominant livelihood modes (e.g., paddy farming + MGNREGA,
tea garden labour, jute/weaving, prawn farming, industrial belt).

### 3e. Media diet

Search: `"West Bengal Bengali news channel cable 2019"`. Media diet is
largely shared across WB but note any constituency-specific channels or
newspapers (e.g., Uttarbanga Sambad for North Bengal ACs).

---

## Step 4 — Write the narrative

Write the full narrative following the template below. Target 400–700 lines.
Do not pad; do not omit a section just because data is thin — use a short
paragraph with what you found and note gaps.

Use the AC 095 (Bangaon Uttar) file at
`constituency_data/constituencies/095_bangaon_uttar/2019/narrative.md`
as the **style and depth reference**. Match its:
- Paragraph length (2-5 sentences per paragraph, no bullet soup)
- Citation style: `[Source name](URL)` inline after the claim
- Temporal discipline: constant hedging phrases like "as of end-2019",
  "through {year}", "by {year}"
- Psychological texture in archetypes (name, age, gender, livelihood,
  emotional stake, vote trajectory — not just demographics)

---

### Template

```markdown
# Narrative — {id}_{name} — pre-{year}
<!-- SCOPE: Frozen at end of {year} state-of-knowledge. Do NOT include events from {year+1} onward. -->

**Purpose.** Narrative anchors for the LLM persona generator. Each
persona's psychology, salience topics, and {year} vote rationale should draw
on the conditions described here. This is **the world the persona lived in
through end-{year}** — nothing later.

> ⛔ **Strict {year}-frozen scope.** Do NOT reference: [list 5-8 specific
> post-{year} events that might be tempting to include, e.g. later elections,
> cyclones, policy changes, party defections, scam exposures]. The [last
> in-scope event] IS in scope; what happens after is not.

---

## 1. Who lives here

[2-3 paragraphs: geography, electorate size, dominant communities
(religion + caste), migration origin, linguistic character, urban/rural split.
Ground every claim in the calibration MD or Census 2011.]

---

## 2. The {year} LS political shock

[1-2 paragraphs: the LS result — winner, %, runner-up, %, margin, turnout.
The prior cycle result for comparison. What the shift (or continuity) means
for the AC's political story. Any known booth-level or segment-level
variation if findable.]

---

## 3. {CONSTITUENCY-SPECIFIC AXIS 1 — e.g. "The citizenship fault-line"}

[2-4 paragraphs on the most distinctive political/social axis for this AC.
Examples: CAA/NRC for Matua belt; land acquisition memory for Nandigram;
Maoist legacy for Jhargram; tea-garden labour contracts for Kalchini.
Tie the axis to how it appears as a vote driver.]

---

## 4. {CONSTITUENCY-SPECIFIC AXIS 2 — e.g. "The welfare stack"}

[2-4 paragraphs on the second most important axis. Often welfare delivery
(TMC schemes) vs. BJP's Hindu-identity offer. Use actual scheme names and,
where available, enrolment numbers.]

---

## 5. {CONSTITUENCY-SPECIFIC AXIS 3 — e.g. "Economy and livelihood"}

[2-4 paragraphs on the dominant livelihood and how it shapes political
preferences. Be specific: which crops, which industries, which middlemen,
what the price/wage story was in the year before the election.]

---

## 6. {CONSTITUENCY-SPECIFIC AXIS 4 — e.g. "The TMC machine"}

[2-3 paragraphs on the dominant party's local organisational grip, cut-money
dynamics, booth-level capture, and any notable weaknesses. For BJP-won ACs,
describe how BJP's local machine compared.]

---

## 7. {OPTIONAL AXIS 5 — e.g. "The opposition's case"}

[1-3 paragraphs on the challenger party's argument — what they offered,
why it resonated or didn't, which demographic segments they targeted.]

---

## 8. Media diet

[1 paragraph: Which Bengali-language TV channels, newspapers, and digital
sources dominate in this AC. Note any constituency-specific outlets.
Note WhatsApp / smartphone penetration in the rural areas.]

---

## 9. Common psychological archetypes

Use these as starting templates — vary, blend, and complicate them with
the demographic axes the persona has:

  - **[Archetype 1 name] ([age range], [gender], [settlement], [community]):**
    [3-5 sentences: livelihood, economic stake in welfare, emotional relationship
    with the dominant party, citizenship or identity anxiety if relevant,
    2019 vote decision and what drove it]

  - **[Archetype 2] ...** [repeat for 6–8 archetypes, covering:
    dominant religion/community, SC/ST if present, minority community,
    young voter, woman beneficiary of welfare, economic migrant or
    labourer, trader/small-business, opposition voter]

---

## 10. Vote-rationale shorthand

For quick persona seeding — one line per demographic group:

| Group | Dominant frame | Lean |
|---|---|---|
| [e.g. SC/Hindu majority] | [e.g. welfare delivery + Matua identity] | [TMC/BJP/split] |
| [Muslim minority] | ... | ... |
| [Young educated] | ... | ... |
| [Agricultural labourer] | ... | ... |
| [Trader/self-employed] | ... | ... |

---

## Appendix: Out of scope

The following developments are explicitly NOT part of this file's scope.
Personas seeded from this document should NOT know about them:

  - [Post-{year} event 1 — e.g. "Cyclone Amphan, May 2020"]
  - [Post-{year} event 2 — e.g. "COVID-19 lockdown, March 2020"]
  - [Post-{year} event 3 — e.g. "2021 Assembly election result"]
  - [Post-{year} party defection / death / scam exposure]
  - [Any national-level post-{year} policy change]
  - [Post-{year} welfare scheme launch — e.g. "Lakshmir Bhandar Aug 2021"]
```

---

## Step 5 — Verify before saving

Before writing the file, check:

- [ ] Vote percentages appear in at least one web source (not guessed)
- [ ] Every named politician's party affiliation is correct **as of the
      target year** (beware defections)
- [ ] No post-{year} event is in any section other than the Out of Scope appendix
- [ ] Religion, caste, migration percentages are consistent with the
      calibration CSV (`{id}_marginals.csv`)
- [ ] At least 6 archetypes cover the AC's demographic spread

---

## Step 6 — Write and confirm

Write the file:

```bash
# Target path
constituency_data/constituencies/{id}_{name}/{year}/narrative.md
```

After writing, print the line count and the first 10 lines to confirm.

---

## Common pitfalls

| Pitfall | Prevention |
|---|---|
| Hallucinated vote percentages | Always cite a source URL in the file |
| Leader still attributed to old party | Search "{name} party {year}" explicitly |
| Post-scope cyclone/scheme included | Put it in the Appendix; hedge with "would come later" |
| Generic WB narrative not AC-specific | Every section needs ≥1 AC-specific fact |
| Archetypes are demographic labels not people | Give each a livelihood, a stake, a feeling |
| Missing calibration data read | Always do Step 2 before Step 3 |

## Reference

- **Style model:** `constituency_data/constituencies/095_bangaon_uttar/2019/narrative.md`
- **Other completed narratives:** `constituency_data/constituencies/*/2019/narrative.md`
- **Calibration source:** `constituency_data/constituencies/{id}_{name}/2019/{id}_{name}_2019.md`
- **AC-level election results:** ECI `results.eci.gov.in`, Wikipedia, `myneta.info`
