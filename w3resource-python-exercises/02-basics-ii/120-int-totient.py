import math

def int_totient(n):
    values = range(1, n)
    result = [x for x in range(1, n) if math.gcd(n, x) == 1]
    print(len(result))

int_totient(10)
int_totient(15)
int_totient(33)

