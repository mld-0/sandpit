#!/usr/env/bin perl
use strict;
use warnings;
use v5.032;

my $longest_key_length = 0;
for my $k (keys %ENV) {
	my $key_length = length($k);
	$longest_key_length = $key_length if $key_length > $longest_key_length;
}

for my $k (keys %ENV) {
	my $v = $ENV{$k};
	#say "k=($k), v=($v)"
	printf("%-${longest_key_length}s %s\n", $k, $v);
}

