
use Test::More tests => 3;
use Test::Output;

BEGIN { use_ok( 'Animal::Horse' ) }

is( Animal::Horse->sound, 'Neigh', 'Horse makes the right sound');
stdout_is( sub { Animal::Horse->speak } , "A Animal::Horse goes Neigh!\n", 'Horse speaks correctly' );

#	TODO: 2021-07-05T18:48:06AEST perl, intermediate-perl-2ed, 15-animal-instances-getset, make tests out of new getter/setter methods usage example
my $tv_horse = Animal::Horse->named("Mr. Ed");
$tv_horse->set_name("Mister Ed");
$tv_horse->set_color("grey");
print $tv_horse->name, " is ", $tv_horse->color, "\n";

done_testing();



