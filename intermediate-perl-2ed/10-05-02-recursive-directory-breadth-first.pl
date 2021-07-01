#!/usr/bin/env perl
use strict;
use warnings;
use v5.032;
use File::Basename;
use File::Spec;
use Data::Dumper;
#use warnings FATAL => 'recursion';

#	Ongoing: 2021-07-01T21:02:25AEST perl, intermediate-perl-2ed, 10-05-02, perl issues a warning when the number of recursions passes 100: (but does appear to continue past this point) is there any actual limit (beyond time and memory) to how deep perl can recurse? (In any case, the warning implies recursing to such an extent is bad practice/design?)

#	Create nested hash, representing contents of directory. Recursively implements breadth-first search using a queue. This implementation results in a function call for every item in the queue, which is every file/directory - which quickly excedes the recursion limit (which is not easily changed) of perl, meaning <...>
sub directory_fill_hash_breadthfirst {

	#	Base case, return given no (more) items in queue
	if (scalar(@_) == 0) { 
		return; 
	}	

	my $next = shift;
	my @queue = @_;

	#	Handle the case where first argument is a string (initial call), or an arrayref (recursive calls)
	my ($path, $level, $dir_hash_ref);
	if (!ref($next)) {
		$path = $next;
		$level = 0;
		$dir_hash_ref = {};
		@queue = ( [$path, $level, $dir_hash_ref] );
	} elsif (ref($next) eq ref([])) {
		($path, $level, $dir_hash_ref) = @$next;
	}

	my $path_basename = basename($path);

	$dir_hash_ref->{$path_basename} = do {
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
			#	Add to end of @queue for a breadth first search
			my @new_queue_items = map { [$_, $level+1, $do_result ] } @new_paths;
			push @queue, @new_queue_items;
		}
		$do_result;
	}; 

	directory_fill_hash_breadthfirst(@queue);
	return $dir_hash_ref;
}

my $dir_path = $ENV{'mld_data'};

#my $dir_hash_ref = {};
#my @queue = ( [$dir_path, 0, $dir_hash_ref] );
#directory_fill_hash_breadthfirst @queue;
#print Dumper($dir_hash_ref);

my $result_hash_ref = directory_fill_hash_breadthfirst $dir_path;
print Dumper($result_hash_ref);

