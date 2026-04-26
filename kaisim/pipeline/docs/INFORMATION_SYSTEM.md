# Kaisim — Information System

The information system is *how news reaches agents*: which events are
delivered to which agent in which period, with what salience. It is the
mechanism that produces realistic per-demographic ignore rates and
per-event differential reach.

## Three-step pipeline per (period, agent)

```
                NewsPool (active in period)
                            │
                            ▼
            ┌───────────────────────────────┐
            │  Targeting score per event    │
            │   = scope_weight              │
            │   + tag_overlap × per_tag_w   │
            │   + intensity_bonus           │
            │   × media_engagement          │
            │   + loss_aversion_kicker      │
            └───────────────────────────────┘
                            │
                            ▼
              score ≥ threshold (default 4.0)?
                  │ no              │ yes
                  ▼                 ▼
          silently dropped   ┌───────────────┐
            (not delivered)  │  Delivered to │
                             │  feeds.jsonl  │
                             └───────────────┘
                                     │
                                     ▼
                       LLM engagement decision
                  (engaged / skimmed / scrolled_past)
                                     │
                                     ▼
                if engaged or skimmed: write reaction
                            to memory_stream
```

## The events YAML — atomic news items

Each event lives in `simulations/<sim>/news/events_<period>.yaml`:

```yaml
- slug: caa_rules_notified
  date: "2024-03-11"                # OR date_start + date_end for chronic
  temporal: episodic                 # episodic | chronic
  scope: national                    # national | state | district | AC
  intensity: 5                       # 1-5
  headline: "CAA Rules 2024 notified after 4-year delay"
  summary: |
    Two-three sentence explainer of what happened and why it
    matters in this constituency.
  tags: [matua_refugee, muslim_voter, bjp_supporter, tmc_supporter]
  valence:
    matua_refugee:  positive    # pulls toward BJP
    muslim_voter:   negative    # pulls away from BJP
    bjp_supporter:  positive
    tmc_supporter:  negative
  broadcast: true                    # everyone with media engagement might see it
  sources:
    - https://en.wikipedia.org/wiki/CAA_Rules_2024
    - https://www.thehindu.com/news/...
```

**Critical asymmetry**: the *same* event has *opposite* valence for
different identities. This is the load-bearing feature of the targeting
system — it lets one event polarize across two demographics.

### Scope hierarchy

| Scope | Reach | Examples |
|---|---|---|
| `national` | all media-engaged voters everywhere | CAA Rules, Modi rallies, Ram Mandir, Kejriwal arrest |
| `state` | top of WB news cycle | Sandeshkhali, SSC scam, WB Assembly results, Lakshmir Bhandar |
| `district` | district-level resonance | Bangladesh temple attacks (geographic/community connection), Shahjahan arrest |
| `AC` | hyper-local | Modi Thakurnagar visit, Petrapole disruption, Thakurbari clashes, Shantanu renomination |

Pitfall: if news got national TV coverage, scope is at least `state` even
if it physically happened in one district. **Sandeshkhali was technically
N24P-located but its news scope was `state`** because it dominated WB
media for weeks.

### Intensity ladder (1-5)

| Int | Definition | Examples |
|---|---|---|
| 5 | Top-of-mind for affected demographic for weeks | CAA Rules, Lakshmir Bhandar launch, Partha arrest, WB AE results |
| 4 | Major news, persistent for days | Sandeshkhali, Cyclone Amphan, Shantanu MoS, Yaas |
| 3 | Notable but quickly displaced | BSF jurisdiction extension, Krishak Bandhu relaunch, electoral bonds |
| 2 | Minor, only registers in narrow demo | (rare in WB chronology) |
| 1 | Barely noticed | Procedural court hearings |

## The targeting algorithm — `rule_based`

Implemented in `pipeline/simulation/targeting/rule_based.py`. The full
score:

```
score(agent, event) =
    SCOPE_WEIGHTS[event.scope]                          # 1.0..2.0
  + TAG_W × |overlap(agent.tags, event.tags)|           # +1 per shared tag
  + INTENSITY_W × event.intensity                        # +1 per intensity unit ≥3
  × media_engagement(agent)                              # 0.3..1.5
  + LOSS_AVERSION_KICKER if event.valence is "negative"  # +1 — bad news travels
                                                         #       further than good
```

### Scope weights

