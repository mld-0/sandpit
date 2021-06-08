#!/usr/env/bin perl
use strict;
use warnings;

#	To install Scalar::Util::Numeric module:
#>$		cpan Scalar::Util::Numeric
use Scalar::Util::Numeric qw(isint);

print "Enter (str) var_str:\n";
chomp(my $var_str = <STDIN>);
if ($var_str eq "") {
	die "var_str=($var_str) is empty\n";
}

print "Enter (int) var_int:\n";
chomp(my $var_int = <STDIN>);
if (!isint($var_int)) {
	die "var_int=($var_int) is not int\n";
}

my $result = $var_str x $var_int;

print "var_str=($var_str)\n";
print "var_int=($var_int)\n";
print "result=($result)\n";

