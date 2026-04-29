#!/usr/bin/env bash
# Stage-1: regenerate v3 personas for all 10 ACs in parallel.
# Stage-2: run 2021_targeted_v3 sim for all 10 ACs in parallel.
# Stage-3 (optional): run 2024_ls_targeted_v3 if all 2021 sims succeed.
#
# Usage:
#   bash v3_fanout_all10.sh gen     # only regenerate personas
#   bash v3_fanout_all10.sh sim2021 # only run 2021_targeted_v3 (assumes gen done)
#   bash v3_fanout_all10.sh sim2024 # only run 2024_ls_targeted_v3 (assumes gen done)
#   bash v3_fanout_all10.sh all     # gen + sim2021 + sim2024

set -u
cd /root/sim/wb-election-sim
LOGDIR=kaisim/simulations/_phase2_2021/v3_logs
mkdir -p $LOGDIR

ACS=(003 011 064 095 123 143 159 198 210 222)
# Skip 095 + 159 in `gen` and `sim2021` stages — already done by smaller pipeline.
SKIP_DONE_ACS=(095 159)

is_skipped() {
  local ac=$1
  for s in "${SKIP_DONE_ACS[@]}"; do
    [ "$ac" = "$s" ] && return 0
  done
  return 1
}

stage="${1:-all}"

ensure_v3_configs() {
  ac=$1
  src=kaisim/simulations/wb_2021_ac${ac}
  if [ ! -f $src/persona_configs/local_qwen_v3.yaml ]; then
    cp $src/persona_configs/local_qwen.yaml $src/persona_configs/local_qwen_v3.yaml
    sed -i 's|name: "local_qwen_n100"|name: "local_qwen_n100_v3"|' $src/persona_configs/local_qwen_v3.yaml
  fi
  if [ ! -f $src/simulation_configs/2021_targeted_v3.yaml ]; then
    cp $src/simulation_configs/2021_targeted.yaml $src/simulation_configs/2021_targeted_v3.yaml
    sed -i 's|persona_set: local_qwen_n100|persona_set: local_qwen_n100_v3|' $src/simulation_configs/2021_targeted_v3.yaml
    # add intention_probe block if missing
    grep -q "^intention_probe:" $src/simulation_configs/2021_targeted_v3.yaml || \
      printf "intention_probe:\n  at_ticks: [8, 12]\n" >> $src/simulation_configs/2021_targeted_v3.yaml
    # rename
    sed -i "s|name: ${ac}_.*_2021_targeted$|&_v3|" $src/simulation_configs/2021_targeted_v3.yaml
  fi
}

run_gen_one() {
  ac=$1
  ensure_v3_configs $ac
  echo "[gen $ac] start $(date -Iseconds)" >> $LOGDIR/${ac}_gen.log
  python -u kaisim/simulations/wb_2021_ac${ac}/generate.py local_qwen_v3 \
    >> $LOGDIR/${ac}_gen.log 2>&1
  echo "[gen $ac] done rc=$? $(date -Iseconds)" >> $LOGDIR/${ac}_gen.log
}

run_sim_one() {
  ac=$1
  cfg=$2
  out_log=$LOGDIR/${ac}_${cfg}.log
  echo "[sim $ac/$cfg] start $(date -Iseconds)" >> $out_log
  python -u kaisim/simulations/wb_2021_ac${ac}/run_simulation.py $cfg \
    >> $out_log 2>&1
  echo "[sim $ac/$cfg] done rc=$? $(date -Iseconds)" >> $out_log
}

run_in_parallel() {
  fn=$1
  shift
  args=("$@")
  pids=()
  for ac in "${ACS[@]}"; do
    if is_skipped $ac; then
      echo "[skip $ac] $fn (already done in v3_run_pipeline.sh)" >> $LOGDIR/orchestrator.log
      continue
    fi
    $fn $ac "${args[@]}" &
    pids+=($!)
  done
  for pid in "${pids[@]}"; do wait $pid; done
}

if [ "$stage" = "gen" ] || [ "$stage" = "all" ]; then
  echo "=== STAGE: gen for ACs minus done ===" >> $LOGDIR/orchestrator.log
  run_in_parallel run_gen_one
  echo "=== gen complete ===" >> $LOGDIR/orchestrator.log
fi

if [ "$stage" = "sim2021" ] || [ "$stage" = "all" ]; then
  echo "=== STAGE: sim2021 (skip 095/159 — running via v3_run_pipeline) ===" >> $LOGDIR/orchestrator.log
  # Keep the skip list — 095/159 sim is being run by v3_run_pipeline.sh
  run_in_parallel run_sim_one 2021_targeted_v3
  echo "=== sim2021 complete ===" >> $LOGDIR/orchestrator.log
fi

if [ "$stage" = "sim2024" ] || [ "$stage" = "all" ]; then
  echo "=== STAGE: sim2024 (only ACs with 2024 config) ===" >> $LOGDIR/orchestrator.log
  # only run for ACs that have a 2024_ls_targeted_v3.yaml config
  pids=()
  for ac in "${ACS[@]}"; do
    f=kaisim/simulations/wb_2021_ac${ac}/simulation_configs/2024_ls_targeted_v3.yaml
    if [ -f $f ]; then
      run_sim_one $ac 2024_ls_targeted_v3 &
      pids+=($!)
    else
      echo "[skip $ac] no 2024_ls_targeted_v3.yaml" >> $LOGDIR/orchestrator.log
    fi
  done
  for pid in "${pids[@]}"; do wait $pid; done
  echo "=== sim2024 complete ===" >> $LOGDIR/orchestrator.log
fi

echo "[fanout complete] $(date -Iseconds)" >> $LOGDIR/orchestrator.log