```python
SCOPE_WEIGHTS = {"national": 1.0, "state": 2.0, "district": 3.0, "AC": 4.0}
```

Note: AC and district have *higher* base weight than national. Counterintuitive
unless you remember the multiplier: a district event passes the threshold
even for low-engagement personas, while a national event needs media
engagement + tag overlap + intensity to clear it. This produces the
realistic pattern that AC-specific news (Shantanu visits, Petrapole)
hits its target demographic hard while national news (Russia-Ukraine,
electoral bonds) hits diffusely and gets ignored a lot.

### Tag overlap

If the event has tags `[matua_refugee, muslim_voter, bjp_supporter]` and
the agent has tags `{matua_refugee, woman, bjp_supporter}`, overlap = 2,
adding +2 to score.

### Intensity bonus

For events with `intensity ≥ 3`, add `(intensity - 2)` — so 5 adds +3,
4 adds +2, 3 adds +1, ≤2 adds 0.

### Media-engagement multiplier

The whole pre-multiplied score is multiplied by `media_engagement` (range
0.3..1.5). This is why an illiterate elderly persona with no smartphone
sees only AC-level high-intensity news; a graduate urban smartphone-using
youth sees almost everything.

### Loss-aversion kicker

If the event's valence for *any* agent-tag is `negative`, add +1.
Behavioral-economics nod: bad news travels farther than good news, even
controlling for intensity.

### Threshold

Default `accept_threshold = 4.0`. Below → not delivered. Above → delivered
(written to `feeds.jsonl` with `accepted=true`); the LLM then decides
how to engage.

## What gets delivered: WB AC-95 example

For the n=100 WB AC-95 run:
  - **Total events delivered**: 2,436
  - **Total events accepted by LLM**: 2,263
  - **LLM ignore rate**: 7.1%
  - **Implicit dropping** (score below threshold, never shown to LLM):
    not counted in ignore rate (those are pre-LLM)

The ignore-rate by demographic is the cleanest validity check:

| Demographic | Ignore rate |
|---|---|
| ST_total | 15.2% |
| OBC_specific | 12.9% |
| Student | 13.0% |
| Unemployed | 10.1% |
| 18_22 cohort | 9.8% |
| Graduate | 8.7% |
| Muslim | 6.3% |
| 38_42 cohort | 4.6% |

ST_total being highest tracks: low political engagement + low welfare
exposure → most events feel "not for me." 38_42 cohort being lowest
tracks: peak political-engagement adult years + active scheme exposure.

## Engagement decision (LLM-side)

After delivery, the Park-minimal updater asks the LLM:

```
Given your persona and recent memory, you've seen this news event.
Decide:
  - engagement: scrolled_past | skimmed | engaged | obsessed
  - reaction: noted_no_change | shifted_my_view | hardened_my_view |
              made_me_doubt | made_me_angry
  - importance (1-10)
  - monologue (your inner thought)
  - structured_delta:
      party_lean_change: more_BJP | more_AITC | more_LeftINC |
                         more_Other | no_change
      salience_added: [keywords]
      trust_changes: {entity: +small|+large|-small|-large|no_change, ...}
```

If `engagement=scrolled_past` and `monologue` is empty, no MemoryItem is
written (saves storage + cost on next-tick context).

## Why this design works

The system has three nested filters, each catching a realistic dropout:

1. **Targeting score < threshold**: pre-LLM "this isn't your demographic"
2. **LLM engagement = scrolled_past**: post-LLM "I saw it but didn't care"
3. **LLM party_lean_change = no_change**: "I noticed but didn't change my mind"

The cumulative dropout produces the right magnitude of vote-stability:
85/100 agents stay with their 2019 prior, 15/100 switch — close to
realistic 4-year vote-stability rates seen in panel surveys.

## Adding a new strategy

To add `embedding_targeting.py`:

```python
class EmbeddingStrategy:
    def __init__(self, agent_embeddings, event_embeddings, threshold=0.55):
        self.aE, self.eE, self.t = agent_embeddings, event_embeddings, threshold

    def select(self, agent, candidate_events, period):
        out = []
        for e in candidate_events:
            sim = cosine(self.aE[agent.id], self.eE[e.slug])
            if sim >= self.t:
                out.append(e)
        return out
```

Drop into `targeting/`, register in `__init__.py`, reference in
`simulation_configs/embedding.yaml`. No orchestrator changes needed.
