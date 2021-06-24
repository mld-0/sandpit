#!/usr/bin/env perl
use strict;
use warnings;
use v5.032;

my $input_path = "coconet.dat";
my %total_bytes;
my $label_all = "<<<ALL-MACHINES>>>";

#	Read file data into hash-of-hashes %total_bytes
open FH, '<', $input_path or die "Couldn't open input_path=($input_path): $!\n";
while (<FH>) {
	chomp;
	next if /^#/;
	my ($source, $destination, $bytes) = split;
	$total_bytes{$source}{$destination} += $bytes;
	$total_bytes{$source}{$label_all} += $bytes;
}
close FH or die "Couldn't close input_path=($input_path): $!\n";

#	Print hash-of-hashes %total_bytes, sorting by outer and inner hash keys (source/dest names)
foreach my $machine_source (sort keys %total_bytes) {
	my $dest_hash = $total_bytes{$machine_source};
	printf "%-30s\n", $machine_source;
	foreach my $machine_dest (sort keys %$dest_hash) {
		printf "\t%-26s\t%s\n", $machine_dest, $dest_hash->{$machine_dest};
	}
}

