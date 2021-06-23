#!/usr/bin/env perl
use strict;
use warnings;
use v5.032;

#	Usage: 
#	Run script (which will wait until signal recieved), then send signal either with shell kill:
#		kill -<signal> <process-id>
#	Or using perl kill:
#		perl -E 'kill <signal> => <process-id>
#	Where <signal> is one of: 
#		HUP, USR1, USR2, INT

#	Signal handlers
sub my_hup_handler 	{ state $n = 0; say "Caught HUP: $n"; ++$n; }
sub my_usr1_handler { state $n = 0; say "Caught USR1: $n"; ++$n; }
sub my_usr2_handler { state $n = 0; say "Caught USR2: $n"; ++$n; }
sub my_int_handler 	{ say "Caught INT., Exiting"; exit; }

say "Process id \$\$=($$)";

foreach my $signal ( qw(int hup usr1 usr2) ) {
	$SIG{ uc $signal } = "my_${signal}_handler";
}

while (1) {
	sleep 1;
}
