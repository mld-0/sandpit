import math

def check_coprime(a, b):
    check_gcd = math.gcd(a, b)
    print(check_gcd == 1)

check_coprime(17, 13)
check_coprime(17, 21)
check_coprime(15, 21)
check_coprime(25, 45)
