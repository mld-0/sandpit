#include <stdio.h>

int main() 
{
	int s_input, h, m, s;
	
	printf("Input value (int) seconds:\n");
	if (scanf("%d", &s_input) != 1) {
		fprintf(stderr, "scanf failed\n");
		return 2;
	}

	h = s_input / 3600;
	m = (s_input - (3600 * h)) / 60;
	s = s_input - (3600 * h) - (60 * m);

	printf("H:M:S -> %d:%d:%d\n", h, m, s);

	return 0;
}
