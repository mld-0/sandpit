
sub total {
	my @values = @_;
	my $total = 0;

	foreach my $loop_value (@values) {
		$total += $loop_value;
	}

	return $total;
}

my @user_values = (1 .. 1000);
my $user_total = &total(@user_values);
print "The total of those numbers is $user_total.\n";

