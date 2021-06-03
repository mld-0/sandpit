#include <stdio.h>
#include <stdlib.h>

void someFunction(int arg)
{
    printf("This is someFunction being called and arg is: %d\n", arg);
}

int compare(const void* left, const void* right)
{
    return (*(int*)right - *(int*)left);
}

int main()
{
	void (*pf)(int);
	pf = &someFunction;

	(pf)(5);
	pf(7);

	//	function pointer to comparison function for qsort()
	int (*cmp)(const void*, const void*);
	cmp = &compare;
	int values[] = {5, 7, 2, 4, 9, 8, 1};
	qsort(values, sizeof(values)/sizeof(*values), sizeof(*values), cmp);
	//	or use '&compare' instead of 'cmp'
	for (int i = 0; i < sizeof(values)/sizeof(*values); ++i) {
		printf("%d, ", values[i]);
	}

	return 0;
}

