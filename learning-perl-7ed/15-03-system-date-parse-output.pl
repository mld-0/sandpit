#!/usr/bin/env perl
use strict;
use warnings;
use v5.032;

chomp(my $date_str = qx/date/);
say "date_str=($date_str)";

$date_str =~ /^(?<day>[A-Z][a-z]+)\s+(?<month>[A-Z][a-z]+)\s+(?<day>\d+)\s+(?<time>\d{2}:\d{2}:\d{2})\s+(?<timezone>\w+)\s+(?<year>\d{4})$/;

my @date_vals = ( $+{'year'}, $+{'month'}, $+{'day'}, $+{'time'}, $+{'timezone'} );
say "date_vals=(@date_vals)";

my $weekday_str = $+{'day'};
say "weekday_str=($weekday_str)";

chomp(my $weekday_num = qx/date +%u/);
say "weekday_num=($weekday_num)";

if ($weekday_str =~ /^S/) {
	say "Weekend";
} else {
	say "Weekday";
}

