
#	Extract contents between () or )( from each line
echo "a)"
cat "brackets.txt" | perl -F'[()]' -lanE 'print $F[1]'
#	or
#cat "brackets.txt" | perl -nE '/\(([^)]*)\)|\)([^(]*)\(/; say "$1$2"'
echo ""


#	Extract Name (0th) and Physics (2nd) fields from each line
echo "b)"
cat "scores.csv" | perl -F',' -lanE 'BEGIN {$" = ":"}; print "@F[0,2]"'
#	or
#cat "scores.csv" | perl -F',' -lanE 'print "$F[0]:$F[2]"'
echo ""


#	Display Names (0th) where Maths (1st) score > 80
echo "c)"
cat "scores.csv" | perl -F',' -lanE 'print $F[0] if $F[1] > 80'
echo ""

#	Display number of word characters for given inputs:
echo "d)"
echo 'hi there' | perl -nE 'say s/\w//g'
echo 'u-no;co%."(do_12:as' | perl -F'\w' -anE 'say $#F' 
#	or
#echo 'u-no;co%."(do_12:as' | perl -nE 's/\W//g; say length($_)'
echo ""


#	Single solution which turns both s1/s2 into provided outputs
echo "e)"
s1='1 "grape" and "mango" and "guava"'  # "grape","guava","mango"
s2='("a 1""d""c-2""b")'  # "a 1","b","c-2","d"
echo "$s1" | perl -nE 'say join ",", sort /"[^"]+"/g'
echo "$s2" | perl -nE 'say join ",", sort /"[^"]+"/g'
echo ""


#	Display 3rd/5th characters (0-indexed) from each line
echo "f)"
printf 'restore\ncat one\ncricket' | perl -F'' -lanE 'say @F[2,4]'
echo ""


#	Read fixed width fields, replace empty with 'NA'
echo "g)"
cat "fw.txt" | perl -nE 'BEGIN {$"=","}; @f = unpack("a3x2a2x3a2x2a*"); @f = map { /^\s*$/ ? "NA" : $_ } @f; print "@f[0,1,-1]"'
#	or
#cat "fw.txt" | perl -nE '@f = unpack("a3x2a2x7a*"); @f = map { /^\s*$/ ? "NA" : $_ } @f; print join ",", @f'
echo ""


#	Display header (first row), as well as any row containing 'b' or 't' (case-insensitive)
echo "h)"
cat "scores.csv" | perl -nE 'print $_ if $. == 1 or /b|t/i'
echo ""


#	Extract words that contain '42' but not at the edge of a word
echo "i)"
s='hi42bye nice1423 bad42 cool_42a 42fake'
echo "$s" | perl -nE 'say join "\n", /\w+42\w+/g'
#	or
#echo "$s" | perl -lanE 'foreach (@F) { say $_ if /\w+42\w+/ }'
echo ""


#	Add column 'GP' = 0.5 * maths + 0.25 * physics + 0.25 * chemistry
echo "j)"
cat "scores.csv" | perl -F',' -lanE 'BEGIN{ $"="," }; $F[4] = 0.5*$F[1]+0.25*$F[2]+0.25*$F[3]; $F[4] = "GP" if $. == 1; say "@F"'
#	or
#cat "scores.csv" | perl -F',' -lanE 'print join ",", @F, $.==1 ? "GP" : 0.5*$F[1]+0.25*$F[2]+0.25*$F[3]'
echo ""


#	For file with mixed seperators, print first two fields of each line
echo "k)"
cat "mixed_fs.txt" | perl -nE 'chomp; $" = ($.==1 or $.==2) ? " " : ",";  @f=split($", $_); say "@f[0,1]"'
#	or
#cat "mixed_fs.txt" | perl -lnE '$s = $.<3 ? " " : ","; print join $s, (split $s)[0,1]'
echo ""


#	Print only numbers in range [20, 1000]
echo "l)"
s='20 -983 5 756 634223'
echo "$s" | perl -lanE 'print join " ", grep { $_ >= 20 and $_ <= 1000 } @F; '
echo ""


#	Filter lines containing characters in ascending or descending order:
echo "m)"
echo "Ascending:"
cat "words.txt" | perl -lnE 'print $_ if $_ eq join "", sort split "", $_';
echo "Descending:"
cat "words.txt" | perl -lnE 'print $_ if $_ eq join "", reverse sort split "", $_';
#	or
#cat "words.txt" | perl -lnE 'print $_ if $_ eq join "", sort {$b cmp $a} split "", $_';
echo ""


#	Three longest words
echo "n)"
s='I bought two bananas and three mangoes'
echo "$s" | perl -anE 'say join ", ", (sort {length($b) <=> length($a)} @F)[0..2];'
#	or
#echo "$s" | perl -nE '@f=sort {length($b) <=> length($a)} split; say join ", ", @f[0..2]'
echo ""


#	Convert (as shown)
echo "o)"
#cat "split.txt" | perl -F',' -anE '@f = split(":", $F[1]); print join "\n", map { "$F[0],$_,$F[2]" } @f'
cat "split.txt" | perl -F',' -lanE 'print join "\n", map { "$F[0],$_,$F[2]" } split ":", $F[1];'
echo ""


#	Generate combinations
echo "p)"
s='{x,y,z}{1,2,3}'
echo "$s" | perl -nE 'say join " ", glob($_);'
#	or
#echo "$s" | perl -nE '/{([^}]*)}{([^}]*)}/; foreach $j (split(",", $1)) { foreach $i (split(",", $2)) { print "$j$i "; }  } print "\n";'
echo ""


