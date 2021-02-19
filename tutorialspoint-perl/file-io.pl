#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=3:
#   }}}1
use strict; 
use warnings;
no warnings 'shadow';
use File::Spec;

my $path_data = $ENV{'mld_data'};
my $path_nums = "$path_data/nums.txt";
print "path_nums=($path_nums)\n";
print "\n";

#	open(), close()
open(DATA, "+<", "$path_nums") or die "Failed to open path_nums=($path_nums), $!\n"; 
while (<DATA>) {
	print "$_";
}
close(DATA) or die "Failed to close path_nums=($path_nums), $!\n";
print "\n";

#	File Open modes
#		< or r 				Read only
#		> or w 				Create, Write, Truncate
#		>> or a 			Write, Append, Create
#		+< or r+ 			Read and Write
#		+> or w+			Read, Write, Create, Truncate
#		+>> or a+ 			Read, Write, Append, Create

#	<FILEHANDLE> Operator
#		in a scalar context, returns a single line from file handle
#		in list context, returns a list of lines from filehandle

#	Read file to list
open(FILE, "+<", "$path_nums") or die "Failed to open path_nums=($path_nums), $!\n";
my @list_nums = <FILE>;
close(FILE);
print @list_nums;
print "\n";

#	getc(FILE)
#		getc returns a single character from the specified filehandle (or stdin by default)

#	read(FILE, scalar, length[, offset])
#		read 'length' characters into variable 'scalar' from given filehandle. offset, if given, specifies number of characters from beginning (or from end for negative value) to begin reading. Return number of characters read, zero at end-of-file, or undef if there is an error

#	print(FILEHANDLE, list)
#		prints evaluated value of 'list' to 'FILEHANDLE', or to the current output filehandle (default STDOUT)

#	rename(previous, new)
#		rename an existing file 'previous' to 'new'

#	unlink(path)
#		delete the file at 'path'

#	Position within file
#	tell(FILEHANDLE)
#		get position (in bytes) of FILEHANDLE, (or currently selected filehandle)
#	seek(FILEHANDLE, POSITION, WHENCE)
#		set position relative to WHENCE

#	File information (-X tests)
my $file = $path_nums;
my (@description, $size);
if (-e $file)
{
push @description, 'binary' if (-B _);
push @description, 'a socket' if (-S _);
push @description, 'a text file' if (-T _);
push @description, 'a block special file' if (-b _);
push @description, 'a character special file' if (-c _);
push @description, 'a directory' if (-d _);
push @description, 'executable' if (-x _);
push @description, (($size = -s _)) ? "$size bytes" : 'empty'; print "$file is ", join(', ',@description),"\n";
}
print "\n";

#	Copy file line-by-line example:
#	#	Copy file example
#	# 	Open file to read
#	open(DATA1, "<file1.txt");
#	# 	Open new file to write
#	open(DATA2, ">file2.txt");
#	# 	Copy data from one file to another. 
#	while(<DATA1>)
#	{
#	    print DATA2 $_;
#	}
#	close( DATA1 );
#	close( DATA2 );


#	sysopen()
#		sysopen(DATA, "file.txt", O_RDWR)
#		sysopen(DATA, "file.txt", O_RDWR|O_TRUNC)

#	sysopen modes
#		O_RDWR 				Read and Write
#		O_RDONLY 			Read Only
#		O_WRONLY 			Write Only
#		O_CREAT 			Create file
#		O_APPEND 			Append file
#		O_TRUNC 			Truncate file
#		O_EXCL 				Stop if file exists
#		O_NONBLOCK 			Non-blocking

