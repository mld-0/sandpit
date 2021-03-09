#!/usr/bin/env perl
use strict; 
use warnings;
no warnings 'shadow';

print "Enter strings\n";
my @user_vals = <STDIN>;
chomp @user_vals;
print "\n";

foreach my $loop_val (sort @user_vals) {
	print "$loop_val\n";
}
print "\n";

foreach my $loop_val (sort @user_vals) {
	print "$loop_val ";
}

