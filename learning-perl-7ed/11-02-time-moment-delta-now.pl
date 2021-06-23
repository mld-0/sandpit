#!/usr/bin/env perl
use strict;
use warnings;
use v5.032;
use Time::Moment;
use Scalar::Util;

my $current_datetime = Time::Moment->now;
say "current_datetime=($current_datetime)";
say Scalar::Util::blessed($current_datetime);

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
say Scalar::Util::blessed($previous_datetime);

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
say "";

use DateTime;
use DateTime::Format::MySQL;
use DateTime::Format::Duration;

#	Using DateTime to find deltas -> result is ($delta_years, $delta_months, ..., $delta_seconds) which add to give the total delta, rather than each giving the total delta

#	Purpouse/effect of 'floating' timezone?
#my $dt1 = DateTime->now( time_zone => 'local' )->set_time_zone('floating');
my $dt1 = DateTime->now( time_zone => 'local' );
say "dt1=($dt1)";
say Scalar::Util::blessed($dt1);

my $dt2 = DateTime->new(
	year => $previous_year, 
	month => $previous_month, 
	day => $previous_day, 
	hour => $previous_hour, 
	minute => $previous_minutes, 
	second => $previous_seconds,
	time_zone => 'local',
	);
say "dt2=($dt2)";

my $dt_delta = $dt1->subtract_datetime($dt2);
say "dt_delta=($dt_delta)";
say Scalar::Util::blessed($dt_delta);

$delta_years = $dt_delta->years();
$delta_months = $dt_delta->months();
$delta_days = $dt_delta->days();
$delta_hours = $dt_delta->hours();
$delta_mins = $dt_delta->minutes();
$delta_seconds = $dt_delta->seconds();
say "delta_years=($delta_years)";
say "delta_months=($delta_months)";
say "delta_days=($delta_days)";
say "delta_hours=($delta_hours)";
say "delta_mins=($delta_mins)";
say "delta_seconds=($delta_seconds)";
say "";

#	Finding delta using epochs: convert $dt1/$dt2 to epoch, and subtract to give total delta in seconds
my $delta_total_seconds = $dt1->epoch() - $dt2->epoch();
say "delta_total_seconds=($delta_total_seconds)";

