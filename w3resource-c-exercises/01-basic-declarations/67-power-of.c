#include <stdlib.h>
#include <stdio.h>
#include <math.h>

int main()
{
	double a = 9.0;
	printf("a=(%lf)\n", a);

	int b = 4;
	printf("b=(%d)\n", b);

	int n = 3;
	printf("n=(%i)\n", n);

	int z = pow(b, n);
	printf("z=(%d)\n", z);

	double y = pow(a, n);	
	printf("y=(%lf)\n", y);

	return 0;
}
