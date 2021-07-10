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
mutually_exclusive_actions_group.add_argument('-c', '--column', type=str, help="Cut by character")
mutually_exclusive_actions_group.add_argument('-b', '--bytes', type=str, help="Cut by bytes")
mutually_exclusive_actions_group.add_argument('-f', '--field', type=str, help="Cut by field (specify with -d)")
parser.add_argument('-d', '--delim', type=_is_valid_delim, default='\t', help="Split fields by character")
parser.add_argument('--output-delimiter', type=_is_valid_delim, default=None, help="Replace delimiters with character")
parser.add_argument('-s', '--only-delimited', action='store_true', help="Do not print lines not containing delim")
parser.add_argument('-z', '--zero-terminated', action='store_true', help="Each line is ended with null byte, not newline")
parser.add_argument('files', nargs='*', default=sys.stdin, type=_open_if_valid_file, help="Specify file(s)")

args = parser.parse_args()
logging.debug("args=(%r)" % args)

def _parse_rangestr(arg_rangestr):
    """Turn arg_rangestr into list: a number for each indervidually specified field, and a <tuple> for each range, with 0/-1 denoting start/end"""
    logging.debug("arg_rangestr=(%r)" % arg_rangestr)
    result_items = []
    rangestr_split = arg_rangestr.split(',')
    logging.debug("rangestr_split=(%r)" % rangestr_split)

    for loop_item in rangestr_split:
        if loop_item.find('-') == -1:
            result_items.append(int(loop_item))
        else:
            loop_item = loop_item.split('-')
            if (len(loop_item[0]) == 0):
                loop_item[0] = '0'
            if (len(loop_item[1]) == 0):
                loop_item[1] = '-1'
            result_items.append( tuple([ int(loop_item[0]), int(loop_item[1]) ]) )
    #   {{{
    #for loop_item in rangestr_split:
    #    try:
    #        if (loop_item.find('-') != -1):
    #            result_items.extend(int(loop_item))
    #        else:
    #            raise Exception("to be parsed by exception handler - this is undoubtedly bad design")
    #    except Exception as e:
    #        loop_item_split = loop_item.split('-')
    #        logging.debug("loop_item_split=(%r)" % loop_item_split)
    #        loop_item_split_end = 0
    #        loop_item_split_start = 0
    #        if (len(loop_item_split) == 2 and type(loop_item_split) is list):
    #            try:
    #                if len(loop_item_split[0]) == 0:
    #                    loop_item_split_start = 0
    #                else:
    #                    loop_item_split_start = int(loop_item_split[0])
    #                if len(loop_item_split[1]) == 0:
    #                    loop_item_split_end = -1
    #                else:
    #                    loop_item_split_end = int(loop_item_split[1])
    #            except TypeError as e:
    #                raise Exception("e=(%r) can't split loop_item_split=(%r) into two ints" % (e, loop_item_split))
    #            #loop_item_range = range(loop_item_split_start, loop_item_split_end)
    #            result_items.extend( tuple([loop_item_split_start, loop_item_split_end ]) )
    #        else:
    #            raise Exception("e=(%r) can't split loop_item_split=(%r) into two ints" % (e, loop_item_split))
    #   }}}
    logging.debug("result_items=(%r)" % result_items)
    return result_items


#   Continue: 2021-07-10T22:52:23AEST learn-more-python-hard-way, 08, (implementing) last test case, bytes tests, can we use _construct_output_col_line(), substituting the string/list cases which work, for a byte-string usable by the same code?

def _construct_output_col_line(range_values, arg_line, arg_delim=''):
    output_line = ""
    for loop_range in range_values:
        loop_output_substr = ""
        if type(loop_range) is int:
            loop_output_substr = arg_line[loop_range-1:][:1]
        else:
            if (loop_range[1] != -1):
                loop_output_substr = arg_line[loop_range[0]-1:loop_range[1]]
            else:
                loop_output_substr = arg_line[loop_range[0]-1:]
        #logging.debug("loop_range=(%r), loop_output_substr=(%r)" % (loop_range, loop_output_substr))
        if type(loop_output_substr) is list:  # with this addition, will this function work for fields, if given arg_line as the line split into fields?
            loop_output_substr = arg_delim.join(loop_output_substr)
        output_line += loop_output_substr
    logging.debug("output_line=(%r)" % output_line)
    return output_line
    #print(output_line)

if not type(args.files) is list:
    args.files = [ args.files ] 

for loop_file in args.files:
    logging.debug("loop_file=(%r)" % loop_file)

    if type(loop_file) is str:  # skip non-files
        logging.debug("Skip nonfile loop_file=(%r)" % loop_file)
        continue

    for loop_line in loop_file:
        output_line = ""
        loop_line = loop_line.removesuffix("\n")
        #logging.debug("loop_line=(%r)" % loop_line)
        if (args.bytes):
            pass

        elif (args.column):
            range_values = _parse_rangestr(args.column)
            #   {{{
            #for loop_range in range_values:
            #    loop_output_substr = ""
            #    if type(loop_range) is int:
            #        loop_output_substr = loop_line[loop_range-1:][:1]
            #    else:
            #        if (loop_range[1] != -1):
            #            loop_output_substr = loop_line[loop_range[0]-1:loop_range[1]]
            #        else:
            #            loop_output_substr = loop_line[loop_range[0]-1:]
            #    #logging.debug("loop_range=(%r), loop_output_substr=(%r)" % (loop_range, loop_output_substr))
            #    output_line += loop_output_substr
            #logging.debug("output_line=(%r)" % output_line)
            #   }}}
            output_line = _construct_output_col_line(range_values, loop_line)
            print(output_line)

        elif (args.field):
            range_values = _parse_rangestr(args.field)
            if (args.output_delimiter is None):
                args.output_delimiter = args.delim
            loop_line_fields_split = loop_line.split(args.delim)
            #if len(loop_line_fields_split) == 0:
            #    loop_line_fields_split = [ '' ]
            logging.debug("loop_line_fields_split=(%r)" % loop_line_fields_split)
            output_line = _construct_output_col_line(range_values, loop_line_fields_split, args.output_delimiter)
            print(output_line)


#   Ongoing: 2021-07-10T22:12:32AEST learn-more-python-hard-way, 08, Use of '-' to specify range -> precludes use of negative indexes?

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



