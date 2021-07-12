#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=3:
#   }}}1
import sys
import os
import argparse
import re
import logging
#   {{{2
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
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

def _remove_nondict(arg_text):
    """Remove characters not in [A-Za-z0-9] from arg_text"""
    #   {{{
    dict_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnoprstuvwxyz0123456789'.split()
    logging.debug("arg_text=(%r)" % arg_text)
    result = ''.join([i for i in arg_text if i not in dict_chars])
    logging.debug("result=(%r)" % result)
    return result
    #   }}}

def _atoi(text):
    return int(text) if text.isdigit() else text

def _natural_keys(text):
    return [ _atoi(c) for c in re.split('(\d+)',text) ]

parser = argparse.ArgumentParser(prog='python-sort', add_help=False)
#   {{{
parser.add_argument('--help', action='help')
parser.add_argument('--version', version='%(prog)s ' + str(self_version), action='version')

parser.add_argument('-b', '--ignore-leading-blanks', action='store_true', help="Ignore leading blanks")

parser.add_argument('-d', '--dictionary-order', action='store_true', help="Consider only blanks and alphanum characters")
parser.add_argument('-h', '--human-numeric-sort', action='store_true', help="Compare human readable numbers")
parser.add_argument('-n', '--numeric-sort', action='store_true', help="Compare according to string numerical value")
parser.add_argument('-V', '--version-sort', action='store_true', help="Natural sort of version numbers within text")

parser.add_argument('-r', '--reverse', action='store_true', help="Reverse the result of comparisons")

parser.add_argument('-f', '--ignore-case', action='store_true', help="Ignore case")
parser.add_argument('-i', '--ignore-nonprinting', action='store_true', help="Consider only printable characters")

parser.add_argument('-R', '--random-sort', action='store_true', help="Shuffle, but group identical keys")
#parser.add_argument('--random-source')

#parser.add_argument('--stable', action='store_true', help="")  # Is not python's sort already stable?

#parser.add_argument('--merge', action='store_true', help="Merge already sorted files, do not sort")

parser.add_argument('-o', '--output', action='store', type=str, nargs=1, help="")

parser.add_argument('files', nargs='*', default=sys.stdin, type=_open_if_valid_file, help="Specify file(s), (or default to stdin)")
#   }}}

args = parser.parse_args()
if not type(args.files) is list:
    args.files = [ args.files ] 
logging.debug("args=(%r)" % args)

sort_options = dict()
if (args.reverse):
    sort_options['reverse'] = True

if (args.dictionary_order):
    sort_options['key'] = _remove_nondict
elif (args.human_numeric_sort):
    #   TODO: 2021-07-12T20:55:05AEST how to sort numerical suffixes like 'sort' does in python?
    logging.error("-h --human-numeric-sort unimplemented")
    exit(2)
elif (args.numeric_sort):
    sort_options['key'] = _natural_keys
elif (args.version_sort):
    #   Ongoing: 2021-07-12T19:59:24AEST Both incorrect vis-a-vis behaviour of 'sort --version-sort'
    #from distutils.version import StrictVersion
    #sort_options['key'] = StrictVersion
    sort_options['key'] = lambda x: list(map(_atoi, x.split('.')))  # 

if (args.ignore_leading_blanks):
    logging.error("-b --ignore-leading-blanks unimplemented")
    exit(2)

if (args.random_sort):
    logging.error("-R --random-sort unimplemented")
    exit(2)

lines_buffer = []
for loop_file in args.files:
    logging.debug("loop_file=(%r)" % loop_file)
    for loop_line in loop_file:
        loop_line = loop_line.removesuffix('\n')
        lines_buffer.append(loop_line)

logging.debug("lines_buffer=(%r)" % lines_buffer)
logging.debug("sort_options=(%r)" % sort_options)

try:
    lines_buffer.sort(**sort_options)
except Exception as e:
    #logging.error("While sorting: %s %s" % (type(e), str(e)))
    sys.stderr.write("While sorting: %s %s\n" % (type(e), str(e)))
    exit(2)

logging.debug("lines_buffer=(%r)" % lines_buffer)

if (args.output):
    logging.error("-o --output [FILE] unimplemented")
    exit(2)

for loop_line in lines_buffer:
    print(loop_line)

