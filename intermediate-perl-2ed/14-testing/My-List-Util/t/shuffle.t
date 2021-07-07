
use Test::More;

BEGIN { use_ok( 'My::List::Util' ) }


ok( defined &My::List::Util::shuffle, 'shuffle() is defined' );

{
my @shuffled = My::List::Util::shuffle();
is( scalar(@shuffled), 0, 
	'No args returns an empty list');
}

{
my @array = 1..10;
my @shuffled = My::List::Util::shuffle(@array);
is( scalar(@array), scalar(@shuffled), 
	'The output list is the same size');
#	Ongoing: 2021-07-04T20:55:04AEST perl, intermediate-perl-2ed, 14-01, testing shuffle(), dealing with (extremely unlikely) case, where (random) shuffling of the list results in the origional list
isnt( "@array", "@shuffled", 
	'The list is shuffled' );
}

done_testing();

