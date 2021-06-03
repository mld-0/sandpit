#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main() 
{
	long CMD_ALL_MAX = 1024 * 1024;  // 1 MB
	char cmd_out_all[CMD_ALL_MAX];
	long CMD_LINE_MAX = 10 * 1024;  // 10 kB
	char cmd_out_line[CMD_LINE_MAX];

	FILE *fp_system_cmd;
	int status;

	// command to use: list contents of $HOME
	//char *cmd_str = "ls ~";
	char *cmd_str = "echo $SHELL";

	//	Execute cmd_str with popen(), and open resulting stream
	fp_system_cmd = popen(cmd_str, "r");
	if (fp_system_cmd == NULL) {
		perror("fp_system_cmd=popen() error\n"); 
		exit(2);
	}

	//	Read cmd_str results line-by-line, appending to cmd_out_all
	long _strncat_remaining;
	while (fgets(cmd_out_line, CMD_LINE_MAX, fp_system_cmd) != NULL) { 
		_strncat_remaining = CMD_ALL_MAX - strlen(cmd_out_all);
		strncat(cmd_out_all, cmd_out_line, _strncat_remaining);
	    	printf("cmd_out_line=(%s)\n", cmd_out_line);
	}
	printf("\n");

	status = pclose(fp_system_cmd);
	if (status == -1) {
		perror("pclose error\n");
		exit(2);
	}

	printf("cmd_out_all=(%s)\n", cmd_out_all);
	printf("strlen(cmd_out_all)=(%lu)\n", strlen(cmd_out_all));

	return 0;	
}


