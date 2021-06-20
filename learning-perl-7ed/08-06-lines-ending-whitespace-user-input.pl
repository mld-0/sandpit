#!/usr/bin/env perl
use strict;
use warnings;
use v5.032;

#	Example input:
#	"abc\ndef \nhij\n"

while (<>) {
	chomp;
	if (/\s$/) {
		say "\$_=($_)";
	}
}
