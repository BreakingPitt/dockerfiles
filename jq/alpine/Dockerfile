# Base image to be used.
FROM alpine:3.7

# Maintainer of the Dockerfile.
LABEL maintainer="Pedro Garcia Rodriguez <pedgarrod@gmail.com>"

# Metadata information.
LABEL org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.vcs-url="https://github.com/breakingpitt/dockerfiles"

# Environment variables to setup JQ application.
ENV version 1.5

# Update the apk indexes and installs curl package.
# Following the best practices for Dockerfiles we do all the apk stuff
# in a single line execution.
RUN apk update \
    && apk add --update \
       ca-certificates \
       curl \
    && rm -rf /var/cache/apk/*
    
# Download an configure required files in order to work 
# with JQ application.
RUN curl -o /usr/local/bin/jq -L https://github.com/stedolan/jq/releases/download/jq-$VERSION/jq-linux64 \
    && chmod +x /usr/local/bin/jq

# Default command for the container.
ENTRYPOINT ["/usr/local/bin/jq"]

# Configure Dockerfile cmd.
CMD        ["--help"]
