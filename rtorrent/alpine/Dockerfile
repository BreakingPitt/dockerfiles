# Base image to be used.
FROM alpine:3.7

# Maintainer of the Dockerfile.
LABEL maintainer="Pedro Garcia Rodriguez <pedgarrod@gmail.com>"

# Metadata information.
LABEL org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.vcs-url="https://github.com/breakingpitt/dockerfiles"

# Update the apk indexes and installs rTorrent packag.
# Following the best practices for Dockerfiles we do all the apk stuff
# in a single line execution.
RUN apk update \
    && apk add --update \
       rtorrent \
	  && rm -rf /var/cache/apk/*
    
# Set environment variables to set up rTorrent.
ENV RTORRENT_USER=rtorrent
ENV RTORRENT_HOME_DIR=/rtorrent
ENV RTORRENT_DOWNLOAD_DIR=$RTORRENT_HOME_DIR/rDownload
ENV RTORRENT_SESSION_DIR=$RTORRENT_HOME_DIR/rSession

# Configure user app.
RUN adduser -h $RTORRENT_HOME_DIR -s /bin/sh -D -g "" $RTORRENT_USER \ 
    && mkdir -p $RTORRENT_HOME_DIR $RTORRENT_DOWNLOAD_DIR \
    && mkdir -p $RTORRENT_HOME_DIR $RTORRENT_SESSION_DIR \
    && chmod 1777 $RTORRENT_HOME_DIR \
    && chown -R $RTORRENT_USER:$RTORRENT_USER $RTORRENT_HOME_DIR

# Copy configuration file to rTorrent home directory.
COPY rtorrent.rc $RTORRENT_HOME_DIR/.rtorrent.rc

# Volume to store rTorrent data.
VOLUME /torrents

# Run as rTorrent user.
USER $RTORRENT_USER

# Default command for the container.
ENTRYPOINT ["rtorrent"]
