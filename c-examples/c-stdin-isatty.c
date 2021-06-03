#include <stdio.h>
#include <unistd.h>


int main()
{
	if (isatty(fileno(stdin)))
		puts("stdin is connected to a terminal");
	else
		puts("stdin is NOT connected to a terminal");

	return 0;
}
