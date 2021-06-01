#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define STRLEN 20

int main()
{
	//	Can't use fgets(), as it terminates after encountering newline, (and we want multi-line input)
	//fgets(_str, STRLEN, stdin);	

	//	Read input until _str is full, or EOF encountered, (<C-d> on Unix, <C-z> on Windows)
	char _str[STRLEN] = "";
	char input_char;
	int chars_remaining = STRLEN - 1;
	while (chars_remaining > 0 && (input_char = fgetc(stdin)) != EOF) {
		strcat(_str, &input_char);
		chars_remaining -= strlen(&input_char);		
	}

	int _str_len = strlen(_str);
	printf("_str=(%s)\n", _str);
	printf("_str_len=(%d)\n", _str_len);

	int _count_space = 0;
	int _count_tab = 0;
	int _count_newline = 0;

	int c;
	for (int i = 0; i != strlen(_str); ++i) {
		c = _str[i];
		if (c == ' ') {
			_count_space++;
		} 
		if (c == '\t') {
			_count_tab++;
		}
		if (c == '\n') {
			_count_newline++;
		}
	}

	printf("space=(%d), tab=(%d), newline=(%d)\n", _count_space, _count_tab, _count_newline);

	return 0;
}
