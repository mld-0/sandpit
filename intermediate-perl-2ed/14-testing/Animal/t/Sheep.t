
use Test::More tests => 3;
use Test::Output;

BEGIN { use_ok( 'Animal::Sheep' ) }

is( Animal::Sheep->sound, 'Baaah', 'Sheep makes the right sound');
stdout_is( sub { Animal::Sheep->speak } , "A Animal::Sheep goes Baaah!\n", 'Sheep speaks correctly' );

done_testing();


