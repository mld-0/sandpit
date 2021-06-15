#include <stdio.h>
#include <stdlib.h>

//	argc: [ar]gument [c]ount
//		number of command-line arguments. (At least 1, because argv[0] is the command used to invoke program).

//	argv	[ar]gument [v]ector

int main(int argc, char *argv[])
{
	printf("argc=(%d)\n", argc);
	printf("argv[0]=(%s)\n", argv[0]);
	return 0;
}
