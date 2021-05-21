#include <stdio.h>
#include <math.h>

int main() 
{
	double result[2];
	double a, b, c;

	printf("Enter values a, b, c:\n");
	if (scanf("%lf %lf %lf", &a, &b, &c) != 3) {
		fprintf(stderr, "scanf failure\n");
		printf("a=(%lf), b=(%lf), c=(%lf)\n", a, b, c);
		return 2;
	}

	printf("a=(%lf), b=(%lf), c=(%lf)\n", a, b, c);

	//	TODO: 2021-05-19T23:27:18AEST C, how to handle quadratic formula, complex result case? (Is it a massive PITA?)
	result[0] = ((-1 * b) + sqrt(pow(b, 2) - 4 * a * c)) / (2 * a);
	result[1] = ((-1 * b) - sqrt(pow(b, 2) - 4 * a * c)) / (2 * a);

	printf("results=(%lf, %lf)\n", result[0], result[1]);

	return 0;
}
