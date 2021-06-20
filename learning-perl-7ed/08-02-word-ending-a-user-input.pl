#!/usr/bin/env perl
use strict;
use warnings;
use v5.032;

while (<>) {
	if (/\b(\w*a)\b/) {
		say "\$1=($1)";
	}
}
