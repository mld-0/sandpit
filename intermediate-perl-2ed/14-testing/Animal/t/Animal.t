use strict;
use warnings;
use v5.032;

use Test::More tests => 5;
use Test::Output;

BEGIN { use_ok('Animal') || print "Unable to load 'Animal'\n"; }

diag("Testing Animal $Animal::VERSION, Perl $], $^X");

#	Check that speak/sound are defined
ok( defined &Animal::speak, 'Animal::speak is defined' );
ok( defined &Animal::sound, 'Animal::sound is defined' );

my $result;
my $at;

#	Check that sound() dies
eval { Animal->sound() } or $at = $@;
like( $at, qr/Subclass must define sound/, 'sound() dies with message' );

eval { Animal->speak() } or $at = $@;
like( $at, qr/Subclass must define sound/, 'speak() dies with message' );

#	<>
#$result = eval { Animal->speak() } or $at = $@;
#print "at=($at)\n";
#print "result=($result)\n";


#	Ongoing: 2021-07-04T21:38:37AEST perl, intermediate-perl-2ed, 14-02, use of Foofle subclass, defined in block, works, but not when called inside is() testing function?
#{ 
#	package Foofle;
#	use parent qw(Animal);
#	sub sound { return 'foof' }
#	is( Foofle->speak, "A Foofle goes foof!\n", 'Animal subclass successfully implements speak()');
#}

