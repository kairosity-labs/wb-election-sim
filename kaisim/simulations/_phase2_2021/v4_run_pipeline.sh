#!/usr/bin/env bash
# v4 mini-experiment: gen + sim for AC 064, 095, 159 with v4 prompt
# (brief 2019 anchor, no rationalization). Tests partial-anchor approach.
set -u
cd /root/sim/wb-election-sim
LOGDIR=kaisim/simulations/_phase2_2021/v4_logs
mkdir -p $LOGDIR

ACS=(064 095 159)
stage="${1:-all}"

run_gen_one() {
  ac=$1
  echo "[gen $ac] start $(date -Iseconds)" >> $LOGDIR/${ac}_gen.log
  python -u kaisim/simulations/wb_2021_ac${ac}/generate.py local_qwen_v4 \
    >> $LOGDIR/${ac}_gen.log 2>&1
  echo "[gen $ac] done rc=$? $(date -Iseconds)" >> $LOGDIR/${ac}_gen.log
}

run_sim_one() {
  ac=$1
  echo "[sim $ac] start $(date -Iseconds)" >> $LOGDIR/${ac}_sim.log
  python -u kaisim/simulations/wb_2021_ac${ac}/run_simulation.py 2021_targeted_v4 \
    >> $LOGDIR/${ac}_sim.log 2>&1
  echo "[sim $ac] done rc=$? $(date -Iseconds)" >> $LOGDIR/${ac}_sim.log
}

if [ "$stage" = "gen" ] || [ "$stage" = "all" ]; then
  echo "=== STAGE: gen for AC ${ACS[@]} ===" >> $LOGDIR/orchestrator.log
  pids=()
  for ac in "${ACS[@]}"; do run_gen_one $ac & pids+=($!); done
  for pid in "${pids[@]}"; do wait $pid; done
  echo "=== gen complete ===" >> $LOGDIR/orchestrator.log
fi

if [ "$stage" = "sim" ] || [ "$stage" = "all" ]; then
  echo "=== STAGE: sim for AC ${ACS[@]} ===" >> $LOGDIR/orchestrator.log
  pids=()
  for ac in "${ACS[@]}"; do run_sim_one $ac & pids+=($!); done
  for pid in "${pids[@]}"; do wait $pid; done
  echo "=== sim complete ===" >> $LOGDIR/orchestrator.log
fi
echo "[v4 pipeline complete] $(date -Iseconds)" >> $LOGDIR/orchestrator.log
