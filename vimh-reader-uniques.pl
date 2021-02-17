#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=3:
#   }}}1
use strict; 
use warnings;
no warnings 'shadow';

my $path_vimh = "$ENV{HOME}/.vimh";

my %unique_paths_count = ();
my @file_datetimes = ();
my @file_paths = ();

open(my $filedata, '<', $path_vimh) or die "Failed to open path_vimh=($path_vimh)\n";
while (my $loop_line = <$filedata>) {
	chomp $loop_line;
	my @loop_fields = split('\t' , $loop_line);
	my $loop_path = $loop_fields[4];

	if (exists($unique_paths_count{$loop_path})) {
		$unique_paths_count{$loop_path} += 1
	} else {
		$unique_paths_count{$loop_path} = 1
	}
}

foreach my $key ( sort { $unique_paths_count{$b} <=> $unique_paths_count{$a} } keys %unique_paths_count) {
	print "$unique_paths_count{$key}\t$key\n";
}


