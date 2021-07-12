#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=3:
#   }}}1
import sys
import os
import argparse
import re
import logging
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
#   {{{2
self_version = "0.0"

#def _script_input(arg_script):
#    return arg_script

def _in_place_input(arg_suffix):
    return arg_suffix

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

def _seperate_and_validate_cmd(arg_cmd):
    """Validate and split s(sep)find(sep)replace(sep)options, returning the tuple (sep, match, replace, options)"""
    #   {{{
    logging.debug("arg_cmd=(%r)" % arg_cmd)
    if type(arg_cmd) is list:
        if len(arg_cmd) > 1:
            logging.error("(Should not happen) len sublist arg_cmd > 1, arg_cmd=(%r)" % arg_cmd)
            exit(2)
        arg_cmd = arg_cmd[0]
    if not type(arg_cmd) is str:
        logging.error("Invalid arg_cmd: Must be str, type(arg_cmd)=(%r)" % type(arg_cmd))
        exit(2)
    if not re.match("^s", arg_cmd):
        logging.error("Invalid arg_cmd: must begin with 's'")
        exit(2)
    if len(arg_cmd) < 4:
        logging.error("Invalid arg_cmd: must be at least 4 characters")
        exit(2)
    #   arg_cmd must be of the form s(sep)match(sep)replace(sep)options, 
    candidate_sep = arg_cmd[1]
    #search_sep = re.findall(candidate_sep, arg_cmd)
    search_sep = [letter for i, letter in enumerate(arg_cmd) if letter == candidate_sep]
    if len(search_sep) < 3:
        logging.error("Invalid arg_cmd: Must contain at least 3 candidate_sep=(%r), arg_cmd=(%r)" % (candidate_sep, arg_cmd))
        exit(2)
    if len(search_sep) > 3:
        logging.error("Invalid arg_cmd: Must contain no more than 3 candidate_sep=(%r), arg_cmd=(%r)" % (candidate_sep, arg_cmd))
        exit(2)
    sep = candidate_sep
    arg_cmd_split = arg_cmd.split(sep)
    match = arg_cmd_split[1]
    replace = arg_cmd_split[2]
    options = arg_cmd_split[3]
    logging.debug("sep=(%r), match=(%r), replace=(%r), options=(%r)" % (sep, match, replace, options))
    return ( sep, match, replace, options )
    #   }}}

parser = argparse.ArgumentParser(prog='python-sed')
#   {{{
parser.add_argument('--version', action='version', version='%(prog)s ' + str(self_version))
parser.add_argument('-n', '--quiet', '--silent', action='store_true', help="")

parser.add_argument('-e', '--expression', action='append', nargs=1, help="")

#   Ongoing: 2021-07-12T18:07:07AEST learn-more-python-hard-way, 09/implement-sedp.y, This is complicated substantially, by python not having support for BRE or ERE? 
#parser.add_argument('-E', '-r', '--regexp-extended', action='store_true', help="")  # Not applicable, ERE not supported
#parser.add_argument('--pcre', action='store_true', help="Use perl regex")
#parser.add_argument('--pyre', action='store_true', help="Use python regex")

#parser.add_argument('cmd_str', action='store', type=_script_input, nargs='?', help="")
parser.add_argument('cmd_str', action='store', nargs='?', help="")

parser.add_argument('-f', '--file', default=[], action='append', nargs=1, help="")

#parser.add_argument('-s', '--seperate', help="")
#parser.add_argument('-z', '--null-data', help="")
#parser.add_argument('-i', '--in-place', type=_in_place_input, nargs='?', help="")
#parser.add_argument('--follow-symlinks', action='store_true', help="")

parser.add_argument('input', nargs='*', default=sys.stdin, type=_open_if_valid_file, help="Specify file(s), (or default to stdin)")
#   }}}

args = parser.parse_args()
logging.debug("args=(%r)" % args)
if not type(args.input) is list:
    args.input = [ args.input ]
if (args.expression):  # If given one-or-more regex strings using '-e', cmd_str (the first positional argument) is treated as a file, not used as regex string
    if (args.cmd_str):
        args.input += [ _open_if_valid_file(args.cmd_str) ]
else: 
    if (args.cmd_str):
        #cmds_sed += [ args.cmd_str ]
        args.expression = [ args.cmd_str ] 
logging.debug("args=(%r)" % args)

if (args.file):
    logging.debug("file=(%r) not supported" % args.file)
    exit(2)

for loop_file in args.input:
    for loop_line in loop_file:
        logging.debug("loop_line=(%r)" % loop_line)
        for loop_cmd_str in args.expression:
            result = _seperate_and_validate_cmd(loop_cmd_str)
            (loop_sep, loop_match, loop_replace, loop_options) = result
            loop_line = re.sub(loop_match, loop_replace, loop_line)  # flags? 
            logging.debug("loop_line=(%r)" % loop_line)
        print(loop_line, end='')


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
