import random

def interleave_lists_randomly(a, b):
    result = a + b
    random.shuffle(result)
    print(result)

a = [1, 2, 7, 8, 3, 7]
b = [4, 3, 8, 9, 4, 3, 8, 9]

interleave_lists_randomly(a, b)

