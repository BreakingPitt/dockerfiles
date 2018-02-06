# Base image to be used.
FROM java:8

# Maintainer of the Dockerfile.
LABEL maintainer "Pedro Garcia Rodriguez <pedgarrod@gmail.com>"

# Set environment variables for non interactive apt.
ENV DEBIAN_FRONTEND noninteractive

# Metadata information.
LABEL org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.vcs-url="https://github.com/breakingpitt/dockerfiles"

# Download and extract ElasticSearch.
# Following the best practices for Dockerfiles we do all the apt stuff
# in a single line execution for avoid unwanted layers in our docker image.
RUN cd /tmp \
    && wget https://download.elastic.co/elasticsearch/release/org/elasticsearch/distribution/tar/elasticsearch/2.4.0/elasticsearch-2.4.0.tar.gz \
    && tar xvzf elasticsearch-2.4.0.tar.gz \
    && rm -f elasticsearch-2.4.0.tar.gz \
    && mv /tmp/elasticsearch-2.4.0 /opt/elasticsearch

# Volume to store RethinkDB data.
VOLUME ["/data"]

# Set workdir directory.
WORKDIR /data

# Expose required ports.
EXPOSE 9200 9300

# Configure Dockerfile cmd comma
CMD ["/opt/elasticsearch/bin/elasticsearch"]
