#!/usr/bin/env perl
use strict;
use warnings;
use v5.032;
use File::Spec;
use Data::Dumper;

#	Create nested hash, representing contents of directory
sub directory_fill_hash {
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
			$dir_hash{$item_name} = directory_fill_hash($loop_next_path);
		}
		return \%dir_hash;
	}
	warn "Neither file nor directory, return undef, path=($path)";
	return undef;
}

#	Print nested hash created by directory_fill_hash, with tabs prefixed to indicate depth
sub directory_print_indented {
	my $path = shift;
	my $dir_hash_ref = shift;
	my $level = shift || 0;

	print "\t" x $level . $path;

	if (!ref($dir_hash_ref)) {
		print "\n";
		return;
	}
	print "/\n";

	foreach my $loop_item (sort keys %$dir_hash_ref) {
		directory_print_indented($loop_item, $dir_hash_ref->{$loop_item}, $level+1);
	}
}

my $dir_path;
$dir_path = $ENV{'mld_data'};

my $dir_hash_ref = directory_fill_hash $dir_path;

directory_print_indented $dir_path, $dir_hash_ref;

