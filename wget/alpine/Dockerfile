# Base image to be used.
FROM alpine:3.7

# Maintainer of the Dockerfile.
LABEL maintainer "Pedro Garcia Rodriguez <pedgarrod@gmail.com>"

# Metadata information.
LABEL org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.vcs-url="https://github.com/breakingpitt/dockerfiles"

# Update the apk indexes and installs Apache Benchmark.
# Following the best practices for Dockerfiles we do all the apk stuff
# in a single line execution.
RUN apk update \
    && apk add --update \
       wget \
       ca-certificates \
    && rm -rf /var/cache/apk/*

# Default command for the container.
ENTRYPOINT ["wget"]

# Configure Dockerfile cmd.
CMD ["--help"]
