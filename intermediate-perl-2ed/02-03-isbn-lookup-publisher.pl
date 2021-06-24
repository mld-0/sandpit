#!/usr/bin/env perl
use strict;
use warnings;
use v5.032;
use Business::ISBN;

my $isbn_str = "9781449393090";
say "isbn_str=($isbn_str)";

my $isbn = Business::ISBN->new($isbn_str);
printf "ISBN=(%s)\n", $isbn->as_string;
printf "Publisher-code=(%s)\n", $isbn->publisher_code;
#printf "Country-code=(%s)\n", $isbn->country_code;  # not available?

