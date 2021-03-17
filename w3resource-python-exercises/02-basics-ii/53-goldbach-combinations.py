import itertools

def is_prime(n):
    if (n < 2):
        return False
    for i in range(2, n-1):
        if (n % i == 0):
            return False
    return True

def prime_range(n):
    prime_list = []
    for i in range(n+1):
        if is_prime(i):
            prime_list.append(i)
    return prime_list

def goldbach_combinations(n):
    prime_list = prime_range(n)
    prime_combinations = itertools.combinations(prime_list, 2)
    combinations_count = 0
    for a, b in prime_combinations:
        if (a + b == n):
            combinations_count += 1
            #print("%s, %s" % (a, b))
    print(combinations_count)

goldbach_combinations(100)
