# Base image to be used.
FROM ubuntu:16.04

# Maintainer of the Dockerfile.
LABEL maintainer="Pedro Garcia Rodriguez <pedgarrod@gmail.com>"

# Set environment variables for non interactive apt.
ENV DEBIAN_FRONTEND noninteractive

# Metadata information.
LABEL org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.vcs-url="https://github.com/breakingpitt/dockerfiles"

# Add Firefox-Next ppa repository to sources.lists.d directory.
RUN apt-key adv --keyserver keyserver.ubuntu.com \
                --recv-keys 0AB215679C571D1C8325275B9BDB3D89CE49EC21 \ 
    && echo "deb http://ppa.launchpad.net/mozillateam/firefox-next/ubuntu xenial main" \
    >> /etc/apt/sources.list.d/firefox.list

# Update the apt indexes and install the required software.
# Following the best practices for Dockerfiles we do all the apt stuff
# in a single line execution for avoid unwanted layers in our docker image.
RUN apt-get update \
  && apt-get install -y --no-install-recommends \
     firefox \
     hicolor-icon-theme \
     ca-certificates \
     libasound2 \
     libgl1-mesa-dri \
     libgl1-mesa-glx \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# Container entrypoint.
ENTRYPOINT ["/usr/bin/firefox"]
