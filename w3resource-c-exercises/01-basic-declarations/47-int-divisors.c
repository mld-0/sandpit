#include <stdio.h>
#include <stdlib.h>

int main()
{
	int x;
	printf("Enter (positive int) value:\n");
	if (scanf("%d", &x) != 1) {
		fprintf(stderr, "scanf error\n");
		exit(2);
	}
	printf("x=(%d)\n\n", x);

	printf("divisors:\n");
	for (int i = 1; i < x; ++i) {
		if (x % i == 0) {
			printf("%d, ", i);
		}
	}
	printf("\n");

	return 0;
}
