#!/usr/bin/env sh

sudo apt-get install aptitude
sudo aptitude update
sudo aptitude -y upgrade
sudo aptitude -y install python3-bs4 libnss-resolve nscd
