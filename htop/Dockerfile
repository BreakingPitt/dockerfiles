# Base image to be used.
FROM ubuntu:latest

# Maintainer of the Dockerfile.
MAINTAINER Pedro Garcia Rodriguez<pedgarrod@gmail.com>

# Set environment variables for non interactive apt.
ENV DEBIAN_FRONTEND noninteractive

# Update the apt indexes and installs htop.
# Following the best practces for Dockerfiles we do all the apt stuff
# in a single line execution.
RUN apt-get update \
    && apt-get install -y htop --no-install-recommends \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Default command for the container.
CMD ["htop"]
