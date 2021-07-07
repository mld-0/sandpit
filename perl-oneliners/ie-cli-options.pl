

#	Loop over input:
#	Implicit loop over filename arguments (non-printing) '-n'
#			perl -ne '...' 
#	is equivalent to:
#			while (<>) { ... }
#	
#	Implicit loop over filename arguments (printing) '-p'
#			perl -pe '...'
#	is equivalent to:
#			while (<>) { ... } continue { die $!\n" unless print $_; }


#	-n				Implicit loop over filename arguments, without printing lines. 
#	-p				Implicit printing loop over filename arguments, prints lines. Overrides '-n'. 
#
#	-a				Autosplit line mode ($_ into @F array) (delimiter -F<delim>). Implicitly sets '-n'. 
#
#	-F<delim>		Specify pattern to split on for '-a'. 
#						Use //, '', or "", or '' will be used implicitly. Sets both '-a' and '-n'.
#
#	-e				Specify line of program as argument text
#	-E				As per '-e', but enable optional features (see: Optional features '-E') 
#
#	-l[octnum]		Automatic line-ending processing. When used with '-n' or '-p', $/ (IRS) is chomped. Sets $\ 
#						(ORS) to octnum, or if not given, to current value of $/.
#
#	-i[extension]	Specifies that files processed by <> construct are to be edited in place. 
#					If extension is supplied, backup file is made (see below for rules)
#
#	-0[octal/hex]	Specify $/ (IRS) as octal or hexadecimal, or set to null character \0 if value not given. 
#
#	-I[directory]	Prepend directory to module search path (@INC)
#
#	-s				Rudimentary switch parsing
#
#	-d				Run under debugger
#
#	-dt				Run under debugger, indicates use of threads. 
#
#	-h				Help, prints summary of options
#
#	-D<>			Set debugging flags (see options below)
#
#	-c				Check syntax of program (runs BEGIN and CHECK blocks). 
#
#	-C				Controls Unicode features (see options below). 
#
#	-f				Disable executing sitecustomize at start-up
#
#	-m[module]		Execute 'use module' at start-up (but do not call module imports)		
#	-M[module]		Execute 'use module' at start-up
#
#	-S				Use PATH to search for program unless name contains path seperators
#
#	-T				Taint, prevent insecure operations
#	-t				Taint, but with warnings instead of fatal errors
#	-w				Enable warnings (sets $^W)
#	-W				Force enable warnings
#	-X				Force disable warnings
#	-u				Dump core after compiling program
#	-U				Allow unsafe operations
#	-v				Print version of perl
#	-V				Print summary of perl configuration, and values of @INC
#	-x[directory]	Tell perl that program is embedded in unrelated text. If directory is specified, switch to said 
#						directory before running. 

