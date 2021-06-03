#include <stdio.h>
#include <stdlib.h>

//	A union allows multiple names to the same variable, which can treat the same memory as different types (the size of the union is the size of the largest type, plus any padding added by compiler)
//	For example, intParts, examining an integer byte-by-byte
union intParts {
	int theInt;
	char bytes[sizeof(int)];
};

//	For (an unnamed) union that is part of a struct, members of the union are accessible from struct
struct operator {
    int type;
    union {
        int intNum;
        float floatNum;
        double doubleNum;
    }; // no name!
};

//	(Or?) with an unnamed struct that is part of a union:
union Coins {
    struct {
        int quarter;
        int dime;
        int nickel;
        int penny;
    }; // anonymous struct acts the same way as an anonymous union, members are on the outer container
    int coins[4];
};

void print_intParts(union intParts *p)
{
	printf("The int is %i\n", p->theInt);
	printf("The bytes are [%x, %x, %x, %x]\n", p->bytes[3], p->bytes[2], p->bytes[1], p->bytes[0]);	
	printf("That is, [%x, %x, %x, %x]\n", *((char*) &p->theInt+3), *((char*) &p->theInt+2), *((char*) &p->theInt+1), *((char*) &p->theInt+0));
}

int main()
{
	union intParts p;
	p.theInt = 5968145;
	print_intParts(&p);

	operator op;
	op.type = 0; // int
	// intNum is part of the union, but since it's not named you access it directly off the struct itself
	op.intNum = 352;

	return 0;
}
