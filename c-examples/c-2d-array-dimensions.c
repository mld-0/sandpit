#include <stdio.h>

#define LEN(arr) ((int) (sizeof (arr) / sizeof (arr)[0]))

int main(void)
{
    int result[10][7];

    printf("Number of rows: %d\n", LEN(result));
    printf("Number of columns: %d\n", LEN(result[0]));

	for (int i = 0; i < LEN(result); ++i) {
		for (int j = 0; j < LEN(result[0]); ++j) {
			printf("%d, ", result[i][j]);
		}
		printf("\n");
	}
	printf("\n");

    return 0;
}

