#!/usr/bin/env perl
use strict;
use warnings;
use v5.032;

my @skipper   = qw(blue_shirt hat jacket preserver sunscreen);
my @professor = qw(sunscreen water_bottle slide_rule batteries radio);
my @gilligan  = qw(red_shirt hat lucky_socks water_bottle);

my %var_all = (
	Gilligan  => \@gilligan, 
	Skipper   => \@skipper, 
	Professor => \@professor,
);

check_items_for_all(\%var_all);

sub check_items_for_all {
	my $var_all = shift;
	for my $person (sort keys %{$var_all}) {
		say "person=($person), var_all=(@{$var_all->{$person}})";
		check_required_items($person, $var_all->{$person});
		say "person=($person), var_all=(@{$var_all->{$person}})";
		say "";
	}
}

sub check_required_items { 
	my $who = shift;
	my $items = shift;
	my %whos_items = map { $_, 1 } @{$items};
	my @required = qw(preserver sunscreen water_bottle jacket); 
	my @missing;
	for my $item (@required) {
		unless ( $whos_items{$item} ) { 
			# not found in list
			push @missing, $item;
		} 
	}
	say "who=($who), missing=(@missing)";
	push @{$items}, @missing;
}

