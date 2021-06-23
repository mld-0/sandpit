use strict;
use warnings;
use v5.032;

#my @var_A = ("abc", "def");
#my $result = reverse(@var_A);
#say "result=($result)";

my %var_B = ( abc => 'a', def => 'b' );

for my $k (keys(%var_B)) {
	my $v = $var_B{$k};
	say "k=($k), v=($v)";
}

my %result = reverse(%var_B);

for my $k (keys(%result)) {
	my $v = $result{$k};
	say "k=($k), v=($v)";
}
