# std modules:
from unittest import TestCase

# tested module(s):
from l2_processing import ocssw_example_usage

class Test_generate_l2bin_call(TestCase):

    # === tests ============================================================
    def test_cli_command_looks_right(self):
        """  """
        self.assertEqual(
            ocssw_example_usage.generate_l2bin_call("test/filepath.txt"),
            [
                'l2bin', 
                'ifile=test/filepath.txt', 
                'ofile=/srv/imars-objects/arctic/L2BIN/OC/test/filepath.txt.l3b', 
                'parfile=/srv/imars-objects/arctic/parfiles/example_parfile_filname.par'
            ]
        )
