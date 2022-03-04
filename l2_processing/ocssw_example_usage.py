# === use OCSSW scripts directly (instead of GPT)
# export OCSSWROOT=/opt/ocssw
# source $OCSSWROOT/OCSSW_bash.env
# prefix="A2007143"
# cmd_list = [
#     'ocssw_install/bin/l2bin', 
#     'ifile=files_to_mosaic_2007-05-23.txt',
#     f'ofile={prefix}.L2b',
#     'par=L2BIN_ARC_OC.par'
# ]

# import subprocess
# subprocess.run(
#     cmd_list,
#     # env='ocssw_install/OCSSW_bash.env',
# )

FPATH_PREFIX = "/srv/imars-objects/arctic"

def generate_l2bin_call(txt_filepath_in):
    # TODO: get metadata txt_filepath_in filepath
    # TODO: get parfile depending on what we are processing
    #       3 product classes: oc, sst4, iop
    # TODO: generalize filepath generation
    return [
        'l2bin', 
        f'ifile={txt_filepath_in}',  # .txt with list of .nc files
        f'ofile={FPATH_PREFIX}/L2BIN/OC/{txt_filepath_in}.l3b',  # where the .l3b will go
        f'parfile={FPATH_PREFIX}/parfiles/example_parfile_filname.par'  # different par file for OC
    ]

