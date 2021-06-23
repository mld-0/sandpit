#!/usr/bin/env perl
use strict;
use warnings;
use v5.032;
use DateTime;

#	Add existing files from ARGV to hash file_creation as keys, with corresponding mtimes as values
my %file_creation;
for (@ARGV) {
	if (-e $_) {
		my $modified_delta_days = -M $_;
		my $modified_epoch = (stat $_)[9];
		$file_creation{$_} = $modified_epoch;
	}
}

#	For each file, sorted by mtime, print mtime as epoch and as datetime
for my $filename (sort { $file_creation{$a} <=> $file_creation{$b} } keys %file_creation) {
	my $mtime_epoch = $file_creation{$filename};
	my $mtime_datetime = DateTime->from_epoch(epoch => $mtime_epoch);
	say "filename=($filename), mtime_epoch=($mtime_epoch)";
	say "mtime_datetime=($mtime_datetime)";
}

