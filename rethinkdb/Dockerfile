# Base image to be used.
FROM ubuntu:16.04

# Maintainer of the Dockerfile.
LABEL maintainer="Pedro Garcia Rodriguez <pedgarrod@gmail.com>"

# Set environment variables for non interactive apt.
ENV DEBIAN_FRONTEND noninteractive

# Metadata information.
LABEL org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.vcs-url="https://github.com/breakingpitt/dockerfiles"
      
# Configure RethinkDB apt repositories
# and import the repository public key. 
RUN apt-key adv --keyserver pgp.mit.edu --recv-keys 1614552E5765227AEC39EFCFA7E00EF33A8F2399 \
    && echo "deb http://download.rethinkdb.com/apt xenial main" > /etc/apt/sources.list.d/rethinkdb.list

# Update the apt indexes and install the required software.
# Following the best practices for Dockerfiles we do all the apt stuff
# in a single line execution for avoid unwanted layers in our docker image.
RUN apt-get update \
    && apt-get install -y --no-install-recommends --allow-unauthenticated \
       rethinkdb \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Volume to store RethinkDB data.
VOLUME ["/data"]

# Set workdir directory.
WORKDIR /data

# Expose required ports.
EXPOSE 28015 29015 8080

# Configure Dockerfile cmd comma
CMD ["rethinkdb", "--bind", "all"]
