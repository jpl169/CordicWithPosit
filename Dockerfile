FROM ubuntu:18.04

ENV DEBIAN_FRONTEND noninteractive

##################################################################
# Install necessary apt packages
##################################################################
RUN apt-get update && \
    apt-get install -yq --no-install-recommends apt-utils && \
    apt-get install -yq build-essential python3 python3-pip libgmp3-dev libmpfr-dev git && \
    python3 -m pip install numpy matplotlib

WORKDIR /home

##################################################################
# Install SoftPosit
##################################################################
RUN git clone https://gitlab.com/cerlane/SoftPosit.git && \
    cd SoftPosit/build/Linux-x86_64-GCC/ && \
    make && \
    cd ../../..

##################################################################
# Set environment variables
##################################################################
ENV SOFTPOSITPATH=/home/SoftPosit/

##################################################################
# Download and make Cordic with Posit
##################################################################
RUN git clone https://github.com/jpl169/CordicWithPosit.git && \
    cd CordicWithPosit && \
    make