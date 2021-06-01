#include <stdlib.h>
#include <stdio.h>

//	Works only for static arrays
#if !defined(ARRAY_SIZE)
    #define ARRAY_SIZE(x) (sizeof((x)) / sizeof((x)[0]))
#endif

//	Ongoing: 2021-05-27T01:04:30AEST On telling the difference between a (variable that is a) pointer and an array - one can't?

void A() 
{
	//	Using a dynamic array
	int count_chars_len = 3;  //	Define length and pass to calloc -> can't get length from dynamic array
	int *count_chars = calloc(0, count_chars_len * sizeof *count_chars);
	if (count_chars == NULL) {
		fprintf(stderr, "count_chars malloc error\n");
		exit(2);
	}
	//	Iterate over dynamic array
	for (int i = 0; i < count_chars_len; ++i) {
		printf("%d, ", *(count_chars+1));
	}
	printf("\n");
}

void B()
{
	// Equivelent, creation of fixed-length array (using literal)
	int count_chars[] = {0, 0, 0};
	int count_chars_len = sizeof(count_chars)/sizeof(*count_chars);  // Or use macro ARRAY_SIZE
	for (int i = 0; i < count_chars_len; ++i) {
	  	printf("%d, ", count_chars[i]);
	}
	printf("\n");
}

int main()
{
	// Different dynamic array declarations
	// Ongoing: 2021-05-26T22:47:26AEST The latter is better than the former (in C, if we consider our C seperate and apart from C++?)
	//int *count_chars = (int *) malloc(sizeof(int)*count_chars_len);
	//int *count_chars = malloc(count_chars_len * sizeof *count_chars);
	//int *count_chars = (int []) {0, 0, 0};
	//	In any even -> the prefered C++ declaration would be?
	//int *count_chars = new int[count_chars_len]

	A();
	B();

	return 0;
}

