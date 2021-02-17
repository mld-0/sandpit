#!/usr/bin/perl
#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=3:
#   }}}1
use strict;
use warnings;
#	Hide warning about repeated use of 'my' for variable of same name
no warnings 'shadow';

#	scalars
#		prefixed by $
#		either a number, string, or reference

#	arrays
#		prefixed by @
#		ordered list of scalars

#	hashes
#		prefixed with %
#		unordered sets of key/value pairs (dictionaries)

#	numeric literals
my $var_int = 1234;
my $var_nint = -100;
my $var_scientific = 16.12E14;
my $var_hex = 0xffff;

#	String Literals
#	\\ 		Backslash
#	\' 		Single quote \" Double quote
#	\a 		Alert or bell
#	\b 		Backspace
#	\f 		Form feed
#	\n 		Newline
#	\r 		Carriage return
#	\t 		Horizontal tab
#	\v 		Vertical tab
#	\0nn 	Creates Octal formatted numbers
#	\xnn	Creates Hexideciamal formatted numbers
#	\cX 	Controls characters, x may be any character
#	\u 		Forces next character to uppercase
#	\l 		Forces next character to lowercase
#	\U 		Forces all following characters to uppercase
#	\L 		Forces all following characters to lowercase
#	\Q 		Backslash all following non-alphanumeric characters \E End \U, \L, or \Q

#	strings with single and double quotations
# This is case of interpolation.
my $str = "Welcome to \ntutorialspoint.com!"; 
print "$str\n";
# This is case of non-interpolation.
my $str = 'Welcome to \ntutorialspoint.com!'; 
print "$str\n";
# Only W will become upper case.
my $str = "\uwelcome to tutorialspoint.com!"; 
print "$str\n";#
# Whole line will become capital.
my $str = "\UWelcome to tutorialspoint.com!"; 
print "$str\n";
# A portion of line will become capital. 
my $str = "Welcome to \Ututorialspoint\E.com!"; 
print "$str\n";
# Backsalash non alpha-numeric including spaces. 
my $str = "\QWelcome to tutorialspoint's family"; 
print "$str\n";
print "\n";

#	Scalars:
#	int
my $age = 25;
#  string
my $name = "John Paul";
#  float
my $salary = 1445.50;
#	say is an alternative to print, which includes a trailing newline
use feature qw(say);
say "Age = $age";
say "Name = $name";
say "Salary = $salary";
print "\n";

#	Arrays:
my @ages = (25, 30, 40);
my @names = ("John Paul", "Lisa", "Kumar");

#	iterate over values in multiple arrays - (unlike zip) uses longest array
use List::MoreUtils qw( each_array );
my $iter = each_array(@ages, @names);
while (my ($loop_age, $loop_name) = $iter->()) {
	print "loop_age=($loop_age), loop_name=($loop_name)\n";
}
print "\n";

#use List::MoreUtils qw( each_array );
#my $iter = each_array(@ages, @names);
#while (my ($loop_age, $loop_name) = $iter->()) {
#for zip(@ages, @names) -> $loop_age, $loop_name {
#	print "loop_age=($loop_age), loop_name=($loop_name)\n";
#}


#	Hash:
my %var_data = ('John Paul', 45, 'Lisa', 30, 'Kumar', 40);
#	Iterate over key,value in hash
while ((my $key, my $value) = each(%var_data)) {
	print "key=($key), value=($value)\n";
}
print "\n";
print "\$var_data{'John Paul'} = $var_data{'John Paul'}\n"; 
print "\$var_data{'Lisa'} = $var_data{'Lisa'}\n";
print "\$var_data{'Kumar'} = $var_data{'Kumar'}\n";
print "\n";

#	Scalar operators
# 	concatenate strings '.'
my $str = "hello" . "world";  
#	add numbers '+'
my $num = 5 + 10;
#	multiply numbers '*'
my $mul = 4 * 5;
#	Concatenate string and number '.'
my $mix = $str . $num;
print "str = $str\n";
print "num = $num\n";
print "mix = $mix\n";

#	heredoc
print <<EOF;
This is
a multiline
string
EOF
print "\n";

#	v-strings, 
my $smile  = v9786;
my $foo    = v102.111.111;
my $martin = v77.97.114.116.105.110;
print "smile = $smile\n";
print "foo = $foo\n";
print "martin = $martin\n";
print "\n";

print "File name ". __FILE__ . "\n"; 
print "Line Number " . __LINE__ ."\n"; 
print "Package " . __PACKAGE__ ."\n";


#	ARRAYS:
#	{{{
my @array = (1, 2, 'Hello');
my @array = qw/This is an array/;

#	Sequential values, '..' is the range operator
my @var_10 = (1..10);
my @var_20 = (10..20);
my @var_abc = ('a'..'z');
print "@var_10\n";  # Prints numbers from 1 to 10
print "@var_20\n";  # Prints numbers from 10 to 20
print "@var_abc\n"; # Prints chars from a to z
print "\n";

#	Size of an array
my @array = (1,2,3);
print "Size: ",scalar @array,"\n";
print "\n";


#	Adding and removing array elements
#		push(@array, list)
#			pushes the values of the list onto the end of the array
#		pop(@array)
#			pops off and returns the last element of the array
#		shift(@array)
#			removes and returns first element of the array
#		unshift(@array, list)
#			prepend the values of list to the start of array, returning number of elements in new array

