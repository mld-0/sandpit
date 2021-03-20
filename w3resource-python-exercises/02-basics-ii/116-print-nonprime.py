
def is_prime(n):
    for i in range(2, n-1):
        if (n % i == 0):
            return False
    return True

values = range(1, 101)
primes = [x for x in values if not is_prime(x)]
print(primes)
