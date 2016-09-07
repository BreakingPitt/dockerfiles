# Base image to be used.
FROM ubuntu:16.04

# Maintainer of the Dockerfile.
MAINTAINER Pedro Garcia Rodriguez<pedgarrod@gmail.com>

# Set environment variables for locale settings.
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

# Set environment variables for non interactive apt.
ENV DEBIAN_FRONTEND noninteractive

# Configure MongoDB apt repositories
# and import the repository public key. 
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10 \ 
    &&  echo "deb http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.0 main" > /etc/apt/sources.list.d/mongodb-org-3.0.list

# Update the package list and install the mongodb-10gen package.
RUN apt-get update \
    && apt-get install -y mongodb-org

# Clean unused packages and free some used space.
RUN apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Create the data dir.
VOLUME ["/data/db"]

# Set workdir directory.
WORKDIR /data/db

# Expose the default mongodb port.
EXPOSE 27017

# Default command for the container.
ENTRYPOINT ["/usr/bin/mongod"]
