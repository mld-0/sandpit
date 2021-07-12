#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=3:
#   }}}1
import sys
import os
import argparse
import re
import logging
import subprocess
import unittest
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
#   {{{2
test_bin_python = "/usr/local/bin/python3"

test_script_sort = "implement-sort.py"
#   {{{
if not (os.path.isfile(test_script_sort)):
    self_dir = os.path.dirname(os.path.realpath(__file__))
    test_script_sort = os.path.join(self_dir, test_script_sort)
assert os.path.isfile(test_script_sort), "Failed to find 'implement-find.py' and '%s'" % test_script_sort
#   }}}

test_data_dir = "../data_test"
#   {{{
if not (os.path.isdir(test_data_dir)):
    test_data_dir = "data_test"
assert os.path.isdir(test_data_dir), "Failed to find '../data_test' and 'data_test'"
#   }}}

test_file_path_csv = os.path.join(test_data_dir, "values.csv")
test_file_path_allbytes = os.path.join(test_data_dir, "allbytes.hex")

class Test_ImplementSort(unittest.TestCase):

    #   TODO: 2021-07-11T22:17:29AEST Before tests, test (using unittest) for existance each filesystem item that needs to exists, then script version, and exit if either fail

    def get_BinPython_Pipe_Sort_OutputAndRC(self, args_binpython, args_sort, arg_input_pipe='', decode_result=True):
        args_binpython = [ test_bin_python, test_script_sort ] + args_binpython
        proc = subprocess.Popen(args_binpython, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        (out_test, err_test) = proc.communicate(input=arg_input_pipe.encode())
        rc_test = proc.returncode
        args_sort = [ 'sort' ] + args_sort
        proc = subprocess.Popen(args_sort, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        (out_check, err_check) = proc.communicate(input=arg_input_pipe.encode())
        rc_check = proc.returncode
        if (decode_result):
            return (out_test.decode(), rc_test, out_check.decode(), rc_check)
        else:
            return (out_test, rc_test, out_check, rc_check)

    #   Not yet implemented
    def test_sort_pipe_humannumeric_01(self):
        val_input = "12k\n5G\n9M\n470"
        args = [ '--human-numeric-sort' ] 
        result = self.get_BinPython_Pipe_Sort_OutputAndRC(args, args, val_input)
        (out_test, rc_test, out_check, rc_check) = result
        self.assertEqual(out_test, out_check)
        self.assertEqual(rc_test, rc_check)

    #def test_sort_pipe_letters_outfile(self):
    #    pass
    #def test_sort_pipe_mixedletters_ignorecase(self):
    #    pass
    #def test_sort_pipe_mixedletters(self):
    #    pass
    #def test_sort_pipe_textvariousindent(self):
    #    pass
    #def test_sort_pipe_textvariousindent_ignoreleadingblanks(self):
    #    pass

    #   Seemingly working:
    def test_sort_pipe_letters_01(self):
        val_input = "def\nhij\nabc\nxyz\n"
        args = []
        result = self.get_BinPython_Pipe_Sort_OutputAndRC(args, args, val_input)
        (out_test, rc_test, out_check, rc_check) = result
        self.assertEqual(out_test, out_check)
        self.assertEqual(rc_test, rc_check)
    def test_sort_file_csv_01(self):
        args = [ test_file_path_csv ]
        result = self.get_BinPython_Pipe_Sort_OutputAndRC(args, args)
        (out_test, rc_test, out_check, rc_check) = result
        self.assertEqual(out_test, out_check)
        self.assertEqual(rc_test, rc_check)
    def test_sort_pipe_dictionaryorder_01(self):
        val_input = "def.01.02\nhij.03.04\nabc.00.01\ndef.00.01\n"
        args = [ '--dictionary-order' ] 
        result = self.get_BinPython_Pipe_Sort_OutputAndRC(args, args, val_input)
        (out_test, rc_test, out_check, rc_check) = result
        self.assertEqual(out_test, out_check)
        self.assertEqual(rc_test, rc_check)
    def test_sort_pipe_numeric_01(self):
        val_input = "def.01.02\nhij.03.04\nabc.00.01\ndef.00.01\n"
        args = [ '--numeric-sort' ] 
        result = self.get_BinPython_Pipe_Sort_OutputAndRC(args, args, val_input)
        (out_test, rc_test, out_check, rc_check) = result
        self.assertEqual(out_test, out_check)
        self.assertEqual(rc_test, rc_check)
    def test_sort_pipe_versionorder_01(self):
        val_input = "def.01.02\nhij.03.04\nabc.00.01\ndef.00.01\n"
        args = [ '--version-sort' ] 
        result = self.get_BinPython_Pipe_Sort_OutputAndRC(args, args, val_input)
        (out_test, rc_test, out_check, rc_check) = result
        self.assertEqual(out_test, out_check)
        self.assertEqual(rc_test, rc_check)

    #   Others:
    def test_getversion(self):
        """Verify version string starts with 'python-cut' followed by a decimal number"""
        args = [ '--version' ]
        result = self.get_BinPython_Pipe_Sort_OutputAndRC(args, args)
        (out_test, rc_test, out_check, rc_check) = result
        self.assertRegex(out_test, re.compile("^python-sort \d+\.\d+.*"))
        self.assertEqual(rc_test, rc_check)
    #   TODO: incorrect args tests


if __name__ == '__main__':
    unittest.main()

