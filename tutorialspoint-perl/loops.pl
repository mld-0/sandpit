
my $a = 10;
 # while loop execution
while( $a < 20 ) {
	printf "Value of a: $a\n";
	$a = $a + 1; 
}
print "\n";

$a = 5;
 # until loop execution
until( $a > 10 ) {
	printf "Value of a: $a\n";
	$a = $a + 1; 
}
print "\n";

# for loop execution
for( $a = 10; $a < 20; $a = $a + 1 ){
	print "value of a: $a\n"; 
}
print "\n";

@list = (2, 20, 30, 40, 50);
# foreach loop execution
foreach $a (@list) {
	print "value of a: $a\n"; 
}
print "\n";

$a = 10;
 # do...while loop execution
do {
	printf "Value of a: $a\n";
    $a = $a + 1;
} while( $a < 20 );
print "\n";

my $a = 0;
my $b = 0;
 # outer while loop
 while($a < 3) {
    $b = 0;
    # inner while loop
    while( $b < 3 ) {
		print "value of a = $a, b = $b\n";
		$b = $b + 1; 
	}
	$a = $a + 1;
    print "Value of a = $a\n";
}
print "\n";

#	Loop control statements:
#	next [label]
#		skip remainder of body and immediately retest loop condition before reiteraterating
#	last [label]
#		terminate loop and jump to statement immediately following loop
#	continue
#		always executed just before the loop condition is to be evaluated again
#	redo
#		restart loop block, without evaluating continue block
#	goto
#		goto label
#		goto expr
#		goto &name
#		bad bad bad bad bad

#	next example
$a = 10;
 while( $a < 20 ){
    $a = $a + 1;
	if( $a == 15) {
		next;
	}
    print "value of a: $a\n";
}
print "\n";

#	next with labels INNER, OUTER
$a = 0;
OUTER: while( $a < 4 ){
   $b = 0;
   print "value of a: $a\n";
   INNER:while ( $b < 4) {
      if( $a == 2){
			$a = $a + 1;
			next OUTER; 
		}
		$b = $b + 1;
		print "Value of b : $b\n";
	}
	$a = $a + 1; 
}
print "\n";

#	last example
 $a = 10;
 while( $a < 20 ){
	if( $a == 15) {
		last;
	}
    print "value of a: $a\n";
    $a = $a + 1;
}
print "\n";

#	last with labels INNER, OUTER
$a = 0;
 OUTER: while( $a < 4 ){
    $b = 0;
    print "value of a: $a\n";
    INNER:while ( $b < 4){
       if( $a == 2){
           # terminate outer loop
           last OUTER;
       }
       $b = $b + 1;
       print "Value of b : $b\n";
    }
    $a = $a + 1;
}
print "\n";

#	continue example, foreach loop
@list = (1, 2, 3, 4, 5);
 foreach $a (@list){
    print "Value of a = $a\n";
 } continue {
    last if $a == 4;
 }
print "\n";


#	redo example
$a = 0;
while($a < 10){
	if( $a == 5 ){
		$a = $a + 1;
		redo; 
	}
    print "Value of a = $a\n";
 } continue {
$a = $a + 1; 
}
print "\n";

#	loop using goto
$a = 10;
LOOP:do {
	if( $a == 15){
 		$a = $a + 1;
		goto LOOP;
	}
	print "Value of a = $a\n";
     $a = $a + 1;
} while( $a < 20 );
print "\n";

