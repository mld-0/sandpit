use v5.10;
use strict; 
use warnings;
no warnings 'shadow';

$ENV{ZERO}      = 0;
$ENV{EMPTY}     = '';
$ENV{UNDEFINED} = undef;

#	Sort by value
foreach my $k (sort {$ENV{$a} cmp $ENV{$b}} keys(%ENV)) {
	printf("%20s\t%60s\n", $k, $ENV{$k} // "undefined");
}
print "\n";


##	Sort by key
#foreach my $k (sort keys(%ENV)) {
#	printf("%20s\t%60s\n", $k, $ENV{$k});
#}
#print "\n";

