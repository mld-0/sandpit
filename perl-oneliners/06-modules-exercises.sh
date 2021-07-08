
#	Display max word determined by alphabetical order
s='let in bat xml me lion'
echo "a)"
echo "$s" | perl -anE 'say((sort @F)[-1])'
echo ""

#	Randomize the characters of each word
s='this is a sample sentence'
echo "b)"
echo "$s" | perl -MList::Util=shuffle -anE 'say( join " ", (map { join "", shuffle split //  } @F) )'
#	or
#echo "$s" | perl -MList::Util=shuffle -anE 'BEGIN{$,=" "} say( map {join "", shuffle split //} @F)'
echo ""

echo "c)"
#cat "sample.xml" | perl -nE ''
echo ""


