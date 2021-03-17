import itertools

def combination_sum(n):
    combinations = 0
    _max = 10
    for (a, b, c, d) in itertools.product(range(_max), range(_max), range(_max), range(_max)):
        _sum = a + b + c + d
        if (_sum == n):
            combinations += 1
    print(combinations)

combination_sum(15)
