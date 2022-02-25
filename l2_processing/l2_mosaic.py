# TODO: accept cmd line args for prefix & ifile below

# === Command line sequence for gpt. Command line gpt call:
# '/opt/snap_6_0/bin/gpt xml_path/map_WFS_VSNPP.xml -t target_path/target_filename -f NetCDF-BEAM in_path/inputfile1.nc in_path/inputfile2.nc'
# TODO: GPT is not yet set up

# use OCSSW scripts directly (instead of GPT)
# export OCSSWROOT=/opt/ocssw
# source $OCSSWROOT/OCSSW_bash.env
prefix="A2007143"
cmd_list = [
    'ocssw_install/bin/l2bin', 
    'ifile=files_to_mosaic_2007-05-23.txt',
    f'ofile={prefix}.L2b',
    'par=L2BIN_ARC_OC.par'
]

import subprocess
subprocess.run(
    cmd_list,
    # env='ocssw_install/OCSSW_bash.env',
)

# # processes given image in a loop
# # define variables
# for files in /srv/imars-objects/arctic/L2BIN_filelist/OC/*.txt; do input=$files
# filename="${input##*/}"
# prefix=${filename:0:15}

# DATA_DIR=/srv/imars-objects/arctic

# echo running l2bin ${prefix}... 
