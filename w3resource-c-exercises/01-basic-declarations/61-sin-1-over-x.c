#include <stdlib.h>
#include <stdio.h>
#include <math.h>

int main()
{
	double x;
	printf("Input (double) x:\n");
	if (scanf("%lf", &x) != 1) {
		fprintf(stderr, "scanf error\n");
		exit(2);
	}
	printf("x=(%lf)\n", x);

	if (x == 0) {
		fprintf(stderr, "Cannot invert zero\n");
		exit(2);
	}

	double result = sin(1/x);
	printf("result=(%0.4lf)\n", result);

	return 0;
}
