#include <stdlib.h>
#include <stdio.h>
#include <time.h>

int main()
{
	printf("Size of C Types:\n");
	printf("%-20s%-8s\n", "Type", "Bytes");
	printf("----------------------------\n");
	printf("%-20s\t%lu\n", "char", sizeof(char));
	printf("%-20s\t%lu\n", "int8_t", sizeof(int8_t));
	printf("%-20s\t%lu\n", "unsigned char", sizeof(unsigned char));
	printf("%-20s\t%lu\n", "uint8_t", sizeof(uint8_t));
	printf("%-20s\t%lu\n", "short", sizeof(short));
	printf("%-20s\t%lu\n", "int16_t", sizeof(int16_t));
	printf("%-20s\t%lu\n", "uint16_t", sizeof(uint16_t));
	printf("%-20s\t%lu\n", "int", sizeof(int));
	printf("%-20s\t%lu\n", "unsigned", sizeof(unsigned));
	printf("%-20s\t%lu\n", "size_t", sizeof(size_t));
	printf("%-20s\t%lu\n", "long", sizeof(long));
	printf("%-20s\t%lu\n", "unsigned long", sizeof(unsigned long));
	printf("%-20s\t%lu\n", "int32_t", sizeof(int32_t));
	printf("%-20s\t%lu\n", "uint32_t", sizeof(uint32_t));
	printf("%-20s\t%lu\n", "long long", sizeof(long long));
	printf("%-20s\t%lu\n", "int64_t", sizeof(int64_t));
	printf("%-20s\t%lu\n", "clock_t", sizeof(clock_t));
	printf("%-20s\t%lu\n", "unsigned long long", sizeof(unsigned long long));
	printf("%-20s\t%lu\n", "uint64_t", sizeof(uint64_t));
	printf("%-20s\t%lu\n", "float", sizeof(float));
	printf("%-20s\t%lu\n", "double", sizeof(double));
	printf("%-20s\t%lu\n", "long double", sizeof(long double));
	printf("%-20s\t%lu\n", "_Bool", sizeof(_Bool));

	return 0;
}
