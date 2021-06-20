#!/usr/bin/env perl
use strict;
use warnings;
use v5.032;

while (<>) {
	if (/\./) {  # alternatively: /[.]/
		print;
	}
}

