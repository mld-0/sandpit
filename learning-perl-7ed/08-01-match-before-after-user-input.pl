#!/usr/bin/env perl
use strict;
use warnings;
use v5.032;

while (<>) {           
	chomp;
	if (/match/) {
		say "before=($`) match=($&) after=($')\n";  
	} else {
		say "No match: |$_|";
	} 
}

