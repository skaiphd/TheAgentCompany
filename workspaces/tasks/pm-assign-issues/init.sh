#!/bin/sh
set -ex

########## PRE INIT PHASE ############
python /utils/pre_init.py
######################################

########## RUN INITIALIZATION ########
python /utils/populate_data.py
######################################