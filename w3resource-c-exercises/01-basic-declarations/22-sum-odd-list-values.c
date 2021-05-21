#include <stdlib.h>
#include <stdio.h>

int main()
{
	int values[5];
	int result = 0;

	printf("Enter five list values (ints):\n");
	if (scanf("%d %d %d %d %d", &values[0], &values[1], &values[2], &values[3], &values[4]) != 5) {
		fprintf(stderr, "scanf read five values failure\n");
		exit(2);
	}

	for (int i = 0; i < 5; ++i) {
		if (values[i] % 2 != 0) {
			result += values[i];
		}
	}

	printf("result=(%i)\n", result);

	return 0;
}

