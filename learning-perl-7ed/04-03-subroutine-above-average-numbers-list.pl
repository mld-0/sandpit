#!/usr/bin/env perl
use strict;
use warnings;

my @fred_input = 1..10;
my @fred = above_average(@fred_input);
print "fred_input=(@fred_input)\n";
print "fred=(@fred)\n";

my @barney_input = (100, 1..10);
my @barney = above_average(@barney_input);
print "barney_input=(@barney_input)\n";
print "barney=(@barney)\n";

#	Return average value of input list
sub average {
	my $values_sum = 0;
	my $values_count = scalar @_;
	foreach (@_) {
		$values_sum += $_;
	}
	my $result = $values_sum / $values_count;
	return $result;
}

#	Return a list of values in input list which are above average value of input list
sub above_average {
	my $values_average = average(@_);
	my @result = qw();
	foreach (@_) {
		if ($_ > $values_average) {
			push(@result, $_);
		}
	}
	return @result;
}

