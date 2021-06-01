#include <stdio.h>

#define VALUES_LEN 7

int main()
{
	int values[VALUES_LEN];
	int n;

	printf("Enter %d int values:\n", VALUES_LEN);
	for (int i = 0; i < VALUES_LEN; ++i) {
		scanf("%d", &n);
		if (n <= 0) {
			n = 1;
		}
		values[i] = n;
	}
	printf("\n");

	printf("values:\n");
	for (int i = 0; i < VALUES_LEN; ++i) {
		printf("values[%d] = %d\n", i, values[i]);
	}
	printf("\n");

	return 0;
}
