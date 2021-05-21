#include <stdio.h>

//	scanf(const char *format, ...)
//		format		C 	

//		%d		int
//		%f		float
//		%c		char
//		%s		character string

//	scanf can handle multiple values:
//		scanf("%d, %i", &a, &b);
//	an '*' before type indicates it is to be skipped
//		scanf("%*d %i", &a, &b);

//	Returns number of values read successfully
//	Behaviour of binary using scanf when run in non-interactive context?
//	fscanf(FILE *ptc, const char *format, ...), as per scanf(), for reading from files
//	fgets() is 'better' than scanf() (for reading multi-line data)
//	gets() is used IRL, scanf generally ... isn't?

int main() 
{
	int x, y, sum;
	int rc;

	printf("Enter first integer\n");
	if (scanf("%d", &x) != 1) {
		fprintf(stderr, "Failed to read first integer\n");
		return 2;
	}
	printf("got x=(%i)\n\n", x);

	printf("Enter the second integer\n");
	if (scanf("%d", &y) != 1) {
		fprintf(stderr, "Failed to read second integer\n");
		return 2;
	}
	printf("got y=(%i)\n\n", y);

	sum = x + y;
	printf("sum=(%d)\n", sum);

	return 0;
}

