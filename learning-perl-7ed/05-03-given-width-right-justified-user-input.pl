#!/usr/bin/env perl
use strict;
use warnings;

print "Enter output column width:\n";
chomp(my $col_width = <STDIN>);

print "Enter input text (then <C-d>):\n";
chomp(my @input_lines = <STDIN>);

#	Print ruler 
printf("ruler=(10x%d)\n", (($col_width / 10) + 1));
print "1234567890" x (($col_width / 10) + 1);
print "\n";

foreach (@input_lines) {
	printf("%${col_width}s\n", $_);
}

