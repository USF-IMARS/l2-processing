## Processing steps and MATLAB routines for dashboard processing

### @dotis recently updated MATLAB processing routines for the workflows below in July 2023
### These new scripts are here: /home1/dotis/DB_files/DB_v23

### Processing streams:
1. Satellite imagery
2. River discharge data from USGS
3. Buoy data from NDBC (FK only)
4. WQ data from NERRS (SEUS only)

### TODO: These routines are in the process of being cleaned up and naming conventions standardized (in-progress July 2023)

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

### NERRS WQ Data for SEUS roi only - could use for others
1. Historical data - downloaded at (https://cdmo.baruch.sc.edu/aqs/)
   - Files are big! Order one station at a time. Need 4 digit code to select station to match w/NDBC real-time data
   - loc_IDs={'sapldq','acegp','niwws','noczb','gtmpc'};
2. Current data - Through NDBC: 
   - Sap Island SAQG1 (sapldq - Lower Duplin) Last 45 days of data (https://www.ndbc.noaa.gov/data/realtime2/SAQG1.ocean)
   - ACE Basin ACQS1 (acegp - Grove Plantation) Last 45 days of data (https://www.ndbc.noaa.gov/data/realtime2/ACQS1.ocean)
   - Winyah Bay WYSS1 (niwws - Winyah Bay Surface) - Last 45 days of data (https://www.ndbc.noaa.gov/data/realtime2/WYSS1.ocean)
   - Zeke's Basin ZBQN7 (noczb - Zekes's Basin) Last 45 days of data (https://www.ndbc.noaa.gov/data/realtime2/ZBQN7.ocean)
   - GuanTM GTQF1 (gtmpc - Pellicer Creek) Last 45 days of data (https://www.ndbc.noaa.gov/data/realtime2/GTQF1.ocean)




### USGS discharge
1. get_USGS_disharge_dbv2.sh (gets raw text files from API)
2. txt2csv_USGS_FGB_dbv2.m (converts raw text file to output .csv)
3. txt2csv_USGS_FK_dbv2.m (converts raw text file to output .csv)
Can we merge the above (2 and 3)?
