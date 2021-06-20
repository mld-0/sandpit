#!/usr/bin/env perl
use strict;
use warnings;
use v5.032;

#	Example input:
#	"abc\ndef\nhij\nzaka be\nbada def"

my $regex_var = qr/\b(\w*a)\b(.{0,5})/;
while (<>) {
	if (/$regex_var/) {
		say "\$1=($1)";
		say "\$2=($2)";
	}
}

