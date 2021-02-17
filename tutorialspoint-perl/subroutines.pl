#!/usr/local/bin/perl
#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=3:
#   }}}1

#	Perl uses the terms subroutine, method and function interchangeably.
#	(or so you say?)

# 	Function definition
sub Hello{
   print "Hello, World!\n";
}
# 	Function call
Hello();
print "\n";


#	Arguments are found in the array @_. Thus the first argument to the function is in $_[0], the second is in $_[1], and so on.
sub Average {
	# get total number of arguments passed. 
	my $n = scalar(@_);
	my $sum = 0;
	foreach $item (@_){
		$sum += $item;
	}
	my $average = $sum / $n;
	return $average
}
my $avg = Average(10, 20, 30);
print "avg=($avg)\n";
print "\n";


#	Passing list to subroutine
sub PrintList {
	my $arg_a = $_[0];
	shift(@_);
	my @arg_b = @_;
    print "arg_a=($arg_a), arg_b=(@arg_b)\n";
}
my $a = 10;
my @b = (1, 2, 3, 4);
PrintList($a, @b);
print "\n";


#	Passing hash to subroutine
sub PrintHash {
	my (%hash) = @_;
	foreach my $key ( keys %hash ) { 
		my $value = $hash{$key};
		print "key=($key), value=($value)\n";
	}
}
%hash = ('name' => 'Tom', 'age' => 19);
PrintHash(%hash);
print "\n";


#	Function scope - global and local variable
$string = "Hello, World!";
sub PrintHello {
	my $string = "Hello, Perl!";
	print "Inside the function $string\n";
}
PrintHello();
print "Outside the function $string\n";
print "\n";

#	my vs local function variables
#		'my' creates a new variable, 'local' temporarily amends the value of a variable.
#		local variable is visible to callee function
$string = "Hello, World!";
sub PrintHello_Local{
	local $string = "Hello, Perl!";
	print "Inside PrintHello_Local Print $string\n";
	PrintMe();
}
sub PrintHello_My{
	my $string = "Hello, Perl!";
	print "Inside PrintHello_My Print $string\n";
	PrintMe();
}
sub PrintMe{
	print "Inside PrintMe Print $string\n";
}
PrintHello_Local();
print "Outside the function $string\n";
PrintHello_My();
print "Outside the function $string\n";
print "\n";

#	state variable
#		maintain their state and they do not get reinitialized upon multiple calls of the subroutines.
use feature 'state';
sub PrintCount {
	state $count = 0; # initial value
	print "Value of counter is $count\n";
	$count++; 
}
 for (1..5) {
    PrintCount();
}


#	Subroutine Call Context	
#		The context of a subroutine or statement is defined as the type of return value that is expected. This allows you to use a single function that returns different values based on what the user is expecting to receive.	
#		For example, the following localtime() returns a string when it is called in scalar context, but it returns a list when it is called in list context.
my $datestring = localtime(time);
($sec,$min,$hour,$mday,$mon, $year,$wday,$yday,$isdst) = localtime(time);

#	Continue: 2021-02-18T00:56:43AEDT overloading function return value/type 


