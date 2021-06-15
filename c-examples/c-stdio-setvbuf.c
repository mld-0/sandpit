#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

int main () {
   char buff[1024];

   memset( buff, '\0', sizeof( buff ));

   fprintf(stdout, "Going to set full buffering on\n");
   setvbuf(stdout, buff, _IOFBF, 1024);

   fprintf(stdout, "This is tutorialspoint.com\n");
   fprintf(stdout, "This output will go into buff\n");

   fprintf(stdout, "and this will appear when programm\n");
   //sleep(2);
   //fflush( stdout );
   //sleep(2);
   fprintf(stdout, "will come after sleeping 2 seconds\n");
   sleep(2);
   fflush(stdout);


   return(0);
}
