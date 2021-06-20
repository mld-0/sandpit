#!/usr/env/bin perl
use strict;
use warnings;
use v5.032;

say "Enter words, one-per-line, then <C-d>:";
chomp(my @input_words = <STDIN>);

say "input_words=(@input_words)";

my %words_counter = ();
for (@input_words) {
	$words_counter{$_} += 1;
}

for my $k (keys %words_counter) {
	my $v = $words_counter{$k};
	say "k=($k), v=($v)";
}
