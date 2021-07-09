
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
cat "sample.xml" | perl -MXML::LibXML -E '$ip = XML::LibXML->load_xml(IO => STDIN); say $_->to_literal() for $ip->findnodes("//blue")'
#	or
#perl -MXML::LibXML -E '$ip = XML::LibXML->load_xml(location => $ARGV[0]); say $_->to_literal() for $ip->findnodes("//blue")' "sample.xml"
echo ""

#	Current time in given format
echo "d)"
f='%FT%H:%M:%S%Z'
perl -MDateTime -sE 'say DateTime->now(time_zone=>q/local/)->strftime($f)' -- -f="$f"
echo ""

