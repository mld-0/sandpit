#!/usr/bin/env perl
use strict;
use warnings;
use v5.032;
use File::HomeDir;
use File::Basename;

my $cmd_str = "ls -gtr";
my $rc;

my $user_home = File::HomeDir->my_home;
say "user_home=($user_home)";
-d $user_home or die "invalid dir, user_home=($user_home): $!\n";

chdir $user_home;

#	Use name of script, $0, with (last) extension removed
(my $scriptname_no_extension = $0) =~ s/\.[^.]+$//;
#say "scriptname_no_extension=($scriptname_no_extension)";

#	Paths to which stdout/stderr will be redirected
my $path_stdout = "/tmp/$scriptname_no_extension.stdout";
my $path_stderr = "/tmp/$scriptname_no_extension.stderr";
say "path_stdout=($path_stdout)";
say "path_stderr=($path_stderr)";

#	Make copies of stdout/stderr so we can restore them later
open my $STDOUT_OLD, '>&', STDOUT or die "Can't save STDOUT_OLD: $!\n";
open my $STDERR_OLD, '>&', STDERR or die "Can't save STDERR_OLD: $!\n";

#	Redirect stdout/stderr to files path_stdout/path_stderr
open STDOUT, '>', $path_stdout or die "Can't write to path_stdout=($path_stdout): $!\n";
open STDERR, '>', $path_stderr or die "Can't write to path_stderr=($path_stderr): $!\n";

#	system() does not capture stdout, it is printed instead. return-code is returned.
$rc = system("$cmd_str");
say "rc=($rc)";
say "";

#	qx/backtick returns stdout from command instead of printing it. return-code can be accessed from variable $?
my $cmd_stdout = qx/$cmd_str/;
#	or
#my $cmd_stdout = `$cmd_str`;
$rc = $?;
say "cmd_stdout=($cmd_stdout)";
say "rc=($rc)";

#	Restore stdout/stderr
open STDOUT, '>&', $STDOUT_OLD or die "Can't restore STDOUT_OLD: $!\n";
open STDERR, '>&', $STDERR_OLD or die "Can't restore STDERR_OLD: $!\n";

say "say something";


#	Alternatively, stdout can be redirected with select(), however this does not redirect output from system(), only output from print/say functions
#open my $outfile, '>', $path_stdout;
#select $outfile;
##	<...>
#select STDOUT;

