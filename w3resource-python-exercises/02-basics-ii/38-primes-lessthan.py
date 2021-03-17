def is_prime(x):
    for i in range(2, x-1):
        if (x % i == 0):
            return False
    return True

def primes_lessthan(n):
    primes_count = 0
    for i in reversed(range(2, n+1)):
        if is_prime(i):
            primes_count += 1
    print(primes_count)

primes_lessthan(35)
