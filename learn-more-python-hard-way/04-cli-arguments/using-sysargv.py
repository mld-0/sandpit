import sys
import os
import re
import logging
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

def print_help():
    print('''using-sysargv:
    position arguments:
        files

    optional arguments:
    -h | --help             help
    -a | --alpha [value]    option a
    -b | --beta  [value]    option b
    -x                      switch option x
    -y                      switch option y
    -z                      switch option z''')
    exit()

logging.debug("argv=(%r)" % sys.argv)

#   Ongoing: 2021-07-09T16:55:52AEST python, learn-more-python-hard-way/04-cli-arguments/using-sysargv.py, needing to skip ahead when iterating over argv, choose to use counter, (instead of iterating over list and removing items from that list, which behaves how in python?) -- all in all, the moral of the story being parsing sys.argv one's self is an inane waste of effort

arg_val_A, arg_val_B = None, None
arg_x, arg_y, arg_z = False, False, False
loop_i = 0
arg_files = []
while (loop_i < len(sys.argv)):
    arg = sys.argv[loop_i]
    if (loop_i == 0):
        loop_i += 1
        continue
    logging.debug("loop_i=(%i), arg=(%r)" % (loop_i, arg))

    if (re.match("^-h$", arg) or re.match("^--help$", arg)):
        print_help()
    elif (re.match("^-a$", arg) or re.match("^--alpha$", arg)):
        logging.debug("Option a:")
        try:
            arg_val_A = sys.argv[loop_i+1]
            loop_i += 2
            logging.debug("arg_val_A=(%r)" % (arg_val_A))
            continue
        except IndexError as e:
            logging.error("error, value for -a not given")
            print("error, value for -a not given")
            exit()
        except Exception as e:
            logging.error("e=(%r)" % e)
    elif (re.match("^-b$", arg) or re.match("--beta$", arg)):
        logging.debug("Option b:")
        try:
            arg_val_B = sys.argv[loop_i+1]
            loop_i += 2
            logging.debug("arg_val_B=(%r)" % (arg_val_B))
            continue
        except IndexError as e:
            logging.error("error, value for -a not given")
            print("error, value for -a not given")
            exit()
        except Exception as e:
            logging.error("e=(%r)" % e)
    elif (re.match("^-x$", arg)):
        arg_x = True
    elif (re.match("^-y$", arg)):
        arg_y = True
    elif (re.match("^-z$", arg)):
        arg_z = True
    else:
        arg_files.append(arg)

    loop_i += 1


if (len(arg_files) != 0):
    logging.debug("arg_files=(%r)" % arg_files)
    print(len(arg_files))

if (arg_val_A is None and arg_val_B is None and not arg_x and not arg_y and not arg_z and (len(arg_files) == 0)):
    logging.error("no option, print help and exit")
    print("Require at least one option")
    print_help()
        
if (arg_val_A is not None):
    print("arg_val_A=(%s)" % arg_val_A)

if (arg_val_B is not None): 
    print("arg_val_B=(%s)" % arg_val_B)

if (arg_x):
    print("switch option x")

if (arg_y):
    print("switch option y")

if (arg_z):
    print("switch option z")

if (arg_files):
    if type(arg_files) is str:
        arg_files = [ arg_files ]
    paths_list = [os.path.join(os.getcwd(), path) for path in arg_files]
    #logging.debug("paths_list=(%f)" % paths_list)
    print("paths_list=(%s)" % paths_list)


