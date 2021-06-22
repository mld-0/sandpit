#!/usr/bin/env perl
use strict;
use warnings;
use v5.032;
use Module::CoreList;

#	Get hash of modules included with current version of perl 
my $check_version = $];
my %modules_included = %{ $Module::CoreList::version{$check_version} };

say "check_version=($check_version)";

#	Get maximum width of key field in %modules_included
my $key_maxwidth = 0;
foreach my $k (keys %modules_included) { $key_maxwidth = length($k) > $key_maxwidth ? length($k) : $key_maxwidth; }

#	Print each k-v pair in %modules_included
foreach my $k (keys %modules_included) {
	my $v = $modules_included{$k} // "(undef)";
	printf("%-${key_maxwidth}s\t%s\n", $k, $v);
}

