
my @input_lines = ( 'wilma', 'barney', 'Mrs Wilma Flinstone', 'wilma&fred', 'I saw Wilma yesterday', 'I, Wilma!' );

foreach $_ (@input_lines) {
	chomp;
	if (/\b\w*(?<capture>a\b)(?<second>.{0,5})/) {
		print "Matched: capture=($+{capture}), second=($+{second}), ($`)($&)($')\n";  # the special match vars
	} else {
		print "No match: ($_)\n";
	} 
}



