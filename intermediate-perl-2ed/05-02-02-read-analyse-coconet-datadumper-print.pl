#!/usr/bin/env perl
use strict;
use warnings;
use v5.032;
use Data::Dumper;

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

##	Print hash-of-hashes %total_bytes
#for my $machine_source (keys %total_bytes) {
#	my $machine_sent = $total_bytes{$machine_source};
#	say "$machine_source";
#	for my $machine_destination (keys %$machine_sent) {
#		my $sent = $$machine_sent{$machine_destination};		
#		printf "\t%-30s\t%s\n", $machine_destination, $sent;
#	}
#}
#say "";

print Dumper(\%total_bytes);
say "";

#use Data::Dump qw(dump);
use Data::Dump;
print Data::Dump->dump(\%total_bytes);

