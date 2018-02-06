# Base image to be used.
FROM ubuntu:16.04

# Maintainer of the Dockerfile.
LABEL maintainer "Pedro Garcia Rodriguez <pedgarrod@gmail.com>"

# Metadata information.
LABEL org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.vcs-url="https://github.com/breakingpitt/dockerfiles"

# Operate with root user.
USER root

# Set environment variables for noninteactive user choices
# in package managementenoninteactive user choices.
ENV DEBIAN_FRONTEND noninteractive

# Update the apt indexes and install the required software.
# Following the best practices for Dockerfiles we do all the apt stuff
# in a single line execution for avoid unwanted layers in our docker image.
RUN apt-get update \
    && apt-get install -y \
    curl \
    tar \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set environment variables for Sonatype Nexus configuration.
ENV SONATYPE_WORK /sonatype-work
ENV NEXUS_VERSION 2.13.0-01

# Set environament variables for Java configuration.
ENV JAVA_HOME /opt/java

ENV JAVA_VERSION_MAJOR 8
ENV JAVA_VERSION_MINOR 74
ENV JAVA_VERSION_BUILD 02

ENV CONTEXT_PATH /nexus
ENV MAX_HEAP 768m
ENV MIN_HEAP 256m
ENV JAVA_OPTS -server -Djava.net.preferIPv4Stack=true
ENV LAUNCHER_CONF ./conf/jetty.xml ./conf/jetty-requestlog.xml

# install Oracle JRE
RUN mkdir -p /opt \
    && curl --fail --silent --location --retry 3 \
    --header "Cookie: oraclelicense=accept-securebackup-cookie; " \
    http://download.oracle.com/otn-pub/java/jdk/${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-b${JAVA_VERSION_BUILD}/server-jre-${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-linux-x64.tar.gz \
    | gunzip \
    | tar -x -C /opt \
    && ln -s /opt/jdk1.${JAVA_VERSION_MAJOR}.0_${JAVA_VERSION_MINOR} ${JAVA_HOME}

# Download, configure and install Sonatype Nexus.
RUN mkdir -p /opt/sonatype/nexus \
    && curl --fail --silent --location --retry 3 \
    https://download.sonatype.com/nexus/oss/nexus-${NEXUS_VERSION}-bundle.tar.gz \
    | gunzip \
    | tar x -C /tmp nexus-${NEXUS_VERSION} \
    && mv /tmp/nexus-${NEXUS_VERSION}/* /opt/sonatype/nexus/ \
    && rm -rf /tmp/nexus-${NEXUS_VERSION}

# Create Nexu user.
RUN useradd -r -u 200 -m \
    -c "nexus role account" \
    -d ${SONATYPE_WORK} -s \
    /bin/false nexus

# Volume to store Sonatype Nexus data.
VOLUME ${SONATYPE_WORK}

# Exposed port.
EXPOSE 8081

# Set working directory.
WORKDIR /opt/sonatype/nexus

# Operate with Nexus user.
USER nexus

# Set container CMD option.
CMD ${JAVA_HOME}/bin/java \
    -Dnexus-work=${SONATYPE_WORK} -Dnexus-webapp-context-path=${CONTEXT_PATH} \
    -Xms${MIN_HEAP} -Xmx${MAX_HEAP} \
    -cp 'conf/:lib/*' \
    ${JAVA_OPTS} \
   org.sonatype.nexus.bootstrap.Launcher ${LAUNCHER_CONF}
