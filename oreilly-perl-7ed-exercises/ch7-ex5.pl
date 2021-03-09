use strict; 
use warnings;
no warnings 'shadow';

my @user_input = ( 'Mississippi', 'Bamm-Bamm', 'llama', 'Fred', 'fredrick', 'Alfred', 'Quebec', 'DINO', 'party-parrot', 'Mr. Slate' );

foreach my $loop_line (@user_input) {
	if ($loop_line =~ m/([a-z])\1/) {
		print "$loop_line\n";
	}
}

