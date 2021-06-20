#!/usr/bin/env perl
use strict;
use warnings;
use v5.032;

my $input_file_path = "example-text-file.txt";
my $bak_extension = "bak";
say "input_file_path=($input_file_path)";
say "bak_extension=($bak_extension)";

my $output_file_path = "$input_file_path.$bak_extension";
say "output_file_path=($output_file_path)";

open(my $fh_in, '<', $input_file_path) or die "Can't open input_file_path=($input_file_path)";
open(my $fh_out, '>', $output_file_path) or die "Can't open output_file_path=($output_file_path)";

while (<$fh_in>) {
	s/Fred/Larry/gi;  # replace all, case insensitive

	#	Regarding printing to filehandles: A filehandle should never be seperated from any following arguments with a comma
	#print($fh_out, $_);  # invalid, prints ($fh_out, $_) to stdout
	# use: 
	print $fh_out $_;
	#	or
	#$fh_out->print($_)
	#	or
	#print($fh_out $_);
}

close($fh_in) or die "Can't close input_file_path=($input_file_path)";
close($fh_out) or die "Can't close output_file_path=($output_file_path)";

