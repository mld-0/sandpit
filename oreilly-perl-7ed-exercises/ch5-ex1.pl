use strict; 
use warnings;
no warnings 'shadow';

my @input_lines = <STDIN>;
chomp @input_lines;

foreach my $loop_line (reverse @input_lines) {
	print "$loop_line\n";
}
