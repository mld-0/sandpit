#!/usr/bin/perl

#	This is a single line comment
print "Hello, world\n";

=begin comment
This is all part of multiline comment.
You can use as many lines as you like
These comments will be ignored by the compiler until the next =cut is encountered. 
=cut

#	Only double quotes interpolate variables, and special characters such as \n
print "Hello, world\n";
print 'Hello, world\n';

my $a = 10;
print "Value of a = $a\n";
print 'Value of a = $a\n';
print "\n\n";

my $var = <<"EOF";
This is the syntax for here document and it will continue until it encounters a EOF in the first line.
This is case of double quote so variable value will be interpolated. For example value of a = $a
EOF

print "$var\n";

$result = "This is \"number\"";
print "$result\n";
print "\$result\n";

