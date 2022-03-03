# std modules:
from unittest import TestCase

from l2_processing.GranuleAggregator import GranuleAggregator

class Test_GranuleAggregator_get_granule_files(TestCase):
    def test_collect_granules_from_test_data(self):
        """List of granules in ./MODA_OC_py_data is correct"""
        aggregator = GranuleAggregator(granules_directory='./MODA_OC_py_data')
        self.assertEqual(
            aggregator.get_granule_files(),
            [
                'A2007143182500.L2_LAC_OC.x.nc',
                'A2007143183000.L2_LAC_OC.x.nc',
                'A2007143200500.L2_LAC_OC.x.nc',
                'A2007144191000.L2_LAC_OC.x.nc',
                'A2007145181500.L2_LAC_OC.x.nc',
                'A2007145195000.L2_LAC_OC.x.nc',
                'A2007145195500.L2_LAC_OC.x.nc',
                'A2007146185500.L2_LAC_OC.x.nc',
                'A2007146190000.L2_LAC_OC.x.nc',
                'A2007146203500.L2_LAC_OC.x.nc',
            ]
        )

        
class Test_GranuleAggregator_get_granule_files(TestCase):
    def test_daily_group_granules_from_test_data(self):
        """List .txt files generated from granules in ./MODA_OC_py_data is correct"""
        aggregator = GranuleAggregator(granules_directory='./MODA_OC_py_data')
        self.assertEqual(
            aggregator.get_daily_granules(),
            [
                'files_to_mosaic_000.txt',
                'files_to_mosaic_001.txt',
            ]
        )

        
