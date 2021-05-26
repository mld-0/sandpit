#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//	int snprintf(char *s, size_t n, cost char * format, ...)
//		Composes a string wit the same text that would be printed if format were used with printf, and store result as C-string in buffer s (taking n as maximum buffer capacity to fill).
//		(or sprintf - equivelent without buffer size argument)

//	char * itoa(int value, char *str, int base)
//		Convert integer value to null-terminated string useing the specified base and store result in array given by str

int main()
{
	int value_int = 2345678;
	printf("value_int=(%d)\n", value_int);

	int buffer_size = 20;
	char value_str[buffer_size];

	//	Integer to string, 
	//	using snprintf (more portable than itoa)
	snprintf(value_str, buffer_size, "%d", value_int);
	printf("value_str=(%s)\n", value_str);
	
	//	using itoa (not supported by gcc/clang?)
	//itoa(value_int, value_str);
	//printf("value_int=(%d)\n", value_int);
	
	for (int i = 0; i < strlen(value_str); ++i) {
		printf("%c\n", value_str[i]);
	}

	return 0;
}
