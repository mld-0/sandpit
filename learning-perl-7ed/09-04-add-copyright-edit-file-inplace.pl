#!/usr/bin/env perl
use strict;
use warnings;
use v5.032;

#	Add 'copyright_line' immediately after shebang if file does not already contain it

#	Example input:
#	example-add-copyright.pl
#	(default if no arguments given)

#	Note: remove 'copyright' line (or replace file with example-add-copyright.pl.bak) in order for file to be edited

my $default_edit_file = "example-add-copyright.pl";
if (!@ARGV) {
	say "ARGV not given, use default_edit_file=($default_edit_file)";
	push @ARGV, $default_edit_file;
}

#	Copyright line:
my $copyright_line = "#\tCopyright (C) Matthew, Perl Exercises LLC\n";

#	Add each argument that is a filename to hash
my %files_to_update;
foreach (@ARGV) {
	$files_to_update{$_} = 1 if -e $_;
}

#	Remove filename from hash for any file that contains copyright line
while (<>) {
	if (/\Q$copyright_line\E/) {  # alternatively, use quotemeta()
		say "regex check, file contains copyright_line, skip ARGV=($ARGV)";
		delete $files_to_update{$ARGV};
	}
}

#	Edit the remaining files
@ARGV = sort(keys(%files_to_update));

if (!@ARGV) {
	say "No files need editing";
	exit(0);
}

#	Enable in-place editing (with backup extension .bak)
$^I = ".bak";

while (<>) {
	#	Add copyright line immediately after shebang
	if (/^#!/) {  
		if ($files_to_update{$ARGV} == 1) {  # Only add copyright line once
			$_ .= $copyright_line;
			$files_to_update{$ARGV} = 0;
		}
	}
	print;
}

