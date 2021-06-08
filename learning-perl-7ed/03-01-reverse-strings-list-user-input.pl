#!/usr/bin/env perl
use strict;
use warnings;

print "Enter words (one per line), then <C-d> or <C-z> to exit:\n";
chomp(my @var_words = <STDIN>);

my $var_words_len = scalar @var_words;
my @var_words_reversed = reverse(@var_words);

print "var_words_len=($var_words_len)\n";
print "var_words=(@var_words)\n";
print "var_words_reversed=(@var_words_reversed)\n";

