#!/usr/bin/env perl
use strict;
use warnings;

#	note: had we not removed the newline, it would be included in our 20 width, resulting in output that is 'only' 19 wide
chomp(my @input_lines = <STDIN>);

#	Debugging 40-wide 'ruler' 
print "1234567890" x 2, "\n";  

foreach (@input_lines) {
	#	Print lines as right-justified, 20 character values
	printf("%20s\n", $_); 
}

