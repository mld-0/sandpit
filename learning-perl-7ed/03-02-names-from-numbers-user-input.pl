#!/usr/bin/env perl
use strict;
use warnings;

use Scalar::Util::Numeric qw(isint);

my @names = qw( fred betty barney dino wilma pebbles bamm-bamm );
my $names_len = scalar @names;

#	Get list of values from user
print "Enter (integers, in range [0, $names_len), seperated by newlines) user_nums, then <C-d>:\n";
chomp(my @user_nums = <STDIN>);

my @selected_names = qw();

#	Verify each item in user_nums is an int in acceptable range [0, $names_len), and create @selected_names with values in @names using indexes in @user_nums
foreach (@user_nums) {
	if (!isint($_)) {
		die "($_) in user_nums=(@user_nums) is not int\n";
	}
	if ($_ < 0 or $_ >= $names_len) {
		die "($_) in user_nums=(@user_nums) outside range [0, $names_len)\n";
	}
	push(@selected_names, $names[$_]);
}


#	Output:
print "names=(@names)\n";
print "user_nums=(@user_nums)\n";
print "selected_names=(@selected_names)\n";

