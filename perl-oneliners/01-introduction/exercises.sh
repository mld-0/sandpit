
#	Print lines containing 'is'
echo "a)"
cat "ip.txt" | perl -nE 'print $_ if /is/'
echo ""

#	Print first field (delimiter ' ') of lines not containing 'y' 
echo "b)"
cat "ip.txt" | perl -lanE 'say @F[0] if !/y/'
#	or
#cat "ip.txt" | perl -F'\\ ' -lanE 'say @F[0] if !/y/'
echo ""

#	Display lines containing no more than 2 fields (delimiter ' ')
echo "c)"
cat "ip.txt" | perl -lanE 'say $_ if (scalar(@F) <= 2)'
#	or
#cat "ip.txt" | perl -lanE 'say $_ if ($#F < 2)'
echo ""

#	Display lines containing 'is' in the second field
echo "d)"
cat "ip.txt" | perl -lanE 'say $_ if $F[1] =~ /is/'
echo ""

#	For each line, replace first 'o' with '0'
echo "e)"
cat "ip.txt" | perl -nE 's/o/0/; print $_'
echo ""

#	Ongoing: 2021-07-07T19:02:43AEST perl, perl-oneliners, is-numeric check (that fits (neatly) into a oneliner)

#	Calculate product of numbers in last field of each line
echo "f)"
cat "table.txt" | perl -lanE 'BEGIN{$result=1}; $result *= $F[-1]; END{say $result};'
echo ""

#	Append '.' to all input lines
echo "g)"
printf 'last\nappend\nstop\n' | perl -pE 's/$/./'
#	or
#printf 'last\nappend\nstop\n' | perl -nE 'chomp; print "$_.\n"'
echo ""

#	Ongoing: 2021-07-07T19:08:50AEST perl, perl-oneliners, what qualifies for inclusion in %ENV, (exported variables and those declared on the same line from which perl is envoked?)
#	Ongoing: 2021-07-07T19:12:39AEST perl, perl-oneliners, (best/all methods of) imbedding shell variables in oneliner

#	Display all lines containing shell variable $s, preceded by a word character
echo "h)"
s='is'
cat "ip.txt" | s="$s" perl -nE 'print $_ if /\w+$ENV{s}/'
#	or
#cat "ip.txt" | perl -snE 'print $_ if /$s/' -- -s=$s
#	or
#cat "ip.txt" | perl -nE 'print $_ if /'"$s"'/'
echo ""

#	Display contents of file in second field
echo "i)"
echo 'report.log ip.txt sorted.txt' | perl -anE 'print qx/cat $F[1]/;'
#	or
#echo 'report.log ip.txt sorted.txt' | perl -anE 'print `cat $F[1]`;'
#	or
#echo 'report.log ip.txt sorted.txt' | perl -anE 'system("cat $F[1]")'




