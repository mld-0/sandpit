#include <stdio.h>

int main() 
{
	char id[11];  // length of string, plus 1 for NULL terminator
	int hours; 
	double pay_rate_hourly, pay_total;

	printf("Input employee ID (up to 10 chars):\n");
	//	Read up to 10 string characters
	if (scanf("%10s", id) != 1) {
		fprintf(stderr, "scanf failed");
		return 2;
	}
	printf("read id=(%s)\n\n", id);

	printf("Input working hours (int):\n");
	if (scanf("%d", &hours) != 1) {
		fprintf(stderr, "scanf failed");
		return 2;
	}
	printf("read hours=(%d)\n\n", hours);

	printf("Input hourly rate (double):\n");
	if (scanf("%lf", &pay_rate_hourly) != 1) {
		fprintf(stderr, "scanf failed");
		return 2;
	}
	printf("read pay_rate_hourly=(%lf)\n\n", pay_rate_hourly);

	pay_total = pay_rate_hourly * (double) hours;
	printf("pay_total=(%lf)\n", pay_total);

	return 0;
}
