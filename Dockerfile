#####################################################################
# This dockerfile is to set up the environment for this svo package.
# Ex. usage:
#  bash "docker build -t kinetic-svo ."
#####################################################################
FROM ros:kinetic-ros-core

# Install python opencv, cv_bridge and usb_cam ros package.
RUN apt-get update && apt-get install --no-install-recommends -y \
    ros-kinetic-cv-bridge \
    ros-kinetic-usb-cam \
    && rm -rf /var/lib/apt/lists/*
