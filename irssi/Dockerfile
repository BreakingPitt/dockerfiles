# Base image to be used.
FROM ubuntu:latest

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
       irssi  \
       irssi-scripts \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set IRSSI environment variables.
ENV IRSSI_USER=irssi
ENV IRSSI_HOME=/home/irssi
ENV IRSSI_CONF_DIR=$IRSSI_HOME/.irssi
ENV IRSSI_SCRIPTS_DIR=$IRSSI_CONF_DIR/scripts

# Configure IRSSI install.
RUN adduser --home $IRSSI_HOME --shell /bin/sh --disabled-password --gecos "" $IRSSI_USER \
    && mkdir -p $IRSSI_CONF_DIR $IRSSI_SCRIPTS_DIR  \
    && chown -R $IRSSI_USER:$IRSSI_USER $IRSSI_CONF_DIR $IRSSI_SCRIPTS_DIR

# Run as Irssi user.
USER $IRSSI_USER

# Default command for the container.
ENTRYPOINT ["/usr/bin/irssi"]

# Default command for the container.
CMD ["--help"]
