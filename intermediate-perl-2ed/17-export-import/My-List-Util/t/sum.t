
use Test::More;

BEGIN { use_ok( 'My::List::Util' ) }

#	Note that unlike in ch14, calls to shuffle()/sum() are not prefixed with 'My::List::Util::', since those functions are now imported by default

ok( defined &My::List::Util::sum, 'sum() is defined' );

is( sum(1,2,3), 6, 
	'1+2+3 is 6' );

is( sum(qw(1 2 3)), 6, 
	'1+2+3 as strings is 6' );

is( sum(4, -9, 37, 6), 38, 
	'4-9+37+6 is 6' );

is( sum(3.14, 2.2), 5.34, 
	'3.14+2.2 is 5.34' );

is( sum(), undef, 
	'No arguments returns undef' );

is( sum(qw(a b)), undef,
	'All character arguments gives undef' );

is( sum(qw(a b 4 5)), 9, 
	'Mixed character/number args correct');

done_testing();



