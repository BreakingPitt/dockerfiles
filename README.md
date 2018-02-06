[![Source Code](https://img.shields.io/badge/source-GitHub-blue.svg?style=flat)](https://github.com/BreakingPitt/dockerfiles) 
[![Build Status](https://travis-ci.org/BreakingPitt/dockerfiles.svg?branch=master)](https://travis-ci.org/BreakingPitt/dockerfiles)

# Breaking Pitt dockerfile learning repository.

This is a collection Dockerfiles sample configurations.

To be used with Docker http://www.docker.io

# Doucmentation of how to build images.

Build an image is pretty simple:

    cd mtr/alpine
    docker build -t breakingpitt/mtr-alpine .

Run the previously created image and attach to it at the same time:

    docker run -i -t breakingpitt/mtr-alpine:latest
    
Run the previously created image in the background
  
    docker run -d breakingpitt/mtr-alpine:latest
