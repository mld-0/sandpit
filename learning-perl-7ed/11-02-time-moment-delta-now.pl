#!/usr/bin/env perl
use strict;
use warnings;
use v5.032;
use Time::Moment;

my $current_datetime = Time::Moment->now;
say "current_datetime=($current_datetime)";

my $previous_year = 2020;
my $previous_month = 04;
my $previous_day = 17;
my $previous_hour = 13;
my $previous_minutes = 23;
my $previous_seconds = 15;

#	Ongoing: 2021-06-22T22:15:44AEST Treatment of timezone?
my $previous_datetime = Time::Moment->new(
	year => $previous_year, 
	month => $previous_month, 
	day => $previous_day, 
	hour => $previous_hour, 
	minute => $previous_minutes, 
	second => $previous_seconds
	);

say "previous_datetime=($previous_datetime)";

#	Ongoing: 2021-06-22T22:19:40AEST perl, learning-perl-4ed, 11-02-time-moment-delta-now-user-input.pl, Time::Moment->delta_months gives total number of months, delta_days total number of days, ect -> that is to say, ($delta_years, $delta_months, ..., $delta_seconds) have not elapsed between $current_datetime and $previous_datetime, instead each of these gives the entire interval as expressed in that unit of time (and rounded) -> better/more complete delta-datetime example for perl?
my $delta_years = $previous_datetime->delta_years($current_datetime);
my $delta_months = $previous_datetime->delta_months($current_datetime);
my $delta_days = $previous_datetime->delta_days($current_datetime);
my $delta_hours = $previous_datetime->delta_hours($current_datetime);
my $delta_mins = $previous_datetime->delta_minutes($current_datetime);
my $delta_seconds = $previous_datetime->delta_seconds($current_datetime);
say "delta_years=($delta_years)";
say "delta_months=($delta_months)";
say "delta_days=($delta_days)";
say "delta_hours=($delta_hours)";
say "delta_mins=($delta_mins)";
say "delta_seconds=($delta_seconds)";
