#!/usr/bin/env perl
use strict;
use warnings;
use v5.032;

use Animal::Horse::RaceHorse;

my ($runner, $mover);
$runner = Animal::Horse::RaceHorse->named('Billy Boy');
$runner->won;
print $runner->name, ' has standings ', $runner->standings, ".\n";
$mover = Animal::Horse::RaceHorse->named('Lil Step');
$mover->won;
$mover->placed;
$mover->lost;
print $mover->name, ' has standings ', $mover->standings, ".\n";

