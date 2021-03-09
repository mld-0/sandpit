
my @input_lines = ( 'wilma', 'barney', 'Mrs Wilma Flinstone', 'wilma&fred' );

foreach $_ (@input_lines) {
	chomp;
	if (/\b\w*(a)\b/) {
		print "Matched: 1=($1) ($`)($&)($')\n";  # the special match vars
	} else {
		print "No match: ($_)\n";
	} 
}



