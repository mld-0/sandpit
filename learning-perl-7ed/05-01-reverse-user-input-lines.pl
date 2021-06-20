#!/usr/bin/env perl
use strict;
use warnings;

#	Alternatively, as a one-liner:
#>%		print reverse <>

chomp(my @lines_input = <STDIN>);
my @lines_input_reversed = reverse(@lines_input);

foreach (@lines_input_reversed) {
	print "$_\n";
}

