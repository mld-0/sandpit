import itertools

def combinations_n_distinct_itertools(values, n):
    result = list(itertools.combinations(values, n))
    print(result)

def combinations_n_distinct(values, n):
    result = []
    if n <= 0:
        yield result
        return
    for i in range(len(values)):
        c = values[i]
        for a in combinations_n_distinct(values[i+1:], n-1):
            yield [c] + a

values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
combinations_n_distinct_itertools(values, 2)

result = combinations_n_distinct(values, 2)
print(list(result))
