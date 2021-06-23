#!/usr/bin/env perl
use strict;
use warnings;
use v5.032;

my $var_str = "This is a test string is it not?";
my $substr = "is";
my @match_locations;

say "var_str=($var_str)";
say "substr=($substr)";

#	Find all instances of $substr in $var_str and store in @match_locations
my $match_pos = -1;
while (1) {
	$match_pos = index($var_str, $substr, $match_pos+1);
	last if $match_pos == -1;
	push @match_locations, $match_pos;
}
say "match_locations=(@match_locations)";

#	Extract and print each match instance
foreach (@match_locations) {
	my $loop_substr = substr($var_str, $_, length($substr));
	say "\$_=($_), loop_substr=($loop_substr)";
}

