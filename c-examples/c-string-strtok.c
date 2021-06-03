#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int main()
{

	//	string is required to be mutable - make copy of (what should be a const)
	//char *str1 = "1,6,23,7,9,4";
	//char str2[] = "1,6,23,7,9,4";
	//char *str = strdup(str1);

	//char str[] = "abc,6,23,7,9,4";
	char str[] = "abcder";
	char *token;
	char *ptr = str;
	char *delim = ",";
	while ((token = strtok(ptr, delim)) != NULL)
	{
		printf("token=(%s)\n", token);
		ptr = NULL;  // Replacing pointer with null to advance through buffer at last pointer recieved
	}

    //char str[] = "Geeks-for-Geeks";
    //// Returns first token
	//printf("str=(%s)\n", str);
    //char* token = strtok(str, "-");
	//printf("str=(%s)\n", str);
  
    //// Keep printing tokens while one of the
    //// delimiters present in str[].
    //while (token != NULL) {
    //    printf("%s\n", token);
    //    token = strtok(NULL, "-");
    //}

	return 0;
}
