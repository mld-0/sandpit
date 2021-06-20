#!/usr/env/bin perl
use strict;
use warnings;
use v5.032;

my $regex_str = "[Ff]red";

while (<>) {
	if (/$regex_str/) {
		print $_;
	}
}
