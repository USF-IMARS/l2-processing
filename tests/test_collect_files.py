# std modules:
from unittest import TestCase

class Test_CollectDataFiles(TestCase):

    # === tests ============================================================
    def test_collect_granules(self):
        """ look at the .nc files in a dir and ls the ones to be used in a mosaic """
        import os
        path_in=os.path.expanduser('~/MODA_OC_py_data')
        # Retrieve filelist
        basename = os.path.basename(path_in)

        files = os.listdir(path_in)
        
        from parse import parse
        from datetime import datetime
        import subprocess

        days_to_mosaic = {}
        for filename in files:
        #     params_parsed = parse("A{year:4d}{jday:3d}{hrs:2d}{min:2d}{sec:2d}.L{level:d}_LAC_{product_type:l}.x.nc", filename)
            params_parsed = parse("A{dt:d}.L{level:d}_LAC_{product_type:l}.x.nc", filename)
            print(f"{filename} | {params_parsed}")

        #     if params_parsed['product_type'] == "OC":
        #         print("ocean color")
        #     elif params_parsed['product_type'] == "SST":
        #         print("sea surface temp")
        #     else:
        #         print("unknown product type")
            dt_obj = datetime.strptime(str(params_parsed['dt']), "%Y%j%H%M%S")

            if days_to_mosaic.get(dt_obj.date()) is None:
                days_to_mosaic[dt_obj.date()] = []

            days_to_mosaic[dt_obj.date()].append(path_in + '/' + filename)


        # print(days_to_mosaic)
        # for each day:
        for day_to_mosaic in days_to_mosaic:
            # create .txt with list of input files
            with open(f"files_to_mosaic_{day_to_mosaic}.txt", 'w') as txt_file:
                txt_file.write(' \n'.join(days_to_mosaic[day_to_mosaic]))

            # call gpt w/ outfile name, xml graph, & list of input files   
            # TODO: set this command to the actual gpt command
            # subprocess.run([
            #     'echo', 
            #     'gpt', 
            #     'xmlgraph=yada.xml', 
            #     f"outfile={day_to_mosaic}_8d.nc", 
            #     "filenames="+" ".join(days_to_mosaic[day_to_mosaic])
            # ])


        
