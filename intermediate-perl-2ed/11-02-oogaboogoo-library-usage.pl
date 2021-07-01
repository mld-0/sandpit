#!/usr/bin/env perl
use strict;
use warnings;
use v5.032;
use DateTime;

#	Relative import requires script be run from containing dir:
require './11-01-oogaboogoo-cleanup-into-library.pm';

my $dt_now = DateTime->now(time_zone=>'local');
say "dt_now=($dt_now)";

my $current_wday = $dt_now->day_of_week;
my $current_month = $dt_now->month;
say "current_wday=($current_wday), current_month=($current_month)";

my $converted_wday = Oogaboogoo::Date::day($current_wday);
my $converted_month = Oogaboogoo::Date::month($current_month);
say "converted_wday=($converted_wday), converted_month=($converted_month)";

