#include <stdlib.h>
#include <stdio.h>

int main()
{
	int n;
	printf("Enter int [1, 50]:\n");
	if (scanf("%d", &n) != 1) {
		perror("scanf error");
		exit(EXIT_FAILURE);
	}
	if (n < 1 || n > 50) {
		fprintf(stderr, "n=(%d) outside valid range\n", n);
		exit(EXIT_FAILURE);
	}

	int result_count = 0;
	for (int a = 0; a <= 9; ++a) {
		for (int b = 0; b <= 9; ++b) {
			for (int c = 0; c <= 9; ++c) {
				for (int d = 0; d <= 9; ++d) {
					if (a + b + c + d == n) {
						printf("%d + %d + %d + %d = %d\n", a, b, c, d, n);
						result_count++;
					}
				}
			}
		}
	}

	printf("result_count=(%d)\n", result_count);
	return 0;
}
