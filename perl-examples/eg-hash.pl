#!/usr/bin/env perl
use strict;
use warnings;
use v5.032;

my %var_hash = ('Welcome' => 10, 'to' => 20, 'Geeks' => 80);
#	or
%var_hash = ('Welcome', 10, 'to', 20, 'Geeks', 80);

#say "$var_hash{'Welcome'}";
#say "@var_hash{'Welcome', 'to'}";
#

#foreach (values(%var_hash)) {
#	$_ = 23;
#}
#say %var_hash;
#for (values(%var_hash)) {
#	#$_ = 15;
#}
#$_ = 15;
#say %var_hash;

##	Ongoing: 2021-06-14T15:49:01AEST perl, difference between accessing hash with '$', '%', and '@' (see below):
#say @var_hash{'Welcome'};
#say $var_hash{'Welcome'};
#say %var_hash{'Welcome'};

##for (values(%var_hash)) { $_ = 23; }
#for (%var_hash{keys %var_hash}) { $_ = 23; }
#say %var_hash;

#	Iterate over loop with keys() 
foreach my $k (keys %var_hash) {
	my $v = $var_hash{$k};
	say "k=($k), v=($v)";
}
say %var_hash;

#	Iterate over loop with each() - the previous method with keys() should be prefered
while ( my($k, $v) = each(%var_hash) ) {
	say "k=($k), v=($v)";
}
say %var_hash;
say "";

my $result = exists($var_hash{'Welcome'});
say "result=($result)";
say %var_hash;

my @result = delete(%var_hash{'Welcome', 'to'});
say "result=(@result)";
say %var_hash;
say "";

my $abc = 0;
say defined($abc);


