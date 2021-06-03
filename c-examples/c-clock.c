#include <stdlib.h>
#include <stdio.h>
#include <time.h>

int main()
{
	clock_t a = clock();
	printf("a=(%lu)\n", a);
	printf("a=(%lu)\n", sizeof(a));
	return 0;
}
