#!/usr/bin/env perl
use strict;
use warnings;
use v5.032;
use File::HomeDir;

my $cmd_str = "ls -gtr";
my $rc;

my $user_home = File::HomeDir->my_home;
say "user_home=($user_home)";
-d $user_home or die "invalid dir, user_home=($user_home): $!\n";

chdir $user_home;

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

