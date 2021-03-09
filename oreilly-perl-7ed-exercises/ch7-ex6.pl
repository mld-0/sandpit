use strict; 
use warnings;
no warnings 'shadow';

my @user_input = ( 'wilma and fred', 'fred and wilma', 'Mississippi', 'Bamm-Bamm', 'llama', 'Fred', 'fredrick', 'Alfred', 'Quebec', 'DINO', 'party-parrot', 'Mr. Slate' );

foreach my $loop_line (@user_input) {
	if ($loop_line =~ m/wilma.*fred|fred.*wilma/) {
		print "$loop_line\n";
	}
}

#	or

foreach my $loop_line (@user_input) {
	if ($loop_line =~ m/wilma/ && $loop_line =~ m/fred/) {
		print "$loop_line\n";
	}
}


