#include <stdio.h>
#include <stdlib.h>

void bin(unsigned n)
{
    unsigned i;
    for (i = 1 << 31; i > 0; i = i / 2)
        (n & i) ? printf("1") : printf("0");
}

int main()
{
	int x = 27;
	printf("x=(%d)\n", x);
	bin(x);
	printf("\n\n");

	int result = x << 2;
	printf("result=(%d)\n", result);
	bin(result);
	printf("\n");

	return 0;
}
