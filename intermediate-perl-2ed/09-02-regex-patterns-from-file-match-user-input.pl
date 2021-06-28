#!/usr/bin/env perl
use strict;
use warnings;
use v5.032;

my $path_regex_patterns = "regex-patterns.txt";
my @regex_patterns;

#	Ongoing: 2021-06-28T16:17:54AEST perl, intermediate-perl-2ed, 09-02-regex-patterns-from-file-match-user-input.pl, differences between regex read from file as qr/$_/ vs $_ 

#	Read regex from path_regex_patterns to @regex_patterns
open my $fh_regex, '<', $path_regex_patterns or die "Can't open path_regex_patterns=($path_regex_patterns): $!\n";
while (readline($fh_regex)) {
	chomp;
	my $loop_regex = eval { qr/$_/ } or do { warn "Invalid pattern \$_=($_): $@\n" };
	say ref($loop_regex);

	#	Both produce the same results? Which is 'correct', what is an example where they do differ?
	push @regex_patterns, $loop_regex;
	#push @regex_patterns, $_;

}
close $fh_regex or die "Can't close path_regex_patterns=($path_regex_patterns): $!\n";
say "regex_patterns=(@regex_patterns)";
say "";

#	Get user input search_str, or use default value
my $search_str = '';
say "Enter search_str:";
$search_str = <STDIN>;
if (!$search_str) {
	$search_str = "Mary-Anne\nBububububble-cocoanet\nThe Skipper\nquantile indubiously therefore\nbring it around town (town)\n";
	say "Use default search_str=($search_str)";
	say "";
}

#	Ongoing: 2021-06-28T16:18:33AEST perl, intermediate-perl-2ed, 09-02-regex-patterns-from-file-match-user-input.pl, writing a loop of the form while (my ($i, $line) = each(split("\n", $var_str))) {...} (since apparently split() is being evaluated in scalar context here?

#	Alternative approach to line numbering, using $. -> open filehandle to \$search_str and read that?

#	Find and print matches of @regex_patterns items in (lines of) $search_str with line numbers
my $loop_i = 0;
foreach my $loop_line (split("\n", $search_str)) {
	#say "\$_=($_)";
	foreach my $loop_regex (@regex_patterns) {
		#say "loop_regex=($loop_regex)";

		if ($loop_line =~ /$loop_regex/) {
			say "Match line $loop_i ($loop_line), regex=($loop_regex)";

			#	Print all capture groups (if any)
			if (scalar @{^CAPTURE} > 0) {
				print "\tAll Capture groups: ";
				foreach (@{^CAPTURE}) {
					print "($_), ";
				} say "";
			}

			#	Print all named capture groups (if any)
			if (scalar(keys %-) > 0) {
				print "\tNamed capture grousp: ";
				foreach my $matches_key (keys %-) {
					print "matches_key=($matches_key), ";
					print "matches_list=(@{$-{$matches_key}}), ";
				} say "";
			}

		}
	}
	say "";
	$loop_i++;
}

