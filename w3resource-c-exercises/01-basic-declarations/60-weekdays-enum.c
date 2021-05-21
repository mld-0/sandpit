#include <stdlib.h>
#include <stdio.h>

//	About C enums
//	LINK: https://www.geeksforgeeks.org/enumeration-enum-c/
//		Enum is used to assign names to constants
//		Multiple enum names can have the same value
//		Values can be explicitly specified, or left to the compiler (which will assign 0, 1, ...)
//		Enum values do not need to be ordered. 
//		If some names are assigned values and others are not, the unassigned names will have the value of the previous name plus 1.
//		Enum names must be unique within their scope
//		Enums do not provde value->name lookup

int main()
{
	enum weekdays {Sun, Mon, Tue, Wed, Thu, Fri, Sat};

	printf("Sun = %d\n", Sun);
	printf("Mon = %d\n", Mon);
	printf("Tue = %d\n", Tue);
	printf("Wed = %d\n", Wed);
	printf("Thu = %d\n", Thu);
	printf("Fri = %d\n", Fri);
	printf("Sat = %d\n", Sat);
	printf("\n");

	//	Iterating over enum (this is equivelent to substituting s/Sun/0/ and s/Sat/6/)
	for (int i = Sun; i <= Sat; ++i) {
		printf("%i, ", i);
	}
	printf("\n");

	return 0;
}
