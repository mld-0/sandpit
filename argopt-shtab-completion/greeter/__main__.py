#!/usr/bin/env python
"""Greetings and partings.

Usage:
  greeter [options] [<you>] [<me>]

Options:
  -g, --goodbye  : Say "goodbye" (instead of "hello")

Arguments:
  <you>  : Your name [default: Anon]
  <me>  : My name [default: Casper]
"""
import sys, argopt, shtab  # NOQA

__version__ = "0.0.1"

parser = argopt.argopt(__doc__)

def cligreet():
    args = parser.parse_args()
    msg = "k thx bai!" if args.goodbye else "hai!"
    print("{} says '{}' to {}".format(args.me, msg, args.you))
