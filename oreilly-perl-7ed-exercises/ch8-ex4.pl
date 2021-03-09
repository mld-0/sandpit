
my @input_lines = ( 'wilma', 'barney', 'Mrs Wilma Flinstone', 'wilma&fred' );

foreach $_ (@input_lines) {
	chomp;
	if (/\b\w*(?<capture>a\b)/) {
		print "Matched: capture=($+{capture}) ($`)($&)($')\n";  # the special match vars
	} else {
		print "No match: ($_)\n";
	} 
}



