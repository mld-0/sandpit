import sys
import os
import re
import argparse
import logging
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

def open_if_valid_file(parser, arg):
    if not os.path.isfile(arg):
        logging.warning("skip non-file arg=(%r)" % arg)
        return arg
    else:
        return open(arg, 'r')  # return an open file handle

parser = argparse.ArgumentParser()

parser.add_argument('pattern', action='store', type=str, help="Search Pattern")
parser.add_argument('files',  type=lambda x: open_if_valid_file(parser, x), nargs='*', default=sys.stdin, help="Path to search for item")

parser.add_argument('-i', '--ignore-case', action='store_true')
parser.add_argument('-v', '--invert-match', action='store_true')

args = parser.parse_args()
logging.debug("args=(%r)" % args)

if not type(args.files) is list:
    args.files = [ args.files ] 

#   if searching files, include filenames in matches
flag_output_filenames = 0
if (len(args.files) > 1):
    flag_output_filenames = 1

pattern_regex_flags = 0
if (args.ignore_case):
    pattern_regex_flags |= re.IGNORECASE  # is |= correct way to combine options?

filename_seperator = ":"
output_str = ""
linenum = 0
for loop_file in args.files:
    logging.debug("loop_file=(%r)" % loop_file)
    linenum = 0
    #if not os.path.isfile(loop_file):
    logging.debug("type(loop_file)=(%r)" % type(loop_file))
    if type(loop_file) is str:  # skip non-files 
        logging.debug("Skip nonfile loop_file=(%r)" % loop_file)
        continue
    for loop_line in loop_file:
        loop_re_match = re.search(args.pattern, loop_line, pattern_regex_flags)
        if ((loop_re_match and not args.invert_match) or (not loop_re_match and args.invert_match)):
            output_str = ""
            if flag_output_filenames:
                output_str = loop_file.name + filename_seperator
            output_str += loop_line
            print(output_str.rstrip())
        linenum += 1

#   grep options:
#       grep [OPTION...] PATTERNS [FILE...]
#       grep [OPTION...] -e PATTERNS ... [FILE...]
#       grep [OPTION...] -f PATTERN_FILE ... [FILE...]
#   Options
#       -i  --ignore-case
#       -v  --invert-match


