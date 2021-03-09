#!/usr/bin/env perl
use strict; 
use warnings;
no warnings 'shadow';

my @input_lines = ( 'fredfredfred', 'fred', 'barneyfredfred', 'barneybarneybarney', 'abc' );
my $what = 'fred|barney';

foreach $_ (@input_lines) {
	chomp $_;
	if (m/(?:$what){3}/) {
		print "$_\n";
	}
}



