#!/bin/bash

PYTHON_PATH=$(which python3)
PWD=$(pwd)

sed "1 i\\#!$PYTHON_PATH " housekeeping.py
chmod +x housekeeping.py
ln -s $PWD/housekeeping.py /usr/bin/housekeeping

