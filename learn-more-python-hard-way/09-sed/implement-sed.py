#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=3:
#   }}}1
import sys
import os
import argparse
import logging
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
#   {{{2
self_version = "0.0"

def _script_input(arg_script):
    #   Ongoing: 2021-07-11T21:57:55AEST when is something considered a script by sed? Quoted/unquoted string? If it matches a filename/path? <- not considered a file unless accompanyed by '-f'? 
    return arg_script

def _in_place_input(arg_suffix):
    return arg_suffix

def _open_if_valid_file(arg):
    """Return an open filehandle to a valid file, otherwise return arg as string with a warning"""
    #   {{{
    if not os.path.isfile(arg):
        logging.warning("skip non-file arg=(%r)" % arg)
        return arg
    else:
        return open(arg, 'r')  
    #   }}}
    
parser = argparse.ArgumentParser(prog='python-sed')

parser.add_argument('--version', action='version', version='%(prog)s ' + str(self_version))
parser.add_argument('-n', '--quiet', '--silent', action='store_true', help="")

parser.add_argument('-e', '--expression', nargs='+', help="")
parser.add_argument('-E', '-r', '--regexp-extended', nargs='+', help="")
parser.add_argument('--pcre', nargs='+', help="Use perl regex")
parser.add_argument('--pyre', nargs='+', help="Use python regex")

parser.add_argument('cmd_str', action='store', type=_script_input, nargs=1, help="")

parser.add_argument('-f', '--file', nargs=1, help="")

parser.add_argument('-s', '--seperate', help="")
parser.add_argument('-z', '--null-data', help="")
parser.add_argument('-i', '--in-place', type=_in_place_input, nargs='?', help="")

parser.add_argument('--follow-symlinks', action='store_true', help="")

parser.add_argument('files', nargs='*', default=sys.stdin, type=_open_if_valid_file, help="Specify file(s), (or default to stdin)")

args = parser.parse_args()
logging.debug("args=(%r)" % args)


#   Note: 
#       sed -E -f "file" 
#   is a valid sed command, as is 
#       sed -E "regex"
#   however the following is not:
#       sed -e -f "file"

#   sed (gnu version?)
#       sed [OPTION]... {script-only-if-no-other-script} [input-file]...
#   -h, --help
#   --version
#   --debug
#   -n, --quiet, --silent               supress (automatic) printing of pattern space
#   
#   -i[SUFFIX], --in-place[=SUFFIX]     edit files in place (backup file using SUFFIX if given)
#
#   -l N, --line-length=N
#   -s, --seperate                      consider files as seperate rather than a single 
#   
#   --sandbox                           disable e/r/w
#   -z, --null-data             Seperate lines by NUL characters
#
#   -f script-file, --file=script-file
#
#   Regex versions:
#       BRE         -e script, --expression=script
#       ERE         (-E,-r) script, --regexp-extended=script
#       pcre        <--pcre>                                      
#       python      <--pyre>
#   
#   yeah nah options:
#   {{{
#   --follow-symlinks
#   -u, --unbuffered
#   }}}


#   Sed Help:
#   {{{
#   Usage: sed [OPTION]... {script-only-if-no-other-script} [input-file]...
#   
#     -n, --quiet, --silent
#                    suppress automatic printing of pattern space
#         --debug
#                    annotate program execution
#     -e script, --expression=script
#                    add the script to the commands to be executed
#     -f script-file, --file=script-file
#                    add the contents of script-file to the commands to be executed
#     --follow-symlinks
#                    follow symlinks when processing in place
#     -i[SUFFIX], --in-place[=SUFFIX]
#                    edit files in place (makes backup if SUFFIX supplied)
#     -l N, --line-length=N
#                    specify the desired line-wrap length for the `l' command
#     --posix
#                    disable all GNU extensions.
#     -E, -r, --regexp-extended
#                    use extended regular expressions in the script
#                    (for portability use POSIX -E).
#     -s, --separate
#                    consider files as separate rather than as a single,
#                    continuous long stream.
#         --sandbox
#                    operate in sandbox mode (disable e/r/w commands).
#     -u, --unbuffered
#                    load minimal amounts of data from the input files and flush
#                    the output buffers more often
#     -z, --null-data
#                    separate lines by NUL characters
#         --help     display this help and exit
#         --version  output version information and exit
#   
#   If no -e, --expression, -f, or --file option is given, then the first
#   non-option argument is taken as the sed script to interpret.  All
#   remaining arguments are names of input files; if no input files are
#   specified, then the standard input is read.
#   
#   GNU sed home page: <https://www.gnu.org/software/sed/>.
#   General help using GNU software: <https://www.gnu.org/gethelp/>.
#   }}}
#   
