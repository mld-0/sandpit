#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=3:
#   }}}1
use strict; 
use warnings;
no warnings 'shadow';

#	Open directory
#	opendir DIRHANDLE, EXPR 

#	read directory
#	readdir DIRHANDLE

#	position pointer to beginning
#	rewinddir DIRHANDLE

#	return current position 
#	telldir DIRHANDLE

#	point pointer to POS inside dir
#	seekdir DIRHANDLE, POS

#	close dir
#	closedir DIRHANDLE


#	List files in dir
my $path_data = $ENV{'mld_data'};
my $path_nums = "$path_data/nums.txt";
my $path_example = "$path_data/example";

my @example_files_list = glob( "$path_example/*" );
print "Files in path_example=($path_example)\n";
foreach (@example_files_list) {
	print $_ . "\n";
}
print "\n";


#	List files using opendir
#		includes '.' and '..'
opendir(DIRHAN, "$path_example") or die "Couldn't open path_example=($path_example), $!\n";
while (my $loop_file = readdir DIRHAN) {
	print "$loop_file\n";
}
closedir(DIRHAN);
print "\n";

#	Create directory
my $path_tmp = "/tmp";
my $path_new_dir = "$path_tmp/perl-example-new-dir";
mkdir($path_new_dir) or die "Failed to create path_new_dir=($path_new_dir), $!\n";
print "Created path_new_dir=($path_new_dir)\n";

#	Remove directory
rmdir($path_new_dir) or die "Failed to remove path_new_dir=($path_new_dir), $!\n";
print "Removed path_new_dir=($path_new_dir)\n";

#	Change directory
chdir($path_tmp) or die "Failed to chdir path_tmp=($path_tmp), $!\n";
print "chdir path_tmp=($path_tmp)\n";





