# Base image to be used.
FROM alpine:3.7

# Maintainer of the Dockerfile.
LABEL maintainer="Pedro Garcia Rodriguez <pedgarrod@gmail.com>"

# Metadata information.
LABEL org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.vcs-url="https://github.com/breakingpitt/dockerfiles"

# Set environment variable for downloading terraform version.
ENV PACKER_VERSION=1.2.0

# Update the apt indexes and install the required software.
# Following the best practices for Dockerfiles we do all the apt stuff
# in a single line execution for avoid unwanted layers in our docker image.
RUN apk update \
    && apk add --update \ 
       ca-certificates \
       curl \
       unzip \
    && rm -rf /var/cache/apk/* \
    && curl -o /tmp/packer_${PACKER_VERSION}_linux_amd64.zip https://releases.hashicorp.com/packer/${PACKER_VERSION}/packer_${PACKER_VERSION}_linux_amd64.zip \
    && mkdir -p /opt/packer \
    && unzip /tmp/packer_${PACKER_VERSION}_linux_amd64.zip -d /opt/packer 

# Volume to store Terraform data.
VOLUME ["/data"]

# Set workdir directory.
WORKDIR /data

# Entrypoint command for the container.
ENTRYPOINT ["/opt/packer/packer"]

# Default command for the container.
CMD ["--help"]
