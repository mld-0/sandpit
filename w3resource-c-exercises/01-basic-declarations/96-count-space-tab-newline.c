#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int main()
{
	int count_chars[] = {0, 0, 0};
	for (int i = 0; i < sizeof(count_chars)/sizeof(*count_chars); ++i) {
		printf("%d, ", count_chars[i]);
	}
	printf("\n");

	printf("count_chars=(%lu)\n", sizeof(count_chars)/sizeof(*count_chars));	


	return 0;
}
