#!/usr/bin/env perl
use strict;
use warnings;
use v5.032;
use Cwd;
use Sub::Identify qw/sub_fullname/;

#	Suggested Input:
#		/tmp $HOME

sub Print_Dir_Contents {
	my $path_dir = shift;
	die "Not a dir, path_dir=($path_dir)\n" unless (-d $path_dir);

	say sub_fullname(__SUB__) . ": $path_dir";

	#	Using dirhandle:
	opendir my $dir_handle, $path_dir or die "Couldn't opendir path_dir=($path_dir)\n";
	foreach (readdir $dir_handle) {
		#	Skip '.' / '..'
		next if ($_ eq '.' or $_ eq '..');
		say $_;
	}
	closedir $dir_handle;

	##	Using globbing:
	#my $previous_cwd = cwd;
	#chdir $path_dir;
	#my @dir_contents = <.* *>;
	#foreach (@dir_contents) {
	#	next if ($_ eq '.' or $_ eq '..');
	#	say $_;
	#}
	#chdir $previous_cwd;
}

#	Read dirs given as arguments
my @user_dirs;
foreach (@ARGV) {
	if (-d $_) {
		push @user_dirs, $_;
	} else {
		warn "Not a dir, skip ARGV=($ARGV) \$_=($_)\n";
	}
}
die "Empty user_dirs, no directories given\n" unless scalar(@user_dirs) > 0;

foreach (@user_dirs) {
	Print_Dir_Contents $_;
}

