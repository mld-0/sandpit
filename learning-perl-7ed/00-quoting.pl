
#	Ongoing: 2021-06-08T03:13:30AEST (using quote-like operators in regex context/for regex operations)
#	Quote like operators: 
#
#	Literal string
#		q/STRING/
#		'STRING'
#
#	Interpolated string
#		qq/STRING/
#		"STRING"
#	
#	Interpolate and execute as system command
#		qx/STRING/
#		`STRING`
#
#	


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

