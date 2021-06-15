#include <stdio.h>
#include <unistd.h>
#include <errno.h>


int main()
{
	if (isatty(fileno(stdin)))
		puts("stdin is connected to a terminal");
	else
		puts("stdin is NOT connected to a terminal");

	if (isatty(fileno(stdout)))
		puts("stdout is connected to a terminal");
	else
		puts("stdout is NOT connected to a terminal");
	
	//	Get 
	char *result = ttyname(fileno(stdin));
	if (!result) {
		perror("ttyname returned null for stdin");
		printf("errno=(%d)\n", errno);
	}
	printf("result=(%s)\n", result);

	char *result_ctermid = ctermid(NULL);
	printf("result_ctermid=(%s)\n", result_ctermid);

	return 0;
}
