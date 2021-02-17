
#	Operators in perl
#		Arithmetic Operators
#		Equality Operators
#		Logical Operators
#		Assignment Operators
#		Bitwise Operators
#		Logical Operators
#		Quote-like Operators
#		Miscellaneous Operators

#	Arithmatic:
#	Addition
#		+
#	Subtraction
#		-
#	Multiplication
#		*
#	Division
#		/
#	Modulus (remainder)
#		%
#	Exponent (power)
#		**
$a = 21;
$b = 10;
print "Value of \$a = $a and value of \$b = $b\n";
$c = $a + $b;
print 'Value of $a + $b = ' . $c . "\n";
$c = $a - $b;
print 'Value of $a - $b = ' . $c . "\n";
$c = $a * $b;
print 'Value of $a * $b = ' . $c . "\n";
$c = $a / $b;
print 'Value of $a / $b = ' . $c . "\n";
$c = $a % $b;
print 'Value of $a % $b = ' . $c. "\n";
$a = 2;
$b = 4;
$c = $a ** $b;
print 'Value of $a ** $b = ' . $c . "\n";
print "\n";

#	Numerical Equality:
#	Equal
#		==
#	Not equal
#		!=
#	Not equal (returns -1, 0, or 1)
#		<=>
#	Greater than
#		>
#	Greater than equal to
#		>=
#	Less than
#		<
#	Less than equal to
#		<=
$a = 21;
$b = 10;
print "Value of \$a = $a and value of \$b = $b\n";
if( $a == $b ){
   print "$a == \$b is true\n";
}else{
   print "\$a == \$b is not true\n";
}
if( $a != $b ){
   print "\$a != \$b is true\n";
}else{
   print "\$a != \$b is not true\n";
}
$c = $a <=> $b;
print "\$a <=> \$b returns $c\n";
if( $a > $b ){
	print "\$a > \$b is true\n";
 }else{
    print "\$a > \$b is not true\n";
 }
 if( $a >= $b ){
    print "\$a >= \$b is true\n";
 }else{
    print "\$a >= \$b is not true\n";
}
 if( $a < $b ){
    print "\$a < \$b is true\n";
 }else{
    print "\$a < \$b is not true\n";
}
 if( $a <= $b ){
    print "\$a <= \$b is true\n";
 }else{
    print "\$a <= \$b is not true\n";
}
print "\n";

#	String Equality:
#	Less than
#		lt
#	Greater than
#		gt
#	Greater than equal
#		ge
#	Less than equal
#		le
#	Equal
#		eq
#	Not equal
#		ne
#	Not equal, (-1, 0, or 1)
#		cmp
$a = "abc";
$b = "xyz";
print "Value of \$a = $a and value of \$b = $b\n";
if( $a lt $b ){
   print "\$a lt \$b is true\n";
}else{
    print "\$a lt \$b is not true\n";
}
 if( $a gt $b ){
    print "\$a gt \$b is true\n";
 }else{
    print "\$a gt \$b is not true\n";
}
 if( $a le $b ){
    print "\$a le \$b is true\n";
 }else{
    print "\$a le \$b is not true\n";
}
 if( $a ge $b ){
    print "\$a ge \$b is true\n";
 }else{
    print "\$a ge \$b is not true\n";
}
 if( $a ne $b ){
    print "\$a ne \$b is true\n";
 }else{
    print "\$a ne \$b is not true\n";
 }
 $c = $a cmp $b;
 print "\$a cmp \$b returns $c\n";
print "\n";

#	Assignment operators
#	Simple assignment
#		=
#	Add assign
#		+=
#	Subtract assign
#		-=
#	Multiply assign
#		*=
#	Divide assign
#		/=
#	Modulus assign
#		%=
#	Exponent assign
#		**=
$a = 10;
$b = 20;
print "Value of \$a = $a and value of \$b = $b\n";
$c = $a + $b;
print "After assignment value of \$c = $c\n";
$c += $a;
print "Value of \$c = $c after statement \$c += \$a\n";
$c -= $a;
print "Value of \$c = $c after statement \$c -= \$a\n";
$c *= $a;
print "Value of \$c = $c after statement \$c *= \$a\n";
$c /= $a;
print "Value of \$c = $c after statement \$c /= \$a\n";
$c %= $a;
print "Value of \$c = $c after statement \$c %= \$a\n";
$c = 2;
$a = 4;
print "Value of \$a = $a and value of \$c = $c\n";
$c **= $a;
print "Value of \$c = $c after statement \$c **= \$a\n";
print "\n";

#	Bitwise operators
#	Binary and
#		&
#	Binary or
#		|
#	Binary xor
#		^
#	Binary ones compliement (flip bits)
#		~
#	Binary left shift
#		<<
#	Binary right shift
#		>>
use integer;
$a = 60;
$b = 13;
print "Value of \$a = $a and value of \$b = $b\n";
$c = $a & $b;
print "Value of \$a & \$b = $c\n";
 $c = $a | $b;
 print "Value of \$a | \$b = $c\n";
 $c = $a ^ $b;
 print "Value of \$a ^ \$b = $c\n";
 $c = ~$a;
 print "Value of ~\$a = $c\n";
 $c = $a << 2;
 print "Value of \$a << 2 = $c\n";
 $c = $a >> 2;
 print "Value of \$a >> 2 = $c\n";

#	Logical operators
#	And
#		and
#		&&
#	Or
#		or
#		||
#	Not
#		not
$a = true;
$b = false;
print "Value of \$a = $a and value of \$b = $b\n";
$c = ($a and $b);
print "Value of \$a and \$b = $c\n";
$c=($a &&$b);
print "Value of \$a && \$b = $c\n";
$c = ($a or $b);
print "Value of \$a or \$b = $c\n";
$c = ($a || $b);
print "Value of \$a || \$b = $c\n";
$a = 0;
$c = not($a);
print "Value of not(\$a)= $c\n";
print "\n";


#	Quote-like operators
#		q{} 		(Quote) Enclose a string in single quotes
#		qq{}		(Double Quote) Enclose a string with double quotes
#		qx{}		(Quote Execute) Enclose a string in invent quotes
#		qw{}		(Quote word) Word list (list of single-quoted items)
$a = 10;
$b = q{a = $a};
print "Value of q{a = \$a} = $b\n";
$b = qq{a = $a};
print "Value of qq{a = \$a} = $b\n";
# unix command execution
$t = qx{date};
print "Value of qx{date} = $t\n";
print "\n";


#	Misc operators
#	Binary operator (concatenate strings)
#		.
#	Repetition operator (repeat a string a given number of times)
#		x
#	Range operator 
#		..
#	Auto increment 
#		++
#	Auto decrement
#		--
#	Dereferencing a method or variable from an object or class name
#		->
$a = "abc";
$b = "def";
print "Value of \$a = $a and value of \$b = $b\n";
$c = $a . $b;
print "Value of \$a . \$b = $c\n";
$c = "-" x 3;
print "Value of \"-\" x 3 = $c\n";
@c = (2..5);
print "Value of (2..5) = @c\n";
$a = 10;
$b = 15;
print "Value of \$a = $a and value of \$b = $b\n";
$a++;
$c = $a ;
print "Value of \$a after \$a++ = $c\n";
$b--;
$c = $b ;
print "Value of \$b after \$b-- = $c\n";
print "\n";


