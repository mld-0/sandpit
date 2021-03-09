use strict; 
use warnings;
no warnings 'shadow';

my @user_input = ( 'Fred', 'fredrick', 'Alfred', 'Quebec', 'dino', 'party-parrot', 'Mr. Slate' );

foreach my $loop_line (@user_input) {
	if ($loop_line =~ m/\./) {
		print "$loop_line\n";
	}
}
