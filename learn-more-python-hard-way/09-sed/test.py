import sys
import os
import argparse
import re
import logging
import subprocess
import unittest
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

test_bin_python = "/usr/local/bin/python3"

test_script_sed = "implement-sed.py"
if not (os.path.isfile(test_script_sed)):
    self_dir = os.path.dirname(os.path.realpath(__file__))
    test_script_sed = os.path.join(self_dir, test_script_sed)
assert os.path.isfile(test_script_sed), "Failed to find 'implement-find.py' and '%s'" % test_script_sed

test_data_dir = "../data_test"
if not (os.path.isdir(test_data_dir)):
    test_data_dir = "data_test"
assert os.path.isdir(test_data_dir), "Failed to find '../data_test' and 'data_test'"
    
test_file_path_csv = os.path.join(test_data_dir, "values.csv")
test_file_path_allbytes = os.path.join(test_data_dir, "allbytes.hex")

class Test_ImplementSed(unittest.TestCase):

    #   TODO: 2021-07-11T22:17:29AEST Before tests, test for existance each filesystem item that needs to exists, then script version, and exit if either fail

    def get_BinPython_Sed_OutputAndRC(self, args_binpython, args_sed, decode_result=True):
        args_binpython = [ test_bin_python, test_script_sed ] + args_binpython
        proc = subprocess.Popen(args_binpython, stdout=subprocess.PIPE)
        (out_test, err_test) = proc.communicate()
        rc_test = proc.returncode
        args_sed = [ 'sed' ] + args_sed
        proc = subprocess.Popen(args_sed, stdout=subprocess.PIPE)
        (out_check, err_check) = proc.communicate()
        rc_check = proc.returncode
        if (decode_result):
            return (out_test.decode(), rc_test, out_check.decode(), rc_check)
        else:
            return (out_test, rc_test, out_check, rc_check)

    #   Others:
    def test_getversion(self):
        """Verify version string starts with 'python-cut' followed by a decimal number"""
        args = [ '--version' ]
        result = self.get_BinPython_Sed_OutputAndRC(args, args)
        (out_test, rc_test, out_check, rc_check) = result
        self.assertEqual(rc_test, rc_check)
        self.assertRegex(out_test, re.compile("^python-sed \d+\.\d+.*"))
    #   TODO: incorrect args tests
    
    
if __name__ == '__main__':
    unittest.main()
