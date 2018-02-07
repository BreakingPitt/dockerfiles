# Base image to be used.
FROM ubuntu:14.04

# Maintainer of the Dockerfile.
LABEL maintainer="Pedro Garcia Rodriguez <pedgarrod@gmail.com>"

# Based on the work done by...
MAINTAINER Michael Guymon, michael@tobedevoured.com

# Operate with root user.
USER root

# Set environment variables.
ENV DEBIAN_FRONTEND noninteractive

# Metadata information.
LABEL org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.vcs-url="https://github.com/breakingpitt/dockerfiles"

# Set environment variables for JBoss Torquebox...
ENV TORQUEBOX_HOME /opt/torquebox
ENV JBOSS_HOME /opt/torquebox/jboss
ENV JRUBY_HOME /opt/torquebox/jruby
ENV PATH $JBOSS_HOME/bin:$JRUBY_HOME/bin:$PATH

# Create Torquebox user...
RUN useradd torquebox -c "Torquebox system user" -M -ptorquebox

# Install required packages...
RUN apt-get update \
    && apt-get install -y software-properties-common \
    && add-apt-repository ppa:webupd8team/java -y \
    && apt-get update \
    && echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections \
    && apt-get install -y unzip wget oracle-java8-installer

# Download, unzip and configure JBoss Torquebox...
RUN wget -O /opt/torquebox-dist-3.1.0-bin.zip http://torquebox.org/release/org/torquebox/torquebox-dist/3.1.0/torquebox-dist-3.1.0-bin.zip \
    && unzip -q /opt/torquebox-dist-3.1.0-bin.zip -d /opt \
    && mv /opt/torquebox-3.1.0 /opt/torquebox \
    && mkdir -p /opt/torquebox/applications \
    && chown -R torquebox:torquebox /opt/torquebox

# Expose ports...
EXPOSE 9990 8080

# The command that run the container...
CMD ["/opt/torquebox/jboss/bin/standalone.sh","-b", "0.0.0.0"]
