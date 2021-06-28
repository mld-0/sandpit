#!/usr/bin/perl
use utf8;
use strict;
use warnings;

use v5.12;

sub rightmost {
	my ($var_string, $patterns_hashref) = @_;

	#	Check patterns_hashref is a hash reference
	ref($patterns_hashref) eq 'HASH' or die "Expect patterns_hashref to be a hash reference\n";

	#	Print patterns_hashref, var_string
	say "patterns_hashref:";
	foreach my $key (keys %{$patterns_hashref}) {
		my $v = $patterns_hashref->{$key};
		print "\tkey=($key), v=($v)\n";
	} 
	say "var_string=($var_string)";


	my ($rightmost, $rightmost_key) = (-1, undef);

	#	Find rightmost index and key of %{$patterns_hashref} value match in $var_str:
	foreach my $key (keys %{$patterns_hashref}) {
		my $pattern = $patterns_hashref->{$key};
		my $loop_position = $var_string =~ m/$pattern/ ? $-[0] : -1;
		if ($loop_position > $rightmost) {
			($rightmost, $rightmost_key) = ($loop_position, $key);
		}
	}

	return $rightmost_key;
}

my %patterns = (
		Gilligan   => qr/(?:Wiley )?Gilligan/,
		'Mary-Ann' => qr/Mary-Ann/,
		Ginger     => qr/Ginger/,
		Professor  => qr/(?:The )?Professor/,
		Skipper    => qr/Skipper/,
		'A Howell' => qr/Mrs?. Howell/,
		);

my $rightmost_key = rightmost( 
		'There is Mrs. Howell, Ginger, and Gilligan',
		\%patterns,
		);	
say "";

say "righmost_key=($rightmost_key)";
say "rightmost_val=($patterns{$rightmost_key})";

