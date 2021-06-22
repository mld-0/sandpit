#!/usr/bin/env perl
use strict;
use warnings;
use v5.032;

#	Example input:
#	"Fred wilma\nwilma fred\nabcdef fred"

#	Use "\0\1\2" (bytes: 00 01 02) as placeholder when swapping 'fred' and 'wilma'
my $swap_placeholder = "\000\001\002";  # octal
#	or
$swap_placeholder = "\x00\x01\x02";  # hex
#	or
$swap_placeholder = chr(00) . chr(01) . chr(02);  # decimal

while (<>) {
	s/Fred/$swap_placeholder/gi;
	s/Wilma/Fred/gi;
	s/$swap_placeholder/Wilma/gi;
	print;
}

