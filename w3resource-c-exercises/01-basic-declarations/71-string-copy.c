#include <stdlib.h>
#include <stdio.h>
#include <string.h>

//	char * strcpy(char * destination, const char * source)
//	Copies the C string pointed by source into the array pointed by destination, including the terminating null character (and stopping at that point). To avoid overflows, the size of the array pointed by destination shall be long enough to contain the same C string as source (including the terminating null character), and should not overlap in memory with source. Function also returns copied string. Provided by <string.h>

int main()
{
	char str_input[] = "w3resource example c-string";
	printf("str_input=(%s)\n", str_input);
	printf("len(str_input)=(%lu)\n", sizeof(str_input)/sizeof(*str_input));
	printf("strlen(str_input)=(%lu)\n", strlen(str_input));
	printf("\n");

	char str_copy[100];
	printf("Before copy:\n");
	printf("str_copy=(%s)\n", str_copy);
	printf("len(str_copy)=(%lu)\n", sizeof(str_copy)/sizeof(*str_copy));
	printf("strlen(str_copy)=(%lu)\n", strlen(str_copy));
	printf("\n");

	char *result = strcpy(str_copy, str_input);
	printf("After copy:\n");
	printf("str_copy=(%s)\n", str_copy);
	printf("len(str_copy)=(%lu)\n", sizeof(str_copy)/sizeof(*str_copy));
	printf("strlen(str_copy)=(%lu)\n", strlen(str_copy));

	return 0;
}

