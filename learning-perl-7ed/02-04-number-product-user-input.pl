#!/usr/bin/env/perl
use strict;
use warnings;
use Scalar::Util qw(looks_like_number);

print "Enter (numeric) var_a:\n";
chomp(my $var_a = <STDIN>);
if (!looks_like_number($var_a)) {
	die "radius=($var_a) is not numeric\n";
}

print "Enter (numeric) var_b:\n";
chomp(my $var_b = <STDIN>);
if (!looks_like_number($var_b)) {
	die "radius=($var_b) is not numeric\n";
}

my $result = $var_a * $var_b;

print "var_a=($var_a)\n";
print "var_b=($var_b)\n";
print "result=($result)\n";

