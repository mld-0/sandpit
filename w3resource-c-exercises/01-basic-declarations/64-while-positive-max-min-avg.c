#include <stdlib.h>
#include <stdio.h>

int main()
{
	int max = 0, min = 0;
	int current = 1;
	int n = 0;
	long sum = 0;

	printf("Enter (int) values, then 0 to exit\n");
	while (current > 0) {
		if (scanf("%d", &current) != 1) {
			fprintf(stderr, "scanf error\n");
			exit(2);
		}
		if (current <= 0) 
			break;

		if (n == 0 || max < current) {
			max = current;
		}
		if (n == 0 || min > current) {
			min = current;
		}

		sum += (long) current;
		++n;
	}

	double avg = (double) sum / (double) n;

	printf("n=(%d)\n", n);
	printf("sum=(%li)\n", sum);
	printf("avg=(%lf)\n", avg);
	printf("min=(%d)\n", min);
	printf("max=(%d)\n", max);
	
	return 0;
}

