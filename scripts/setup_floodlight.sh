#!/usr/bin/env bash

if [ "$EUID" != "0" ];then
  echo "Must be run as root"
  exit 1
fi

# install dependencies
apt update
apt install -y openjdk-8-jre-headless openjdk-8-jdk-headless build-essential ant maven python-dev git

# add sources
cd /
git clone https://github.com/floodlight/floodlight.git -b v1.2 floodlight
cd /floodlight
git submodule init
git submodule update

# build
ant
sudo mkdir /var/lib/floodlight
sudo chmod 777 /var/lib/floodlight
