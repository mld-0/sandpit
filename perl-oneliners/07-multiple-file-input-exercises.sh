
#	Print filename, followed by last field of the first two lines of each file (delim space)
echo "a)"
#perl -anE 'if ($.==1) {say ">$ARGV<";}; if ($.>2) {close ARGV; say "-"x8; next; }  say $F[-1]  ' table.txt ip.txt
#	or
perl -anE 'say ">$ARGV<" if ($.==1); say $F[-1]; if ($.>2) { close ARGV; say "-"x8; }' table.txt ip.txt
echo ""

#	Display the filename of files containing 'at' or 'fun' in the third field of any row  (delim space)
echo "b)"
perl -anE 'if ($F[2] =~ /at|fun/) { say $ARGV; close ARGV; }' sample.txt secrets.txt ip.txt table.txt
echo ""

#	Print the first two lines for each input file, with seperator (but not at end)
echo "c)"
#	Ongoing: 2021-07-09T15:44:27AEST perl, one-liners, $ARGV is not necessarily same as $ARGV[0], if we close ARGV, $ARGV[0] is the file after, $ARGV is that file?
perl -lnE 'say $_; if ($. >= 2) { close ARGV; say "-"x3 if $ARGV[0];  } ' ip.txt sample.txt table.txt
#	or
#perl -pE 'print $s if ($.==1); if ($.==2) { close ARGV; $s="---\n" }' ip.txt sample.txt table.txt
echo ""


