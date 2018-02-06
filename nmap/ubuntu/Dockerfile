# Base image to be used.
FROM ubuntu:latest

# Maintainer of the Dockerfile.
LABEL maintainer "Pedro Garcia Rodriguez <pedgarrod@gmail.com>"

# Set environment variables..
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       nmap \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Default entrypoint for the container.
ENTRYPOINT ["nmap"]

# Default command for the container.
CMD ["--help"]
