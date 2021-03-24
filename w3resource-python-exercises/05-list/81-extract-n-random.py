import random

def extract_n_random(values, n):
    result = []
    while n > 0:
        rand_index = random.randint(0, len(values))
        result.append(values.pop(rand_index))
        n -= 1
    print(result)

values = [1, 1, 2, 3, 4, 4, 5, 1]
extract_n_random(values, 3)
