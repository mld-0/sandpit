import sys
import os
import argparse
import logging
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
logging.debug("argv=(%r)" % sys.argv)

parser = argparse.ArgumentParser()

parser.add_argument('-n', '--number', action='store_true', help="Number all output lines")
parser.add_argument('-s', '--squeeze-blank', action='store_true', help="Supress repeated empty output lines")

parser.add_argument('files', metavar='F', nargs='*', help="File(s) arguments")

args = parser.parse_args()

def print_filehandle(f, args):
    """Print lines of filehandle, with line numbers and/or squeeze_blanks if given args"""
    loop_linenumsblank = 0
    #for loop_linenum, loop_line in enumerate(f.readlines()):
    loop_linenum = 1
    for loop_line in f.readlines():
        #   If squeeze_blank, skip repeated empty lines
        if (args.squeeze_blank):
            if loop_line == "\n":
                if loop_linenumsblank == 1:
                    loop_linenum += 1
                    continue 
                loop_linenumsblank = 1
            else:
                loop_linenumsblank = 0
        #   If number, prefix linenumber followed by tab
        if (args.number):
            loop_linenum_str = "%i\t" % loop_linenum
            print(loop_linenum_str, end='')
        print(loop_line, end='')
        loop_linenum += 1

#   Call print_filehandle for each file given as argument, or with stdin if no files given
if (args.files):
    if type(args.files) is str:
        args.files = [ args.files ]
    #   TODO: 2021-07-09T18:33:47AEST if file is '-', use stdin
    paths_list = [os.path.join(os.getcwd(), path) for path in args.files]
    logging.debug("paths_list=(%s)" % paths_list)
    for loop_file in paths_list:
        f = open(loop_file, 'r')
        print_filehandle(f, args)
        f.close()
else:
    print_filehandle(sys.stdin, args)


if __name__ == '__main__':
    unittest.main()

##   cat args:
#       With no FILE, or when FILE is -, read standard input.
#       -A, --show-all
#              equivalent to -vET
#       -b, --number-nonblank
#              number nonempty output lines, overrides -n
#       -e     equivalent to -vE
#       -E, --show-ends
#              display $ at end of each line
#       -n, --number
#              number all output lines
#       -s, --squeeze-blank
#              suppress repeated empty output lines
#       -t     equivalent to -vT
#       -T, --show-tabs
#              display TAB characters as ^I
#       -u     (ignored)
#       -v, --show-nonprinting
#              use ^ and M- notation, except for LFD and TAB
#       --help display this help and exit
#       --version
#              output version information and exit


