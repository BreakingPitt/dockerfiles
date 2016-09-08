# Base image to be used.
FROM python:2.7

# Maintainer of the Dockerfile.
MAINTAINER Pedro Garcia Rodriguez <pgr@taric.es>

# Operate with root user.
USER root

# Set environment variables for noninteactive user choices
# in package managementenoninteactive user choices.
ENV DEBIAN_FRONTEND noninteractive

# Install pypiserver.
RUN pip install -U pypiserver \
    && pip install passlib

# Create pypiserver default user.
RUN useradd -d /var/lib/pypiserver -m pypiserver -p pyp1s3rv3r

# Create required directories for pypiserver.
# Data directory: /var/lib/pypiserver.
# Package directory: /var/lib/pypiserver/packages.
# Env package directory: /usr/share/pypiserver/senv.
# Scrupt directory: /var/lib/pypiserver/scripts.
RUN mkdir -p /var/lib/pypiserver \
    /var/lib/pypiserver/packages \
    /usr/share/pypiserver/senv \
    /var/lib/pypiserver/scripts

# Set owner and group to pypeserver:www-data
# on the required dirs.
RUN chown -R pypiserver:www-data /var/lib/pypiserver \
    /var/lib/pypiserver/packages \
    /usr/share/pypiserver/senv \
    /var/lib/pypiserver/scripts

# Copy required download-pckages.py program to scripts directory.
COPY files/download-packages.py /var/lib/pypiserver/scripts

# Copy required download-pckages.sh program to scripts directory.
COPY files/download-packages.sh /var/lib/pypiserver/scripts

# Copy required fetch-missed-packages.sh program to scripts directory.
COPY files/fetch-missed-packages.sh /var/lib/pypiserver/scripts

# Copy required fetch-missed-packages.sh program to scripts directory.
COPY files/.htaccess /var/lib/pypiserver/

# Set enviroment variables to set pypserver home directory.
ENV HOME /var/lib/pypiserver

# Set enviroment variables to configure the behavior of pypiserver.
ENV WORKERS 4

# Set workdir directory.
WORKDIR /var/lib/pypiserver

# Operate with root user.
USER pypiserver

# Exposed port.
EXPOSE 8080

# Always starts with the .htaccess,
ENTRYPOINT ["pypi-server", "-P", "/var/lib/pypiserver/.htaccess", "-r", "/var/lib/pypiserver/packages"]

# Hack : add a CMD with default value to enable passing other options.
CMD ["-p", "8080"]
