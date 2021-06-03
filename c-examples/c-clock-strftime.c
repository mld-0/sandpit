// C program to demonstrate the
// working of strftime()
#include <stdlib.h>
#include <stdio.h>
#include <time.h>
#include <string.h>
#define Size 50
 
int main ()
{
    time_t t ;
    struct tm *tmp ;
    char MY_TIME[Size];
    time( &t );
     
    //localtime() uses the time pointed by t ,
    // to fill a tm structure with the
    // values that represent the
    // corresponding local time.
     
    tmp = localtime( &t );

	char* _format = strdup("%FT%H:%M:%S%Z");
     
    // using strftime to display time
    size_t result = strftime(MY_TIME, sizeof(MY_TIME), _format, tmp);

	printf("result=(%lu)\n", result);
     
    printf("Formatted date & time : %s\n", MY_TIME );
    return(0);
}
