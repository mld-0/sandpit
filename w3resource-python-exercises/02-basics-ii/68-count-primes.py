
def is_prime(n):
    for i in range(2, n-1):
        if (n % i == 0):
            return False
    return True

def list_primes(_max):
    primes = [2]
    i = 3
    while i < _max:
        if is_prime(i):
            primes.append(i)
        i += 1
    print(len(primes))

list_primes(10)
list_primes(100)
        
