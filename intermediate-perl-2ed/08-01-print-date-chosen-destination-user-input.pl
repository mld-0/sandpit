#!/usr/bin/env perl
use strict;
use warnings;
use v5.032;
use DateTime;
use IO::Tee;

say "Select output destination [F]ile/[S]calar/[B]oth:";
chomp(my $user_dest_select = <STDIN>);

my $today_date_str = DateTime->now(time_zone=>'local')->strftime("%FT%H:%M:%S%Z");
my $path_file_output = "today-date.txt";
my $scalar_str_output;

my $fh_out;

if ($user_dest_select =~ /^F/) {
	open $fh_out, '>', $path_file_output or die "Can't open path_file_output=($path_file_output): $!\n";
} elsif ($user_dest_select =~ /^S/) {
	open $fh_out, '>', \$scalar_str_output or die "Can't open scalar_str_output: $!\n";
} elsif ($user_dest_select =~ /^B/) {	
	open my $fh_file, '>', $path_file_output or die "Can't open path_file_output=($path_file_output): $!\n";
	open my $fh_scalar, '>', \$scalar_str_output or die "Can't open scalar_str_output: $!\n";
	$fh_out = IO::Tee->new( $fh_file, $fh_scalar );

} else {
	die "Invalid user_dest_select=($user_dest_select)";
}

printf $fh_out "%s\n", $today_date_str;
say "scalar_str_output=($scalar_str_output)";

#	A Tee filehandle must be closed using object notation (which also works for regular filehandles)
$fh_out->close or die "Can't close fh_out=($fh_out): $!\n";

