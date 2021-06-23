#!/usr/bin/env perl
use strict;
use warnings;
use v5.032;

#	Add items from @ARGV that are readable/writable files owned by current user:
my @files_rwx;
for (@ARGV) {
	if (-r -w -o $_) {
		push @files_rwx, $_;
	}
}

#	Print result:
say "files_rwx:";
for (@files_rwx) {
	say "$_";
}
