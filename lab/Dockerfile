FROM apache/openmeetings:min-9.1.0
# Official min-9.1.0 ships OM/Tomcat but no JRE. Install Java 21 so catalina can start.
USER root
RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        openjdk-21-jre-headless \
        ca-certificates \
    && rm -rf /var/lib/apt/lists/*
ENV JAVA_HOME=/usr/lib/jvm/java-21-openjdk-amd64
ENV JRE_HOME=/usr/lib/jvm/java-21-openjdk-amd64
ENV PATH="/usr/lib/jvm/java-21-openjdk-amd64/bin:${PATH}"
COPY cluster-entrypoint.sh /opt/cluster-entrypoint.sh
RUN chmod 0755 /opt/cluster-entrypoint.sh
ENTRYPOINT ["/opt/cluster-entrypoint.sh"]
