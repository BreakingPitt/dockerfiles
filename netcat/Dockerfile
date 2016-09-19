# Base image to be used.
FROM ubuntu:latest

# Maintainer of the Dockerfile.
MAINTAINER Pedro Garcia Rodriguez<pedgarrod@gmail.com>

# Set environment variables for timezone configuration.
ENV TZ Europe/Madrid
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8
ENV DEBIAN_FRONTEND noninteractive

# Set the correct time to avoid problems.
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Configure locales to en_US.UTF-8.
RUN locale-gen en_US.UTF-8

RUN apt-get update \
    && apt-get install -y netcat --no-install-recommends \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Create work directory
RUN mkdir /work

# Volume to store nmap data.
VOLUME ["/work"]

# Set workdir directory.
WORKDIR /work

# Default command for the container.
ENTRYPOINT ["netcat"]
