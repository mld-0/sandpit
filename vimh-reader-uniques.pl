#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=3:
#   }}}1
use strict; 
use warnings;
no warnings 'shadow';
use List::MoreUtils qw(any);

my $path_vimh = "$ENV{HOME}/.vimh";

my @git_repos=`find $ENV{HOME} -name .git -type d -prune | perl -pe 's|\/\.git\$||'`;
#print "git_repos=(@git_repos)\n";

my @git_repos_used = ();

my %unique_paths_count = ();
my %unique_paths_repo = ();

#my %unique_repo_paths = ();

#my @file_datetimes = ();
#my @file_paths = ();

open(my $filedata, '<', $path_vimh) or die "Failed to open path_vimh=($path_vimh)\n";
while (my $loop_line = <$filedata>) {
	chomp $loop_line;
	my @loop_fields = split('\t' , $loop_line);
	my $loop_path = $loop_fields[4];


	if (exists($unique_paths_count{$loop_path})) {
		$unique_paths_count{$loop_path} += 1;
	} else {
		$unique_paths_count{$loop_path} = 1;

		#	Find the repo that is the longest substring of loop_path, and add to %unique_paths_repo
		my $loop_repo_match = "";
		foreach my $loop_repo_search (@git_repos) {
			chomp($loop_repo_search);
			if ((length($loop_repo_search) > length($loop_repo_match)) and (index($loop_path, $loop_repo_search) != -1)) {
				$loop_repo_match = $loop_repo_search;
			}
		}
		$unique_paths_repo{$loop_path} = $loop_repo_match;

		#	Add repo path to list of used repos, if it is not already contained in it
		if ( ! any { $_ eq $loop_repo_match } @git_repos_used) {
			if (length($loop_repo_match) > 0) {
				push(@git_repos_used, $loop_repo_match);
			}
		}
	}
}

##	unique paths with counts and containing repos
#foreach my $key ( sort { $unique_paths_count{$b} <=> $unique_paths_count{$a} } keys %unique_paths_count) {
#	print "$unique_paths_count{$key}\t$key\t$unique_paths_repo{$key}\n";
#}

#	For each git repo (that has been used), output each file belonging to said repo
foreach my $loop_repo  (@git_repos_used) {
	print "$loop_repo\n"; 
	foreach my $key (keys %unique_paths_count) {
		my $loop_check_path = "$unique_paths_repo{$key}";
		if ($loop_check_path eq $loop_repo) {
			print "\t$key\n";
		}
	}
}

#	

