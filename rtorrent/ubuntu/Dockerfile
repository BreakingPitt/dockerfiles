# Base image to be used.
FROM ubuntu:17.10

# Maintainer of the Dockerfile.
LABEL maintainer "Pedro Garcia Rodriguez <pedgarrod@gmail.com>"

# Metadata information.
LABEL org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.vcs-url="https://github.com/breakingpitt/dockerfiles"
      
# Set environment variables for non interactive apt.
ENV DEBIAN_FRONTEND noninteractive

# Update the apt indexes and install the rTorrent package.
# Following the best practces for Dockerfiles we do all the apt stuff
# in a single line execution.
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       rtorrent \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set environment variables to set up rTorrent.
ENV RTORRENT_USER=rtorrent
ENV RTORRENT_HOME_DIR=/rtorrent
ENV RTORRENT_DOWNLOAD_DIR=$RTORRENT_HOME_DIR/rDownload
ENV RTORRENT_SESSION_DIR=$RTORRENT_HOME_DIR/rSession

# Configure user app.
RUN adduser --home $RTORRENT_HOME_DIR --shell /bin/sh --disabled-password --gecos "" $RTORRENT_USER \ 
    && mkdir -p $RTORRENT_HOME_DIR $RTORRENT_DOWNLOAD_DIR \
    && mkdir -p $RTORRENT_HOME_DIR $RTORRENT_SESSION_DIR \
    && chmod 1777 $RTORRENT_HOME_DIR \
    && chown -R $RTORRENT_USER:$RTORRENT_USER $RTORRENT_HOME_DIR

# Copy configuration file to rTorrent home directory.
COPY rtorrent.rc $RTORRENT_HOME_DIR/.rtorrent.rc

# Run as rTorrent user.
USER $RTORRENT_USER

# Default command for the container.
ENTRYPOINT ["rtorrent"]
