#!/usr/bin/env perl
use strict;
use warnings;
use v5.032;
use File::Basename;
use File::Spec;

my ($file_source, $file_dest) = @ARGV;
say "file_source=($file_source)";
say "file_dest=($file_dest)";

#	If destination is a directory, add the source basename to that directory to form the destination
if (-d $file_dest) {
	my $file_source_basename = basename $file_source;
	$file_dest = File::Spec->catfile($file_dest, $file_source_basename);
	say "Prepended file_source_basename=($file_source_basename) to file_dest=($file_dest)";
}

#	Hardlink file
#link $file_source, $file_dest or die "Can't link file_source=($file_source) to file_dest=($file_dest): $!\n";

