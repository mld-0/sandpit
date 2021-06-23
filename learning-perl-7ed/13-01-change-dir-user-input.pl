#!/usr/bin/env perl
use strict;
use warnings;
use v5.032;
use File::HomeDir;

#	Prompt user for directory and navigate to it, use HOME if given directory is not valid
say "Enter directory to navigate to:";
chomp(my $selected_dir = <STDIN>);
if (! -d $selected_dir) {
	say "Not a valid directory, selected_dir=($selected_dir)";
	$selected_dir = File::HomeDir->my_home;
	-d $selected_dir or die "Failed to find home dir, selected_dir=($selected_dir)";
	say "Use home, selected_dir=($selected_dir)";
}

#	Changing directory in context of perl script does not change directory of terminal used to run said script
chdir $selected_dir;
say "";

#	List directory contents using globbing
my @files_in_dir = glob ".* *";
#	or
#my @files_in_dir = <.* *>;
say "Files in dir:";
foreach (@files_in_dir) {
	say "$_";
}
say "";

#	Ongoing: 2021-06-23T16:23:27AEST The 'no comma after filehandle' rule *doesn't* apply to directory handles?

#	List directory contents using directory handle
opendir my $dir_h, $selected_dir or die "Cannot open selected_dir=($selected_dir)";
say "Files in dir:";
foreach (readdir $dir_h) {
	say "$_";
}
closedir $dir_h;

