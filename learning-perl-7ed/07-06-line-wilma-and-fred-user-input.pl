#!/usr/bin/env perl
use strict;
use warnings;
use v5.032;

while (<>) {
	if (/wilma/ and /fred/) {
		print $_;
	}
}

