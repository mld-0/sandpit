def is_prime(n):
    if (n < 2):
        return False
    for i in range(2, n-1):
        if (n % i == 0):
            return False
    return True

def sum_n_primes(n):
    total = 0
    prime_count = 0
    loop_val = 0
    list_primes = []
    while (prime_count < n):
        if is_prime(loop_val):
            prime_count += 1
            total += loop_val
            list_primes.append(loop_val)
            #print("%s, %s, %s" % (prime_count, loop_val, total))
        loop_val += 1
    print(list_primes)
    print(sum(list_primes))

sum_n_primes(25)
