#!/usr/bin/env perl
use strict;
use warnings;
use v5.032;
use Storable;
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

my $storefile_path = "store_total_bytes.data";

#	Store variable %total_bytes to storefile_path
my $rc = store \%total_bytes, $storefile_path or die "Couldn't store data in storefile_path=($storefile_path): $!\n";

#	Ongoing: 2021-06-24T21:10:16AEST perl, use of Storable::retrieve -> reason for use of temp variable that is de-referenced into actual variable?

#	Read variable total_bytes from storefile_path
%total_bytes = ();
-e $storefile_path or die "File not found, storefile_path=($storefile_path): $!\n";
{ my $data_temp = retrieve $storefile_path; %total_bytes = %$data_temp; }
print Dumper(%total_bytes);
