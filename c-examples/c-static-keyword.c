#include <stdio.h>
#include <stdlib.h>

//	'static' in C vs C++:
//	LINK: https://stackoverflow.com/questions/943280/difference-between-static-in-c-and-static-in-c
//	When used at file level (outside of a function), it sets the visibility of the item it's applied to. Static items are not visible outside of their compilation unit (e.g., to the linker). Their duration is the same as the duration of the program. These file-level items (functions and data) should be static unless there's a specific need to access them from outside (and there's almost never a need to give direct access to data since that breaks the central tenet of encapsulation). If (as your comment to the question indicates) this is the only use of static you're concerned with then, no, there is no difference between C and C++.
//	When used within a function, it sets the duration of the item. Again, the duration is the same as the program and the item continues to exist between invocations of that function. It does not affect the visibility of that item since it's visible only within the function. An example is a random number generator that needs to keep its seed value between invocations but doesn't want that value visible to other functions.
//	C++ has one more use, static within a class. When used there, it becomes a single class variable that's common across all objects of that class. One classic example is to store the number of objects that have been instantiated for a given class.

int runner();
static void fun(void);

//	Declaring a global variable as static reduces its scope to file it is defined it
static int myvar = 23;

int main()
{
    printf("%d\n", runner());
    printf("%d\n", runner());
	printf("count=(%d)\n", count);
	fun();
    return 0;
}

int runner()
{
	//	static variables exist of lifetype of <program> containing them, a static variable in a function keeps its value between invocations
	static int count = 0;
	count++;
	return count;
}

//	Declaring a function as static reduces scope of function to file containing it
static void fun(void)
{
	printf("I am a static function\n");
}

//	Declare that function argument array 'a' contains at least a given number of values
//	int someFunction(char a[static 10])
