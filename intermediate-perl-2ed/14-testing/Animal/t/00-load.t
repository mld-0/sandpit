#!perl
use 5.032;
use strict;
use warnings;
use Test::More;

plan tests => 5;

BEGIN {
    use_ok( 'Animal' ) || print "Bail out!\n";
    use_ok( 'Animal::Cow' ) || print "Bail out!\n";
    use_ok( 'Animal::Horse' ) || print "Bail out!\n";
    use_ok( 'Animal::Mouse' ) || print "Bail out!\n";
    use_ok( 'Animal::Sheep' ) || print "Bail out!\n";
}

diag( "Testing Animal $Animal::VERSION, Perl $], $^X" );
