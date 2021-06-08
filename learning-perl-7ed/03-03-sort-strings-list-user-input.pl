#!/usr/bin/env perl
use strict;
use warnings;

print "Enter words, seperated by newlines, then <C-d>:\n";
chomp(my @user_strings = <STDIN>);

my @user_strings_sorted = sort(@user_strings);

print "user_strings=(@user_strings)\n";
print "user_strings_sorted=(@user_strings_sorted)\n";

