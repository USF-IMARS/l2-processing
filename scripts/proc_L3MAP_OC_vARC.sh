#!/bin/bash

# set environment variabless
export OCSSWROOT=/opt/ocssw
source $OCSSWROOT/OCSSW_bash.env

# processes given image in a loop
# define variables
for files in /srv/imars-objects/arctic/L2BIN/OC/*.L2b; do input=$files
filename="${input##*/}"
prefix=${filename:0:8}

DATA_DIR=/srv/imars-objects/arctic

echo running l3mapgen ${prefix}...
l3mapgen ifile=$DATA_DIR/L2BIN/OC/${prefix}_ARC_OC.L2b ofile=$DATA_DIR/L3MAP/OC/${prefix}_ARC_OC.L3map par=$DATA_DIR/L3MAPGEN_ARC_OC.par

done
