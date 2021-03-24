
def sieve_of_eratosthenes(n):
    values = [0] * (n+1)
    values[0:2] = [-1,-1]
    while 0 in values:
        i = values.index(0)
        values[i] = i
        for j in range(1, n//i+1):
            values[i*j] = i

    primes = [i for i in range(len(values)) if values[i] == i]
    print(primes)

sieve_of_eratosthenes(200)