#   sort man:
#   {{{
#NAME
#       sort - sort lines of text files
#
#SYNOPSIS
#       sort [OPTION]... [FILE]...
#       sort [OPTION]... --files0-from=F
#
#DESCRIPTION
#       Write sorted concatenation of all FILE(s) to standard output.
#
#       With no FILE, or when FILE is -, read standard input.
#
#       Mandatory  arguments  to  long  options are mandatory for short options
#       too.  Ordering options:
#
#       -b, --ignore-leading-blanks
#              ignore leading blanks
#
#       -d, --dictionary-order
#              consider only blanks and alphanumeric characters
#
#       -f, --ignore-case
#              fold lower case to upper case characters
#
#       -g, --general-numeric-sort
#              compare according to general numerical value
#
#       -i, --ignore-nonprinting
#              consider only printable characters
#
#       -M, --month-sort
#              compare (unknown) < 'JAN' < ... < 'DEC'
#
#       -h, --human-numeric-sort
#              compare human readable numbers (e.g., 2K 1G)
#
#       -n, --numeric-sort
#              compare according to string numerical value
#
#       -R, --random-sort
#              shuffle, but group identical keys.  See shuf(1)
#
#       --random-source=FILE
#              get random bytes from FILE
#
#       -r, --reverse
#              reverse the result of comparisons
#
#       --sort=WORD
#              sort according to WORD: general-numeric  -g,  human-numeric  -h,
#              month -M, numeric -n, random -R, version -V
#
#       -V, --version-sort
#              natural sort of (version) numbers within text
#
#       Other options:
#
#       --batch-size=NMERGE
#              merge at most NMERGE inputs at once; for more use temp files
#
#       -c, --check, --check=diagnose-first
#              check for sorted input; do not sort
#
#       -C, --check=quiet, --check=silent
#              like -c, but do not report first bad line
#
#       --compress-program=PROG
#              compress temporaries with PROG; decompress them with PROG -d
#
#       --debug
#              annotate the part of the line used to sort, and warn about ques-
#              tionable usage to stderr
#
#       --files0-from=F
#              read input from the files specified by NUL-terminated  names  in
#              file F; If F is - then read names from standard input
#
#       -k, --key=KEYDEF
#              sort via a key; KEYDEF gives location and type
#
#       -m, --merge
#              merge already sorted files; do not sort
#
#       -o, --output=FILE
#              write result to FILE instead of standard output
#
#       -s, --stable
#              stabilize sort by disabling last-resort comparison
#
#       -S, --buffer-size=SIZE
#              use SIZE for main memory buffer
#
#       -t, --field-separator=SEP
#              use SEP instead of non-blank to blank transition
#
#       -T, --temporary-directory=DIR
#              use  DIR  for  temporaries,  not  $TMPDIR  or  /tmp; multiple
#              options specify multiple directories
#
#       --parallel=N
#              change the number of sorts run concurrently to N
#
#       -u, --unique
#              with -c, check for strict ordering; without -c,  output  only
#              the first of an equal run
#
#       -z, --zero-terminated
#              line delimiter is NUL, not newline
#
#       --help display this help and exit
#
#       --version
#              output version information and exit
#
#       KEYDEF  is  F[.C][OPTS][,F[.C][OPTS]]  for  start and stop position,
#       where F is a field number and C a character position in  the  field;
#       both are origin 1, and the stop position defaults to the line's end.
#       If neither -t nor -b is in effect, characters in a field are counted
#       from the beginning of the preceding whitespace.  OPTS is one or more
#       single-letter ordering options [bdfgiMhnRrV], which override  global
#       ordering  options  for that key.  If no key is given, use the entire
#       line as the key.  Use --debug to diagnose incorrect key usage.
#
#       SIZE may be followed by the following multiplicative suffixes: %  1%
#       of memory, b 1, K 1024 (default), and so on for M, G, T, P, E, Z, Y.
#
#       *** WARNING *** The locale specified by the environment affects sort
#       order.   Set  LC_ALL=C  to  get the traditional sort order that uses
#       native byte values.
#
#AUTHOR
#       Written by Mike Haertel and Paul Eggert.
#
#REPORTING BUGS
#       GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
#       Report    any    translation    bugs   to   <https://translationpro-
#       ject.org/team/>
#
#COPYRIGHT
#       Copyright (C) 2020 Free Software Foundation, Inc.   License  GPLv3+:
#       GNU GPL version 3 or later <https://gnu.org/licenses/gpl.html>.
#       This  is  free software: you are free to change and redistribute it.
#       There is NO WARRANTY, to the extent permitted by law.
#
#SEE ALSO
#       shuf(1), uniq(1)
#
#       Full documentation <https://www.gnu.org/software/coreutils/s   
#   }}}

