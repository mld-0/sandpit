
#	Print all but third line of input
echo "a)"
seq 34 37 | perl -nE 'print if $. != 3'  # note $. is one-indexed
echo ""

#	Print lines 4,5,6
echo "b)"
seq 65 78 | perl -nE 'print if 4..7';
echo ""

#	From line 4 til eof, replace s/are/are not/ and s/is/is not/, only displaying changed lines
echo "c)"
cat "ip.txt" | perl -nE 'print if $. > 3 && s/are|is/$& not/g'
#	or
#cat "ip.txt" | perl -nE 'print if $. > 3 && s/(are|is)/\1 not/g'
#	or
#cat "ip.txt" | perl -nE 'if ($. < 4) { next; } $temp = $_; s/are/are not/; s/is/is not/; print $_ if not $temp eq $_; '
echo ""

#	Print first three lines
echo "d)"
seq 14 25 | perl -nE 'print if $. <= 3'
echo ""

#	Print from start until (first) line containing 'game' (inclusive)
echo "e)"
cat "ip.txt" | perl -nE 'print if 1 .. /game/'
#	or
#cat "ip.txt" | perl -nE 'print; exit if /game/'
echo ""

#	Print lines containing 'is' but not 'good'
echo "f)"
cat "ip.txt" | perl -nE 'print if /is/ and not /good/'
#	or
#cat "ip.txt" | perl -nE 'print if /is/ && !/good/'
echo ""

#	Find word before and after 'is', and display in reverse order seperated by ':'
echo "g)"
cat "ip.txt" | perl -nE 'say "$2:$1" if /(\w+)\s+is\s+(\w+)/g'
#	or
#cat "ip.txt" | perl -nE 'if (/(\w+)\s+is\s+(\w+)/g) { say "$2:$1" }'
#	or
#cat "ip.txt" | perl -nE 'if (/(\w+)\s+is\s+(\w+)/g) { say "@{^CAPTURE[1]}:@{^CAPTURE[0]}" }'
echo ""

#	Replace (text not bytes?) s/0xA0/0x7F/ and s/0xC0/0x1F/ 
echo "h)"
var='start address: 0xA0, func1 address: 0xC0'
echo "$var" | perl -nE 's/0xA0/0x7F/g; s/0xC0/0x1F/g; print $_'
#	or
#echo "$var" | perl -pE 's/0xA0/0x7F/g; s/0xC0/0x1F/g;'
echo ""

#	Find the starting index of the first occurence of 'is', 'the', 'was', or 'to' for each line
echo "i)"
cat "idx.txt" | perl -nE '/is|the|was|to/; say $-[0]'
echo ""

#	Display all lines containing '[4]*' 
echo "j)"
var='2.3/[4]*6\n2[4]5\n5.3-[4]*9\n'
printf "$var" | perl -nE 'print if /\Q[4]*\E/'
#	or
#printf "$var" | perl -nE 'print if index($_, "[4]*") != -1'
echo ""

#	Ongoing: 2021-07-07T20:56:21AEST perl, perl-oneliners, line-processing k), neater solution to "Replace all lowercase characters with 'x' for words starting with 'm'" problem that doesn't involve substitute 'e' flag (see below) (though the moral of the story is the power of the substitute 'e' flag - which allows perl expressions in replacement text field)

#	Replace all lowercase characters with 'x' for words starting with 'm'
echo "k)"
var="ma2T3a a2p kite e2e3m meet\n"
printf "$var" | perl -pE 's/\bm\w+/$& =~ tr|a-z|x|r/ge'
#	or
#printf "$var" | perl -nE 'foreach (/\b(\w+)\b/g) { if (/\b(m\w+)\b/) { $result = $&; $result =~ tr|a-z|x|; print "$result "} else { print "$_ " } }'  # Doesn't preserve whitespace, whatever is between each word becomes a single space
echo ""

#	Delete characters other than lowercase vowels and newline, for lines between lien containing 'you' until line 4
echo "l)"
cat "ip.txt" | perl -lpE 'tr/aeiou//cd if /you/ .. 4 '
#	or
#cat "ip.txt" | perl -pE 'tr/aeiou\n//cd if /you/ .. 4'
#	or
#cat "ip.txt" | perl -nE 'if (/you/ .. 4) { tr/aeiou\n//cd } print'
echo ""

