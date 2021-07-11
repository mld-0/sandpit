#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=3:
#   }}}1
import sys
import os
import subprocess
import unittest
import logging
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
logging.debug("argv=(%r)" % sys.argv)

#   Run tests with:
#       python -m unittest test.py

test_bin_python = "/usr/local/bin/python3"

#   
test_script_find = "implement-find.py"
if not (os.path.isfile(test_script_find)):
    self_dir = os.path.dirname(os.path.realpath(__file__))
    test_script_find = os.path.join(self_dir, test_script_find)
assert os.path.isfile(test_script_find), "Failed to find 'implement-find.py' and '%s'" % test_script_find

test_data_dir = "data_test"
if not (os.path.isdir(test_data_dir)):
    test_data_dir = "../data_test"
assert os.path.isdir(test_data_dir), "Failed to find '../data_test' and 'data_test'"
    

test_compare_results_sort = True  # haven't implemented same sorting as used by find, therefore sort both results before comparing

class Test_ImplementFind(unittest.TestCase):
    def compare_BinPython_Find(self, args_binpython, args_find):
        """Compare lines of test python script with those of find, optionally sorting them first"""
        _args = [ test_bin_python, test_script_find ] + args_binpython
        proc = subprocess.Popen(_args, stdout=subprocess.PIPE)
        (out_test, err_test) = proc.communicate()
        _args = [ 'find' ] + args_find
        proc = subprocess.Popen(_args, stdout=subprocess.PIPE)
        (out_check, err_check) = proc.communicate()
        out_test_list = out_test.decode().split('\n')
        out_check_list = out_check.decode().split('\n')
        if (test_compare_results_sort):
            out_test_list.sort()
            out_check_list.sort()
        self.assertEqual(out_test_list, out_check_list)

    def test_ItemsInTestDataDir(self):
        args_binpython = [ test_data_dir ]
        args_find = [ test_data_dir ]
        self.compare_BinPython_Find(args_binpython, args_find)

    def test_DirsInTestDataDir(self):
        args_binpython = [ test_data_dir, '--type', 'd' ]
        args_find = [ test_data_dir, '-type', 'd' ]
        self.compare_BinPython_Find(args_binpython, args_find)

    def test_FilesInTestDataDir(self):
        args_binpython = [ test_data_dir, '--type', 'f' ]
        args_find = [ test_data_dir, '-type', 'f' ]
        self.compare_BinPython_Find(args_binpython, args_find)

    def test_FilterFilesInTestDataDir(self):
        args_binpython = [ test_data_dir, '--type', 'f', '--name', '*.csv' ]
        args_find = [ test_data_dir, '-type', 'f', '-name', '*.csv' ]
        self.compare_BinPython_Find(args_binpython, args_find)

    def test_FilterDirsInTestDataDir(self):
        args_binpython = [ test_data_dir, '--type', 'd', '--name', 'hij*' ]
        args_find = [ test_data_dir, '-type', 'd', '-name', 'hij*' ]
        self.compare_BinPython_Find(args_binpython, args_find)

if __name__ == '__main__':
    unittest.main()

