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
    && wget -P /tmp/ https://releases.hashicorp.com/terraform/0.7.4/terraform_0.7.4_linux_amd64.zip \
    && mkdir -p /opt/terraform \
    && unzip /tmp/terraform_0.7.4_linux_amd64.zip -d /opt/terraform 

# Volume to store Terraform data.
VOLUME ["/data"]

# Set workdir directory.
WORKDIR /data

# Entrypoint command for the container.
ENTRYPOINT ["/opt/terraform/terraform"]

# Default command for the container.
CMD ["--help"]
