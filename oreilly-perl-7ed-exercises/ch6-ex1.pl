use strict; 
use warnings;
no warnings 'shadow';

my %surname_lookup = (fred => 'flinstone', barney => 'rubble', wilma => 'flinstone');
my @people = qw/ fred barney wilma /;

foreach my $loop_person (@people) {
	my $loop_surname = $surname_lookup{$loop_person};
	print "loop_person=($loop_person), loop_surname=($loop_surname)\n";
}

