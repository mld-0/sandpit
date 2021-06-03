#include <errno.h>
#include <stdio.h>
#include <stdlib.h>
#include <wchar.h>

int main(void)
{
	FILE    *stream;
	wchar_t  wcs[100];
	wint_t wc; 

   if ((stream = fopen("input-unicode.txt", "r")) == NULL) {
	  perror("fopen error\n");
      exit(1);
   }

	do {
		wc = fgetwc(stream);
		putwc(wc, stdout);
	} while (wc != WEOF);

   fclose(stream);
   return 0;
}

