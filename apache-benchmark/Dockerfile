# Base image to be used.
FROM ubuntu:17.10

# Maintainer of the Dockerfile.
LABEL maintainer "Pedro Garcia Rodriguez <pedgarrod@gmail.com>"

# Metadata information.
LABEL org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.vcs-url="https://github.com/breakingpitt/dockerfiles"
      
# Set environment variables for non interactive apt.
ENV DEBIAN_FRONTEND noninteractive

# Update the apt indexes and install the Apache2 server.
# Following the best practces for Dockerfiles we do all the apt stuff
# in a single line execution.
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       apache2-utils \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Default command for the container.
ENTRYPOINT ["/usr/bin/ab"]

# Default command for the container.
CMD ["--help"]
