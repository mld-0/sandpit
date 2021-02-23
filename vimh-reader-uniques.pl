#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=3:
#   }}}1
use strict; 
use warnings;
no warnings 'shadow';
use List::MoreUtils qw(any);
#	{{{2

my $path_vimh = "$ENV{HOME}/.vimh";


sub GetListOfFilesPerRepo {
#	{{{

	my $path_vimh = shift;

my @git_repos=`find $ENV{HOME} -name .git -type d -prune | perl -pe 's|\/\.git\$||'`;

#	For each git repo (that has been used), output each file belonging to said repo
my @git_output_repos = ();
my @git_output_filepaths = ();
my %git_repos_totalCount = ();
my @git_repos_used = ();
my %git_repos_uniqueCount = ();
my %unique_paths_count = ();
my %unique_paths_repo = ();

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
					$git_repos_uniqueCount{$loop_repo_match} = 1	
				}
			} else {
				$git_repos_uniqueCount{$loop_repo_match} += 1
			}
		}
	}
	
	
	my $loop_check_path = "";
	my $loop_path_count = 0;
	foreach my $loop_repo ( sort { $git_repos_uniqueCount{$b} <=> $git_repos_uniqueCount{$a} } keys %git_repos_uniqueCount) {
		#print "$loop_repo\n"; 
		push(@git_output_repos, $loop_repo);
		$git_repos_totalCount{$loop_repo} = 0;
		my @loop_list_keys = ();
		foreach my $key ( sort { $unique_paths_count{$b} <=> $unique_paths_count{$a} } keys %unique_paths_count) {
			$loop_check_path = "$unique_paths_repo{$key}";
			$loop_path_count = $unique_paths_count{$key};
			if ($loop_check_path eq $loop_repo) {
				#print "$loop_path_count\t$key\n";
				$git_repos_totalCount{$loop_repo} += $loop_path_count;
				push(@loop_list_keys, $key);
				#print "\t$key\n";
			}
		}
		push(@git_output_filepaths, \@loop_list_keys);
	}

	return ( \@git_output_repos, \@git_output_filepaths );
}
#	}}}

#	Iterate over git_output_repos, git_output_filepaths
my $i = 0;
(my $git_output_repos_ref, my $git_output_filepaths_ref) = &GetListOfFilesPerRepo($path_vimh);
my @git_output_repos = @{$git_output_repos_ref};
my @git_output_filepaths = @{$git_output_filepaths_ref};
foreach my $loop_repo (@git_output_repos) {  # For each repo
	print "$loop_repo\n";
	my $loop_dirs_list = $git_output_filepaths[$i];
	#print "loop_dirs_list=(@$loop_dirs_list)\n";
	for my $loop_dir (@$loop_dirs_list) {  # For each file in repo
		print "\t$loop_dir\n";
	}
	$i++;
}


#	}}}1
