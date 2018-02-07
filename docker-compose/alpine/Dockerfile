# Base image to be used.
FROM alpine:3.7

# Maintainer of the Dockerfile.
LABEL maintainer "Pedro Garcia Rodriguez <pedgarrod@gmail.com>"

# Metadata information.
LABEL org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.vcs-url="https://github.com/breakingpitt/dockerfiles"

# Update the apk indexes and installs Docker Compose.
# Following the best practices for Dockerfiles we do all the apk stuff
# in a single line execution.
RUN apk update \
    && apk add --update \
       python \
       py-setuptools \
       py2-pip \
       su-exec \
    && rm -rf /var/cache/apk/*

# Set Docker Compose installation env vars.
ENV DOCKER_COMPOSE_VERSION 1.18.0

# Configure Docker Compose install.
RUN pip install --no-cache-dir docker-compose==${DOCKER_COMPOSE_VERSION}

# Volume to store Docker Compose data.
VOLUME ["/data"]

# Default command for the container.
ENTRYPOINT ["docker-compose"]

# Configure Dockerfile cmd.
CMD ["--help"]
