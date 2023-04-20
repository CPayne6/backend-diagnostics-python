FROM mcr.microsoft.com/devcontainers/base:ubuntu-20.04

# Install Python and pip

RUN apt-get update && apt-get install -y python3.7 python3-pip

# Install app dependencies

RUN pip3 install Flask

EXPOSE 8000
