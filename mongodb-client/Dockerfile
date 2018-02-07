# Base image to be used.
FROM ubuntu:14.04

# Maintainer of the Dockerfile.
LABEL maintainer="Pedro Garcia Rodriguez <pedgarrod@gmail.com>"

# Set environment variables for non interactive apt.
ENV DEBIAN_FRONTEND noninteractive

# Metadata information.
LABEL org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.vcs-url="https://github.com/breakingpitt/dockerfiles"

# Configure MongoDB apt repositories
# and import the repository public key.
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10 \
    &&  echo "deb http://repo.mongodb.org/apt/ubuntu "$(lsb_release -sc)"/mongodb-org/3.2 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-3.2.list

# Update the package list and install the mongodb-10gen package.
RUN apt-get update \
    && apt-get install -y --force-yes --no-install-recommends \
       mongodb-org-tools \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Create the data dir.
VOLUME ["/data/db"]

# Set workdir directory.
WORKDIR /data/db

# Expose the default mongodb port.
EXPOSE 27017

# Default command for the container.
ENTRYPOINT ["/usr/bin/mongod"]
