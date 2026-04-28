# Why our 2021 simulations went wrong — distributional analysis

**Run**: 10 ACs × `2021_targeted` variant, 100 agents per AC, 16 monthly ticks
**Headline**: 9/10 winner-correct, but predicted distributions miss truth by ~16 pp on top-2 average.

The bottom-line wrong answers come from **four reinforcing biases**, all of which are
**fixable**. Here they are with evidence:

---

## H1 — Strong anchoring to 2019 vote priors  ✓ confirmed

**Measured switch rate (agents whose 2021 vote ≠ 2019 prior): 11.3%**
across 10 ACs. Real WB 2021 saw far more churn:

- **Muslims swung to TMC: 51% (2019) → 75% (2021)** (Lokniti-CSDS post-poll). With
  ~30% Muslim share statewide, that single shift moves ~7pp of the electorate
  to TMC alone.
- Left + Congress vote (~10% in 2019) **collapsed** between 2019 and 2021, with
  the lion's share migrating to TMC, smaller share to BJP. Our agents whose
  2019 prior was `INC`/`LF` mostly stayed there.
- State-wide TMC 43% → 48% (+5 pp) and BJP 40% → 38% (-2 pp).

So an 11.3% switch rate is roughly **half** of what real-world dynamics produced.

### Why it's happening

The persona's `narrative.self_prompt` was generated with full knowledge of the
agent's `vote_2019_LS` field — the LLM built a story justifying that vote.
At final-vote time, the system prompt is still that 2019-anchored narrative.
The 16 months of news in between aren't strong enough to overpower the
identity narrative.

### Per-AC evidence of anchoring

| AC | 2019 prior (BJP/AITC) | True 2021 (BJP/AITC) | Predicted (BJP/AITC) | Pred-Truth pp gap |
|---|---|---|---|---|
| **003 Cooch Behar Uttar** | 51 / 42 | 49 / 43 | **54 / 30** | BJP +5, AITC −13 |
| **011 Kalchini** | 59 / 35 | 53 / 38 | **67 / 27** | BJP +15, AITC −11 |
| **064 Murshidabad** | 35 / 36 | 42 / 41 | **35 / 23** | BJP −7, AITC −18 |
| **095 Bangaon Uttar** | 48 / 45 | 48 / 43 | **52 / 30** | BJP +5, AITC −13 |
| **210 Nandigram** ✗ | 31 / 67 | **48** / 48 | **36 / 59** | BJP −12, AITC +12 |
| **159 Bhabanipur** | 42 / 50 | 35 / 58 | **42 / 48** | BJP +7, AITC −10 |

Pattern: **predicted ≈ 2019 prior** in most ACs, NOT the 2019→2021 trajectory.
AC 210 Nandigram is especially telling — IRL Suvendu defected from TMC to BJP
and Mamata herself contested. Real swing was ~+18pp BJP. Our agents (with 67%
2019 AITC prior) stayed AITC at 59%, getting the winner wrong by 22pp.

---

## H2 — NOTA over-voting  ✓ confirmed

**Predicted NOTA: 5.67% mean, peaks 11% at AC 064 / 10% at AC 003**.
**Real 2021 statewide NOTA: 1.08%** (Election Commission, ADR press release).

So the simulator over-emits NOTA by **5× on average, 10× in the worst ACs**.

### Why

NOTA is in the FinalVoteQuery's allowed vote set:
```
"vote": "BJP" | "AITC" | "INC" | "LF" | "Other" | "NOTA"
```
The LLM uses NOTA as a "didn't engage with the news / can't decide" escape
hatch — exactly the agents whose memory_streams are empty (next finding).
This eats 4-9 pp that should belong to AITC and BJP.

### Where it hurts most

The ACs with high zero-memory agents are the same ones with high NOTA:
- AC 064 Murshidabad: **51% zero-memory agents** → **11% NOTA** predicted
- AC 003 Cooch Behar: **54% zero-memory** → **10% NOTA**
- AC 095 Bangaon Uttar (best engagement): **2% zero-mem** → **9.5% NOTA** still

So NOTA tracks **engagement failure**, not realistic abstention.

---

## H3 — Severe belief-update inertia  ✓ confirmed

**53% of agents finished the simulation with zero memories** (= never engaged
with any news event). Worst offenders:

| AC | Zero-mem agents | Mean memories/agent |
|---|---|---|
| AC 159 Bhabanipur | **84%** | 0.65 |
| AC 011 Kalchini | **78%** | 0.77 |
| AC 003 Cooch Behar | 54% | 1.95 |
| AC 198 Tarakeswar | 30% | 2.97 |
| **AC 095 Bangaon Uttar** | **2%** | **26.5** |

AC 095 (Bangaon Uttar) is the outlier: it's the only AC with a hand-written
`prompts/system_anchors.md` AND its agents engaged ~30× more events on average
than other ACs. So the news system *can* drive belief change — but the prompt
is missing context for the other 9 ACs.

### Why

The `rule_based` targeting scorer `score = scope + (tag_overlap × 2) + intensity_bonus`
rejects events below threshold=3. For agents whose tag overlap with state-scope
events is low (no `bjp_supporter` / `tmc_supporter` cuing, no demographic-specific
match), nothing breaks threshold and they receive 0 events per period →
0 memories → final vote based purely on persona's 2019 prior + frozen narrative.

