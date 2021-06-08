#!/usr/bin/env perl
use v5.10;  # needed for state variables
use strict;
use warnings;


greet("Fred");
greet("Barney");
greet("Wilma");
greet("Betty");

sub greet {
	#	Persistant list variable
	state @callee_names = qw();

	#	Get $name as first argument value
	my $name = shift(@_);
	print "Hi $name\n";

	if (!@callee_names) {
		print "You are the first one here\n";
	} else { 
		print "Also here are: @callee_names\n";
	}

	#	Add $name to our persistant variable
	push(@callee_names, $name);
}

