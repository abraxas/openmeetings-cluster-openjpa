#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
export COMPOSE_PROJECT_NAME="${COMPOSE_PROJECT_NAME:-om-g11-cluster}"
export PYTHONUNBUFFERED=1
export OM_SERVICE="${OM_SERVICE:-om}"
chmod +x poc.py cluster-entrypoint.sh

LABEL="OPENMEETINGS-CLUSTER-OPENJPA-WITNESS"

down() {
  echo "== docker compose down -v =="
  docker compose -p "${COMPOSE_PROJECT_NAME}" down -v --remove-orphans || true
}

fail_run() {
  echo "FAIL ${LABEL} $*" | tee poc-last-run.txt
  docker compose -p "${COMPOSE_PROJECT_NAME}" logs --no-color --tail=160 om db || true
  down
  exit 1
}

trap down EXIT

echo "== docker compose down (clean) =="
down

echo "== docker pull apache/openmeetings:min-9.1.0 =="
pull_ok=0
for attempt in $(seq 1 12); do
  if docker pull --platform linux/amd64 apache/openmeetings:min-9.1.0; then
    pull_ok=1
    break
  fi
  echo "IOC image-pull-retry attempt=${attempt}"
  sleep 20
done
if [[ "${pull_ok}" != 1 ]]; then
  fail_run "image pull failed"
fi

echo "== docker compose build (JRE wrap) =="
build_ok=0
for attempt in $(seq 1 12); do
  if docker compose -p "${COMPOSE_PROJECT_NAME}" build om; then
    build_ok=1
    break
  fi
  echo "IOC compose-build-retry attempt=${attempt}"
  sleep 20
done
if [[ "${build_ok}" != 1 ]]; then
  fail_run "compose build failed"
fi

run_phase() {
  local phase="$1"
  local cluster="$2"
  echo "== phase ${phase} ENABLE_CLUSTER=${cluster} compose up =="
  down
  export ENABLE_CLUSTER="${cluster}"
  up_ok=0
  for attempt in $(seq 1 12); do
    if docker compose -p "${COMPOSE_PROJECT_NAME}" up -d; then
      up_ok=1
      break
    fi
    echo "IOC compose-up-retry phase=${phase} attempt=${attempt}"
    sleep 20
    down
  done
  if [[ "${up_ok}" != 1 ]]; then
    fail_run "compose up failed phase=${phase}"
  fi
  echo "== poc.py --phase ${phase} =="
  set +e
  python3 ./poc.py --phase "${phase}" | tee -a poc-last-run.txt
  local rc=${PIPESTATUS[0]}
  set -e
  return "${rc}"
}

: > poc-last-run.txt

echo "== PHASE A stock default =="
if ! run_phase a 0; then
  fail_run "phase A stock inspect failed"
fi

echo "== PHASE B clustering leftover =="
if ! run_phase b 1; then
  echo "FAIL ${LABEL} phase B deserialize not proven" | tee -a poc-last-run.txt
  docker compose -p "${COMPOSE_PROJECT_NAME}" logs --no-color --tail=200 om || true
  down
  exit 1
fi

if ! grep -q "^SUCCESS ${LABEL}$" poc-last-run.txt; then
  fail_run "missing SUCCESS line"
fi

echo "SUCCESS ${LABEL}" | tee -a poc-last-run.txt
exit 0
