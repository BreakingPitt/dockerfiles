# Base image to be used.
FROM ubuntu:16.04

# Maintainer of the Dockerfile.
LABEL maintainer="Pedro Garcia Rodriguez <pedgarrod@gmail.com>"

# Metadata information.
LABEL org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.vcs-url="https://github.com/breakingpitt/dockerfiles"

# Set environment variables for non interactive apt.
ENV DEBIAN_FRONTEND noninteractive

# Add the PGP keys for the PostgreSQL repos.
# Add a repository source list for PostgreSQL.
RUN apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys \
    B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8 \
    && echo "deb http://apt.postgresql.org/pub/repos/apt/ trusty-pgdg main" > \
    /etc/apt/sources.list.d/postgresql.list

# Apt operations...
RUN apt-get update \
 && apt-get install -y \
    postgresql-client-9.3 \
    python-software-properties \
    software-properties-common \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*
