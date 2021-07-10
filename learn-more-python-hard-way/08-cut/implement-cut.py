import sys
import os
import argparse
import logging
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

parser = argparse.ArgumentParser(prog='python-cut')
self_version = "0.0"

def _is_valid_delim(delim):
    """Require delim to be a string of a single character"""
    if not type(delim) is str:
        raise TypeError("Invalid type(delim)=(%s) for delim=(%r)" % (delim, type(delim)))
    if not len(delim) == 1:
        raise Exception("delim=(%r) must be 1 char" % delim)
    return delim


def _open_if_valid_file(arg):
    """Return an open filehandle to a valid file, otherwise return arg as string with a warning"""
    if not os.path.isfile(arg):
        logging.warning("skip non-file arg=(%r)" % arg)
        return arg
    else:
        return open(arg, 'r')  # return an open file handle

parser.add_argument('--version', action='version', version='%(prog)s ' + str(self_version))
mutually_exclusive_actions_group = parser.add_mutually_exclusive_group(required=True)
mutually_exclusive_actions_group.add_argument('-b', '--bytes', type=str, help="Cut by bytes")
mutually_exclusive_actions_group.add_argument('-c', '--column', type=str, help="Cut by character")
mutually_exclusive_actions_group.add_argument('-f', '--field', type=str, help="Cut by field (specify with -d)")
parser.add_argument('-d', '--delim', type=_is_valid_delim, help="Split fields by character")
parser.add_argument('--output-delimiter', type=_is_valid_delim, help="Replace delimiters with character")
parser.add_argument('-s', '--only-delimited', action='store_true', help="Do not print lines not containing delim")
parser.add_argument('-z', '--zero-terminated', action='store_true', help="Each line is ended with null byte, not newline")
parser.add_argument('files', nargs='*', default=sys.stdin, type=_open_if_valid_file, help="Specify file(s)")

args = parser.parse_args()
logging.debug("args=(%r)" % args)


if not type(args.files) is list:
    args.files = [ args.files ] 

for loop_file in args.files:
    logging.debug("loop_file=(%r)" % loop_file)
    if type(loop_file) is str:  # skip non-files
        logging.debug("Skip nonfile loop_file=(%r)" % loop_file)
        continue
    for loop_line in loop_file:
        if (args.bytes):
            pass
        elif (args.column):
            pass
        elif (args.field):
            pass


#   cut:    remove sections from each line of files
#       cut [args] [File(s)]
#   args: 
#       (one of: -b, -c, -f must be specified) 
#        -b     --bytes  LIST       Extract specific bytes, LIST is comma seperated numbers 
#                                   for those bytes (which are one-indexed), or hyphen '-' 
#                                   seperated numbers for ranges
#   
#       -c      --column LIST       Cut by character, list of numbers separated comma or a 
#                                   range of numbers separated by hyphen(-)
#   
#       -f      --field  LIST       Cut by field, list of numbers seperated by comma or a range of 
#                                   numbers seperated by hyphen (-)
#
#       -d      --delim             Field delimiter (default tab)
#       -s      --only-delimited    Do not print lines not containing delimiters
#
#               --complement        Complement of output
#       -z      --zero-terminated   Each line is ended with 0x00, not newline
#       --output-delimiter  DELIM   Default is input delimiter, replace delimiters with value
#



