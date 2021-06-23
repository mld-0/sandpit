#!/usr/bin/env perl
use strict;
use warnings;
use v5.032;

my $s = "The black cat climbed the green tree";
my $color  = substr $s, 4, 5;      # black
my $middle = substr $s, 4, -11;    # black cat climbed the
my $end    = substr $s, 14;        # climbed the green tree
my $tail   = substr $s, -4;        # tree
my $z      = substr $s, -4, 2;     # tr

#substr($s, -2, 1) = 'd';	
#say "s=($s)";

my $name = 'fred';
substr($name, 4) = 'dy';         # $name is now 'freddy'
my $null = substr $name, 6, 2;   # returns "" (no warning)

#my $oops = substr $name, 7;      # returns undef, with warning
#say "oops=($oops)";

#my $result = substr($name, -20);
#say "result=($result)";

substr($name, 2, 1) = 'gap';        # (doesn't) raise an exception?
#substr($name, 7) = 'gap';        # raises an exception
say "name=($name)";


#my $result = substr($name, -20, 2);
#say "result=($result)";
say "";

my $x = '1234';
for (substr($x,1,2)) {
    $_ = 'a';   print $x,"\n";    # prints 1a4
    $_ = 'xyz'; print $x,"\n";    # prints 1xyz4
    $x = '56789';
    $_ = 'pq';  print $x,"\n";    # prints 5pq9
}
say "";

$x = '1234';
for (substr($x, -3, 2)) { 
	$_ = 'a';   print $x,"\n";    # prints 1a4, as above
	$x = 'abcdefg';
	print $_,"\n";                # prints f
}
say "";

#	Ongoing: 2021-06-15T22:31:57AEST Explain the difference between:
#$x = '1234567890';
#for (substr($x, 1, 2)) {
#	say "\$_=($_)";
#	$_ = 'a'; say "x=($x)";  # 1a4567890
#	say "\$_=($_)";
#	$_ = 'abc'; say "x=($x)";  # 1abc4567890
#	say "\$_=($_)";
#	$_ = 'abcdef'; say "x=($x)";  # 1abcdef4567890
#}
#say "";
#$x = '1234567890';
#for (my $result = substr($x, 1, 2)) {
#	$result = 'a'; say "x=($x)";  # 1234567890
#	$result  = 'abc'; say "x=($x)";  # 1234567890
#	$result  = 'abcdef'; say "x=($x)"; # 1234567890 
#}
#say "";

$x = '1234567890';
for (substr($x, 1, 2)) {
	$_ = 'a'; say "x=($x)";  # 1a4567890
	$_ = 'abc'; say "x=($x)";  # 1abc4567890
	$_ = 'abcdef'; say "x=($x)";  # 1abcdef4567890
}
say "";

$x = '1234567890';
my $result = substr($x, 1, 2);
$result = 'a'; say "x=($x)";  # 1234567890 
$result  = 'abc'; say "x=($x)";  # 1234567890 
$result  = 'abcdef'; say "x=($x)"; # 1234567890 
say "";

use Data::Alias;
$x = '1234567890';
alias $result = substr($x, 1, 2);
$result = 'a'; say "x=($x)";  # 1a4567890 
$result  = 'abc'; say "x=($x)";  # 1abc4567890 
$result  = 'abcdef'; say "x=($x)"; # 1abcdef4567890 
say "";

$x = '1234567890';
for my $result (substr($x, 1, 2)) {
	$result = 'a'; say "x=($x)";  # 1a4567890
	$result  = 'abc'; say "x=($x)";  # 1abc4567890
	$result  = 'abcdef'; say "x=($x)"; # 1abcdef4567890 
}
say "";



