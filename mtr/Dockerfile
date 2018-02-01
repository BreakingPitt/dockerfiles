# Base image to be used.
FROM ubuntu:latest

# Maintainer of the Dockerfile.
MAINTAINER Pedro Garcia Rodriguez<pedgarrod@gmail.com>

RUN apt-get update \
    && apt-get install -y mtr-tiny --no-install-recommends \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Entrypoint command for the container.
ENTRYPOINT ["mtr"]

# Default command for the container.
CMD ["--help"]
