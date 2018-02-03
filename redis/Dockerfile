# Base image to be used.
FROM ubuntu:16.04

# Maintainer of the Dockerfile.
MAINTAINER Pedro Garcia Rodriguez<pedgarrod@gmail.com>

# Set environment variables for locale settings.
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

# Set environment variables for non interactive apt.
ENV DEBIAN_FRONTEND noninteractive

# Add the Chris Lea third party repository, update the apt indexes
# and install the redis server.
# Following the best practces for Dockerfiles we do all the apt stuff
# in a single line execution.
RUN apt-get install -y --no-install-recommends \
       software-properties-common \
    && add-apt-repository ppa:chris-lea/redis-server \
    && apt-get update \
    && apt-get install -y --no-install-recommends \
       redis-server \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Volume to store Redis data.
VOLUME ["/data"]

# Set workdir directory.
WORKDIR /data
