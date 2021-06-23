#!/usr/bin/env perl
use strict;
use warnings;
use v5.032;

say "Enter number values on single line:";
chomp(my $user_input = <STDIN>);
my @user_values = split(/\s+/, $user_input);
#	or
# Single space as split pattern in single or double quotes, is treated as /\s+/
#my @user_values = split(" ", $user_input);  

say "user_values=(@user_values)";

my @user_values_sorted = sort( { $a <=> $b } @user_values);
say "user_values_sorted=(@user_values_sorted)";

