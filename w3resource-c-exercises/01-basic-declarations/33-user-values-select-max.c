#include <stdio.h>
#include <stdlib.h>

#define VALUES_COUNT 5

int main() 
{
	//	How much 'messier' would it be in C to get values from the user, then have an array of that many values?
	int values[VALUES_COUNT];

	printf("Enter %i (int) values:\n", VALUES_COUNT);

	//	Get VALUES_COUNT integers from user - this works whether the integers are entered one-per-line, all on one line, or some combination
	for (int i = 0; i != VALUES_COUNT; ++i) {
		if (scanf("%i", &values[i]) != 1) {
			fprintf(stderr, "scanf error\n");
			exit(2);
		}
	}
	printf("\n\n");

	//	Initalize max_index as 0, and max_val as corresponding 0th element. In python, I would use -1 to denote max_index as 'unchecked', and max_val None for the same reason -> since C doesn't allow this, the 'neatest' solution is to initalize both to the first element of the array and then check the rest?
	int max_index = 0;
	int max_val = values[0];

	for (int i = 1; i != VALUES_COUNT; ++i) {
		if (max_val < values[i]) {
			max_index = i;
			max_val = values[i];
		}
	}

	printf("max_index=(%i)\n", max_index);
	printf("max_val=(%i)\n", max_val);

	return 0;
}

