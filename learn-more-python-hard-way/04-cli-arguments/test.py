import sys
import os
import unittest
import subprocess

test_bin_python = "/usr/local/bin/python3"

test_script_argv = "using-sysargv.py"
test_script_argparse = "using-argparse.py"
test_data_dir = "testdata"

class Test_ProcessingArgs(unittest.TestCase):

    def call_script_argv(self, args):
        return self.call_script(test_script_argv, args)

    def call_script_argparse(self, args):
        return self.call_script(test_script_argparse, args)

    #   Ongoing: 2021-07-10T16:26:12AEST learn-more-python-hard-way/04-cli-arguments/test.py, how to seperate python logging output from stderr (for a python script run via a system() call)
    def call_script(self, test_script, args):
        args_sp = [ test_bin_python, test_script ] + args;
        proc = subprocess.Popen(args_sp, stdout=subprocess.PIPE)
        (out_test, err_test) = proc.communicate()
        out_test = out_test.decode().strip()
        rc = proc.returncode
        return (out_test, rc)


    def test_using_sysargv_Avalid(self):
        args = [ '-a', 'Test Str A' ];
        result = self.call_script_argv(args)
        (out_test, rc) = result
        out_expected = "arg_val_A=(" + args[1] + ")"
        self.assertEqual(out_test, out_expected)

    def test_using_sysargv_Ainvalid(self):
        args = [ '-a' ]
        result = self.call_script_argv(args)
        (out_test, rc) = result
        out_expected = "error, value for -a not given"
        self.assertEqual(out_test, out_expected)


    def test_using_argparse_Avalid(self):
        args = [ '-a', 'Test Str A' ];
        result = self.call_script_argparse(args)
        (out_test, rc) = result
        out_expected = "args.alpha=(" + args[1] + ")"
        self.assertEqual(out_test, out_expected)

    def test_using_argparse_Ainvalid(self):
        args = [ '-a' ]
        result = self.call_script_argparse(args)
        (out_test, rc) = result
        self.assertEqual(out_test, "", "Output is to stderr, stdout should be empty")

    #   Continue: 2021-07-10T16:23:56AEST learn-more-python-hard-way/04-cli-arguments/test.py, (the menial task of) completing the remainder of the "you did/didn't enter these values" tests


