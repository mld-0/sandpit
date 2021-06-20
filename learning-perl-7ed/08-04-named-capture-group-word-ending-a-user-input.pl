#!/usr/bin/env perl
use strict;
use warnings;
use v5.032;

#	Example input:
#	"abc\ndef\nhij\nzaka\nbada"

my $regex_str = qr/\b(?<word_ending_a>\w*a)\b/;
while (<>) {
	if (/$regex_str/) {
		#	Capture buffers list
		say "\@{^CAPTURE}=(@{^CAPTURE})";

		#	Named capture group 'word_ending_a'
		say "\$+{word_ending_a}=($+{word_ending_a})";

		#	Named capture groups hash '%+'
		print "%+: ";
		for my $k (keys %+) {
			my $v = $+{$k};
			print "k=($k), v=($v), ";
		} print "\n";

	}
}
