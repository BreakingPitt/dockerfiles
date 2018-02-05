# Base image to be used.
FROM ubuntu:latest

# Maintainer of the Dockerfile.
LABEL maintainer "Pedro Garcia Rodriguez <pedgarrod@gmail.com>"

# Set environment variables for non interactive apt.
ENV MUTT_USER mutt

# Set environment variables for non interactive apt.
ENV DEBIAN_FRONTEND noninteractive

# Update the apt indexes and install required packages.
# Following the best practces for Dockerfiles we do all the apt stuff
# in a single line execution.
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       msmtp \
       mutt \
       vim \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && adduser --disabled-login --gecos '' $MUTT_USER

WORKDIR /home/$MUTT_USER

USER $MUTT_USER

# Entrypoint command for the container.
ENTRYPOINT ["/usr/bin/mutt"]

# Default command for the container.
CMD [ "--help" ]
