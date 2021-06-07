
#	match 				m//  or  // (m may be omited if slash is used as delimiter) 
#	substitute			s///
#	transliterate 		tr///

#	Perl regex 
#		[...] 			any single character in ...
#		[^...]			any single character not in ...
#		*				0 or more occurences 
#		+				1 or more occurences
#		?				0 or 1 occurences
#		{n}				exactly n occurences
#		{n,}			n or more occurences
#		{,m}			at most m occurences
#		{n,m}			n to m occurences
#		a|b				a or b
#		\w				word character
#		\W				non-word character
#		\s				whitespace [\t\n\r\f]
#		\S				non-whitespace 
#		\d				digit [0-9]
#		\D				non-digit
#		^ or \A			match beginning of string
#		$ or \Z 		match end of string (before newline)
#		\z				end of string
#		\b				word bountry when outside brackets, backspace (0x08) inside brackets
#		\B				non word boundry
#		\n				newline
#		\t				tab
#		\1 ... \9		n-th grouped subexpression
#		\10				10th grouped subexpression if matched, otherwise octal representation of character code

#	Non-greedy quanitifiers
#		??			0 or 1
#		*?			0 or more
#		+?			1 or more
#		{m,n}?		specific number

#	Regex variables
#		$&  entire matched string
#		$`  before matched string
#		$'  after matched string


# Ongoing: 2021-06-08T02:52:31AEST regarding binding operator (and use of default/other variable) (missing something) (some part of what is going on -> (if 'match' is our regex?) where is the text to be searched coming from (from $_?) (or whatever variable is used in place of '$_' in binding operator expression (the point being, clearer example of this perl implicit witchcraft) (being found somewhere in aide/perl, or learning-perl-7ed (this dir) 2021-06-08T02:55:15AEST 

#	Binding operator and default argument:	'=~'
#			$_ ~= m/match/
#	is equivelent to  
#			m/match/  
#	Both statements associates the temporary variable '$_' with the result of 
#	'!~' inverts the match
#	Returns a boolean in a sclar context, or the matches of any grouped expressions in a list context


#	Match in list context
#		When a pattern match (m//) is used in a list context, the return value is a list of the capture variables created in the match, or an empty list if the match failed


#	Substitution alternative delimiters
#	Ongoing: 2021-06-08T03:50:13AEST (that is) the delimiter for FIND and REPLACE can be different?
#>%			s/fred/barney/;
#>%			s{fred}{barney}; 
#>%			s[fred](barney); 
#>%			s<fred>#barney#;

#	Match modifiers:
#		i		case insensitive
#		m		match ^$ against newlines instead of against string boundry
#		o		evaluate expression only once
#		s		allows '.' to match newline
#		x		Allows whitespace in the expression for clarity
#		g		globally find all matches (iterates in scalar context, list in list context)
#		cg		allow search to contine even after a global match fails
#		a 		use only ASCII versions of \d, \s, \w and [[:posix:]] 
#		aa		no ASCII character will match a non-ASCII character if /i is also specified
#		c		don't reset pos on failed matches when using /g
#	may be used in whichever order

#	Substitution modifiers
#		i		case insensitive
#		m		match ^$ against newlines instead of against string boundry
#		o		evaluate expression only once
#		s		allows '.' to match newline
#		x		Allows whitespace in the expression for clarity
#		g		Replace all occurences of the found expression
#		e		Evaluate the replacement as a perl statement, and use the return value as replacement text
#		r		Leave origional string alone and return modified copy

#	Translation modifiers:
#		c		Complements SEARCHLIST
#		d		Delete found-but-unreplaced characters
#		s		Squashes duplicate replaced characters


#	Ongoing: 2021-06-08T02:55:38AEST How the s--- is this so badly documented (or is it just that so is everything else in perl?), (another source for this match-only-once when using 'm??') (for a better definition of what this does/(is called), (how is google unhelpful for 'perl match delimiter questionmark'?
#	TODO: 2021-06-08T03:09:10AEST Examples of match-only-once, and no-interpolation, (and other regex match modifiers) (and) Achieving interpolation bewteen 'no-interpolation' delimiters: interpolate that which is not usually interpolated, (and (to what extent) vice versa?)

#	Alternative Match Delimiter Behaviour:
#	Match only once:
#		m?PATTERN?
#	matches only once within the string. Equivelent to: #		
#		NO IT ISN'T ~~m/(PATTERN?)/~~  


#	No interpolation:
#		m'PATTERN'
#	or
#		quotemeta(PATTERN)
#	or
#		/\QPATTERN\E/

#	Customary  Generic        Meaning        Interpolates
#	    ''       q{}          Literal             no
#	    ""      qq{}          Literal             yes
#	    ``      qx{}          Command             yes*
#	            qw{}         Word list            no
#	    //       m{}       Pattern match          yes*
#	            qr{}          Pattern             yes*
#	             s{}{}      Substitution          yes*
#	            tr{}{}    Transliteration         no (but see below)
#	             y{}{}    Transliteration         no (but see below)
#	    <<EOF                 here-doc            yes*
#	    * unless the delimiter is '' (or quotemeta(), or /\Q\E/)?)

my @list = qw/food foosball subeo footnote terfoot canic footbrdige/;
my ($first, $last);
foreach (@list)
{
   $first = $1 if m?(foo.*)?;
#	or
   $last = $1 if m/(foo.*)/;
}
print "first=($first), last=($last)\n";
print "\n";

#	Case shifting
#		The \U escape forces what follows to all uppercase
#		the \L escape forces lowercase
#		By default, these affect the rest of the (replacement) string, or you can turn off case shifting with \E
#		When written in lowercase (\l and \u ), they affect only the next character
#		You can even stack them up. Using \u with \L means “all lowercase, but capitalize the first letter”#


#	Regex expression precedence
#			Parentheses (grouping or capturing) 		(...) (?:...) (?<LABEL>..)
#			Qualifiers									a*, a+, a?, a{n,m}
#			Anchors and sequences						^ $ \A \b \z \Z
#			Alteration									a|b|c
#			Atoms										a [abc] \d \1 \g{2}


#	regex-related functions
#		split // "$str_value"
#

#	A pattern test program
#>>		while (<>) { # take one input line at a time
#>>			chomp;
#>>			if (/YOUR_PATTERN_GOES_HERE/) {
#>>				print "Matched: |$`<$&>$'|\n"; # the special match vars } else {
#>>				print "No match: |$_|\n"; 
#>>			}
#>>		}

