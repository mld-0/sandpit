#!/usr/bin/env perl
use strict;
use warnings;
use v5.032;
use Cwd;
use File::Spec;

$" = "\n";

#	Get list of files in the current directory ('.'/'..' excluded)
my $dir_path = getcwd();
say "dir_path=($dir_path)";
my @files_list;
opendir DIRH, $dir_path or die "Can't open dir_path=($dir_path): $!\n";
foreach (readdir DIRH) {
	push @files_list, $_;
}
closedir DIRH or die "Can't close dir_path=($dir_path): $!\n";
@files_list = File::Spec->no_upwards(@files_list);
say "files_list=(@files_list)";

#	Convert @files_list entries to absolute paths as @paths_list
my @paths_list;
foreach (@files_list) {
	push @paths_list, File::Spec->rel2abs($_);
}
say "paths_list=(@paths_list)";

