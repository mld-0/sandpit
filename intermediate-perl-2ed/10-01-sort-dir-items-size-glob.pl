#!/usr/bin/env perl
use strict;
use warnings;
use v5.032;
use File::Find;

chdir "/tmp";
#chdir "$ENV{HOME}/Downloads" ;
#chdir;

my @files_list = <*>;  # Ignoring dotfiles
#say "files_list=(@files_list)";
#say "";

#	Note: 2021-06-29T21:40:53AEST Consider 10-02 a beautified version of this same task

#	Ongoing: 2021-06-28T19:55:55AEST perl, intermediate-perl-2ed, 10-01, size of a directory (when using -s)? -> same size is given by 'stat directory' (any relation to data given by 'mdls directory')? (number of items in directory?)  <- and if a directory is 18528 bytes as per stat (Downloads on Minerva), how to view those bytes (and does one even dare hope for a cross-platform answer to that question?)

#	Ongoing: 2021-06-28T20:28:32AEST perl, intermediate-perl-2ed, 10-01, Is the question even meaningful, to compare the size of items (files *and* directories) as given by -s? Ought we use a solution which gets the actual size of directories?

#	'Conventional' form:
#my @files_list_sorted = sort { -s $a <=> -s $b } @files_list;

#	Ongoing: 2021-06-29T20:33:55AEST perl, can a subroutine be used with map(), without assigning said subroutine to a variable?

#	Get the actual size of a given directory given as path
my $item_size = sub {
	my $path_item = shift;
	-e $path_item or die "path_item=($path_item) not found: $!\n";
	if (-f $path_item) {
		return -s $path_item;
	} elsif (-d $path_item) {
		my $total = 0;
		File::Find::find( sub { $total += -s if -f }, $path_item );
		return $total;
	} else {
		warn "path_item=($path_item), not file or directory (using -s)\n";
		return -s $path_item;
	}
};

#	Using Schwartzian Transform:
my @files_list_sorted = 
	map $_->[0],
	sort { $a->[1] <=> $b->[1] }
	#map [$_, -s $_],  # -s does not get the actual size of directories
	map [$_, $item_size->($_)],
	@files_list;

#	Ongoing: 2021-06-29T20:04:40AEST perl, intermediate-perl-2ed, 10-01, Neater (which is to say more perl-esque) solution to the "trim and affix '...' only if too long" problem for printing filenames -> and, solution with have the '...' in the middle?

#	Print results:
my $filename_output_width = 40;
say "files_list_sorted:";
foreach my $file (@files_list_sorted) {
	#my $file_size = (-s $file);
	#my $file_size = item_size $file;
	my $file_size = $item_size->($file);
	my $loop_filename_output;
	if (length($file) >= $filename_output_width) {
		$loop_filename_output = substr($file, 0, $filename_output_width-4) . '...';
	} else {
		$loop_filename_output = $file;
	}
	my $item_type = 'O';
	if (-f $file) {
		$item_type = 'F';
	} elsif (-d $file) {
		$item_type = 'D';
	}
	printf "\t%-${filename_output_width}s\t%s\t%-10s\n", $loop_filename_output, $item_type, $file_size;
}

