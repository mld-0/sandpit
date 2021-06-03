#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>

int main() 
{

	char *r = strdup("abc,123,456,789");
	char *stringp = r;
	char *token;
	char *delim = ",";
	while ((token = strsep(&stringp, delim)) != NULL) {
		printf("token=(%s)\n", token);
	}
	free(r);

	//char str[] = "abc,6,23,7,9,4";
	//char *tokenen;
	//char *ptr = str;
	//char *delim = ",";
	//while ((tokenen = strtoken(ptr, delim)) != NULL)
	//{
	//	printf("tokenen=(%s)\n", tokenen);
	//	ptr = NULL;  // Replacing pointer with null to advance through buffer at last pointer recieved
	//}

	return 0;

}
