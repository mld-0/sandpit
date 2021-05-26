#include <stdio.h>
#include <stdio.h>

int main()
{
	char c;

	for (c = 'A'; c <= 'z'; ++c) {
		if (c > 'Z' && c < 'a') 
			continue;
		printf("[%2d:%c]", c, c);
	}
	printf("\n");

	return 0;
}
