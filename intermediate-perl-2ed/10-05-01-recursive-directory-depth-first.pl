#!/usr/bin/env perl
use strict;
use warnings;
use v5.032;
use File::Spec;
use Data::Dumper;

#	Create nested hash, representing contents of directory
sub directory_fill_hash_depthfirst {
	my $path = shift;
	if (-l $path) {
		return "link";
	}
	if (-f $path) {
		return -s $path;
	}
	if (-d $path) {
		my %dir_hash;
		opendir DIR, $path, or die "Cannot open dir path=($path): $!\n";
		my @dir_contents = readdir DIR;
		closedir DIR or die "Cannot close dir path=($path): $!\n";
		for my $item_name (@dir_contents) {
			next if $item_name eq '.' or $item_name eq '..';
			my $loop_next_path = File::Spec->catfile($path, $item_name);
			$dir_hash{$item_name} = directory_fill_hash_depthfirst($loop_next_path);
		}
		return \%dir_hash;
	}
	warn "Neither file nor directory, return undef, path=($path)";
	return undef;
}

my $dir_path;
$dir_path = $ENV{'mld_data'};

my $dir_hash_ref = directory_fill_hash_depthfirst $dir_path;
print Dumper($dir_hash_ref);


