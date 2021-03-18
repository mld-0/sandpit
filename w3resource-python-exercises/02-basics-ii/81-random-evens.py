import random

def random_evens(a, b, n):
    evens = [x for x in range(a, b+1) if x % 2 == 0]
    evens_random = random.sample(evens, n)
    print(evens_random)

random_evens(1, 100, 10)
