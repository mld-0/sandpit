#!/usr/bin/env perl
use strict;
use warnings;
use v5.032;

use Animal::Cow;
use Animal::Horse;
use Animal::Sheep;
use Animal::Mouse;

my @animals_list = ( 'Animal::Cow', 'Animal::Horse', 'Animal::Sheep', 'Animal::Mouse' );

foreach my $beast (@animals_list) {
	$beast->speak;
}

