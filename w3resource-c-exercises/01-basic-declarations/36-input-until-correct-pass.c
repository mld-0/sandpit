#include <stdio.h>

int main() {
	int pass, x=10;	

	//	This has the rather major problem of entering an infinite loop if the user enters a string -> need to read a string from scanf then convert to an integer, (or just check for '1234' as a string) -> this is being included as a 'bad' example <- those being things w3resource tutorials will presumedly get around to later?
	while (x!=0)
	{
	printf("\nInput the password: ");
	scanf("%d",&pass);	
	
	if (pass==1234)
	{
		printf("Correct password");
		x=0;
    }
    else
    {
       printf("Wrong password, try another");       
	}
	printf("\n");
   }
	return 0;
} 

