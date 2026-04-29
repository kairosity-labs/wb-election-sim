#!/usr/bin/env bash
# v4 fanout: gen for remaining 7 ACs + sim for all 10 + 2024 LS for AC 095/159
# Runs in 3 stages: gen, sim2021, sim2024
set -u
cd /root/sim/wb-election-sim
LOGDIR=kaisim/simulations/_phase2_2021/v4_logs
mkdir -p $LOGDIR

REMAINING_ACS=(003 011 123 143 198 210 222)   # 064/095/159 already gen'd
ALL_ACS=(003 011 064 095 123 143 159 198 210 222)
LS2024_ACS=(095 159)

stage="${1:-all}"
# `all` runs gen+sim2021 only; sim2024 must be invoked explicitly so it can be
# launched in parallel with sim2021 without double-running.

run_gen_one() {
  ac=$1
  echo "[gen $ac] start $(date -Iseconds)" >> $LOGDIR/${ac}_gen.log
  python -u kaisim/simulations/wb_2021_ac${ac}/generate.py local_qwen_v4 \
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

if [ "$stage" = "gen" ] || [ "$stage" = "all" ]; then
  echo "=== STAGE: gen for ${REMAINING_ACS[@]} ===" >> $LOGDIR/orchestrator.log
  pids=()
  for ac in "${REMAINING_ACS[@]}"; do run_gen_one $ac & pids+=($!); done
  for pid in "${pids[@]}"; do wait $pid; done
  echo "=== gen complete ===" >> $LOGDIR/orchestrator.log
fi

if [ "$stage" = "sim2021" ] || [ "$stage" = "all" ]; then
  echo "=== STAGE: sim2021 for ${REMAINING_ACS[@]} (064/095/159 already done) ===" >> $LOGDIR/orchestrator.log
  pids=()
  for ac in "${REMAINING_ACS[@]}"; do run_sim_one $ac 2021_targeted_v4 & pids+=($!); done
  for pid in "${pids[@]}"; do wait $pid; done
  echo "=== sim2021 complete ===" >> $LOGDIR/orchestrator.log
fi

if [ "$stage" = "sim2024" ]; then
  echo "=== STAGE: sim2024 for ${LS2024_ACS[@]} ===" >> $LOGDIR/orchestrator.log
  pids=()
  for ac in "${LS2024_ACS[@]}"; do run_sim_one $ac 2024_ls_targeted_v4 & pids+=($!); done
  for pid in "${pids[@]}"; do wait $pid; done
  echo "=== sim2024 complete ===" >> $LOGDIR/orchestrator.log
fi

echo "[v4 fanout complete] $(date -Iseconds)" >> $LOGDIR/orchestrator.log
