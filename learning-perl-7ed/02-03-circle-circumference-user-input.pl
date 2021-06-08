#!/usr/bin/env perl
use strict;
use warnings;

#	Provides pi()
use Math::Trig;

#	In scalar context, <STDIN> reads a line, including trailing newline
print "Enter (numeric) radius:\n";
chomp(my $radius = <STDIN>);

#	Verify user input was numeric:
use Scalar::Util qw(looks_like_number);
if (!looks_like_number($radius)) {
	die "radius=($radius) is not numeric\n";
}

#	Result:
my $circumference = 2 * pi() * $radius;

#	Replace negative result with zero
if ($circumference < 0) {
	warn "Replace negative circumference with zero\n";
	$circumference = 0;
}

#	Output:
print "radius=($radius)\n";
print "circumference=($circumference)\n";

