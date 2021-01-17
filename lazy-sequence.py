
#   https://www.youtube.com/watch?v=5jwV3zxXc8E
#   Generate prime numbers from sequence with yield operator

def nats(n):
    yield n
    yield from nats(n+1)

s = nats(2)

def sieve(s):
    n = next(s)
    yield n
    yield from sieve(i for i in s if i%n!=0)

p = sieve(nats(2))
print(next(p))
print(next(p))
print(next(p))
print(next(p))
print(next(p))
