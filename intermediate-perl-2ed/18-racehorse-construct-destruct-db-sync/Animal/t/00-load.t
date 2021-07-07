#!perl
use 5.032;
use strict;
use warnings;
use Test::More;

plan tests => 3;

BEGIN {
    use_ok( 'Animal' ) || print "Bail out!\n";
    use_ok( 'Animal::Horse' ) || print "Bail out!\n";
    use_ok( 'Animal::Horse::RaceHorse' ) || print "Bail out!\n";
}

diag( "Testing Animal $Animal::VERSION, Perl $], $^X" );
