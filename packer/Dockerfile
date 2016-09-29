# Base image to be used.
FROM ubuntu:latest

# Maintainer of the Dockerfile.
MAINTAINER Pedro Garcia Rodriguez<pedgarrod@gmail.com>

# Set environment variables for non interactive.
ENV DEBIAN_FRONTEND noninteractive

# Update the apt indexes and install the required software.
# Following the best practices for Dockerfiles we do all the apt stuff
# in a single line execution for avoid unwanted layers in our docker image.
RUN apt-get update \
    && apt-get install -y wget unzip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && wget -P /tmp/ https://releases.hashicorp.com/packer/0.10.2/packer_0.10.2_linux_amd64.zip \
    && mkdir -p /opt/packer \
    && unzip /tmp/packer_0.10.2_linux_amd64.zip -d /opt/packer

# Volume to store Terraform data.
VOLUME ["/data"]

# Set workdir directory.
WORKDIR /data

# Entrypoint command for the container.
ENTRYPOINT ["/opt/packer/packer"]

# Default command for the container.
CMD ["--help"]
