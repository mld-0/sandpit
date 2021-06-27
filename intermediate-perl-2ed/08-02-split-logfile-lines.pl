#!/usr/bin/env perl
use strict;
use warnings;
use v5.032;

use File::Spec::Functions 'catfile';

my $path_input = "fruit-logfile.txt";
my $path_dir_output = "fruit-logfiles";

#	Store output filenames, filehandles: $output_logs{$name} = [ logname, filehandle ]
my %output_log_path;
my %output_log_fh;

mkdir $path_dir_output unless (-d $path_dir_output);

open my $fh_input, '<', $path_input or die "Can't open path_input=($path_input): $!\n";
while (<$fh_input>) {
	#chomp;
	#	Split lines
	my $loop_line = $_;
	my @loop_split = split /: /;
	die "Invalid line, len(loop_split) != 2, \$_=($_)\n" if not scalar(@loop_split) == 2;
	my ($loop_name, $loop_fruit) = @loop_split;

	#	Get filename for each output log
	my $loop_logpath = catfile $path_dir_output , "/" , lc($loop_name) =~ s/. /-/r . ".info";
	die "Invalid filename loop_logpath=($loop_logpath)\n" if not $loop_logpath !~ /^[-\w]\\z/;
	say "loop_logpath=($loop_logpath)";

	if (!exists $output_log_fh{$loop_name}) {
		open my $loop_log_fh, '>', $loop_logpath or die "Can't open loop_logpath=($loop_logpath)";
		#$output_log_fh{$loop_name} = [$loop_logpath, $loop_log_fh];
		$output_log_path{$loop_name} = $loop_logpath;
		$output_log_fh{$loop_name} = $loop_log_fh;
	}

	#	Ongoing: 2021-06-27T23:53:21AEST using filehandle with print directly from hash doesn't work (commented out line immediately below) (but closing the filehandle does?), but does work when assigned with a temporary variable?
	#print $output_log_fh{$loop_name} $loop_line;
	my $loop_fh = $output_log_fh{$loop_name};
	print $loop_fh "$loop_line";
}

#	Close filehandles
close $fh_input or die "Can't close path_input=($path_input): $!\n";
foreach (keys %output_log_fh) {
	close $output_log_fh{$_};
}

