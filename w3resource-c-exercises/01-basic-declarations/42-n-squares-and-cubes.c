#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main() 
{
	int n, _square, _cube;
	printf("Enter value (positive int) limit\n");
	if (scanf("%d", &n) != 1) {
		fprintf(stderr, "scanf error\n");
		exit(2);
	}
	printf("n=(%d)\n\n", n);

	printf("n, square, cube:\n");
	for (int i = 1; i <= n; ++i) {
		_square = pow(i, 2);
		_cube = pow(i, 3);

		printf("%d, %d, %d\n", i, _square, _cube);
	}
	
	return 0;
}
