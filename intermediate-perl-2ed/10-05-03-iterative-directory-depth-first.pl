#!/usr/bin/env perl
use strict;
use warnings;
use v5.032;
use File::Basename;
use File::Spec;
use Data::Dumper;

sub directory_fill_hash_depthfirst_iterative {
	my $path = shift;
	my $dir_hash = {};

	my @queue = ( [$path, 0, $dir_hash] );

	while (my $next = shift @queue) {
		my ($path, $level, $loop_hashref) = @$next;
		my $path_basename = basename($path);

		$loop_hashref->{$path_basename} = do {
			my $do_result = undef;
			if (-l $path) { 
				$do_result = "link"; 
			} elsif (-f $path) { 
				$do_result = -s $path; 
			} else {
				$do_result = {};

				opendir DIR, $path or die "Cannot open dir path=($path): $!\n";
				my @dir_contents = readdir DIR;
				closedir DIR or die "Cannot close dir path=($path): $!\n";

				#	Remove '.' and '..' then prefix current $path to each filename in @dir_contents
				@dir_contents = grep { ! /^\.\.?$/ } @dir_contents;  
				my @new_paths = map {
					File::Spec->catfile($path, $_);
				} @dir_contents;

				#	Add to beginning of @queue for a depth first search
				my @new_queue_items = map { [$_, $level+1, $do_result ] } @new_paths;
				unshift @queue, @new_queue_items;
			}
			$do_result;
		}; 


	}
	return $dir_hash;
}

my $dir_path;
$dir_path = $ENV{'mld_data'};

my $dir_hash_ref = directory_fill_hash_depthfirst_iterative $dir_path;
print Dumper($dir_hash_ref);

