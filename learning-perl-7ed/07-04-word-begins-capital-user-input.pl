#!/usr/bin/env perl
use strict;
use warnings;
use v5.032;

while (<>) {
	if (/\b[A-Z][a-z]+\b/) {
		print $_;
	}
}

