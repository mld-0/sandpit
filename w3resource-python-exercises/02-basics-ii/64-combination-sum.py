import itertools

def combination_sum(values, k):
    result = False
    combinations = itertools.combinations(values, 2)
    for a, b in combinations:
        if (a + b == k):
            result = True
    print(result)

combination_sum([1, 5, 11, 5], 16)
combination_sum([12, 5, 0, 5], 10)
combination_sum([20, 20, 4, 5], 40)
combination_sum([1, -1], 0)
combination_sum([1, 1, 0], 0)

