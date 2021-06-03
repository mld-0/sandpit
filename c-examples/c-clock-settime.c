/*  This program sets the clock forward 1 day. */

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <time.h>

int main( void )
  {
    struct timespec stime;

    if( clock_gettime( CLOCK_REALTIME, &stime) == -1 ) {
       perror( "getclock" );
       return EXIT_FAILURE;
    }

    stime.tv_sec += (60*60)*24L;  /* Add one day */
    stime.tv_nsec = 0;
    if( clock_settime( CLOCK_REALTIME, &stime) == -1 ) {
       perror( "setclock" );
       return EXIT_FAILURE;
    }
    return EXIT_SUCCESS;
  }
