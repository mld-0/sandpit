#!/usr/bin/perl
#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=3:
#   }}}1
use strict; 
use warnings;
no warnings 'shadow';
use Data::Dumper;

my @months = qw( Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec );
my @days = qw( Sun Mon Tue Wed Thu Fri Sat Sun );

(my $sec, my $min, my $hour, my $mday, my $mon, my $year, my $wday, my $yday, my $isdst) = localtime();
print "$mday $mon $wday\n";
print "$mday $months[$mon] $days[$wday]\n";

#	local and gmt datetimes
my $datestring = localtime();
print "datestring=($datestring)\n";
my $gmt_datestring = gmtime();
print "gmt_datestring=($gmt_datestring)\n";
print "\n";

#	iso datetime from system
print `date +%FTTH:%M:%S%Z`;
print "\n";

#	epoch
my $epoc = time();
print "Number of seconds since Jan 1, 1970 - $epoc\n";
print "\n";

#	epoch to datetime
my $epoch_val = 1361022130;
my $datetime_val = localtime($epoch_val);
print "epoch_val=($epoch_val), datetime_val=($datetime_val)\n";
print "\n";

#	datetime to epoch
use Date::Manip;  # need to install (cpan install Date::Manip)
my $datetime_val = "2021-02-17T22:56:52AEDT";
my $epoch_val = UnixDate(ParseDate($datetime_val),"%s");
print "datetime_val=($datetime_val), epoch_val=($epoch_val)\n";
print "\n";


use DateTime::Format::Strptime;  # need to install (cpan install DateTime:Format:Strptime)
my $parser = DateTime::Format::Strptime->new(
  pattern => '%B %d, %Y %I:%M %p %Z',
  on_error => 'croak',
);
my $dt = $parser->parse_datetime('October 28, 2011 9:00 PM PDT');
print "$dt\n";
#	Dumper - print all attirbutes of an object
#	print Dumper($dt)

use DateTime;
use Date::Parse;  # need to install (cpan instal lDate::Parse)
my $str = "2021-02-17T23:20:54AEDT";
my $epoch = str2time($str);
my $datetime = DateTime->from_epoch(epoch => $epoch);
print "datetime=($datetime)\n";

