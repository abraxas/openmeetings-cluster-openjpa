#!/bin/bash
# Wrap official min-9.1.0 om.sh.
# ENABLE_CLUSTER=1 uncomments Clustering.xml RemoteCommitProvider and drops
# OpenJPA lists so catalina matches default bin/startup.sh (lists are only in
# systemd unit / stock docker om.sh).
set -euo pipefail

OM_SH="${work:-/opt}/om.sh"
PERSIST_DIR="/opt/openmeetings/webapps/openmeetings/WEB-INF/classes/META-INF"

if [[ ! -f "${OM_SH}" ]]; then
  echo "FAIL missing ${OM_SH}" >&2
  exit 1
fi

if [[ -z "${JAVA_HOME:-}" || ! -x "${JAVA_HOME}/bin/java" ]]; then
  if command -v java >/dev/null 2>&1; then
    JAVA_HOME="$(dirname "$(dirname "$(readlink -f "$(command -v java)")")")"
  else
    JAVA_HOME=/usr/lib/jvm/java-21-openjdk-amd64
  fi
fi
export JAVA_HOME
export JRE_HOME="${JAVA_HOME}"
export PATH="${JAVA_HOME}/bin:${PATH}"
echo "IOC java-home ${JAVA_HOME} $($JAVA_HOME/bin/java -version 2>&1 | head -1)"

# sudo in om.sh only preserves JAVA_OPTS/CATALINA_OPTS; catalina needs JAVA_HOME.
sed -i 's|--preserve-env=JAVA_OPTS --preserve-env=CATALINA_OPTS|--preserve-env=JAVA_OPTS --preserve-env=CATALINA_OPTS --preserve-env=JAVA_HOME --preserve-env=JRE_HOME --preserve-env=PATH|' "${OM_SH}"

# 2g mem_limit: raise heap after om.sh sets CATALINA_OPTS.
sed -i 's|export CATALINA_OPTS="-DDATA_DIR=${OM_DATA_DIR}"|export CATALINA_OPTS="-DDATA_DIR=${OM_DATA_DIR} -XX:MaxRAMPercentage=70.0"|' "${OM_SH}"

if [[ "${ENABLE_CLUSTER:-0}" == "1" ]]; then
  echo "IOC cluster-enable uncomment RemoteCommitProvider tcp port 5636, strip OpenJPA lists (startup.sh leftover)"
  sed -i 's|<!--property name="openjpa.RemoteCommitProvider" value="tcp(Addresses=127.0.0.1)" /-->|<property name="openjpa.RemoteCommitProvider" value="tcp(Addresses=127.0.0.1)" />|g' \
    "${PERSIST_DIR}"/*_persistence.xml
  # Default unpack path: JAVA_OPTS has no openjpa.serialization.class.* lists.
  sed -i 's|^export JAVA_OPTS=.*|export JAVA_OPTS="-Djava.awt.headless=true -Djava.security.egd=file:/dev/./urandom"|' "${OM_SH}"
else
  echo "IOC stock-start RemoteCommitProvider stays commented"
fi

exec bash "${OM_SH}"
