#!/usr/bin/perl
use strict;
use warnings;

my %gilligan_info = (
	name     => 'Gilligan', 
	hat      => 'White', 
	shirt    => 'Red', 
	position => 'First Mate',
);
my %skipper_info = (
	name     => 'Skipper',
	hat      => 'Black',
	shirt    => 'Blue',
	position => 'Captain',
);

my %mr_howell = (
name => 'Mr. Howell', hat => undef,
shirt => 'White', position => 'Passenger',
);
my @crew = (\%gilligan_info, \%skipper_info, \%mr_howell);

my $format = "%-15s %-7s %-7s %-15s %-15s\n"; 
printf $format, qw(Name Shirt Hat Position Location); 

foreach my $crewmember (@crew) {
	$crewmember->{'location'} = $crewmember->{'name'} =~ /Howell/ ? "The Island Country Club" : "The Island";

	printf $format, 
		$crewmember->{'name'}, 
		$crewmember->{'shirt'}, 
		$crewmember->{'hat'}, 
		$crewmember->{'position'},
		$crewmember->{'location'};
}

