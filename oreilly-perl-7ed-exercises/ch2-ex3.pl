
my $radius = 0;
my $pi = 3.14159;

print "enter radius value:\n";
$radius = <STDIN>;
chomp $radius;

if ($radius < 0) {
	$radius = 0;
}

my $circ = 2 * $pi * $radius;

print "circ=($circ)\n";

