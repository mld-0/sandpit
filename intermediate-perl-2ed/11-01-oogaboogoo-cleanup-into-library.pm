#	Gilligan's Code:
#		@day = qw(ark dip wap sen pop sep kir);
#		sub number_to_day_name { my $num = shift @_; $day[$num]; } 
#		@month = qw(diz pod bod rod sip wax lin sen kun fiz nap dep);

#	Cleanup into library:
package Oogaboogoo::Date;
use strict;
use warnings;
use v5.032;

#	Ongoing: 2021-07-01T21:26:02AEST perl, intermediate-perl-2ed, 11-01, rudimentary day/month itoa library, 'answers' give 'day' /' month' as variable names for mapping arrays, the same names used by the conversion subroutines - that being the point(?), because they're otherwise aweful; would they be better renamed (in which case, no longer (presumedly) overridden by subroutines, we should use some other way to hide them outside the package)?

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

