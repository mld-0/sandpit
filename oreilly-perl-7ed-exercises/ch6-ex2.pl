use strict; 
use warnings;
no warnings 'shadow';

print "Enter input lines:\n";
#my @user_lines = <STDIN>;
#chomp @user_lines;

my @user_lines = qw/ fred barney fred dino wilma fred/;
my %seen_lines = ();

foreach my $loop_line (@user_lines) {
	$seen_lines{$loop_line} += 1;
}

while ( my($k, $v) = each(%seen_lines) ) {
	print "k=($k), v=($v)\n";
}
print "\n";

#	sort hash by keys
foreach my $k (sort keys(%seen_lines)) {
	my $v = $seen_lines{$k};
	print "k=($k), v=($v)\n";
}
print "\n";

#	sort hash by values
foreach my $k (sort { $seen_lines{$b} <=> $seen_lines{$a} } keys(%seen_lines)) {
	my $v = $seen_lines{$k};
	print "k=($k), v=($v)\n";
}
print "\n";

