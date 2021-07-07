
use Test::More tests => 3;
use Test::Output;

BEGIN { use_ok('Animal::Horse::RaceHorse') }

is( Animal::Horse::RaceHorse->sound, 'Neigh', 'RaceHorse makes the right sound');
stdout_is( sub { Animal::Horse::RaceHorse->speak } , "A Animal::Horse::RaceHorse goes Neigh!\n", 'Horse speaks correctly' );

#my $runner = Animal::Horse::RaceHorse->named('Billy Boy');
#$runner->won;
#print $runner->name, 'has standings ', runner->standings, ".\n";

#	TODO: 2021-07-07T18:00:27AEST perl, intermediate-perl-2ed, 18, tests for RaceHorse -> testing reading/writing valuesfrom database

my ($runner, $mover);
$runner = Animal::Horse::RaceHorse->named('Billy Boy');
$runner->won;
print $runner->name, ' has standings ', $runner->standings, ".\n";
$mover = Animal::Horse::RaceHorse->named('Lil Step');
$mover->won;
$mover->placed;
$mover->lost;
print $mover->name, ' has standings ', $mover->standings, ".\n";

done_testing();

