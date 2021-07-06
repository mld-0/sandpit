#!perl
use 5.032;
use strict;
use warnings;
use Test::More;

plan tests => 1;

BEGIN {
    use_ok( 'My::List::Util' ) || print "Bail out!\n";
}

diag( "Testing My::List::Util $My::List::Util::VERSION, Perl $], $^X" );