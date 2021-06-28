#!/usr/bin/env perl
use strict;
use warnings;
use v5.032;
use Regexp::Assemble;

my $path_regex_patterns = "regex-patterns.txt";
my @regex_patterns;

#	Ongoing: 2021-06-28T18:41:10AEST perl, intermediate-exercies-2ed, 09-03, Combining qr/$_/ elements with Regexp::Assemble produces mismatched parenthesis error (each indervidual regex is valid), problem does not occur when combining $_ elements. Note - 'answer' to 09-03 uses $_ instead of qr/$_/ as well, while 'answer' to 09-02 does use qr/$_/

#	Read regex from path_regex_patterns to @regex_patterns
open my $fh_regex, '<', $path_regex_patterns or die "Can't open path_regex_patterns=($path_regex_patterns): $!\n";
while (readline($fh_regex)) {
	chomp;
	my $loop_regex = eval { qr/$_/ } or do { warn "Invalid pattern \$_=($_): $@\n" };
	#	Both produce the same results? Which is 'correct', what is an example where they do differ?
	#push @regex_patterns, $loop_regex;
	push @regex_patterns, $_;
}
close $fh_regex or die "Can't close path_regex_patterns=($path_regex_patterns): $!\n";
say "regex_patterns=(@regex_patterns)";
say "";

#	Combine each item in @regex_patterns into $regex_assembled
my $regex_assembled = Regexp::Assemble->new;
for (@regex_patterns) {
	$regex_assembled->add($_);
}
say "regex_assembled->re=($regex_assembled->re)";

#	Get user input search_str, or use default value
my $search_str = '';
say "Enter search_str:";
$search_str = <STDIN>;
if (!$search_str) {
	$search_str = "Mary-Anne\nBububububble-cocoanet\nThe Skipper\nquantile indubiously therefore\nbring it around town (town)\n";
	say "Use default search_str=($search_str)";
	say "";
}

#	Find and print matches of @regex_patterns items in (lines of) $search_str with line numbers
my $loop_i = 0;
foreach my $loop_line (split("\n", $search_str)) {
	#say "\$_=($_)";

	my $loop_regex = $regex_assembled->re;
	if ($loop_line =~ /$loop_regex/) {
		say "Match line $loop_i ($loop_line), regex=($regex_assembled)";

		#	Ongoing: 2021-06-28T18:21:03AEST perl, intermediate-exercises-2ed, 09-03-assemble-combine-regex-patterns-from-file-user-input.pl, Regex capture variables: @{^CAPTURE} and %- behave differently from 09-02, combining regex items from list with Regexp::Assemble results in empty values when iterating over both these variables, and in the case of %-, every capture group having a key in the hash even when the corresponding list contains no (match) values <- Our 'solution' is checking the existance of each value/list before attempting to print it.

		#	Print all capture groups (if any)
		if (scalar @{^CAPTURE} > 0) {
			print "\tAll Capture groups: ";
			foreach (@{^CAPTURE}) {
				if ($_) {
					print "($_), ";
				}
			} say "";
		}

		#	Print all named capture groups (if any)
		my $any_capture_groups_defined = 0;
		if (scalar(keys %-) > 0) { 
			foreach my $matches_key (keys %-) { 
				if (defined($-{$matches_key}->[0])) { $any_capture_groups_defined = 1; } } 
		}
		if ($any_capture_groups_defined) {
			print "\tNamed capture groups: ";
			foreach my $matches_key (keys %-) {
				if (defined($-{$matches_key}->[0])) {
					print "matches_key=($matches_key), ";
					print "matches_list=(@{$-{$matches_key}}), ";
				}
			} say "";
		}

	}
	say "";
	$loop_i++;
}

