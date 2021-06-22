#!/usr/bin/env perl
use strict;
use warnings;
use v5.032;

#	Ongoing: 2021-06-22T21:43:23AEST Are there circumstances that would lead to a value of ENV being undefined? Since ENV does not currently contain an undefined value, add one for our test
$ENV{'example_undefined'} = undef;

foreach my $k (keys %ENV) {
	my $v = $ENV{$k};
	if (!defined($v)) {
		printf("k=($k), v=(%s)\n", $v // "undefined");
	}
}

