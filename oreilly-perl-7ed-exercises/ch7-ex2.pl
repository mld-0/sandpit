use strict; 
use warnings;
no warnings 'shadow';

my @user_input = qw/ Fred fredrick Alfred Quebec dino party-parrot /;

foreach my $loop_line (@user_input) {
	if ($loop_line =~ m/[Ff]red/) {
		print "$loop_line\n";
	}
}
