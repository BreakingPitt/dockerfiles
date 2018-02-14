# Base image to be used.
FROM ubuntu:17.10

# Maintainer of the Dockerfile.
LABEL maintainer="Pedro Garcia Rodriguez <pedgarrod@gmail.com>"

# Set environment variable for downloading terraform version.
ENV PACKER_VERSION=1.2.0

# Update the apt indexes and install the required software.
# Following the best practices for Dockerfiles we do all the apt stuff
# in a single line execution for avoid unwanted layers in our docker image.
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       ca-certificates \
       curl \
       unzip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && curl -o /tmp/packer_${PACKER_VERSION}_linux_amd64.zip https://releases.hashicorp.com/packer/${PACKER_VERSION}/packer_${PACKER_VERSION}_linux_amd64.zip \
    && mkdir -p /opt/packer \
    && unzip /tmp/packer_${PACKER_VERSION}_linux_amd64.zip -d /opt/packer

# Volume to store Terraform data.
VOLUME ["/data"]

# Set workdir directory.
WORKDIR /data

# Entrypoint command for the container.
ENTRYPOINT ["/opt/packer/packer"]

# Default command for the container.
CMD ["--help"]