# create a simple array
my @coins = ("Quarter","Dime","Nickel"); 
print "1. \@coins = @coins\n";
# add one element at the end of the array 
push(@coins, "Penny");
print "2. \@coins = @coins\n";
# add one element at the beginning of the array 
unshift(@coins, "Dollar");
print "3. \@coins = @coins\n";
# remove one element from the last of the array. 
pop(@coins);
print "4. \@coins = @coins\n";
# remove one element from the beginning of the array. 
shift(@coins);
print "5. \@coins = @coins\n";
print "\n";

#	Array slices:
my @days = qw/Mon Tue Wed Thu Fri Sat Sun/;
print "@days[3,4,5]\n";
print "@days[3..5]\n";
print "\n";

#	splice(@array, offset[, length, list])
#		remove the elements of @ARRAY designated by OFFSET and LENGTH, and replaces them with LIST, if specified. Finally, it returns the elements removed from the array.
my @nums = (1..10);
print "Before - @nums\n";
splice(@nums, 5, 5, 21..25);
print "After - @nums\n";
print "\n";

#	split(pattern[, expr[, limit]])
#		splits a string into an array of strings, and returns it. If LIMIT is specified, splits into at most that number of fields. If PATTERN is omitted, splits on whitespace. Following is the example:
my $var_string = "Rain-Drops-On-Roses-And-Whiskers-On-Kittens"; 
my $var_names = "Larry,David,Roger,Ken,Michael,Tom";
my @list_string = split('-', $var_string); 
my @list_names = split(',', $var_names);
print "@list_string\n";
print "@list_names\n";
print "\n";

#	join(expr, @list)
#		join the seperate strings of list into a single string with fields seperated by the values of expr
# define Strings
my $var_string = "Rain-Drops-On-Roses-And-Whiskers-On-Kittens"; $var_names = "Larry,David,Roger,Ken,Michael,Tom";
# transform above strings into arrays. @string = split('-', $var_string); @names = split(',', $var_names);
my $string1 = join( '-', @list_string );
my $string2 = join( ',', @list_names );
print "$string1\n";
print "$string2\n";
print "\n";

#	sorting arrays
#	sort([subroutine], @list)
#		sorts the elements of an array according to ASCII 
# define an array
my @foods = qw(pizza steak chicken burgers); 
print "Before: @foods\n";
# sort this array
my @foods = sort(@foods);
print "After: @foods\n";
print "\n";

#	Associative sort
my @foods = qw(pizza steak chicken burgers); 
my @nums = (1..@foods);
#	use cmp to sort strings, <=> to sort numbers
my @idx = sort { $foods[$a] cmp $nums[$b] } 0 .. $#foods;
@foods = @foods[@idx];
@nums = @nums[@idx];
print "@foods\n";
print "@nums\n";
print "\n";

# 	$[ variable
# 		First index of all ararys (default 0)

my @odd = (1,3,5);
my @even = (2, 4, 6);
my @numbers = (@odd, @even);
print "numbers=(@numbers)\n";
print "\n";
#	}}}

#	HASHES:
#	{{{
#	denoted by '%'
#	A hash can be defined as a list
my %data = ('John Paul', 45, 'Lisa', 30, 'Kumar', 40);
#	or using the notation
%data = ('John Paul' => 45, 'Lisa' => 30, 'Kumar' => 40);
#	Or value by value
%data = ();
$data{'John Paul'} = 45;
$data{'Lisa'} = 30;
$data{'Kumar'} = 40;
print "\$data{'John Paul'} = $data{'John Paul'}\n"; 
print "\$data{'Lisa'} = $data{'Lisa'}\n";
print "\$data{'Kumar'} = $data{'Kumar'}\n";
print "\n";

while ((my $key, my $value) = each(%data)) {
	print "key=($key), value=($value)\n";
}
print "\n";

#	Preceding keys with '-' removes need for quotes, however keys must be specified with '-'
%data = (-JohnPaul => 45, -Lisa => 30, -Kumar => 40);
print "\$data{'-John Paul'} = $data{'-JohnPaul'}\n"; 
print "\$data{'-Lisa'} = $data{'-Lisa'}\n";
print "\$data{'-Kumar'} = $data{'-Kumar'}\n";
print "\n";

#	hash slices
%data = ('John Paul' => 45, 'Lisa' => 30, 'Kumar' => 40);
my @data_array = @data{'John Paul', 'Kumar'};
print "data_array=(@data_array)\n";
print "\n";

#	keys of hash
my @data_keys = keys %data;
print "data_keys=(@data_keys)\n"; 
print "\n";

#	Existance of key in hash
if (exists($data{'Lisa'})) { 
	print "Lisa is $data{'Lisa'} years old\n";
} else {
	print "Lisa not found";
}
print "\n";

#	Length of hash
my %data = ('John Paul' => 45, 'Lisa' => 30, 'Kumar' => 40);
my @data_keys = keys %data;
my $data_len = @data_keys;
print "data_len=($data_len)\n";

#	Add element to hash
$data{'Ali'} = 55;
my @data_keys = keys %data;
my $data_len = @data_keys;
print "data_len=($data_len)\n";

#	Delete element from hash
delete $data{'Ali'};
my @data_keys = keys %data;
my $data_len = @data_keys;
print "data_len=($data_len)\n";
print "\n";
#	}}}


