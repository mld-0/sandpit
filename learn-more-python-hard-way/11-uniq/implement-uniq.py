#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=3:
#   }}}1
import sys
import os
import argparse
import re
import logging
from collections import defaultdict
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
#   {{{2
self_version = "0.0"

def _open_if_valid_file(arg):
    """Return an open filehandle to a valid file, otherwise return arg as string with an error"""
    #   {{{
    if os.path.isdir(arg):
        logging.error("non-file arg=(%r)" % arg)
        sys.stderr.write("Can't read %s: Is a directory\n" % arg)
        exit(4)
    if not os.path.isfile(arg):
        logging.error("non-file arg=(%r)" % arg)
        sys.stderr.write("Can't read %s: No such file or directory\n" % arg)
        exit(2)
    else:
        return open(arg, 'r')  
    #   }}}

def _filter_line(arg_line, args):
    line_start = args.skip_chars
    line_end = args.check_chars
    result = arg_line[line_start:line_end]
    logging.debug("result=(%r)" % result)
    return result

parser = argparse.ArgumentParser(prog='python-uniq')
parser.add_argument('--version', action='version', version='%(prog)s ' + str(self_version))

parser.add_argument('-c', '--count', action='store_true', help="prefix lines by the number of occurences")

parser.add_argument('-d', '--repeated', action='store_true', help="Only print duplicate lines, one for each group")

parser.add_argument('-D', dest='allduplicate', action='store_true', help="Print all duplicate lintes")

parser.add_argument('-u', '--unique', help="Only print unique lines")

parser.add_argument('-i', '--ignore-case', action='store_true', help="Ignore case")

#   fields vs chars?
parser.add_argument('-s', '--skip-chars', default=None, nargs=1, type=int, help="Avoid comparing the first N chars")
#parser.add_argument('-f', '--skip-fields', nargs=1, type=int, help="Avoid comparing the first N fields")

parser.add_argument('-w', '--check-chars', default=None, nargs=1, type=int, help="Compare no morethan N chars in lines")

parser.add_argument('-z', '--zero-terminated', help="Line delimiter is NUL")

#   --all-repeated[=METHOD]
#   --group[=METHOD]

parser.add_argument('input', nargs='?', default=sys.stdin, type=_open_if_valid_file, help="Specify file, (or default to stdin)")

parser.add_argument('output', nargs='?', default=None, help="Specify output file (or default to stdout)")

args = parser.parse_args()
logging.debug("args=(%r)" % args)

lines_buffer = []
for loop_line in args.input:
    logging.debug("loop_line=(%r)" % loop_line)
    loop_line = loop_line.removesuffix('\n')
    lines_buffer.append(loop_line)

logging.debug("lines_counter=(%r)" % lines_counter)

#   uniq man
#   {{{
#UNIQ(1)                        User Commands                        UNIQ(1)
#
#NAME
#       uniq - report or omit repeated lines
#
#SYNOPSIS
#       uniq [OPTION]... [INPUT [OUTPUT]]
#
#DESCRIPTION
#       Filter adjacent matching lines from INPUT (or standard input), writ-
#       ing to OUTPUT (or standard output).
#
#       With no options, matching lines are merged to the first  occurrence.
#
#       Mandatory  arguments to long options are mandatory for short options
#       too.
#
#       -c, --count
#              prefix lines by the number of occurrences
#
#       -d, --repeated
#              only print duplicate lines, one for each group
#
#       -D     print all duplicate lines
#
#       --all-repeated[=METHOD]
#              like -D, but allow separating  groups  with  an  empty  line;
#              METHOD={none(default),prepend,separate}
#
#       -f, --skip-fields=N
#              avoid comparing the first N fields
#
#       --group[=METHOD]
#              show  all  items,  separating  groups  with  an  empty  line;
#              METHOD={separate(default),prepend,append,both}
#
#       -i, --ignore-case
#              ignore differences in case when comparing
#
#       -s, --skip-chars=N
#              avoid comparing the first N characters
#
#       -u, --unique
#              only print unique lines
#
#       -z, --zero-terminated
#              line delimiter is NUL, not newline
#
#       -w, --check-chars=N
#              compare no more than N characters in lines
#
#       --help display this help and exit
#
#       --version
#              output version information and exit
#
#       A field is a run  of  blanks  (usually  spaces  and/or  TABs),  then
#       non-blank characters.  Fields are skipped before chars.
#
#       Note:  'uniq'  does  not detect repeated lines unless they are adja-
#       cent.  You may want to sort the input first, or use 'sort -u'  with-
#       out 'uniq'.
#   }}}
