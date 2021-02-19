#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=3:
#   }}}1

#	Perl uses a writing template called a 'format' to output reports. To use the format feature of Perl, you have to define a format first and then you can use that format to write formatted data.

#	syntax:
#		format FormatName =
#		fieldline
#		value_one, value_two, value_three fieldline
#		value_one, value_two
#		.

#	fieldholder
#		@<<<<<
#		left justified, with field space of 5


#	example format
format EMPLOYEE = 
==============================
@<<<<<<<<<<<<<<<<<<<< @<<
$name, $age
@#####.##
$salary
.

format EMPLOYEE_HEADER = 
Employees:
.

format EMPLOYEE_PAGE_HEADER =
Name                  Age  Page @<
                                $%
.

select(STDOUT);
$~ = "EMPLOYEE";
$^ = "EMPLOYEE_HEADER";
$% = "EMPLOYEE_PAGE_HEADER";
$= = 30;

@n = ("Ali", "Raza", "Jaffer"); 
@a = (20, 30, 40);
@s = (2000.00, 2500.00, 4000.000);

#	Ongoing: 2021-02-19T16:05:20AEDT not printing page header?
$i = 0;
foreach (@n) {
	$name = $_;
	$age = $a[$i];
	$salary = $s[$i];
	$i++;
	write;
}


