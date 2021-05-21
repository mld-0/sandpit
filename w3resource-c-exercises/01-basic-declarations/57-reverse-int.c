#include <stdlib.h>
#include <stdio.h>

int main()
{
	int value;
	printf("Enter value (int) value:\n");

	if (scanf("%d", &value) != 1) {
		fprintf(stderr, "scanf error");
		exit(2);
	}
	printf("value=(%d)\n", value);

	//	Numerical implementation of integer 'reversal' -> alternative, use a string and reverse that?
	int loop_digit, value_reversed = 0;
	while (value >= 1) {
		loop_digit = value % 10;
		value_reversed = value_reversed * 10 + loop_digit;
		value = value / 10;

		printf("loop_digit=(%d), value_reversed=(%d), value=(%d)\n", loop_digit, value_reversed, value);
	}
	printf("value_reversed=(%d)\n", value_reversed);

	return 0;
}
