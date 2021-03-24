import itertools

def add_different_lengths(a, b):
    result = []
    for i, j in itertools.zip_longest(a, b, fillvalue=0):
        result.append(i + j)
    print(result)

a = [2, 4, 7, 0, 5, 8]
b = [3, 3, -1, 7]
add_different_lengths(a, b)

a = [1, 2, 3, 4, 5, 6]
b = [2, 4, -3]
add_different_lengths(a, b)

