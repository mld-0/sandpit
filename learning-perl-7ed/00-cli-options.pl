
# 	LINK: https://perldoc.perl.org/perlrun
#	Command line perl
#	{{{
#	The normal way to run a Perl program is by making it directly executable, or else by passing the name of the source file as an argument on the command line. (An interactive Perl environment is also possible--see perldebug for details on how to do that.) Upon startup, Perl looks for your program in one of the following places:
#		Specified line by line via -e or -E switches on the command line.
#		Contained in the file specified by the first filename on the command line. (Note that systems supporting the #! notation invoke interpreters this way. See "Location of Perl".)
#		Passed in implicitly via standard input. This works only if there are no filename arguments--to pass arguments to a STDIN-read program you must explicitly specify a "-" for the program name.
#	With methods 2 and 3, Perl starts parsing the input file from the beginning, unless you've specified a "-x" switch, in which case it scans for the first line starting with #! and containing the word "perl", and starts there instead. This is useful for running a program embedded in a larger message. (In this case you would indicate the end of the program using the __END__ token.)
#	The #! line is always examined for switches as the line is being parsed. Thus, if you're on a machine that allows only one argument with the #! line, or worse, doesn't even recognize the #! line, you still can get consistent switch behaviour regardless of how Perl was invoked, even if "-x" was used to find the beginning of the program.
#	}}}

#	LINK: https://learnbyexample.gitbooks.io/command-line-text-processing/content/perl_the_swiss_knife.html#executing-perl-code
#	Command line arguments
#	{{{
#	perlrun (perl flags/options)
#	-a:	split line (specify delimitor -F'delim')
#	-l: end-of-line processing, (chomp input when used with -n or -p), 
#	-p: Places a printing loop around your command so that it acts on each
#	    line of standard input. 
#	-n: Places a non-printing loop around your command.
#	-e: Allows you to provide the program as an argument rather
#	    than in a file. 
#	-i: Modifies your input file in-place (making a backup of the
#	    original unless no argument given to -i)
#	-w: Activates some warnings. Any good Perl coder will use this.
#	-d: Runs under the Perl debugger. For debugging your Perl code,
#	    obviously.
#	-t: Treats certain "tainted" (dubious) code as warnings (proper
#	    taint mode will error on this dubious code). Used to beef
#	    up Perl security, especially when running code for other
#	    users, such as setuid scripts or web stuff.
#	}}}

