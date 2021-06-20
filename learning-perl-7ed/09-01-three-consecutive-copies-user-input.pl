#!/usr/bin/env perl
use strict;
use warnings;
use v5.032;

#	Example input:
#	"fredabc\nfred\nabcfredfredfredzde\nfredz\nabc fredbarneyfred z"

my $regex_var = qr/fred|barney/;
while (<>) {
	chomp;
	if (/($regex_var){3}/) {
		say "\$_=($_)";
	}
}
