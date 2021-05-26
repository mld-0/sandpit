#include <stdlib.h>
#include <stdio.h>
#include <math.h>

int main()
{
	long result_a;
	double result_b;
	long powerof_count = 10;

	for (long i = 0; i <= powerof_count; ++i) {
		result_a = pow(2, i);
		result_b = pow(2, -1*i);

		printf("%ld\t%ld\t%lf\n", i, result_a, result_b);
	}

	return 0;
}
