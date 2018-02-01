# Base image to be used.
FROM ubuntu:latest

# Maintainer of the Dockerfile.
MAINTAINER Pedro Garcia Rodriguez<pedgarrod@gmail.com>

RUN apt-get update \
    && apt-get install -y ca-certificates \
                          lua-cjson \
                          lua-iconv \
                          nginx \
       --no-install-recommends \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Forward request and error logs to docker log collector
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
        && ln -sf /dev/stderr /var/log/nginx/error.log

# Expose required ports.
EXPOSE 80 443

# Default command for the container.
CMD ["nginx", "-g", "daemon off;"]
