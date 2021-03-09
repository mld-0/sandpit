
my @input_lines = qw/beforematchafter/;

foreach $_ (@input_lines) {
	chomp;
	if (/match/) {
		print "Matched: ($`)($&)($')\n";  # the special match vars
	} else {
		print "No match: ($_)\n";
	} 
}



