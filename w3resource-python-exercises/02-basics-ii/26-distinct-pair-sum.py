import itertools

def distinct_pair_sum(values):
    perms = [x for x in list(itertools.permutations(values, 2))if x[0] < x[1]]
    result = 0
    for n in perms:
        abs_diff = abs(n[0] - n[1])
        result += abs_diff
        print("%s, " % str(n), end='')
    print(result)

values = [1, 2, 3]
distinct_pair_sum(values)

values = [1, 4, 5]
distinct_pair_sum(values)

