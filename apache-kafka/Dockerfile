#Base image to be used.
FROM ubuntu:16.04

# Maintainer of the Dockerfile.
MAINTAINER Pedro Garcia Rodriguez<pedgarrod@gmail.com>

# Set environment variables for locale settings.
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

# Set environment variables for non interactive apt.
ENV DEBIAN_FRONTEND noninteractive

ENV KAFKA_VERSION 0.10.0
# Add required Ubuntu package por PPA repository management
# and other kind of required programs like wget.
RUN apt-get update \
    && apt-get install -y \
    python-software-properties \
    software-properties-common \
    wget \
    --no-install-recommends \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Update the apt indexes and install the required software.
# Following the best practices for Dockerfiles we do all the apt stuff
# in a single line execution for avoid unwanted layers in our docker image.
RUN add-apt-repository ppa:webupd8team/java \
    && apt-get update \
    && echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections \
    && apt-get install -y oracle-java8-installer \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Download Kafka tgz file.
RUN wget -q -O -  http://apache.rediris.es/kafka/0.10.0.0/kafka_2.10-0.10.0.0.tgz  | tar -C /opt -xz

# Container cmd.
CMD /opt/kafka_2.10-0.10.0.0/bin/kafka-server-start.sh /opt/kafka/config/server.properties
