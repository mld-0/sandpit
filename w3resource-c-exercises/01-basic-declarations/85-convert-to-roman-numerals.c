#include <stdlib.h>
#include <stdio.h>
#include <string.h>

void to_roman_numeral(int x, char* result, size_t result_max_len)
{
	int n = x;

	if (n >= 4000) {
		fprintf(stderr, "Out of range n=(%d), largest supported value is 3999\n", n);
		exit(2);
	}

	//	result must be an empty string, with buffer length result_max_len
	strncpy(result, "", result_max_len);

	int result_len_remaining;
	while (n != 0)
	{
		//	strncat() restricts the size of the string being appened, not the size of the resulting string, so use 'result_len_remaining' -> number of characters remaining in buffer 'result'
		result_len_remaining = result_max_len - strlen(result);

		if (n >= 1000) {
			strncat(result, "M", result_len_remaining);
			n -= 1000;
		}
		else if (n >= 900) {
			strncat(result, "CM", result_len_remaining);
			n -= 900;
		}
		else if (n >= 500) {
			strncat(result, "D", result_len_remaining);
			n -= 500;
		}
		else if (n >= 400) {
			strncat(result, "CD", result_len_remaining);
			n -= 400;
		}
		else if (n >= 100) {
			strncat(result, "C", result_len_remaining);
			n -= 100;
		}
		else if (n >= 90) {
			strncat(result, "XC", result_len_remaining);
			n -= 90;
		}
		else if (n >= 50) {
			strncat(result, "L", result_len_remaining);
			n -= 50;
		}
		else if (n >= 40) {
			strncat(result, "XL", result_len_remaining);
			n -= 40;
		}
		else if (n >= 10) {
			strncat(result, "X", result_len_remaining);
			n -= 10;
		}
		else if (n >= 9) {
			strncat(result, "IX", result_len_remaining);
			n -= 9;
		}
		else if (n >= 5) {
			strncat(result, "V", result_len_remaining);
			n -= 5;
		}
		else if (n >= 4) {
			strncat(result, "IV", result_len_remaining);
			n -= 4;
		}
		else if (n >= 1) {
			strncat(result, "I", result_len_remaining);
			n -= 1;
		}
	}
}

int main()
{
	int result_max_len = 50;
	int value;
	char result[result_max_len];

	value = 560;
	to_roman_numeral(value, result, result_max_len);
	printf("value=(%d)\n", value);
	printf("result=(%s)\n", result);

	value = 3999;
	to_roman_numeral(value, result, result_max_len);
	printf("value=(%d)\n", value);
	printf("result=(%s)\n", result);

	return 0;
}
