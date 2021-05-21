#include <stdio.h>
#include <stdlib.h>

int main()
{
	int x = 56;
	int y = 9;
	printf("x=(%d), y=(%d)\n", x, y);

	//	Using XORs: 
	//	LINK: https://www.geeksforgeeks.org/swap-two-numbers-without-using-temporary-variable/
	x ^= y;  // x = x ^ y;
	y ^= x;  // y = y ^ x; (this is the same as x ^ y ?)
	x ^= y;  // x = x ^ y;

	// This can be achieved in one line with:
	// LINK: https://www.geeksforgeeks.org/swap-two-variables-in-one-line-in-c-c-python-php-and-java/
	// (x ^= y), (y ^= x), (x ^= y);

	printf("x=(%d), y=(%d)\n", x, y);
	return 0;
}
