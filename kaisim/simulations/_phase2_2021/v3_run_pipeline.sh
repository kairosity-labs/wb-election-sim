#!/usr/bin/env bash
# v3 pipeline: regenerate personas (A1 prompt), run targeted sim (A2/A3/B4 active),
# for AC095 + AC159 only. Each AC runs in its own background process.
# Logs go to v3_logs/.
set -u
cd /root/sim/wb-election-sim
LOGDIR=kaisim/simulations/_phase2_2021/v3_logs
mkdir -p $LOGDIR

stage="${1:-all}"   # all | gen | sim

run_gen() {
  ac=$1
  echo "[gen $ac] starting at $(date -Iseconds)" | tee -a $LOGDIR/${ac}_gen.log
  python -u kaisim/simulations/wb_2021_ac${ac}/generate.py local_qwen_v3 \
    >> $LOGDIR/${ac}_gen.log 2>&1
  rc=$?
  echo "[gen $ac] exit=$rc at $(date -Iseconds)" | tee -a $LOGDIR/${ac}_gen.log
  return $rc
}

run_sim() {
  ac=$1
  echo "[sim $ac] starting at $(date -Iseconds)" | tee -a $LOGDIR/${ac}_sim.log
  python -u kaisim/simulations/wb_2021_ac${ac}/run_simulation.py 2021_targeted_v3 \
    >> $LOGDIR/${ac}_sim.log 2>&1
  rc=$?
  echo "[sim $ac] exit=$rc at $(date -Iseconds)" | tee -a $LOGDIR/${ac}_sim.log
  return $rc
}

if [ "$stage" = "all" ] || [ "$stage" = "gen" ]; then
  echo "=== STAGE: persona generation (parallel ac095+ac159) ===" | tee -a $LOGDIR/orchestrator.log
  run_gen 095 &
  PID1=$!
  run_gen 159 &
  PID2=$!
  wait $PID1; G1=$?
  wait $PID2; G2=$?
  echo "[gen done] ac095=$G1 ac159=$G2" | tee -a $LOGDIR/orchestrator.log
  if [ $G1 -ne 0 ] || [ $G2 -ne 0 ]; then
    echo "[gen FAILED]; aborting before sim stage." | tee -a $LOGDIR/orchestrator.log
    exit 1
  fi
fi

if [ "$stage" = "all" ] || [ "$stage" = "sim" ]; then
  echo "=== STAGE: simulation (parallel ac095+ac159 targeted_v3) ===" | tee -a $LOGDIR/orchestrator.log
  run_sim 095 &
  PID3=$!
  run_sim 159 &
  PID4=$!
  wait $PID3; S1=$?
  wait $PID4; S2=$?
  echo "[sim done] ac095=$S1 ac159=$S2" | tee -a $LOGDIR/orchestrator.log
fi

echo "[v3_pipeline complete] $(date -Iseconds)" | tee -a $LOGDIR/orchestrator.log
