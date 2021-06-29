#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=3:
#   }}}1
#!/usr/bin/env perl
use strict;
use warnings;
use v5.032;
use Cwd;
use Benchmark;
use File::Find;
#	{{{2

#chdir "/tmp";
chdir "$ENV{HOME}/Downloads" ;
#chdir;

say "test dir: " . cwd;

#	Ongoing: 2021-06-29T21:29:51AEST perl, intermediate-perl-2ed, 10-02, would a files_list that includes dotfiles (specifically ./..) <alter/disrupt> sorting-by-size (or displaying of results) (that being the task 10-01)
my @files_list = <*>;  # Ignoring dotfiles
my @files_list_sorted;

sub trim_filename_output {
#	{{{
	my $file = shift;
	my $filename_output_width = shift;
	my $filename_output_trimmed;
	if (length($file) >= $filename_output_width) {
		$filename_output_trimmed = substr($file, 0, $filename_output_width-4) . '...';
	} else {
		$filename_output_trimmed = $file;
	}
	return $filename_output_trimmed;	
}
#	}}}

#	Get the actual size of a given directory given as path
my $item_size = sub {
#	{{{
	my $path_item = shift;
	-e $path_item or die "path_item=($path_item) not found: $!\n";
	if (-f $path_item) {
		return -s $path_item;
	} elsif (-d $path_item) {
		my $total = 0;
		File::Find::find( sub { $total += -s if -f }, $path_item );
		return $total;
	} else {
		#warn "path_item=($path_item), not file or directory (using -s)\n";
		return -s $path_item;
	}
};
#	}}}

sub filetype_shortcode {
#	{{{
	my $file = shift;
	-e $file or die "Not found, file=($file)\n";
	my $item_type = 'O'; if (-f $file) { $item_type = 'F'; } elsif (-d $file) { $item_type = 'D'; }
	return $item_type;
}
#	}}}

#	Ongoing: 2021-06-29T22:23:37AEST perl, intermediate-perl-2ed, (how to) order tests performed by Benchmark::timethese
timethese( -5, {
	"Ordinary, non dirsize" => sub { @files_list_sorted = sort { -s $a <=> -s $b } @files_list; },
	"Schwartzian, non dirsize" => sub { @files_list_sorted = map $_->[0], sort { $a->[1] <=> $b->[1] } map [$_, -s $_],  @files_list; }, 

	"Ordinary, dirsize" => sub { @files_list_sorted = sort {  $item_size->($a) <=> $item_size->($b) } @files_list; }, 
	"Schwartzian, dirsize" => sub { @files_list_sorted = map $_->[0], sort { $a->[1] <=> $b->[1] } map [$_, $item_size->($_)], @files_list; }, 

}, );


