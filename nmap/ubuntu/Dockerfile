# Base image to be used.
FROM ubuntu:17.10

# Maintainer of the Dockerfile.
LABEL maintainer "Pedro Garcia Rodriguez <pedgarrod@gmail.com>"

# Metadata information.
LABEL org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.vcs-url="https://github.com/breakingpitt/dockerfiles"

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
