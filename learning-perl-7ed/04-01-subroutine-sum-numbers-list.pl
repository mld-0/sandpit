#!/usr/bin/env perl
use strict;
use warnings;

my @fred = qw{ 1 3 5 7 9 };
my $fred_total = total(@fred);
print "fred=(@fred)\n";
print "The total of \@fred is $fred_total.\n";

my @values = (1 .. 1000);
my $values_total = total(@values);
print "values=(@values)\n";
print "values_total=($values_total)\n";

sub total {
	my $result_sum = 0;	
	foreach (@_) {
		$result_sum += $_;
	}
	return $result_sum;
}

