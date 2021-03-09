use strict; 
use warnings;
no warnings 'shadow';

my @dino_names = qw/ fred betty barney dino wilma pebbles bamm-bamm /;


print "Enter numbers on lines\n";
my @user_vals = <STDIN>;
chomp @user_vals;

my $loop_name;
foreach my $loop_val (@user_vals) {
	if ($loop_val > 0 && $loop_val <= $#dino_names) {
		$loop_name = $dino_names[$loop_val];
	} else {
		$loop_name = "other";
	}
	print "$loop_name\n";
}
