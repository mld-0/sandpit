#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define __is_constant_int(X) _Generic((&X), \
        const int *: "const int", \
        int *:       "non-const int")

int main()
{
	char ch1[] = "abcdef";
	printf("strlen(ch1)=(%lu)\n", strlen(ch1));
	char ch2[7];
	strcpy(ch2, ch1);
	printf("ch2=(%s)\n", ch2);

	const int i = 1;
	printf("i=(%d)\n", __builtin_constant_p(i));
	int j = 1;
	printf("j=(%d)\n", __builtin_constant_p(j));

	printf("%d\n", BUFSIZ);
	int a = printf("%d\n", EOF);
	printf("%d\n", a);
	return 0;
}
