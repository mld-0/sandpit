#include <stdlib.h>
#include <stdio.h>

/*	Pascals Triangle (the binomial coefficents)
 *		The value of the i-th value, of the n-th line is given by
 *			F(n, i) = n! / ( (n-i)! * i! ) 
 *		The number of values in the n-th line is equal to the line number.
 *	*/

long factorial(int x) 
{
	long result = 1;
	while (x > 1) {
		result = result * x;
		--x;
	}
	return result;
}

long binomial_coefficent(int line, int row) 
{
	if (row > line) {
		fprintf(stderr, "Error, row=(%d) > line=(%d)\n", row, line);
		exit(2);
	}
	long result = factorial(line) / ( factorial(line-row) * factorial(row) );
	return result;
}

int main() 
{
	int rows_limit = 11;
	long value;
	char *delim = "\t";
	for (int line = 0; line < rows_limit; ++line) {
		//	Print leading tabs, such that our triangle is symetrical
		for (int i = 0; i < (rows_limit-line-1)/2; ++i) {
			printf("%s", delim);
		}
		for (int row = 0; row <= line; ++row) {
			value = binomial_coefficent(line, row);
			printf("%ld%s", value, delim);
		}
		printf("\n");
	}
	return 0;
}

