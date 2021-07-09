import sys
import os
import argparse
import logging
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

logging.debug("argv=(%r)" % sys.argv)

parser = argparse.ArgumentParser()
parser.add_argument('-a', '--alpha', action='store', type=str, help="Example value a")
parser.add_argument('-b', '--beta', action='store', type=str, help="Example value b")

parser.add_argument('-x', action='store_true', help="Switch option x")
parser.add_argument('-y', action='store_true', help="Switch option y")
parser.add_argument('-z', action='store_true', help="Switch option z")

parser.add_argument('files', nargs='+', help="Specify files")

args = parser.parse_args()

if (args.alpha is None and args.beta is None and not args.x and not args.y and not args.z and not args.files):
    print("Require at least one argument.")
    parser.print_help()
    exit(2)

if (args.alpha is not None):
    print("args.alpha=(%s)" % args.alpha)

if (args.beta is not None):
    print("args.beta=(%s)" % args.beta)

if (args.x):
    print("Switch option x")

if (args.y):
    print("Switch option y")

if (args.z):
    print("Switch option z")

if (args.files):
    if type(args.files) is str:
        args.files = [ args.files ]
    paths_list = [os.path.join(os.getcwd(), path) for path in args.files]
    print("paths_list=(%s)" % paths_list)

