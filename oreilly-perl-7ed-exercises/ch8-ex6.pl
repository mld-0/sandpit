use strict; 
use warnings;
no warnings 'shadow';

my @input_lines = ( 'asdf ' );

foreach $_ (@input_lines) {
	chomp;
	if (/\s$/) {
		print "$_#\n";
	} 
}
