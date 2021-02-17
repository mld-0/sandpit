#!/usr/bin/perl
#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=3:
#   }}}1
use strict;
use warnings;
#	Hide warning about repeated use of 'my' for variable of same name
no warnings 'shadow';

my $a = 10;
# check the boolean condition using if statement 
if( $a < 20 ){
     printf "a is less than 20\n";
 }
print "value of a is : $a\n";

my $a = "";
# check the boolean condition using if statement 
if ( $a ) {
	printf "a has a true value\n"; 
}
print "value of a is : $a\n";
print "\n";

$a = 100;
# check the boolean condition using if statement 
if ($a == 20) {
	printf "a has a value which is 20\n"; 
}
elsif ($a == 30) {
	printf "a has a value which is 30\n"; 
} else {
	printf "a has a value which is $a\n"; 
}
print "\n";

$a = 20;
# check the boolean condition using unless statement 
unless( $a < 20 ) {
     printf "a is not less than 20\n";
}
print "value of a is : $a\n";
print "\n";

$a = 20;
# check the boolean condition using if statement 
unless( $a == 30 ){
	printf "a has a value which is not 20\n"; 
} elsif( $a == 30 ) {
	printf "a has a value which is 30\n"; 
} else {
	printf "a has a value which is $a\n"; 
}
print "\n";

#	requires Switch module
#	use Switch;
#	 switch(argument){
#	    case 1 		{ print "number 1" }
#	    case "a"	{ print "string a" }
#	    case [1..10,42] {print "number in list" }
#	    case (\@array) { print "number in list"}
#	    else 			{ print "else" }
#	}

#	? : operator
my $name = "Ali";
my $age = 10;
my $status = ($age > 60 ) ? "A senior citizen" : "Not a senior citizen"; 
print "$name is - $status\n";


