use strict; 
use warnings;
no warnings 'shadow';

my @user_input = ( 'Fred', 'fredrick', 'Alfred', 'Quebec', 'DINO', 'party-parrot', 'Mr. Slate' );

foreach my $loop_line (@user_input) {
	if ($loop_line =~ m/[A-Z][a-z]+/) {
		print "$loop_line\n";
	}
}
