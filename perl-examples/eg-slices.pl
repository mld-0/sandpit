#!/usr/bin/env perl
use strict;
use warnings;
use v5.032;

my $value_str = "fred flintstone:2168:301 Cobblestone Way:555-1212:555-2121:3
barney rubble:709918:299 Cobblestone Way:555-3333:555-3438:0";

foreach (split("\n", $value_str)) {
	say "\$_=($_)";

	#	Using undef as placeholder for discarded values
	#my (undef, $card_num, undef, undef, undef, $count) = split /:/;

	#	Using slicing
	my ($card_num, $count) = (split /:/)[1, 5];
	say "card_num=($card_num)";
	say "count=($count)";
	say "";
}

#	Equivalent:
#		@names[2, 5]
#		($names[2], $names[5])

my @names = qw{ zero one two three four five six seven eight nine };

my @numbers = ( @names )[ 9, 0, 2, 1, 0 ];
say "numbers=(@numbers)";  

my ($first, $last) = @names[0, -1];
say "first=($first), last=($last)";

#	Interpolate Slice:
say "evens=(@names[0, 2, 4, 6, 8])";

#	Generating a range with step
#	python: list(range(0, 8+1, 2))
my @index_evens = map { 2 * $_ } 0..4;
#	or
@index_evens = ();
for (my $i = 0; $i < 8+1; $i += 2) { push @index_evens, $i; }
#	or
#use List::Gen;
#@index_evens = range(0, 8+1, 2);
#	or
#	...
say "index_evens=(@index_evens)";

#	Ongoing: 2021-06-24T00:04:07AEST perl, List::Gen, which provides a range(start,end,step) function, won't install with a failed test
#use List::Gen;
#@index_evens = range(0, 8+1, 2);
#say "index_evens=(@index_evens)";
say "";


#	Hash slices:
my %score;
my @players = qw/ barney fred dino /;
my @bowling_scores = (195, 205, 30);
#	or
@score{ @players } = @bowling_scores;
foreach my $k (keys %score) {
	my $v = $score{$k};
	say "k=($k), v=($v)";
}
say "players=(@players)";
say "score=(@score{@players})";
say "";

my %new_hash = map { $_ => $score{$_} } @players;
foreach my $k (keys %new_hash) {
	my $v = $new_hash{$k};
	say "k=($k), v=($v)";
}
say "";

my %first_last_scores = %bowling_scores[0, -1];
foreach my $k (keys %first_last_scores) {
	my $v = $first_last_scores{$k};
	say "k=($k), v=($v)";
}
say "";



