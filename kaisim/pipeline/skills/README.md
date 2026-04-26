# `kaisim/pipeline/skills/` — reusable workflow skills

Each subdirectory contains a `SKILL.md` (Claude Code skill format) that
documents a reusable Kaisim workflow. Skills here are repo-internal so
they're versioned with the codebase.

## Available skills

| Skill | When to use |
|---|---|
| [`new-constituency`](new-constituency/SKILL.md) | Scaffold a brand-new (region, election) simulation under `simulations/<sim_name>/` |
| [`run-calibration`](run-calibration/SKILL.md) | Run pre-LLM rule-based persona generation + verifier audit |
| [`run-simulation`](run-simulation/SKILL.md) | Launch the full LLM belief-evolution simulation |
| [`analyze-run`](analyze-run/SKILL.md) | Generate the full analysis pack for a completed run |
| [`add-news-event`](add-news-event/SKILL.md) | Add a single news event to an existing simulation's events YAML |
| [`compare-runs`](compare-runs/SKILL.md) | Side-by-side diff two simulation runs (ablation studies) |

## How to use

For Claude Code sessions running in this repo, configure
`.claude/settings.json` to discover skills here:

```json
{
  "skills": {
    "discoveryPaths": ["kaisim/pipeline/skills"]
  }
}
```

Then invoke as `/skill-name` (e.g., `/run-simulation`).

For non-Claude-Code use, treat each `SKILL.md` as a runnable playbook —
the markdown body is a step-by-step recipe with copy-pasteable shell
commands.

## Adding a new skill

1. `mkdir kaisim/pipeline/skills/<name>/`
2. Create `SKILL.md` with frontmatter:
   ```yaml
   ---
   name: <name>
   description: <one sentence — when to use>
   ---
   ```
3. Body is a playbook: prerequisites, steps with commands, expected output,
   common pitfalls.
4. Update this README's table.
