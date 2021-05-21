#include <stdlib.h>
#include <stdio.h>

int main() 
{
	double perimeter = 0.0, area = 0.0;
	double a, b, c;

	printf("Enter lengths (doubles) a, b, c: (suggest 25, 15, 35)\n");
	if (scanf("%lf %lf %lf", &a, &b, &c) != 3) {
		fprintf(stderr, "scanf failed\n");
		exit(2);
	}
	printf("read a=(%f), b=(%f), c=(%f)\n\n", a, b, c);

	//	Using the Triangle Inequality Theorem - can [a, b, c] form a triangle
	if (a < (b+c) && b < (a+c) && c < (b+a)) {
		perimeter = a + b + c;
		area = (a + b + c) / 2.0;
		printf("perimeter=(%f)\n", perimeter);
		printf("area=(%f)\n", area);
	} else { 
		printf("Impossible to create triangle\n");
	}

	return 0;
}

