#!/usr/bin/env perl
use strict;
use warnings;
use v5.032;

#chdir "/tmp";
chdir;

my @files_list = <*>;  # Ignoring dotfiles
say "files_list=(@files_list)";

#	Ongoing: 2021-06-28T19:55:55AEST perl, intermediate-perl-2ed, 10-01, size of a directory (when using -s)? -> same size is given by 'stat directory' (any relation to data given by 'mdls directory')? (number of items in directory?)  <- and if a directory is 18528 bytes as per stat (Downloads on Minerva), how to view those bytes (and does one even dare hope for a cross-platform answer to that question?)

#	Ongoing: 2021-06-28T20:28:32AEST perl, intermediate-perl-2ed, 10-01, Is the question even meaningful, to compare the size of items (files *and* directories) as given by -s? Ought we use a solution which gets the actual size of directories?

#	'Conventional' form:
#my @files_list_sorted = sort { -s $a <=> -s $b } @files_list;

#	Using Schwartzian Transform:
my @files_list_sorted = 
	map $_->[0],
	sort { $a->[1] <=> $b->[1] }
	map [$_, -s $_], 
	@files_list;

foreach my $file (@files_list_sorted) {
	my $file_size = (-s $file);
	printf "%-40s\t%10s\n", $file, $file_size;
}



