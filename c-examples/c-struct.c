#include <stdlib.h>
#include <stdio.h>

struct point {
    int x;
    int y;
};

//	Declared as a typedef, we do not have to specify 'struct' on subsiquent uses of said struct
//	According to Linux stype guide: In general, a pointer, or a struct that has elements that can reasonably be directly accessed should never be a typedef.
typedef struct {
	char* brand;
	int modelyear;
} vehicle;

//	Structure with bit fields - each variable in struct 'status' is limited to 1 byte
struct {
   unsigned int widthValidated : 1;
   unsigned int heightValidated : 1;
} status;

void print_point(const struct point* p);
void print_car(const vehicle* v);

int main()
{
	struct point p;
	p.x = 10;
	p.y = 5;
	print_point(&p);

	struct point *q = (struct point*) malloc(sizeof(struct point));
	q->x = 13;
	q->y = 7;
	print_point(q);

	vehicle car;
	car.brand = "Saab";
	car.modelyear = 1999;
	print_car(&car);

	vehicle *transport = (vehicle*) malloc(sizeof(vehicle));
	transport->brand = "Pagani";
	transport->modelyear = 2017;
	print_car(transport);
	
	return 0;
}

void print_point(const struct point* p) 
{
	printf("%d, %d\n", p->x, p->y);
}

void print_car(const vehicle* v)
{
	printf("%s, %d\n", v->brand, v->modelyear);
}
