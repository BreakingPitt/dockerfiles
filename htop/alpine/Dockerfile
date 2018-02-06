# Base image to be used.
FROM alpine:3.7

# Maintainer of the Dockerfile.
LABEL maintainer "Pedro Garcia Rodriguez <pedgarrod@gmail.com>"

# Update the apk indexes and installs htop.
# Following the best practices for Dockerfiles we do all the apk stuff
# in a single line execution.
RUN apk update \
    && apk add --update htop \
    && rm -rf /var/cache/apk/*

# Default command for the container.
ENTRYPOINT ["htop"]

# Configure Dockerfile cmd
CMD ["--help"]
