#include <stdio.h> 

//	Specifying GCC Standards
//		-std=c90
//		-std=c99
//		-std=c11
//		-std=c18	(Default, current standard)

int main(int argc, char** argv) 
{
	printf("__STDC_VERSION__=(%li)\n", __STDC_VERSION__);

	for (int i = 0; i < 1000000; ++i) {
		;
	}

	#if __STDC_VERSION__ >=  201710L
	printf("We are using C18!\n");
	#elif __STDC_VERSION__ >= 201112L
	printf("We are using C11!\n");
	#elif __STDC_VERSION__ >= 199901L
	printf("We are using C99!\n");
	#else
	printf("We are using C89/C90!\n");
	#endif
	return 0;
}

