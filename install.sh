#!/bin/bash

PYTHON_PATH=$(which python3)
PWD=$(pwd)

sed "1 i\\#!$PYTHON_PATH " -i housekeeping.py
chmod +x housekeeping.py
ln -s $PWD/housekeeping.py /usr/bin/housekeeping

echo "house-directories: /etc/housekeeping.d" > /etc/housekeeping.yaml
mkdir /etc/housekeeping.d