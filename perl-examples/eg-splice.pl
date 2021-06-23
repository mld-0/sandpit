#!/usr/bin/env perl
use strict;
use warnings;
use 5.032;

my @a = (1, 2, 3, 4);
say "a=(@a)";
say "";

my $result = splice(@a, -1);
say "result=($result)";
say "a=(@a)";
say "";

$result = splice(@a, @a, 0, $result);
say "result=($result)";
say "a=(@a)";
say "";

#$result = splice(@a, 0);
#say "result=($result)";
#say "a=(@a)";
#say "";

say "a=(@a)";

