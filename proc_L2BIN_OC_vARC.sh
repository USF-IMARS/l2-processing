#!/bin/bash

# set environment variabless
export OCSSWROOT=/opt/ocssw
source $OCSSWROOT/OCSSW_bash.env

# processes given image in a loop
# define variables
for files in /srv/imars-objects/arctic/L2BIN_filelist/OC/*.txt; do input=$files
filename="${input##*/}"
prefix=${filename:0:15}

DATA_DIR=/srv/imars-objects/arctic

echo running l2bin ${prefix}...
l2bin ifile=$DATA_DIR/L2BIN_filelist/OC/${prefix}_filelist.txt ofile=$DATA_DIR/L2BIN/OC/${prefix}.L2b par=$DATA_DIR/L2BIN_ARC_OC.par

done
