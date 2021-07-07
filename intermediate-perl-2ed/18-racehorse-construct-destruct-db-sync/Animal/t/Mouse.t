
use Test::More tests => 3;
use Test::Output;

BEGIN { use_ok( 'Animal::Mouse' ) }

is( Animal::Mouse->sound, 'Squeak', 'Mouse makes the right sound');
stdout_is( sub { Animal::Mouse->speak } , "A Animal::Mouse goes Squeak!\n(but you can barely hear it)\n", 'Mouse speaks correctly' );

done_testing();



