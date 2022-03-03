from datetime import datetime
import os

from parse import parse

class GranuleAggregator(object):
    """
    used to aggregate granule files into temporal resolutions like:
        * daily
        * 8d
        * 30d
        * monthly
    """    
    def __init__(self, granules_directory='./MODA_OC_py_data', granule_file_format_str="A{dt:d}.L{level:d}_LAC_{product_type:l}.x.nc"):
        """
        Parameters
        ----------
        granules_directory : filepath str
            Directory with granule files.
        granule_file_format_str : parse package format string
            String describing the metadata that can be extracted from the filename. 
            Examples: 
                * "A{year:4d}{jday:3d}{hrs:2d}{min:2d}{sec:2d}.L{level:d}_LAC_{product_type:l}.x.nc"
        """
        self.granule_file_format_str = granule_file_format_str
        self.granules_dir = os.path.expanduser(granules_directory)    
        self.granule_files = self.get_granule_files()
        self.granules = {}
        self.granule_metadata = self.parse_granule_metadata_from_filenames()
        
    def get_granule_files(self):
        """Gets a list of granule files in the granules directory.
        Returns
        -------
        list of filename strings
            List containing all granule files in the directory.
        
        Code assumes this directory contains *only* data files matching the given granule_file_format_str.
        TODO: deal with subdirectories. 
        TODO: Do not list non-granule files in the granules_dir.
        """
        return os.listdir(self.granules_dir)

    def parse_granule_metadata_from_filenames(self):
        """Read metadata from the granule file paths and create the self.granule_files dict."""
        for filename in self.granule_files:
            params_parsed = parse(self.granule_file_format_str, filename)
            file_metadata = {
                'metadata_parsed_from_fname': params_parsed,
                'datetime_obj': datetime.strptime(str(params_parsed['dt']), "%Y%j%H%M%S")
            }
            print(f"{filename} | {file_metadata}")  # TODO: use logger here
            self.granules[filename] = file_metadata     
            
        #     if params_parsed['product_type'] == "OC":
        #         print("ocean color")
        #     elif params_parsed['product_type'] == "SST":
        #         print("sea surface temp")
        #     else:
        #         print("unknown product type")

    def get_daily_granules(self):
        """Group granule files by date and write a .txt file for each day.
        
        Returns
        -------
        list of .txt filepaths
            list of .txt files created
        """
        days_to_mosaic = {}
        for granule_filename in self.granules:
            granule_metadata = self.granules[granule_filename]
            day_date = granule_metadata["datetime_obj"].date()
            if days_to_mosaic.get(day_date) is None:  # if no granules for this day yet
                days_to_mosaic[day_date] = []
            days_to_mosaic[day_date].append(granule_filename)  # add this granule to the appropriate day

        txt_file_list = []
        for day_to_mosaic in days_to_mosaic:
            # create .txt with list of input files
            txt_fpath = f"files_to_mosaic_{day_to_mosaic}.txt"
            with open(txt_fpath, 'w') as txt_file:
                txt_file.write(' \n'.join(days_to_mosaic[day_to_mosaic]))
                txt_file_list.append(txt_fpath)
        return txt_file_list

