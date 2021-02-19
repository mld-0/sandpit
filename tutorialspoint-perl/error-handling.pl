#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=3:
#   }}}1

use strict; 
use warnings;
no warnings 'shadow';

use Carp;
use Carp qw(cluck);

my $path_data = $ENV{'mld_data'};
my $path_nums = "$path_data/nums.txt";
print "path_nums=($path_nums)\n";
print "\n";

#	[or] die
#		exit with error if operation fails
open(DATA, "+<", "$path_nums") or die "Failed to open path_nums=($path_nums), $!\n"; 
while (<DATA>) {
	print "$_";
}
close(DATA) or die "Failed to close path_nums=($path_nums), $!\n";
print "\n";

#	warn
#		output to stderr, and continue
chdir('/tmp') or warn "Failed to chdir /tmp $!\n";


#	carp()
#		print message to stderr along with line number
sub func_carp {
	carp "Example carp message\n";
}
func_carp();

#	cluck()
#		print message to stderr along with stack trace of modules leading to cluck call
sub func_cluck {
	cluck "Example cluck message\n";
}
func_cluck();

#	croak()
#		equivelent to carp and then die

#	confess()
#		equivelent to cluck and then die


