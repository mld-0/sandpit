#!/usr/bin/env perl
use strict;
use warnings;
use v5.032;
use JSON;
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

#	Write %total_bytes to $jsonfile_path as JSON
my $jsonfile_path = "total_bytes.json";
{
	open FH_JSON, '>:utf8', $jsonfile_path or die "Failed to open for writing jsonfile_path=($jsonfile_path): $!\n";
	print FH_JSON to_json(\%total_bytes, { pretty => 1 });
	close FH_JSON or die "Failed to close jsonfile_path=($jsonfile_path): $!\n";
}

#	Read JSON from jsonfile_path to %total_bytes
%total_bytes = ();
-e "$jsonfile_path" or die "File not found jsonfile_path=($jsonfile_path): $!\n";
{
	local $/ = undef;  # slurp mode
	open FH_JSON, '<:raw', $jsonfile_path or die "Failed to open for reading jsonfile_path=($jsonfile_path): $!\n";
	my $json_str = <FH_JSON>;  # read entire file as string
	%total_bytes = %{decode_json($json_str)};  # dereference decode_json() result
	close FH_JSON or die "Failed to close jsonfile_path=($jsonfile_path): $!\n";
}

print Dumper(%total_bytes);

