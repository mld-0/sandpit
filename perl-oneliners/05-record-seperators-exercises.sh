
#	Find words containing 'an', 'at', 'in', 'it'
echo "a)"
cat "jumbled.txt" | perl -0777 -nE 'say join "\n", /\w*(?:an|at|in|it)\w*/g'
#	or
#cat "jumbled.txt" | perl -00 -nE 'say join "\n", /\w*(?:an|at|in|it)\w*/g'
#	or
#cat "jumbled.txt" | perl -nE 'BEGIN{ $/ = undef }; say join "\n", /\w*(?:an|at|in|it)\w*/g'
echo ""

#	Emulate 'paste -sd'
echo "b)"
cat "ip.txt" | perl -lpE '$\ = eof ? "\n" : ",";'
#	or
#cat "ip.txt" | perl -lnE 'push @f, $_; END{  say join ",", @f; }'
#	or
#cat "ip.txt" | perl -lnE 'push @f, $_; END{ $" = ","; say "@f"; }'
echo ""

#	extract paragraphs containing words starting with 'do'
echo "c)" 
cat "sample.txt" | perl -00 -lnE 'if (/\bdo/) { say($nl, $_); $nl="\n"; }'
echo ""

#	join lines of each paragraph, and append '.'
echo "d)"
cat "sample.txt" | perl -00 -nE 'print "$nl"; say((join ". ", split "\n"), "."); $nl="\n";'
#	or
#cat "sample.txt" | perl -F'\n' -00 -lane '$\ = eof ? ".\n" : ".\n\n"; print join ". ", @F'
echo ""

#	Display all records with second field > 50. Use ';;' as record seperator, ':' as field seperator.
echo "e)"
s='mango:100;;apple:25;;grapes:75'
echo "$s" | perl -F':' -lanE 'BEGIN{ $/ = $\ = ";;"; }; s/\n$//; print if $F[1]>50'
echo ""

