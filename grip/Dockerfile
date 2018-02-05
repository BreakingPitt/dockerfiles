# Base image to be used.
FROM python:2.7

# Maintainer of the Dockerfile.
LABEL maintainer "Pedro Garcia Rodriguez <pedgarrod@gmail.com>"

# Update the apt indexes and install required packages.
# Following the best practces for Dockerfiles we do all the apt stuff
# in a single line execution.
RUN pip install grip \
    && mkdir -p /export

# Expose the default Grip Server port.
EXPOSE 80

# Entrypoint command for the container.
ENTRYPOINT ["grip"]

# Default command for the container.
CMD [ "--help" ]
