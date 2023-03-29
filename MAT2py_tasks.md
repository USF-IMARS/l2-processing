## General info and tasks to move L2 processing from MATLAB to py

L2 to L3 (three product suites - OC, SST, SST4/N)

There are two ways to do this:
1. OCSSW: use L2BIN and then L3MAPGEN (requires param file) - I think @7yl4r started some py code for this method 
2. gpt: use mosaic operator (requires xml file)

Currently ML routines by @dotis use the 2nd method. GPT may not be installed on manglilloo?

## ML routines w/brief description (these are found in /home1/dotis/DB_files/DB_v2/):
1. MOSAIC_1D_func_GOMdb_v2023.m (function to call gpt to map and bin L2 files by day for a selected ROI (GOM, *FK, *FGB) *will be deprecated
2. CLIM_7D_dbv2_MODA.m (function to create 7Day climatolgy files for MODA (OC, SST, SST4).
3. CLIM_7D_dbv2_VSNPP.m (function to create 7Day climatology files for VSNPP (OC, SST, SSTN). The MODA and VSNPP functions can be combined.
4. MEAN_7D_func_GOMdbv2_MODA.m (function to create 7Day mean files for MODA (OC, SST, SST4). Requires climatology files for each product.
5. MEAN_7D_func_GOMdbv2_VSNPP.m (function to create 7Day mean files for VSNPP (OC, SST, SST4). The MODA and VSNPP functions can be combined.
6. Extract_rawTS_func_dbv2.m (function to extract sat. data from daily L3 mapped files and output as .mat).
7. Output_sat_csv_func_dbv2.m (function to convert .mat files made in #6 to .csv)

There are some other dashboard related functions for NDBC buoy data and USGS river discharge data that are not on this list. 
