#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=3:
#   }}}1

#	Global Scalar Special Variables
#		$_		$ARG				Default input and pattern-searching space
#		$.		$NR					Current line number (last filehandle that was read)
#		$/		$RS					Record seperator (default newline), if null, treat blank line as delim
#		$,		$OFS				Output field seperator (for print)
#		$\		$ORS				Output record seperator (for print)
#		$"		$LIST_SEPARATOR		Like $, but applies to list values interpolated in quoted string (Default space)
#		$;		$SUBSCRIPT_SEPERATOR	Seperator for multidimensional array emulation (Default \034)
#		$^L		$FORMAT_FORMFEED	What format to output a formfeed (Default \f)
#		$:		$FORMAT_LINE_BREAK_CHACTERS		Set of characters after which a string may be broken (Default \n)
#		$^A		$ACCUMULATOR		Write accumulator for format lines
#		$#		$OFMT				Output format for printed numbers (deprecated)
#		$?		$CHILD_ERROR		Status returned by last pipe close, backtick, or system operator command
#		$!		$OS_ERROR or $ERRNO	Numeric context = ERRNO value, String context = error string
#		$@		$EVAL_ERROR			Perl syntax error message from last eval command
#		$$		$PID				pid of this process
#		$<		$UID				Read user id (uid) of this process
#		$>		$EUID				Effective user id of this process
#		$(		$GID				Real group id (gid) of this process
#		$)		$EGID				Effective gid of this process
#		$0 		$PROGRAM_NAME		Name of the file containing the perl script being executed
#		$[							Index of the first element of an array (Default 0)
#		$]		$PERL_VERSION		Version, plus patchlevel, / 1000
#		$^D		$DEBUGGING			Value of debugging flag
#		$^E		$EXTENDED_OS_ERROR		Extended error message (on some platforms)
#		$^F		$SYSTEM_FD_MAX		Maximum system file descriptor
#		$^H							Internal compiler hints
#		$^I		$INPLACE_EDIT		Current value of inplace-edit extension
#		$^M							Emergency memory pool
#		$^O		$OSNAME				Name of the OS perl was compiled for
#		$^T		$BASETIME			Epoch time at which script began running
#		$^W		$WARNING			Current value of the warning switch
#		$^X		$EXECUTABLE_NAME	Name of the perl binary
#		$ARGV						Name of the current file when reading from '.'

#	Global Array Special Variables
#		@ARGV		Array containing command line arguments for script
#		@INC		List of places to look for Perl scripts, for the 'do', 'require', or 'use' constructs
#		@F			Array into which input lines are split by -a cli switch

#	Global Hash Special Variables
#		%INC		Hash containing entries for the filenames that have been included via 'do' or 'require'
#		%ENV		Hash containing current shell environement
#		%SIG		Hash used to set signal handlers

#	Global Special Filehandles
#		ARGV		Iterates over command line filenames in @ARGV
#		STDERR		Standard error
#		STDIN		Standard input
#		STDOUT		Standard output
#		DATA		Referes to anything following '__END__' token 
#		_			Cached information from last 'stat', 'lstat', or file test operator

#	Global Special Constants
#		__END__			Indicates end of program, beginning of text to be read by DATA, (not interpolated)
#		__FILE__		Filename at point in program where used, (not interpolated)
#		__LINE__		Current line number, (not interpolated)
#		__PACKAGE__		Current package name at compile time (or undefined), (not interpolated)

#	Regular Expression Special Variables
#		$digit						Text matched by corresponding set of parentheses in last pattern matched (ie: $1, $2, ...)
#		$&			$MATCH			String matched by last successful pattern match
#		$`			$PREMATCH		String preceding whatever was matched by last successful pattern match
#		$'			$POSTMATCH		String following whatever was matched by last successful pattern match
#		$+			$LAST_PAREN_MATCH	Last bracket matched by the last search pattern

#	Filehandle Special Variables
#		$|			$OUTPUT_AUTOFLUSH		If non-zero, forces an fflush(3) after every read or print on the currently selected output channel
#		$%			$FORMAT_PAGE_NUMBER		Current page number of the current output channel
#		$=			$FORMAT_LINES_PER_PAGE	Page length of the current output channel (Default 60)
#		$-			$FORMAT_LINES_LEFT		Number of lines left on the page of the current output channel
#		$~			$FORMAT_NAME			Name of the current report format for the current output channel (Default name of filehandle)
#		$^			$FORMAT_TOP_NAME		Name of the top-of-page format for the current output channel

