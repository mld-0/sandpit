use v5.10;
use strict; 
use warnings;
no warnings 'shadow';

my $Debug = $ENV{DEBUG} // 1;

my $random_pick = int(1 + rand 100);
my $user_pick = -1;

if ($Debug) {
	print "random_pick=($random_pick)\n";
}

while ($user_pick != $random_pick) {
	print "Enter a guess [0-100]\n";
	$user_pick = <STDIN>;
	if ($user_pick =~ m/quit|exit/i || $user_pick =~ m/^\s*$/) {
		print "Exiting\n";
		last;
	}
	if ($user_pick > $random_pick) {
		print "Too high\n";
	} elsif ($user_pick < $random_pick) {
		print "Too low\n";
	} elsif ($user_pick == $random_pick) {
		print "Correct\n";
	}
}

