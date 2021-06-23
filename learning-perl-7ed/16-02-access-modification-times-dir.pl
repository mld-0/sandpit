#!/usr/bin/env perl
use strict;
use warnings;
use v5.032;
use DateTime;
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

#	Get the length of the longest filename found
my $longest_filename_len = -1;
foreach (@files_in_dir) {
	$longest_filename_len = length($_) > $longest_filename_len ? length($_) : $longest_filename_len;
}

#	Print each file, along with mtime/ctime as datetimes:
say "Files in dir:";
foreach (@files_in_dir) {
	if ((-l $_) and (! -e readlink($_))) {
		say "$_\tDangling Symlink";  # mtime/atime for a dangling symlink is a value that cannot be converted to a datetime, therefore skip any dangling symlinks
	} else {
		my @loop_stat = stat($_);
		my $loop_mtime_epoch = $loop_stat[9];
		my $loop_atime_epoch = $loop_stat[8];
		my $loop_mtime = DateTime->from_epoch(epoch => $loop_mtime_epoch, time_zone => 'local');
		my $loop_atime = DateTime->from_epoch(epoch => $loop_atime_epoch, time_zone => 'local');
		printf "%-${longest_filename_len}s\t%12s\t%12s\n", $_, $loop_mtime, $loop_atime;
	}
}
say "";

