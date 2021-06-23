#!/usr/bin/env perl
use strict;
use warnings;
use v5.032;

my %last_name = qw{
          fred flintstone Wilma Flintstone Barney Rubble
          betty rubble Bamm-Bamm Rubble PEBBLES FLINTSTONE
};

say "origional order:";
foreach my $k (keys %last_name) {
	my $v = $last_name{$k};
	say "k=($k), v=($v)";
}
say "";

say "sorted by values:";
#	Sorting keys by lowercase values:
foreach my $k (sort( { "\L$last_name{$a}\E" cmp "\L$last_name{$b}\E" } keys %last_name )) {
	my $v = $last_name{$k};
	say "k=($k), v=($v)";
}
