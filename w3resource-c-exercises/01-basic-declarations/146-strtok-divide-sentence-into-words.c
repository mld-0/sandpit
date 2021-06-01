#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define _str_len 1024

int main()
{
	char _str[_str_len];
	char *_delim = strdup(" .,\n");
	char *loop_word;

	printf("Enter sentence (single line):\n");
	fgets(_str, _str_len, stdin);

	for (loop_word = strtok(_str, _delim); loop_word != NULL; loop_word = strtok(NULL, _delim)) {
		printf("loop_word=(%s)\n", loop_word);
	}
	
	return 0;
}
