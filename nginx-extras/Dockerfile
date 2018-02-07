# Base image to be used.
FROM ubuntu:17.10

# Maintainer of the Dockerfile.
LABEL maintainer="Pedro Garcia Rodriguez <pedgarrod@gmail.com>"

# Metadata information.
LABEL org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.vcs-url="https://github.com/breakingpitt/dockerfiles"

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       ca-certificates \
       lua-cjson \
       lua-iconv \
       nginx-extras \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Forward request and error logs to docker log collector
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
        && ln -sf /dev/stderr /var/log/nginx/error.log

# Expose required ports.
EXPOSE 80 443

# Default command for the container.
CMD ["nginx", "-g", "daemon off;"]
