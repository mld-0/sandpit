#!/usr/bin/env perl

#	Get contents of perldoc atan2 as a list of lines. 
#	Contents of a backquote are executed as shell command
@lines = `perldoc -u -f atan2`;
#	For each line, remove any pair of braces preceded with a word character, capitalize the contents, and print the result
foreach (@lines) {
	s/\w<([^>]+)>/\U$1/g;
	print;
}

#	Default variable is used implicitly. That is, the foreach loop above is equivelent to:
#		foreach $_ (@lines) {
#			$_ =~ s/\w<([^>]+)>/\U$1/g;
#			print $_;
#		}

