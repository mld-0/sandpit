
sub above_average {
	my @values = @_;
	my $total = &total(@values);
	my $avg = $total / ($#values + 1);
	my @above_average = ();

	foreach my $loop_value (@values) {
		if ($loop_value > $avg) {
			push(@above_average, $loop_value);
		}
	}
	return @above_average;
}

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
my @above_avg = &above_average(@user_values);
print "The total of those numbers is $user_total.\n";
print "above_avg=(@above_avg)\n";

my @fred = above_average(1..10);
print "\@fred is @fred\n";
print "(Should be 6 7 8 9 10)\n";
my @barney = above_average(100, 1..10);
print "\@barney is @barney\n";
print "(Should be just 100)\n";

