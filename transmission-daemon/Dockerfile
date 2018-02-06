# Base image to be used.
FROM ubuntu:latest

# Maintainer of the Dockerfile.
LABEL maintainer "Pedro Garcia Rodriguez <pedgarrod@gmail.com>"

# Metadata information.
LABEL org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.vcs-url="https://github.com/breakingpitt/dockerfiles"

# Set environment variables for non interactive apt.
ENV DEBIAN_FRONTEND noninteractive

# Update the apt indexes and install required packages.
# Following the best practces for Dockerfiles we do all the apt stuff
# in a single line execution.
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       transmission-daemon \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set environment variables to set up Transmission Daemon.
ENV TRANSMISSION_HOME_DIR=/transmission
ENV TRANSMISSION_DOWNLOAD_DIR=$TRANSMISSION_HOME_DIR/download
ENV TRANSMISSION_WATCH_DIR=$TRANSMISSION_HOME_DIR/watch
ENV TRANSMISSION_INCOMPLETE_DIR=$TRANSMISSION_HOME_DIR/incomplete
ENV TRANSMISSION_CONFIG_DIR=$TRANSMISSION_HOME_DIR/config

# Configure user app.
RUN mkdir -p $TRANSMISSION_DOWNLOAD_DIR \
                $TRANSMISSION_WATCH_DIR \
                $TRANSMISSION_INCOMPLETE_DIR \
                $TRANSMISSION_CONFIG_DIR \
    && chmod 1777 /transmission

# Expose the default Transmission Daemon port.
EXPOSE 9091

# Entrypoint command for the container.
ENTRYPOINT ["/usr/bin/transmission-daemon"]

# Default command for the container.
CMD [ "--help" ]
