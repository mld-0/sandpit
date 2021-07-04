
use Test::More tests => 3;
use Test::Output;

BEGIN { use_ok( 'Animal::Cow' ) }

is( Animal::Cow->sound, 'Moo', 'Cow makes the right sound');
stdout_is( sub { Animal::Cow->speak } , "A Animal::Cow goes Moo!\n", 'Cow speaks correctly' );

done_testing();

