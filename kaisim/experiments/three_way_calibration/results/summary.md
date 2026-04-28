# Three-way calibration experiment — results

Composite chi-square per AC × calibration state × verifier. Budget = 800.

## Composite scores (lower = closer to source)

|  AC  | mode     | n | strict χ² | partial χ² | strict ✓? | partial ✓? | skipped (j/b) |
|------|----------|---|-----------|------------|-----------|-----------|---------------|
|  003 | pre      | 500 |    8438.2 |     8388.0 |       no  |       no  |          10/3 |
|  003 | plumbing | 500 |    1379.0 |     1328.8 |       no  |       no  |           4/3 |
|  003 | full     | 500 |     660.9 |      610.6 |       no  |       no  |           2/3 |
|      |          |   |           |            |           |           |               |
|  222 | pre      | 500 |    6643.4 |     6398.6 |       no  |       no  |          13/8 |
|  222 | plumbing | 500 |    1347.3 |     1102.5 |       no  |       no  |           9/8 |
|  222 | full     | 500 |     929.4 |      684.6 |       no  |       no  |           0/8 |
|      |          |   |           |            |           |           |               |

## Tier value-add (per AC)

|  AC  | pre→plumbing Δ partial | plumbing→full Δ partial | total drop |
|------|------------------------|-------------------------|------------|
|  003 |                +7059.2 |                  +718.1 |    +7777.3 |
|  222 |                +5296.1 |                  +417.9 |    +5714.0 |

## Reading this table

- **PRE** is the data-faithful baseline (auto-built structures, generic plugins). Distance from budget tells you how bad raw alignment is.
- **PLUMBING** keeps only tier-1 fixes (renames, structural alignments, child-drop, age-bucket expansion, verify_condition). No inferred ratios, no value overrides. The drop from PRE→PLUMBING is the value of pure plumbing.
- **FULL** adds tier-2 (inferred aggregations like Mahishya_Sadgop 70:30) + tier-3 (value overrides like INC capping). The drop from PLUMBING→FULL is the value of those interpretive choices — i.e., what we sacrificed in source-faithfulness for verifier-pass.
- **STRICT verifier** treats absent joint cells as 0% target → fails noisily on any unaligned joint.
- **PARTIAL verifier** skips unrecoverable cells with skipped_reason → fails only on data-real gaps.
