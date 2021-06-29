#!/usr/bin/env perl
use strict;
use warnings;
use v5.032;

my @input_words = ( 'Mary-Anne', 'abc', 'contrived', 'xray', 'Mary-Jane', 'yellow', 'three', 'Purple', );
say "input_words=(@input_words)";

#	Purely alphabetical sort
my @sorted_words = 
	map $_->[0],
	sort { $a->[1] cmp $b->[1] }
	map {
		my $word_dictcase = $_;
		#	to lower case, remove non-letters
		$word_dictcase =~ tr/A-Z/a-z/;  
		$word_dictcase =~ tr/a-z//cd;  
		[ $_, $word_dictcase ];
	} @input_words;
say "sorted_words=(@sorted_words)";

#	Casefolded alphabetical sort
my @sorted_casefold_words = 
	map $_->[0], 
	sort { $a->[1] cmp $b->[1] }
	map {
		my $word_dictcase = $_;
		#	remove non-letters and perform 'proper' casefold
		$word_dictcase =~ s/\P{Letter}//g;  
		$word_dictcase =~ fc( $word_dictcase );  
		[ $_, $word_dictcase ];
	} @input_words;
say "sorted_casefold_words=(@sorted_casefold_words)";

