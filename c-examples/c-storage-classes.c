#include <stdio.h>

//	LINK: https://www.tutorialspoint.com/cprogramming/c_storage_classes.htm

int main()
{
	//	Storage classes:
	//		auto
	//		register
	//		static
	//		extern
	
	//	auto
	//		default storage class for local variables (in functions)

	//	register
	//		define variable that should be stored in a register instead of RAM
	//		variable has maximum size given by register size, and can't have '&' memory location operator applied to it

	// 	static
	// 		Keep variable in existance during lifetime of program - allows variable to maintain value between calls
	// 		restricts (global) variable scope to file in which variable is declared

	//	extern
	//	Make global variable declared in one file visible in another file
	//	extern variables cannot be initalized

	return 0;
}
