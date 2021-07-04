
use Test::More tests => 3;
use Test::Output;

BEGIN { use_ok( 'Animal::Horse' ) }

is( Animal::Horse->sound, 'Neigh', 'Horse makes the right sound');
stdout_is( sub { Animal::Horse->speak } , "A Animal::Horse goes Neigh!\n", 'Horse speaks correctly' );

done_testing();


