# Base image to be used.
FROM ubuntu:17.10

# Maintainer of the Dockerfile.
LABEL maintainer "Pedro Garcia Rodriguez <pedgarrod@gmail.com>"

# Set environment variables for non interactive apt.
ENV DEBIAN_FRONTEND noninteractive

# Update the apt indexes and install Docker Compose.
# Following the best practces for Dockerfiles we do all the apt stuff
# in a single line execution.
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       ca-certificates \
       curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set Docker Compose installation  env vars.
ENV DOCKER_VERSION 1.18.0

# Configure Docker Compose install.
RUN curl -L https://github.com/docker/compose/releases/download/${DOCKER_VERSION}/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose \
    && chmod +x /usr/local/bin/docker-compose

# Volume to store Docker Compose data.
VOLUME ["/data"]

# Default command for the container.
ENTRYPOINT ["/usr/local/bin/docker-compose"]

# Configure Dockerfile cmd.
CMD ["--help"]
