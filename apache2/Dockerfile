# Base image to be used.
FROM ubuntu:17.10

# Maintainer of the Dockerfile.
LABEL maintainer "Pedro Garcia Rodriguez <pedgarrod@gmail.com>"

# Set environment variables for non interactive apt.
ENV DEBIAN_FRONTEND noninteractive

# Update the apt indexes and install the Apache2 server.
# Following the best practces for Dockerfiles we do all the apt stuff
# in a single line execution.
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       apache2 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Expose the default Apach2 Web Server port.
EXPOSE 80

# Default command for the container.
ENTRYPOINT ["/usr/bin/apache2"]
