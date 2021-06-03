#include <stdlib.h>
#include <stdio.h>

//	LINK: https://www.geeksforgeeks.org/dynamically-allocate-2d-array-c/

void with_single_pointer();
void with_array_of_pointers();
void with_pointer_to_pointer();
void with_double_pointers();

int main()
{
	with_single_pointer();
	with_array_of_pointers();
	with_pointer_to_pointer();
	with_double_pointers();

	return 0;
}

void with_single_pointer()
{
    int r = 3, c = 4;
    int *arr = (int *)malloc(r * c * sizeof(int));
  
    int i, j, count = 0;
    for (i = 0; i <  r; i++)
      for (j = 0; j < c; j++)
         *(arr + i*c + j) = ++count;
  
    for (i = 0; i <  r; i++)
      for (j = 0; j < c; j++)
         printf("%d ", *(arr + i*c + j));
  	printf("\n");
  
	//	Free allocated memory
	free(arr);
}

void with_array_of_pointers()
{
    int r = 3, c = 4, i, j, count;
  
    int *arr[r];
    for (i=0; i<r; i++)
         arr[i] = (int *)malloc(c * sizeof(int));
  
    // Note that arr[i][j] is same as *(*(arr+i)+j)
    count = 0;
    for (i = 0; i <  r; i++)
      for (j = 0; j < c; j++)
         arr[i][j] = ++count; // OR *(*(arr+i)+j) = ++count
  
    for (i = 0; i <  r; i++)
      for (j = 0; j < c; j++)
         printf("%d ", arr[i][j]);
  	printf("\n");
  
	//	Free allocated memory
  	for (i=0; i<r; ++i)
		free(arr[i]);
}

void with_pointer_to_pointer()
{
    int r = 3, c = 4, i, j, count;
  
    int **arr = (int **)malloc(r * sizeof(int *));
    for (i=0; i<r; i++)
         arr[i] = (int *)malloc(c * sizeof(int));
  
    // Note that arr[i][j] is same as *(*(arr+i)+j)
    count = 0;
    for (i = 0; i <  r; i++)
      for (j = 0; j < c; j++)
         arr[i][j] = ++count;  // OR *(*(arr+i)+j) = ++count
  
    for (i = 0; i <  r; i++)
      for (j = 0; j < c; j++)
         printf("%d ", arr[i][j]);
  	printf("\n");
  
	//	Free allocated memory
  	for (i=0; i<r; ++i)
		free(arr[i]);
	free(arr);
}

void with_double_pointers()
{
    int r=3, c=4, len=0;
    int *ptr, **arr;
    int count = 0,i,j;
  
    len = sizeof(int *) * r + sizeof(int) * c * r;
    arr = (int **)malloc(len);
  
    // ptr is now pointing to the first element in of 2D array
    ptr = (int *)(arr + r);
  
    // for loop to point rows pointer to appropriate location in 2D array
    for(i = 0; i < r; i++)
        arr[i] = (ptr + c * i);
  
    for (i = 0; i < r; i++)
        for (j = 0; j < c; j++)
            arr[i][j] = ++count; // OR *(*(arr+i)+j) = ++count
  
    for (i = 0; i < r; i++)
        for (j = 0; j < c; j++)
            printf("%d ", arr[i][j]);
	printf("\n");

	//	Free allocated memory
	free(arr);
}
