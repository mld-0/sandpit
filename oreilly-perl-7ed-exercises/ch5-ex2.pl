use strict; 
use warnings;
no warnings 'shadow';

print "Enter lines:\n";
my @user_lines = <STDIN>;
chomp @user_lines;

my $ruler = "1234567890" x 3;

print "$ruler\n";
foreach my $loop_line (@user_lines) {
	printf("%20s\n", $loop_line);
}


