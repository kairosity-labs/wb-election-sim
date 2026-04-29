#!/usr/bin/env bash
# Resume final-vote stage on all 9 crashed v3 sims in parallel.
# Logs go to v3_logs/<ac>_resume.log.
set -u
cd /root/sim/wb-election-sim
LOGDIR=kaisim/simulations/_phase2_2021/v3_logs
mkdir -p $LOGDIR

ACS=(003 011 064 095 123 143 198 210 222)

run_resume_one() {
  ac=$1
  rd=$(ls -td kaisim/simulations/wb_2021_ac${ac}/runs/*_2021_targeted_v3 2>/dev/null | head -1)
  if [ -z "$rd" ]; then
    echo "[resume $ac] no run dir, skipping" >> $LOGDIR/${ac}_resume.log
    return 1
  fi
  echo "[resume $ac] $rd starting at $(date -Iseconds)" >> $LOGDIR/${ac}_resume.log
  python -u kaisim/simulations/_phase2_2021/resume_final_vote.py "$rd" \
    >> $LOGDIR/${ac}_resume.log 2>&1
  rc=$?
  echo "[resume $ac] done rc=$rc at $(date -Iseconds)" >> $LOGDIR/${ac}_resume.log
}

pids=()
for ac in "${ACS[@]}"; do
  run_resume_one $ac &
  pids+=($!)
done
echo "[resume launched ${#pids[@]} ACs]" | tee -a $LOGDIR/orchestrator.log
for pid in "${pids[@]}"; do wait $pid; done
echo "[resume all done $(date -Iseconds)]" | tee -a $LOGDIR/orchestrator.log
