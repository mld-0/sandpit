#!/usr/bin/env perl
use strict;
use warnings;
use v5.032;

#	Origional:
#		The use of {} instead of () results in anonymous hashes, <>
#my %passenger_1 = {
#	name		=> 'Ginger',
#	age			=> 22,
#	occupation	=> 'Movie Star',
#	real_age	=> 35,
#	hat			=> undef,
#};
#my %passenger_2 = {
#	name		=> 'Mary Ann',
#	age			=> 19,
#	hat			=> 'bonnet',
#	favourite_food => 'corn',
#};

my %passenger_1 = (
	name		=> 'Ginger',
	age			=> 22,
	occupation	=> 'Movie Star',
	real_age	=> 35,
	hat			=> undef,
);
my %passenger_2 = (
	name		=> 'Mary Ann',
	age			=> 19,
	hat			=> 'bonnet',
	favourite_food => 'corn',
);

my @passengers = (\%passenger_1, \%passenger_2);

