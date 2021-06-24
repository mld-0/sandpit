#!/usr/bin/env perl
use strict;
use warnings;
use v5.032;

#	Example input:
#		*

my $file_size_limit = 1000;
my @files_list;
@files_list = grep { -e $_ } @ARGV;
@files_list = grep { -s $_ < $file_size_limit } @files_list;
@files_list = map { "    $_\n" } @files_list;

say "files_list=(@files_list)";

