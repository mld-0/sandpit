#!/usr/bin/env perl
use strict;
use warnings;
use v5.032;

use DateTime;
use File::HomeDir;
use File::Find;
use File::Basename;
use Time::Local;


my $target_dayofweek = 1;  # Sun, Mon, ... = 0, 1, ...

#my $path_dir = File::HomeDir->my_home;
my $path_dir = $ENV{'mld_sandpit'};
say "path_dir=($path_dir)";

my @starting_directories = ( $path_dir );
say "starting_directories=(@starting_directories)";

#	Midnight today
my $time_end = DateTime->today( time_zone=>'local' );

#	Number of days since last target_dayofweek
my $delta_days = $time_end->day_of_week - $target_dayofweek;
if ($delta_days <= 0) { $delta_days += 7; }
say "delta_days=($delta_days)";

#	Midnight of last target_dayofweek
my $time_start = $time_end->clone->add( DateTime::Duration->new( days => -1 * $delta_days ) );
printf "time_end=(%s)\n", $time_end->strftime("%FT%H:%M:%S%Z");
printf "time_start=(%s)\n", $time_start->strftime("%FT%H:%M:%S%Z");

#	Implement our gather function without using closure
my $time_start_epoch = $time_start->epoch;
my $time_end_epoch = $time_end->epoch;
my @result_files;
my $gather = sub {
	if ($_ =~ /^\.git$/) {
		warn "Skip, git dir=($File::Find::dir)";
		$File::Find::prune = 1;
		return;
	}
	my $file_mtime_epoch = (stat $_)[9];
	unless (defined $file_mtime_epoch) {
		warn "Skip, can't stat file=($File::Find::name): $!\n";
		return;
	}
	if ($file_mtime_epoch >= $time_start_epoch and $file_mtime_epoch <= $time_end_epoch) {
		push @result_files, $File::Find::name
	}
};
find($gather, @starting_directories);

for my $loop_file (@result_files) {
	my $loop_mtime_epoch = (stat $loop_file)[9];
	my $loop_mtime = DateTime->from_epoch( epoch => $loop_mtime_epoch, time_zone => 'local' );
	my $loop_filename = basename $loop_file;
	my $loop_dirname = dirname $loop_file;
	say "file=($loop_filename), loop_mtime=($loop_mtime), \ndir=($loop_dirname)\n";
}

