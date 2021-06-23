use strict;
use warnings;
use v5.032;

my $var_str = "ABCdef";

my @list_var = (1, 2, 3, 4);
say "list_var=(@list_var)";

#undef(@list_var[1]);
delete($list_var[1]);

say "list_var=(@list_var)";
