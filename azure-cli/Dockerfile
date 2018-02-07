# Base image to be used.
FROM ubuntu:latest

# Maintainer of the Dockerfile.
LABEL maintainer="Pedro Garcia Rodriguez <pedgarrod@gmail.com>"

# Metadata information.
LABEL org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.vcs-url="https://github.com/breakingpitt/dockerfiles"

# Update the apt indexes and install required packages.
# Following the best practces for Dockerfiles we do all the apt stuff
# in a single line execution.
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       apt-transport-https \
       ca-certificates \
       gnupg \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Configure Microsoft apt repositories
# and import the repository public key.
RUN apt-key adv --keyserver packages.microsoft.com --recv-keys 52E16F86FEE04B979B07E28DB02C46DF417A0893 \
    && echo "deb [arch=amd64] https://packages.microsoft.com/repos/azure-cli/ wheezy main" >> /etc/apt/sources.list.d/azure-cli.list

# Update the apt indexes and install Azure Cli.
# Following the best practces for Dockerfiles we do all the apt stuff
# in a single line execution.
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       azure-cli \    
    && apt-get clean \       
    && rm -rf /var/lib/apt/lists/*

# Entrypoint command for the container.
ENTRYPOINT ["az"]

# Default command for the container.
CMD ["--help"]
