#!/usr/bin/env perl
use strict;
use warnings;
use v5.032;

sub File_Check_Properites {
	my $check_filename = shift(@_);
	say "check_filename=($check_filename)";
	say "File exists" if -e $check_filename;
	say "Readable" if -r $check_filename;
	say "Writeable" if -w $check_filename;
	say "Executable" if -x $check_filename;
	say "";
}

foreach (@ARGV) {
	File_Check_Properites "$_";
}

