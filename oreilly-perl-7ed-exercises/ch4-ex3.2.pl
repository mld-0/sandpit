use v5.10;
use strict; 
use warnings;
no warnings 'shadow';

sub greet {
	state @people_seen;
	my $person = shift;
	if ($#people_seen == -1) {
		print "Hi $person! You are the first one here\n";
	} else {
		my $last_person = $people_seen[$#people_seen];
		print "Hi $person! $last_person is also here\n";
	}
	push(@people_seen, $person);
}

greet( "Fred" );
greet( "Barney" );



