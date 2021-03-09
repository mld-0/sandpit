use strict; 
use warnings;
no warnings 'shadow';

#	Getting path from cli
#my $path_in = $ARGV[0];
#defined $path_file or die "$!\nUsage: $0 <filename>\n";

my $path_in = "list-freds.txt";
defined $path_in or die "$!";

my $path_out = "list-wilmas.txt";
defined $path_out or die "$!";

print "path_in=($path_in)\n";
print "path_out=($path_out)\n";

open(my $fh_in, '<', $path_in) or die "Failed to open path_in=($path_in), $!";
open(my $fh_out, '>', $path_out) or die "Failed to open path_out=($path_out), $!";

foreach $_ (<$fh_in>) {
	$_ =~ s/fred/\0/gi;  # use \0 (nul) as placeholder 
	$_ =~ s/wilma/fred/gi;
	$_ =~ s/\0/wilma/gi;
	print $fh_out $_;
}

