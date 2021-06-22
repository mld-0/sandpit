#!/usr/bin/env perl
use strict;
use warnings;
use v5.032;

my $value_max = 100;
my $value_min = 1;

my $selected_value = int( rand($value_max - $value_min) ) + $value_min;
my @quit_values = ( "quit", "exit", "" );
my $user_guess = undef;

say "selected_value=($selected_value)";

do {
	say "Guess value in range [$value_min, $value_max]:";
	chomp($user_guess = lc(<STDIN>));
	if (grep(/$user_guess/, @quit_values)) {
		exit(0);
	}
	if ($user_guess > $selected_value) {
		say "Too high";
	} elsif ($user_guess < $selected_value) {
		say "Too low";
	}
} while ($user_guess != $selected_value);

say "Correct, selected_value=($selected_value), user_guess=($user_guess)";

