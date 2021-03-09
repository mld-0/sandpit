use strict; 
use warnings;
no warnings 'shadow';

print "Enter line width:\n";
my $column_width = int(<STDIN>);
chomp $column_width;

print "Enter lines:\n";
my @user_lines = <STDIN>;
chomp @user_lines;

my $ruler = "1234567890" x int($column_width / 10 + 2);

print "$ruler\n";
foreach my $loop_line (@user_lines) {
	printf("%${column_width}s\n", $loop_line);
}


