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

test_script_sed = "implement-sed.py"
#   {{{
if not (os.path.isfile(test_script_sed)):
    self_dir = os.path.dirname(os.path.realpath(__file__))
    test_script_sed = os.path.join(self_dir, test_script_sed)
assert os.path.isfile(test_script_sed), "Failed to find 'implement-find.py' and '%s'" % test_script_sed
#   }}}

test_data_dir = "../data_test"
#   {{{
if not (os.path.isdir(test_data_dir)):
    test_data_dir = "data_test"
assert os.path.isdir(test_data_dir), "Failed to find '../data_test' and 'data_test'"
#   }}}

test_file_path_csv = os.path.join(test_data_dir, "values.csv")
test_file_path_allbytes = os.path.join(test_data_dir, "allbytes.hex")

class Test_ImplementSed(unittest.TestCase):

    #   TODO: 2021-07-11T22:17:29AEST Before tests, test for existance each filesystem item that needs to exists, then script version, and exit if either fail

    def get_BinPython_Pipe_Sed_OutputAndRC(self, args_binpython, args_sed, arg_input_pipe='', decode_result=True):
        args_binpython = [ test_bin_python, test_script_sed ] + args_binpython
        proc = subprocess.Popen(args_binpython, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        (out_test, err_test) = proc.communicate(input=arg_input_pipe.encode())
        rc_test = proc.returncode
        args_sed = [ 'sed' ] + args_sed
        proc = subprocess.Popen(args_sed, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        (out_check, err_check) = proc.communicate(input=arg_input_pipe.encode())
        rc_check = proc.returncode
        if (decode_result):
            return (out_test.decode(), rc_test, out_check.decode(), rc_check)
        else:
            return (out_test, rc_test, out_check, rc_check)

    #   Ongoing: 2021-07-12T17:41:47AEST Both fail due to unimplemented -E option
    #   {{{
    #def test_replace_pipe_aA_usingEee(self):
    #    val_input = "abc"
    #    val_expected = "Abc"
    #    args = [ '-E', '-e', 's/a/A/', '-e', 's/A/a/' ]
    #    result = self.get_BinPython_Pipe_Sed_OutputAndRC(args, args, val_input)
    #    (out_test, rc_test, out_check, rc_check) = result
    #    self.assertEqual(out_test, out_check)
    #    self.assertEqual(rc_test, rc_check)
    #def test_replace_pipe_aA_usingE(self):
    #    val_input = "abc"
    #    val_expected = "Abc"
    #    args = [ '-E', 's/a/A/' ]
    #    result = self.get_BinPython_Pipe_Sed_OutputAndRC(args, args, val_input)
    #    (out_test, rc_test, out_check, rc_check) = result
    #    self.assertEqual(out_test, out_check)
    #    self.assertEqual(rc_test, rc_check)
    #   }}}

    def test_replace_pipe_capture(self):
        val_input = "abc"
        args = [ 's/(a)(bc)/\\2\\1/' ]
        #   Need to enable ERE to use () capture groups
        args_sed = [ '-E', 's/(a)(bc)/\\2\\1/' ]
        result = self.get_BinPython_Pipe_Sed_OutputAndRC(args, args_sed, val_input)
        (out_test, rc_test, out_check, rc_check) = result
        self.assertEqual(out_test, out_check)
        self.assertEqual(rc_test, rc_check)

    #   (Seemingly) working:
    def test_replace_pipe_aAa_usingee(self):
        val_input = "abc"
        val_expected = "abc"
        args = [ '-e', 's/a/A/', '-e', 's/A/a/' ]
        result = self.get_BinPython_Pipe_Sed_OutputAndRC(args, args, val_input)
        (out_test, rc_test, out_check, rc_check) = result
        self.assertEqual(out_test, out_check)
        self.assertEqual(rc_test, rc_check)
    def test_replace_pipe_aAa_usingee_alt_seperators(self):
        val_input = "abc"
        val_expected = "abc"
        args = [ '-e', 's.a.A.', '-e', 's|A|a|' ]
        result = self.get_BinPython_Pipe_Sed_OutputAndRC(args, args, val_input)
        (out_test, rc_test, out_check, rc_check) = result
        self.assertEqual(out_test, out_check)
        self.assertEqual(rc_test, rc_check)
    def test_replace_file_csv(self):
        args = [ 's/1/0/g', test_file_path_csv ]
        result = self.get_BinPython_Pipe_Sed_OutputAndRC(args, args, '')
        (out_test, rc_test, out_check, rc_check) = result
        self.assertEqual(out_test, out_check)
        self.assertEqual(rc_test, rc_check)
    def test_replace_pipe_aA(self):
        val_input = "abc"
        val_expected = "Abc"
        args = [ 's/a/A/' ]
        result = self.get_BinPython_Pipe_Sed_OutputAndRC(args, args, val_input)
        (out_test, rc_test, out_check, rc_check) = result
        self.assertEqual(out_test, out_check)
        self.assertEqual(rc_test, rc_check)
    def test_replace_pipe_aA_usinge(self):
        val_input = "abc"
        val_expected = "Abc"
        args = [ '-e', 's/a/A/' ]
        result = self.get_BinPython_Pipe_Sed_OutputAndRC(args, args, val_input)
        (out_test, rc_test, out_check, rc_check) = result
        self.assertEqual(out_test, out_check)
        self.assertEqual(rc_test, rc_check)
    #   Others:
    def test_invalid_args_cmdstr_followedby_e(self):
        val_input = "abc"
        args = [ 's/a/A/', '-e', 's/A/a/' ]
        result = self.get_BinPython_Pipe_Sed_OutputAndRC(args, args, val_input)
        (out_test, rc_test, out_check, rc_check) = result
        self.assertEqual(out_test, out_check)
        self.assertEqual(rc_test, rc_check)
    def test_invalid_args_cmdstrIsDir_followedby_e(self):
        val_input = "abc"
        args = [ test_data_dir, '-e', 's/A/a/' ]
        result = self.get_BinPython_Pipe_Sed_OutputAndRC(args, args, val_input)
        (out_test, rc_test, out_check, rc_check) = result
        self.assertEqual(out_test, out_check)
        self.assertEqual(rc_test, rc_check)
    def test_getversion(self):
        """Verify version string starts with 'python-cut' followed by a decimal number"""
        args = [ '--version' ]
        result = self.get_BinPython_Pipe_Sed_OutputAndRC(args, args)
        (out_test, rc_test, out_check, rc_check) = result
        self.assertRegex(out_test, re.compile("^python-sed \d+\.\d+.*"))
        self.assertEqual(rc_test, rc_check)
    #   TODO: incorrect args tests


if __name__ == '__main__':
    unittest.main()

