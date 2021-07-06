
package Oogaboogoo;
use strict;
use warnings;
use v5.032;

use Exporter qw(import);

our @EXPORT = qw(day month);
our %EXPORT_TAGS = ( all => \@EXPORT );

#	Constants for mappings:
my @day = qw( ark dip wap sen pop sep kir );
my @month = qw( diz pod bod rod sip wax lin sen kun fiz nap dep );

#	Weekday number to name conversion subroutine:
sub day {
	my $num = shift;
	my $day_max_val = $#day;
	die "num=($num) is not a valid day [0,$day_max_val]\n" 
		unless $num >= 0 and $num <= $day_max_val;
	return $day[$num];	
}

#	Month number to name conversion subroutine:
sub month {
	my $num = shift;
	my $month_max_val = $#month;
	die "num=($num) is not a valid month [0, $month_max_val]\n" 
		unless $num >= 0 and $num <= $month_max_val;
	return $month[$num];
}

1;  # End of package true value

