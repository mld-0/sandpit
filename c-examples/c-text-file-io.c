#include <stdio.h>
#include <stdlib.h>

int main()
{
	char filename[] = "input-unicode.txt";

	FILE *fp;
	fp = fopen(filename, "r");
	if (fp == NULL) {
		perror("fopen error\n");
		exit(EXIT_FAILURE);
	}

	int c;
	while ((c = getc(fp)) != EOF) {
		putchar(c);
	}

	fclose(fp);

	return 0;
}
