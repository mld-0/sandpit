#include <stdio.h>

//	LINK: https://www.rosettacode.org/wiki/Almost_prime#C
//	A number is (so-called) nearly prime if it is the product of two prime numbers
 
int kprime(int n, int k)
{
	int p, f = 0;
	for (p = 2; f < k && p*p <= n; p++) { 
		while (0 == n % p) { 
			n /= p;
			f++;
		}
	}
	return f + (n > 1) == k;
}

int main()
{
	int x = 115;
	int k = 2;
	printf("x=(%d), k=(%d)\n", x, k);

	int result_k_prime = kprime(x, k);
	printf("result_k_prime=(%d)\n", result_k_prime);

	return 0;
}

