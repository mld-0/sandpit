#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=3:
#   }}}1

#	create a reference for any variable, subroutine or value by prefixing it with a backslash as follows:
#		$scalarref = \$foo;
#		$arrayref  = \@ARGV;
#		$hashref = \%ENV;
#		$coderef = \&handler;
#		$globref = \*foo;

$arrayref = [1, 2, ['a', 'b', 'c']];
 
$hashref = { 'Adam' => 'Eve', 'Clyde' => 'Bonnie', };

print "$hashref\n";
print "$arrayref\n";
print "$hashref\n";
print "\n";

#	Dereferencing returns the value from a reference point to the location.
$var = 10;
$p_var = \$var;
print "Reference type in p_var : ", ref($p_var), "\n";
print "Value of \$var is: " , $$p_var, "\n";

@var = (1, 2, 3);
print "Value of \$var is: " , $$p_var, "\n";
$p_var = \@var;
print "Reference type in p_var : ", ref($p_var), "\n";
print "Value of \@var is: " , @$p_var, "\n";
%var = ('key1' => 10, 'key2' => 20);
print "Value of \@var is: " , @$p_var, "\n";
$p_var = \%var;
print "Reference type in p_var : ", ref($p_var), "\n";
print "Value of \%var is: " , %$p_var, "\n";
print "\n";

#	Circular references
#		two references containing reference to each other
my $foo = 100;
$foo = \$foo;
print "Value of foo is : ", $$foo, "\n";
print "\n";

#	References to functions
sub PrintHash {
	my (%hash) = @_;
	foreach $item (%hash) {
		print "Item: $item\n";
	}
}
my %hash = ('name' => 'Tom', 'age' => 19);
my $cref = \&PrintHash;
&$cref(%hash);




