# Base image to be used.
FROM ubuntu:latest

# Maintainer of the Dockerfile.
LABEL maintainer="Pedro Garcia Rodriguez <pedgarrod@gmail.com>"

# Metadata information.
LABEL org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.vcs-url="https://github.com/breakingpitt/dockerfiles"

# Set environment variables for non interactive apt.
ENV DEBIAN_FRONTEND noninteractive

# Update the apt indexes and install the ClamAV engine.
# Following the best practces for Dockerfiles we do all the apt stuff
# in a single line execution.
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       clamav \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Volume to store ClamAV data.
WORKDIR /data

# Default command for the container.
ENTRYPOINT ["clamscan"]

# Default command for the container.
CMD ["--help"]
