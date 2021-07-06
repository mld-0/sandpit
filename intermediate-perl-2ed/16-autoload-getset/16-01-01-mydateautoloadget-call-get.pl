
use lib "./";
use MyDateAutoloadGet;

#MyDateAutoloadGet->import;
my $date = MyDateAutoloadGet->init();

sub UNIVERSAL::debug {
	my $self = shift;
	my $when = localtime;
	my $message = join '|', @_;
	print "[$when] $message\n";
}

print "The date is " . $date->date . "\n"; 
print "The month is " . $date->month . "\n"; 
print "The year is " . $date->year . "\n";
$date->date(1);
$date->date(1);
$date->year(2000);
print "The date is " . $date->date . "\n"; 
print "The month is " . $date->month . "\n"; 
print "The year is " . $date->year . "\n";

$date->debug("Done now");

