#include <stdio.h>
#include <stdlib.h>
//	Headers for alternative method of getting file length in bytes
//#include <sys/types.h>
//#include <sys/stat.h>
//#include <unistd.h>

int main()
{
	FILE *fp;
	fp = fopen("allbytes.hex", "rb");
	if (fp == NULL) {
		perror("fopen error\n");
		exit(EXIT_FAILURE);
	}

	int file_bytes_len = 0;

	//	Get length of contents of file in bytes
	//int fd = fileno(fp);
	//struct stat _buf;
	//fstat(fd, &_buf);
	//file_bytes_len = _buf.st_size;
	//	or
	fseek(fp, 0L, SEEK_END);
	file_bytes_len = ftell(fp);
	rewind(fp);

	printf("file_bytes_len=(%d)\n", file_bytes_len);

	unsigned char *binary_data = calloc(file_bytes_len, sizeof(char));

	//	Read file_bytes_len bytes to binary_data
	fread(binary_data, sizeof(char), file_bytes_len, fp);

	for (int i = 0; i < file_bytes_len; ++i) {
		printf("%02x  ", *(binary_data+i));
	}

	return 0;
}
