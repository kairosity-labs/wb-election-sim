---
name: compare-runs
description: Compare two Kaisim simulation runs side-by-side — final vote distribution diffs, ignore-rate differences, switcher-matrix overlap, agent-level vote agreement. Use when the user wants to "compare two runs", "ablate a strategy change", "see what targeting changes did", or "diff the simulations".
---

# Kaisim — Compare Two Simulation Runs

Useful for ablations: same persona set, different targeting strategy
(`show_all` vs `rule_based`); or different LLM models; or different
event chronologies; or different psychological-scaffolding settings.

## Inputs

Two run directories from the same simulation folder, ideally on the same
persona set:

```bash
RUN_A=kaisim/simulations/<sim>/runs/<timestamp_A>_<config_A>
RUN_B=kaisim/simulations/<sim>/runs/<timestamp_B>_<config_B>
```

## Quick diff

```bash
python -c "
import json
from collections import Counter
def load(d):
    s = json.load(open(d + '/summary.json'))
    v = json.load(open(d + '/vote_distribution.json'))
    return s, v
sA, vA = load('$RUN_A')
sB, vB = load('$RUN_B')
print(f'A: {sA[\"vote_distribution\"]}  ignore={sA[\"ignore_rate\"][\"ignore_rate\"]}')
print(f'B: {sB[\"vote_distribution\"]}  ignore={sB[\"ignore_rate\"][\"ignore_rate\"]}')
print(f'\\nVote-share diff (B - A):')
for p in set(vA['pcts']) | set(vB['pcts']):
    print(f'  {p:8s} {vA[\"pcts\"].get(p,0):>5.1f} → {vB[\"pcts\"].get(p,0):>5.1f}  Δ={vB[\"pcts\"].get(p,0)-vA[\"pcts\"].get(p,0):+.1f}pp')
"
```

## Per-agent agreement

For runs on the SAME persona set, you can compute "did the same agent
vote the same way in both runs?":

```bash
python -c "
import json, glob
from pathlib import Path
A = Path('$RUN_A'); B = Path('$RUN_B')
agree = disagree = 0
flips = []
for adir_a in sorted((A/'agents').iterdir()):
    aid = adir_a.name
    fv_a = adir_a / 'final_vote.json'
    fv_b = B / 'agents' / aid / 'final_vote.json'
    if not fv_a.exists() or not fv_b.exists(): continue
    va = json.load(open(fv_a))['vote']; vb = json.load(open(fv_b))['vote']
    if va == vb: agree += 1
    else: disagree += 1; flips.append((aid, va, vb))
print(f'Agreement: {agree}/{agree+disagree} ({100*agree/(agree+disagree):.1f}%)')
print(f'Flipped: {disagree} agents')
for aid, va, vb in flips[:10]:
    print(f'  {aid}: A={va} → B={vb}')
"
```

Agreement of 80-95% is typical for runs differing only in a small
config tweak. Below 70% = the change you made is having a big effect
(could be intended, or a bug).

## Visual comparison

Plot the two final-vote distributions side-by-side:

```bash
python -c "
import json, sys
sys.path.insert(0, 'kaisim')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

vA = json.load(open('$RUN_A/vote_distribution.json'))['pcts']
vB = json.load(open('$RUN_B/vote_distribution.json'))['pcts']
parties = ['BJP','AITC','INC','LF','Other','NOTA']
A = [vA.get(p,0) for p in parties]
B = [vB.get(p,0) for p in parties]
fig, ax = plt.subplots(figsize=(9,5))
x = list(range(len(parties))); w = 0.35
ax.bar([i-w/2 for i in x], A, width=w, label='Run A', color='#4C72B0')
ax.bar([i+w/2 for i in x], B, width=w, label='Run B', color='#DD8452')
ax.set_xticks(x); ax.set_xticklabels(parties)
ax.set_ylabel('% of agents'); ax.legend(); ax.grid(axis='y', linestyle=':', alpha=0.5)
ax.set_title('Run comparison — final 2024 vote distribution', fontweight='bold')
fig.tight_layout(); fig.savefig('/tmp/run_compare.png', dpi=120)
print('Saved /tmp/run_compare.png')
"
```

## Reference

  - Sample comparison: `runs/20260425_230641_rule_based/` (run A)
    vs (a hypothetical) `runs/<ts>_show_all/` (run B)
