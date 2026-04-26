## Batch guidance

Use the gap report above to bias this batch's picks. Practical heuristics:

- A category with `gap_pp` strongly **negative** (target > observed) means
  you should generate **more** personas with that category. The bigger the
  |z|, the more you should over-weight it.
- A category with `gap_pp` strongly **positive** (observed > target) means
  you should generate **fewer** of that category in this batch.
- If multiple gaps are coupled (e.g., `Student` is under AND `18_22 age` is
  fine), one persona that combines `age=18_22` + `workforce=Student` +
  `education=Higher_Secondary` closes several at once. Look for these
  combinations explicitly.
- For aggregate vote gaps (e.g., BJP undershooting), bias the next batch's
  vote intent toward that party — but only for personas whose demographics
  make that party plausible per the vote tables.
- Don't simply duplicate previous personas; vary names, household
  composition, life-stage details, and narrative texture.
- Never drop required fields to "save tokens." A persona with missing fields
  will be dropped entirely.
