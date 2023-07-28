## Processing steps and MATLAB routines for dashboard processing

### Processing streams:
1. Satellite imagery
2. Buoy data from NDBC
3. River discharge data from USGS

### TODO: These routines need to be cleaned up and naming conventions standardized

### Satellite imagery 
1. Mosaic pass files to 1-Day scenes over entire ROI (MOSAIC_OC_func_GOMdb_v2023.m - run by run_mosaic_1D_GOMdb_v2023.m)
2. Create 7-day means (MEAN_7D_func_GOMdb_MODA(and VSNPP).m - run by run_mean_7D_GOMdbv2_GOM.m)
3. Extract values at polygons and points of interest (Extract_satTS_func_GOM2023.m - saves as .mat)
  Two versions: one for all files and one for recent files (to save time on tpa_pgs)
4. Convert .mat time series files to .csv (TS_BIN_CSV_func_dbv2_all.m - sets output directory for .csv; transistions at 1/1/2023)
  Two versions: one for all files and one for recent files (to save time on tpa_pgs)
  Both routines above (3 and 4) are run by RUN_EXT_1D_GOM_dbv2.m

### NDBC Buoy data
1. get_NDBC_temp_sal_FK_dbv2.sh (gets raw text files from API)
2. get_data_NDBC_FK_dbv2.m (converts raw text file to output .csv)
Can we streamline the above (will need to include SEUS)

### USGS discharge
1. get_USGS_disharge_dbv2.sh (gets raw text files from API)
2. txt2csv_USGS_FGB_dbv2.m (converts raw text file to output .csv)
3. txt2csv_USGS_FK_dbv2.m (converts raw text file to output .csv)
Can we merge the above (2 and 3)?
