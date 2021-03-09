

print "Enter input (ctrl-d to terminate)\n";
my @var_lines = <STDIN>;
chomp @var_lines;
print "\n";

foreach $loop_line (reverse @var_lines) {
	print "$loop_line\n";
}
print "\n";

#	Perl ... doesn't support 'backwards' ranges?
#print ($#var_lines .. 0) . "\n";
#foreach $loop_line (@var_lines[0 .. $#var_lines]) {
#	print "$loop_line";
#}

for (my $i = $#var_lines; $i >= 0; $i--) {
	print "@var_lines[$i]\n";
}
