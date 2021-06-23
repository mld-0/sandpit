#!/usr/bin/env perl
use strict;
use warnings;
use v5.032;

#	Read non-empty lines from $path_file into @file_lines
my $path_file = "example-text-file.txt";
-e $path_file or die "Can't find file path_file=($path_file): $!\n";
open my $fh, '<', $path_file or die "Couldn't open path_file=($path_file): $!\n";
chomp(my @file_lines = grep { /\S/ } <$fh>);  # read only non-empty lines
close $fh;

#	Print contents of file
say "file_lines:";
foreach (@file_lines) {
	say $_;
}
say "";

#	Prompt user for <pattern> <regex?>
say "Enter pattern to match against file_lines";
chomp(my $user_pattern = <STDIN>);
if (length($user_pattern) == 0) {
	say "Exiting";
	exit;
}
say "";

#	Ongoing: 2021-06-23T20:57:49AEST when should/shouldn't quotemeta() be used on a regex recieved from the user 

#	Filter file_lines using user_pattern 
my @file_line_matches = grep /$user_pattern/, @file_lines;

#	Print results:
printf "file_line_matches: (%i)\n", length(@file_line_matches);
foreach (@file_line_matches) {
	say $_;
}

