# Base image to be used.
FROM ubuntu:17.10

# Maintainer of the Dockerfile.
LABEL maintainer "Pedro Garcia Rodriguez <pedgarrod@gmail.com>"

# Metadata information.
LABEL org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.vcs-url="https://github.com/breakingpitt/docker-vault"

# Set environment variables for non interactive.
ENV DEBIAN_FRONTEND noninteractive

# Update the apt indexes and install the required software.
# Following the best practices for Dockerfiles we do all the apt stuff
# in a single line execution for avoid unwanted layers in our docker image.
RUN apt-get update \
    && apt-get install -y \
       fortune \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* 


# Default command for the container.
ENTRYPOINT [ "/usr/games/fortune" ]

# Default command for the container.
CMD ["--help"]
