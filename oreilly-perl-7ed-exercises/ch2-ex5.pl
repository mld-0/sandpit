

print "enter str value\n";
my $var_a = <STDIN>;
chomp $var_a;

print "enter int value:\n";
my $var_b = <STDIN>;
chomp $var_b;

my $result = "$var_a\n" x $var_b;

print "result=($result)\n";

