#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=3:
#   }}}1
#	{{{1

#	Using standard modules:
#	{{{
echo "max, product, sum:"
# same as: perl -F, -anE 'BEGIN{use List::Util qw(max)} say max @F' 
echo '34,17,6' | perl -MList::Util=max -F, -anE 'say max @F'

echo '34,17,6' | perl -MList::Util=product -F, -anE 'say product @F'

# 'sum0' returns '0' even if array is empty, whereas 'sum' returns 'undef' $ 
echo '3.14,17,6' | perl -MList::Util=sum0 -F, -anE 'say sum0 @F'
echo ""


s='floor bat to dubious four'
echo "shuffle, sample:"
echo "$s" | perl -MList::Util=shuffle -lanE 'say join ":", shuffle @F'

echo 'foobar' | perl -MList::Util=shuffle -F -lanE 'say shuffle @F'

echo "$s" | perl -MList::Util=sample -lanE 'say join ":", sample 2, @F'
echo ""


s='3,b,a,3,c,d,1,d,c,2,2,2,3,1,b'
echo "uniq"
echo "$s" | perl -MList::Util=uniq -F, -lanE 'say join ",",uniq @F'
echo ""

echo "Base64:"
#	Equivalent to: 
#		echo 'hello world' | base64
echo 'hello world' | perl -MMIME::Base64 -ne 'print encode_base64 $_'

#	Reverse base64:
echo 'aGVsbG8gd29ybGQK' | perl -MMIME::Base64 -ne 'print decode_base64 $_'
echo ""

#	}}}

#	Third party modules:
#	{{{
#	Check if modules is installed:
perl -MText::CSV -E ''

#	Install modules:
#	{{{
bin_cpan=cpan
#$bin_cpan "Text::CSV_XS"
#$bin_cpan "Text::CSV"
#$bin_cpan "XML::LibXML"
#	}}}

#	CSV parsing:
#		Text::CSV
#		Text::PP			Perl version (more likely to be supported)
#		Text::CSV_XS		Faster (written in C)

s='eagle,"fox,42",bee,frog\n1,2,3,4'
echo "Text::CSV_XS:"
# 	Note: -n or -p option not used
printf '%b' "$s" | perl -MText::CSV_XS -E 'say $row->[1] 
					while $row = Text::CSV_XS->new->getline(*ARGV)'
echo ""

s='apple,"1\n2\n3",good\nguava,"32\n54",nice'
printf "$s" | perl -MText::CSV_XS -E '
				while($row = Text::CSV_XS->new({binary => 1})->getline(*ARGV))
				{say "$row->[1]\n-----"}'
echo ""


#	JSON: 
#		JSON:PP
#		JSON::XS
s='{"greeting":"hi","marks":[78,62,93]}'
# <> is same as <ARGV>, here it helps to get a line of input
echo "decode_json:"
echo "$s" | perl -MCpanel::JSON::XS -E '$ip=decode_json <>; say $ip->{greeting}'

echo "$s" | perl -MCpanel::JSON::XS -E '$ip=decode_json <>; say join ":", @{$ip->{marks}}'
echo ""

#	Perl JSON shell function shortcut
pj() { perl -MCpanel::JSON::XS -0777 -E '$ip=decode_json <>;'"$@" ; }

s='{"greeting":"hi","marks":[78,62,93]}'
echo "pj():"
echo "$s" | pj 'say $ip->{greeting}'
echo ""

sample='{ "fruit": "apple", "blue": ["toy", "flower", "sand stone"], "light blue": ["flower", "sky", "water"], "language": { "natural": ["english", "hindi", "spanish"], "programming": ["python", "kotlin", "ruby"] }, "physics": 84 }'
#	order may be different than input as hash doesn't maintain key order process top-level keys not containing 'e' 
echo "$sample" | pj 'for (keys %$ip){say "$_:$ip->{$_}" if !/e/}'
echo ""

# 	process keys within 'language' key that contain 't'
echo "$s" | pj '$"=","; while(($k,$v) = each %{$ip->{language}}) {say "$k:@{$v}" if $k=~/t/}'
echo ""

echo "cpanel_json_xs vs JSON_XS->new->pretty->encode:"
#	equivalent:
echo "$s" | cpanel_json_xs
echo "$s" | perl -MCpanel::JSON::XS -e 'print Cpanel::JSON::XS->new->pretty->encode(decode_json <>)'
echo ""


#	}}}


#	Deparsing:
#	Convert one-liners to (pretty) formatted scripts. Note: the input sources (stdin, filenames, ect.) aren't needed
echo "Deparsing:"
perl -MO=Deparse -ne 'print if /at/'
#	You can use -MO=qq,Deparse if you don’t want to see the -e syntax OK message.
perl -MO=Deparse -l -0072 -ne 'print if /a/'



