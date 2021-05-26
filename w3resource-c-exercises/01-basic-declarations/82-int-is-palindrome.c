#include <stdlib.h>
#include <stdio.h>
#include <string.h>

char *strrev(char *str);

int is_palindrome(int x)
{
	int buffsize = 25;
	char x_str[buffsize];
	char x_str_rev[buffsize];
	
	snprintf(x_str, buffsize, "%d", x);
	snprintf(x_str_rev, buffsize, "%d", x);
	strrev(x_str_rev);

	if (strcmp(x_str, x_str_rev) == 0) {
		return 1;
	} else {
		return 0;
	}
}

int main() 
{
	int value, result;

	value = 123456789;
	result = is_palindrome(value);
	printf("value=(%d)\n", value);
	printf("result=(%d)\n", result);
	printf("\n");

	value = 7235327;
	result = is_palindrome(value);
	printf("value=(%d)\n", value);
	printf("result=(%d)\n", result);

	return 0;
}

//	strrev() is not included in <string.h> - So we define our own
char *strrev(char *str)
{
    if (!str || ! *str)
        return str;
    int i = strlen(str) - 1, j = 0;
    char ch;
    while (i > j)
    {
        ch = str[i];
        str[i] = str[j];
        str[j] = ch;
        i--;
        j++;
    }
    return str;
}

