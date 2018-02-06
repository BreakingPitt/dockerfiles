# Base image to be used.
FROM ubuntu:16.04

# Maintainer of the Dockerfile.
LABEL maintainer "Pedro Garcia Rodriguez <pedgarrod@gmail.com>"

# Set environment variables for non interactive apt.
ENV DEBIAN_FRONTEND noninteractive

# Metadata information.
LABEL org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.vcs-url="https://github.com/breakingpitt/dockerfiles"

# Add the PGP keys for the PostgreSQL repos.
# Add a repository source list for PostgreSQL.
RUN apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys \
    B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8 \
    && echo "deb http://apt.postgresql.org/pub/repos/apt/ trusty-pgdg main" > \
    /etc/apt/sources.list.d/postgresql.list

# Apt operations...
RUN apt-get update \
 && apt-get install -y postgresql-9.3 \
    postgresql-client-9.3 \
    postgresql-contrib-9.3 \ 
    python-software-properties \
    software-properties-common \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

# User postgres...
USER postgres

# Start the PostgreSQL service...
RUN    /etc/init.d/postgresql start

# Allow connections in the pga_hba.conf...
RUN echo "host all  all    0.0.0.0/0  md5" >> /etc/postgresql/9.3/main/pg_hba.conf

# Listen all network interfaces...
RUN echo "listen_addresses='*'" >> /etc/postgresql/9.3/main/postgresql.conf

# Volume to store PostgreSQL data.
VOLUME  ["/etc/postgresql", "/var/log/postgresql", "/var/lib/postgresql"]

# Expose required ports.
EXPOSE 5432

# Configure Dockerfile cmd command. 
CMD ["/usr/lib/postgresql/9.3/bin/postgres", "-D", "/var/lib/postgresql/9.3/main", "-c", "config_file=/etc/postgresql/9.3/main/postgresql.conf"]
