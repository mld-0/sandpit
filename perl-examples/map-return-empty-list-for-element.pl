use strict;
use warnings;
use 5.032;

my @numbers = (1..10);
my @squares = map { $_ > 5 ? ($_ * $_) : () } @numbers;
say "squares=(@squares)";

@squares = map { ($_ * $_) } @numbers;
say "squares=(@squares)";

