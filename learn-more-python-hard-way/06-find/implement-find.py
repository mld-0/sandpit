#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=3:
#   }}}1
import sys
import os
import argparse
import glob
import re
import fnmatch
import logging
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
logging.debug("argv=(%r)" % sys.argv)
#   {{{2

parser = argparse.ArgumentParser()
#   {{{
parser.add_argument('searchpath', nargs='?', default=os.getcwd(), help="Path to search for item")
parser.add_argument('--name', action='store', default='*', type=str, help="Name of item")  # default value of '*'?
parser.add_argument('--type', choices=['d', 'f'], help="Match dirs or files")
#   }}}

#   Ongoing: 2021-07-11T20:08:55AEST 'exec' is not actually implemented
#   Ongoing: 2021-07-09T20:45:22AEST learn-more-python-hard-way/06-find/implement-find.py, do we establish an order used in the case of both print/exec/<others?>, or look into making them mutually exclusive? 
parser.add_argument('--print', default=True, action='store_true', help="Output result items, seperated by newlines")
parser.add_argument('--exec', action='store_true', help="")

args = parser.parse_args()
#   {{{
#args = parser.parse_args(['/Users/mldavis/_data', '--name', '--print'])
#args = parser.parse_args(['~/_data', '--name', '*', '--print'])
#args = parser.parse_args(['~/_data', '--name', '*', '--print', '--type', 'd'])
#args = parser.parse_args(['~/_data', '--name', '*', '--print', '--type', 'f'])
#args = parser.parse_args(['/tmp', '--name', '*', '--print'])
#   }}}
args.searchpath = os.path.expanduser(args.searchpath)
logging.debug("args=(%r)" % args)

if not os.path.exists(args.searchpath):
    logging.error("Not found, args.searchpath=(%r)" % args.searchpath)
    print("Not found: %s" % args.searchpath)
    exit(2)
args.searchpath = os.path.abspath(args.searchpath)
logging.debug("args.searchpath=(%r)" % args.searchpath)

dir_items_recursive = [os.path.relpath(os.path.join(root,f), args.searchpath) for root,dirs,files in os.walk(args.searchpath) for f in files + dirs]
dir_items_recursive.insert(0, '')

temp_dir_items_recursive = list(dir_items_recursive)
dir_items_recursive = []
for loop_item in temp_dir_items_recursive:
    loop_item_basename = os.path.basename(loop_item)
    if fnmatch.fnmatch(loop_item_basename, args.name):  # compare each item to name search str
        dir_items_recursive.append(loop_item)

if (args.type == 'd'):
    pass
    dir_items_recursive = [x for x in dir_items_recursive if os.path.isdir(os.path.join(args.searchpath ,x))]
elif (args.type == 'f'):
    pass
    dir_items_recursive = [x for x in dir_items_recursive if os.path.isfile(os.path.join(args.searchpath, x))]

#   TODO: 2021-07-10T15:00:29AEST perform sorting such that [A-Za-z0-9] come before anything else (which is how 'find' behaves - we obsucate this detail currently by sorting the results of both before comparison in tests)
dir_items_recursive.sort()

for loop_item in dir_items_recursive:
    loop_item = os.path.join(os.path.relpath(args.searchpath, os.getcwd()), loop_item)
    if loop_item[-1] == '/':
        loop_item = loop_item[:-1]  # remove any trailing '/'
    if (args.print):
        print(loop_item)
    if (args.exec):
        logging.debug("TODO: execute not implemented loop_relativepath=(%f)" % loop_item)

#   Find arguments (specification):
#   {{{
#   
#           searchpath      A single directory path, 
#       (ans): 
#           --name          (Quoted) supplied regex str to match against items
#           --type [d,f]    results should be dirs, or files
#       (adding to which):
#           <first-arg>     search directory
#           --print
#           --exec
#   }}}



