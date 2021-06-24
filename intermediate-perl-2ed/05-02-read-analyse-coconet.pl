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

#	Print hash-of-hashes %total_bytes
for my $machine_source (keys %total_bytes) {
	my $machine_sent = $total_bytes{$machine_source};
	say "$machine_source";
	for my $machine_destination (keys %$machine_sent) {
		my $sent = $$machine_sent{$machine_destination};		
		printf "\t%-30s\t%s\n", $machine_destination, $sent;
	}
}
say "";

##	Print hash-of-hashes %total_bytes, sorting both by outer and inner hash values
my @source_machines_sorted = sort { $total_bytes{$b}{$label_all} <=> $total_bytes{$a}{$label_all} } (keys %total_bytes);
for my $machine_source (@source_machines_sorted) {
	my $dest_hash = $total_bytes{$machine_source};
	my @destination_machines_sorted = sort { $dest_hash->{$b} <=> $dest_hash->{$a} } (keys %{ $dest_hash });
	printf "%-30s\n", $machine_source;
	for my $machine_destination (@destination_machines_sorted[ 1 .. $#destination_machines_sorted ]) {
		printf "\t%-26s\t%s\n", $machine_destination, $dest_hash->{$machine_destination};
	}
	printf "\t%-26s\t%s\n", "Total:", $dest_hash->{$label_all};
}




