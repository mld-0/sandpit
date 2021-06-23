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

chdir "$selected_dir";

#	List items in selected_dir that are symlinks
opendir my $dir_h, $selected_dir or die "Cannot open selected_dir=($selected_dir)";
say "symlinks in dir:";
foreach (readdir $dir_h) {
	if (-l $_) {
		my $path_readlink = readlink $_;
		say "\$_=($_), path_readlink=($path_readlink)";
	}
}
closedir $dir_h;

