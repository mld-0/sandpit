#include <stdio.h>
//	Not found on MacOS?
#include <stdio_ext.h>

int main(void)
{
    FILE *f;
    size_t bufsize;

    f = fopen("test.txt", "wb");
    if (f == NULL)
    {
        perror("fopen failed\n");
        return -1;
    }

    bufsize = __fbufsize(f);
    printf("The buffer size is %zd\n", bufsize);

    putc('\n', f);
    bufsize = __fbufsize(f);
    printf("The buffer size is %zd\n", bufsize);

    fclose(f);
    return 0;
}