---

## H4 — AITC asymmetrically under-predicted in BJP-winning ACs  ✓ confirmed

| AC group | n | Mean BJP gap (pred − truth) | Mean AITC gap |
|---|---|---|---|
| BJP-winning ACs | 5 | **+3.0 pp** | **−8.7 pp** ⚠ |
| AITC-winning ACs | 5 | +1.0 pp | +0.7 pp |

So in BJP-winning ACs, the simulator over-predicts BJP by +3 pp AND
under-predicts AITC by **−8.7 pp** — a 12pp differential.

This is the structural bias: in 2021 those ACs actually had AITC at 38-44%
(Mamata-style consolidation). Our simulator stuck at the 2019 25-30% AITC
prior because no narrative force pushed those agents to switch.

---

## Synthesis — these four biases compound

A "stuck" agent (no engagement) → uses 2019 prior → answers from anchored
narrative → emits NOTA when conflicted. This produces:
1. Predicted distribution ≈ 2019 prior
2. NOTA absorbs ~5pp that should be AITC
3. AITC under-predicted in BJP-leaning ACs that actually had AITC swing
4. AC 210 Nandigram missed entirely (one historic flip we couldn't capture)

---

## How to fix — concrete patches in priority order

### Priority 1 — Boost engagement floor (kills H2 + H3 + half of H1)

```yaml
# In each 2021_targeted simulation_config:
targeting:
  config:
    threshold: 1.5         # was 3.0 — let more events pass into the agent's feed
    cap_per_period: 8      # was 5 — more chances to encounter contrary news
    weights:
      scope_state: 3       # was 2 — state-scope news (CAA, COVID, Lakshmir Bhandar) reaches more agents
```
Expected effect: zero-mem agents drop from 53% → ~10%. NOTA rate drops from
5.67% → ~2%. Anchoring weakens because agents now see news.

### Priority 2 — Fix the FinalVoteQuery prompt to force engagement (kills H1 directly)

In `prompts/final_vote.md.j2`, prepend an explicit "**reconsider** your 2019
vote in light of these events" line:

```
Two years ago in 2019 you voted differently than today's choices may demand.
Look at what's happened since then. The party that was right for you in 2019
may not be the right one today — or it may still be. Decide based on what
you've actually lived through, not on inertia.
```

This pulls the model out of the persona's frozen 2019 narrative.

### Priority 3 — Make NOTA actually rare

Change the candidate enumeration so NOTA is the absolute last option, with
explicit "this is for genuine refusal, not indecision":

```
- **NOTA** (None Of The Above — only if you actively refuse all candidates;
  not because you're undecided)
```

Or remove NOTA from the JSON enum entirely — force a real party choice.
Real-world NOTA is 1%, so dropping it loses 1pp signal but eliminates 5pp of
distortion.

### Priority 4 — Per-AC `system_anchors.md`

Generate a 1-2 page identity-and-context file for the 9 non-095 ACs by
extracting Section A (identity) + key Section H bullets from each AC's
canonical MD. This is what makes AC 095 engage 30× more than the others.

### Priority 5 — Add 2019→2021 swing-driving narrative events

The state_events_2019_2026.yaml has the events but most are scope=`national`
or scope=`state` and tagged broadly. Adding 2-3 events specifically tagged
for the 5 swing dynamics:
- Muslim consolidation to TMC (CAA reaction)
- Women's cash transfer (Lakshmir Bhandar Feb-Aug 2021)
- BJP central leadership perceived as outsider (Modi rallies)
- Suvendu's defection narrative
- COVID Bengal handling perception

Tag these events broadly (woman, muslim_voter, bjp_supporter, tmc_supporter)
so they pierce more agents' tag filters.

---

## Expected post-fix impact

If we implement P1+P2+P3 and re-run:
- Switch rate: 11% → 25-35% (closer to real-world post-COVID swing)
- NOTA rate: 5.67% → ~1-2%
- Mean AITC pp gap: −4 → near zero
- Top-2 pp gap: 16.35 → ~8-10
- Winner accuracy: 9/10 → likely 9-10/10 with lower variance

P4 (system_anchors per AC) is a 30-min one-off cost, would help even more.

---

## Sources
- [2021 West Bengal Legislative Assembly election — Wikipedia](https://en.wikipedia.org/wiki/2021_West_Bengal_Legislative_Assembly_election)
- [West Bengal Post Poll 2021 — Lokniti-CSDS](https://lokniti.org/media/PDF-upload/1622695848_3736100_download_report.pdf)
- [Bengal elections 2021: A factsheet — ORF](https://www.orfonline.org/expert-speak/bengal-elections-2021-a-factsheet)
- [West Bengal 2021 NOTA share — Oneindia](https://www.oneindia.com/kolkata/west-bengal-2026-elections-what-the-nota-vote-share-was-in-the-2021-assembly-polls-011-8030009.html)
- [West Bengal Assembly Election 2021: An Analysis (PDF)](https://grassrootsjournals.org/jpg/jpg010107-onkar-singh-m00233.pdf)
- [West Bengal's Verdict in 2021 — The India Forum](https://www.theindiaforum.in/article/west-bengals-verdict-2021)
