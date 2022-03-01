# Steps for L2 processing:
Example ROI: Arctic (Chukchi Sea)
Three product suites: OC, SST4, IOP.

OCSSW method:
L2BIN followed by L3MAPGEN (no gpt)
Steps:
1. Cull bad files by counting valid pixels.
Use a test product for each prod_class:
OC: “chlor_a”
SST4: “sst4”
IOP: “ adg_443_giop”
Example ML code:
eval(['data=ncread(file,''/geophysical_data/' test_prod ''');'])
data_scl=data.*scale_factor+offset;
pix_good=(data_scl>=0);
sum_pix_good=nansum(pix_good(:));

2. L2BIN by 1-day intervals. Or, w/8-day?, 30-day?
Set params in .par file



3. Map resulting output using L3MAPGEN 
Set params in .par file
CHUK/AMBON region 
64 to 73N; -179.5 to -157E







Mosaic/gpt operator method:
Input files: /srv/imars-objects/arctic/L2_OC (or SST4, IOP).

Tasks:
1. Remove 
2. Read input files and parse filenames by year and day of year (DOY)
3. Loop on year/DOY and create a gpt calling sequence for each year/DOY/product suite
4. Eeach ROI and product suite needs an xml graph with processing parameters (spatial extent, products, bandmaths)
5. GPT calling sequence: '/opt/snap_6_0/bin/gpt ' xml_file ' -t ' path_out 'V' time_start '_' roi_2 '_' pc '_1D.nc -f NetCDF-BEAM ' list of output files ''';'])
6. Execute calling sequence
7. Output L3 daily files go here: /srv/imars-objects/fk/L3_1D_MODA/OC (or SST,SST4,IOP)

Parameters to consider:
Sensors: VSNPP and MODA (could add S3)

ROI: fk, fgb, wfs, gom, other?

Product suites: OC, SST/SST4, IOP
