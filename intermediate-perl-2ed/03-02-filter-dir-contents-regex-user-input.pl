#!/usr/bin/env perl
use strict;
use warnings;
use v5.032;

my $path_dir = "/tmp";
chdir $path_dir or die "Couldn't chdir path_dir=($path_dir): $!\n";

my @files_list = <.* *>;
say "files_list=(@files_list)";

my $user_regex = undef;

do {
	say "Enter user_regex:";
	chomp($user_regex = <STDIN>);
	#	Use eval {} to handle errors from invalid regex
	my @files_list_filtered = grep { eval { /$user_regex/ } } @files_list;
	say "files_list_filtered=(@files_list_filtered)";

} while (!$user_regex =~ /^\s*$/);

