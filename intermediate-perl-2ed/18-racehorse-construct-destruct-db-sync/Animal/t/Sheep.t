
use Test::More tests => 3;
use Test::Output;

BEGIN { use_ok( 'Animal::Sheep' ) }

is( Animal::Sheep->sound, 'Baaah', 'Sheep makes the right sound');
stdout_is( sub { Animal::Sheep->speak } , "A Animal::Sheep goes Baaah!\n", 'Sheep speaks correctly' );

print Animal::Sheep->name, " colored ", Animal::Sheep->color, " goes ", Animal::Sheep->sound, "\n";

done_testing();




