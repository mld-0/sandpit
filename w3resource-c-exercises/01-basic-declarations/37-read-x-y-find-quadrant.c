#include <stdio.h>
#include <stdlib.h>

int main()
{
	double coords[2];
	printf("Enter coordinates (doubles) (x, y):\n");

	for (int i = 0; i < 2; ++i) {
		if (scanf("%lf", &coords[i]) != 1) {
			fprintf(stderr, "scanf error\n");
			exit(2);
		}
	}
	printf("\n");
	printf("x=(%lf), y=(%lf)\n\n", coords[0], coords[1]);

	char *quadrant_str;

	if (coords[0] > 0 && coords[1] > 0) {
		quadrant_str = "Quadrant I (+,+)";
	} else if (coords[0] > 0 && coords[1] < 0) {
		quadrant_str = "Quadrant II (+,-)";
	} else if (coords[0] < 0 && coords[1] < 0) {
		quadrant_str = "Quadrant III (-,-)";
	} else if (coords[0] < 0 && coords[1] > 0) {
		quadrant_str = "Quadrant IV (-,+)";
	} else if (coords[0] == 0 || coords[1] == 0) {
		printf("Zero value in coordinates - cannot place in quadrant\n");
		exit(0);
	} else {
		fprintf(stderr, "coordinates do not correspond to a quadrant, but are also not zero - this should not be possible?\n");
		exit(2);
	}

	printf("quadrant_str=(%s)\n", quadrant_str);
	return 0;
}
