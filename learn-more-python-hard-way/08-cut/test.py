import sys
import os
import re
import argparse
import unittest
import subprocess
import logging
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

test_bin_python = "/usr/local/bin/python3"

test_script_cut = "implement-cut.py"
if not (os.path.isfile(test_script_cut)):
    self_dir = os.path.dirname(os.path.realpath(__file__))
    test_script_cut = os.path.join(self_dir, test_script_cut)
assert(os.path.isfile(test_script_cut), "Failed to find 'implement-find.py' and '%s'" % test_script_cut)

test_data_dir = "../data_test"
if not (os.path.isdir(test_data_dir)):
    test_data_dir = "data_test"
assert(os.path.isdir(test_data_dir), "Failed to find '../data_test' and 'data_test'")
    


test_file_path_csv = os.path.join(test_data_dir, "values.csv")
test_file_path_allbytes = os.path.join(test_data_dir, "allbytes.hex")

class Test_ImplementCut(unittest.TestCase):

    def get_BinPython_Cut_OutputAndRC(self, args_binpython, args_cut, decode_result=True):
        args_binpython = [ test_bin_python, test_script_cut ] + args_binpython
        proc = subprocess.Popen(args_binpython, stdout=subprocess.PIPE)
        (out_test, err_test) = proc.communicate()
        rc_test = proc.returncode
        args_cut = [ 'cut' ] + args_cut
        proc = subprocess.Popen(args_cut, stdout=subprocess.PIPE)
        (out_check, err_check) = proc.communicate()
        rc_check = proc.returncode
        if (decode_result):
            return (out_test.decode(), rc_test, out_check.decode(), rc_check)
        else:
            return (out_test, rc_test, out_check, rc_check)

    def compare_BinPython_Cut_OutputAndRC(self, args_binpython, args_cut, decode_result=True):
        result = self.get_BinPython_Cut_OutputAndRC(args_binpython, args_cut, decode_result)
        (out_test, rc_test, out_check, rc_check) = result
        self.assertEqual(out_test, out_check, "Comparing stdout values")
        self.assertEqual(rc_test, rc_check, "Comparing return-codes")

    #   TODO: 2021-07-11T14:18:45AEST (find) additional test case(s) for which implement-cut.py is not equivalent to cut?

    #   -f: fields tests
    def test_csv_fields_all(self):
        args = [ "-d", ",", "-f", "1-", test_file_path_csv ]
        self.compare_BinPython_Cut_OutputAndRC(args, args)
    def test_csv_fields_26(self):
        args = [ "-d", ",", "-f", "2-6", test_file_path_csv ]
        self.compare_BinPython_Cut_OutputAndRC(args, args)
    def test_csv_fields_outputdelim_26(self):
        args = [ "-d", ",", "-f", "2-6", "--output-delimiter", ";", test_file_path_csv ]
        self.compare_BinPython_Cut_OutputAndRC(args, args)

    #   -c: columns tests
    def test_csv_cols_all(self):
        args = [ "-c", "1-", test_file_path_csv ]
        self.compare_BinPython_Cut_OutputAndRC(args, args)
    def test_csv_cols_26(self):
        args = [ "-c", "2-6", test_file_path_csv ]
        self.compare_BinPython_Cut_OutputAndRC(args, args)
    def test_csv_cols_26(self):
        args = [ "-c", "1,4,5-6", test_file_path_csv ]
        self.compare_BinPython_Cut_OutputAndRC(args, args)

    #   -b: bytes tests
    def test_allbytes_bytes_all(self):
        args = [ "-b", "1-", test_file_path_allbytes ]
        self.compare_BinPython_Cut_OutputAndRC(args, args, False)
    def test_allbytes_bytes_26(self):
        args = [ "-b", "2-6", test_file_path_allbytes ]
        self.compare_BinPython_Cut_OutputAndRC(args, args, False)
    def test_csv_bytes_all(self):
        args = [ "-b", "1-", test_file_path_csv ]
        self.compare_BinPython_Cut_OutputAndRC(args, args, False)
    def test_csv_bytes_26(self):
        args = [ "-b", "2-6", test_file_path_csv ]
        self.compare_BinPython_Cut_OutputAndRC(args, args, False)

    #   Others:
    def test_getversion(self):
        """Verify version string starts with 'python-cut' followed by a decimal number"""
        args = [ '--version' ]
        result = self.get_BinPython_Cut_OutputAndRC(args, args)
        (out_test, rc_test, out_check, rc_check) = result
        self.assertEqual(rc_test, rc_check)
        self.assertRegex(out_test, re.compile("^python-cut \d+\.\d+.*"))
    #   TODO: 2021-07-10T20:55:36AEST learning-more-python-hard-way, 08/implement-cut.py, incorrect args tests


if __name__ == '__main__':
    unittest.main()

