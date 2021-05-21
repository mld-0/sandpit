#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int main() 
{
	int month_num;

	printf("Select month number [1,12]:\n");
	if (scanf("%i", &month_num) != 1) {
		fprintf(stderr, "scanf failure\n");
		exit(2);
	}
	printf("month_num=(%i)\n\n", month_num);

	char *month_name = NULL;

	switch (month_num) {
		case 1: month_name = "January"; break;
		case 2: month_name = "Febuary"; break;
		case 3: month_name = "March"; break;
		case 4: month_name = "April"; break;
		case 5: month_name = "May"; break;
		case 6: month_name = "June"; break;
		case 7: month_name = "July"; break;
		case 8: month_name = "August"; break;
		case 9: month_name = "September"; break;
		case 10: month_name = "October"; break;
		case 11: month_name = "Novemeber"; break;
		case 12: month_name = "December"; break;
		default: fprintf(stderr, "Invalid month_num=(%i)\n", month_num); exit(2);
	}

	printf("strlen(month_name)=(%lu)\n", strlen(month_name));
	printf("month_name=(%s), (%p)\n", month_name, month_name);
	printf("\n");

	//	Print month_name values as hex and char
	printf("month_name c-string hex:\n");
	char loop_c;
	for (int i = 0; i < strlen(month_name); ++i) {
		printf("%x ", month_name[i]);
	}
	printf("\n");
	for (int i = 0; i < strlen(month_name); ++i) {
		printf("%c  ", month_name[i]);
	}
	printf("\n");
	printf("(%x)\n", *(month_name+9));
	printf("(%c)\n", *(month_name+9));
	printf("\n");
	

	return 0;
}

