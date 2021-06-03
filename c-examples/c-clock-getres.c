#include <stdio.h>
#include <stdlib.h>
#include <inttypes.h>
#include <time.h>

int main() 
{
	printf("%d\n", CLOCK_REALTIME);
	printf("%d\n", CLOCK_MONOTONIC);

	struct timespec resolution;

    if (clock_gettime(CLOCK_REALTIME, &resolution) == -1) {
        perror("clock_gettime");
        exit(2);
    }

	if (clock_getres(CLOCK_REALTIME, &resolution) == -1) {
		perror("clock_getres");
		exit(2);
	}
	printf("resolution=(%jd.%09ld)\n", (intmax_t) resolution.tv_sec, resolution.tv_nsec);

	if (clock_getres(CLOCK_MONOTONIC, &resolution) == -1) {
		perror("clock_getres");
		exit(2);
	}
	printf("resolution=(%jd.%09ld)\n", (intmax_t) resolution.tv_sec, resolution.tv_nsec);

	return 0;
}

