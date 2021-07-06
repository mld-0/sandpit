
package MyDateMethodMakerGet;
use Carp;
use v5.032;

use Class::MethodMaker 
	get_set			=> [qw(date month year)],
;

sub init {
	ref(my $class = shift) and croak "Can't call for class instance";
	my @result_localtime = localtime;
	my $self = { 'date' => $result_localtime[3], 'month' => $result_localtime[4]+1, 'year' => $result_localtime[5]+1900 };
	bless $self, $class;
}

sub DESTROY {}

1;


#use vars qw($AUTOLOAD);
#
#use Carp;
#
#my %Allowed_methods = qw( date 3 month 4 year 5 );
#my @Offsets = qw(0 0 0 0 1 1900 0 0 0); 
#
#sub new { bless {}, $_[0] }
#
#sub DESTROY {}
#
##	Provides a get method for: 'date', 'month', 'year'
#sub AUTOLOAD {
#	my $method = $AUTOLOAD; 
#	$method =~ s/.*:://;
#	unless( exists $Allowed_methods{ $method } ) { 
#		carp "Unknown method: $AUTOLOAD";
#		return;
#	}
#	my $slice_index = $Allowed_methods{ $method };
#	my $result = (localtime)[$slice_index] + $Offsets[$slice_index];
#	return $result;
#} 



