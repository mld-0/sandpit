
package MyDateAutoloadGet;
use vars qw($AUTOLOAD);

use v5.032;
use Carp;

my %Allowed_methods = qw( date 3 month 4 year 5 );
my @Offsets = qw(0 0 0 0 1 1900 0 0 0); 

#sub new { bless {}, $_[0] }

sub init {
	ref(my $class = shift) and croak "Can't call for class instance";
	my @result_localtime = localtime;
	my $self = { 'date' => $result_localtime[3], 'month' => $result_localtime[4]+1, 'year' => $result_localtime[5]+1900 };
	bless $self, $class;
}

sub DESTROY {}

#	Provides a get/set method for: 'date', 'month', 'year'
sub AUTOLOAD {
	my $method = $AUTOLOAD; 
	$method =~ s/.*:://;
	unless( exists $Allowed_methods{ $method } ) { 
		carp "Unknown method: $AUTOLOAD";
		return;
	}

	#	This is now a get method $method if not given an argument, or a set method if given one
	my $self = shift;
	if (!@_) {
		#my $slice_index = $Allowed_methods{ $method };
		#my $result = (localtime)[$slice_index] + $Offsets[$slice_index];
		my $result = $self->{$method};
		return $result;
	} else {
		my $arg = shift;
		$self->{$method} = $arg;
		return $arg;
	}
} 

1;

