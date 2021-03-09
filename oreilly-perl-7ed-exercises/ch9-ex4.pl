use strict; 
use warnings;
no warnings 'shadow';

@ARGV = ('ch9-ex1.pl', 'ch9-ex2.pl');

#	Create dict of files passed as arguments
my %update_files;
foreach (@ARGV) {
	$update_files{$_} = 1;
}

#	Remove files from dict if they contain copyright line 
while (<>) {
	if (/^## Copyright/) {
		print "skip ARGV=($ARGV)\n";
		delete $update_files{$ARGV};
	}
}

#	Exit if update_files is empty
if (! %update_files) {
	die "No files remaining to be updated\n";
}

#	Update those files remaining
#	<> operates on STDIN only if the array @ARGV is empty
@ARGV = sort keys %update_files;
$^I = ".bak";  # make backups
while (<>) {
	if (/\A#!/) {  # is it the shebang line?
		$_ .= "## Copyright (C) 20XX by Yours Truly\n";
		print STDOUT "Update $ARGV\n";
	}
	print $_;  
}

