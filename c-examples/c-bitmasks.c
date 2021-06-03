#include <stdio.h>
#include <stdlib.h>

char *decimal_to_binary(int n);

int main()
{
	int storage = 57;
	int n = 2;

	//	Set bit n: OR with 2**n
	storage |= 1 << n;
	printf("storage=(%s)\n", decimal_to_binary(storage));
	
	//	Clear bit n: AND with inverse of 2**n
	storage &= ~(1 << n);
	printf("storage=(%s)\n", decimal_to_binary(storage));

	//	Flip big n: XOR with 2**n
	storage ^= 1 << n;
	printf("storage=(%s)\n", decimal_to_binary(storage));

	//	Check bit n: AND with 2**n
	int bit = storage & (1 << n);
	printf("    bit=(%s)\n", decimal_to_binary(bit));

	return 0;
}

char *decimal_to_binary(int n)
{
  int c, d, t = 0;
  char *p = (char*)malloc(32+1);
  if (p == NULL)
    exit(EXIT_FAILURE);
  for (c = 31 ; c >= 0 ; c--) {
    d = n >> c;
    if (d & 1)
      *(p+t) = 1 + '0';
    else
      *(p+t) = 0 + '0';
    t++;
  }
  *(p+t) = '\0';
  return  p;
}
