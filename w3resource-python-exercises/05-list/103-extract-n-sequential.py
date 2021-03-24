import itertools

def extract_n_sequential(values, n):
    results = [k for k, g in itertools.groupby(values) if len(list(g)) == n]
    print(results)

values = [1, 1, 3, 4, 4, 5, 6, 7]
extract_n_sequential(values, 2)

values = [0, 1, 2, 3, 4, 4, 4, 4, 5, 7]
extract_n_sequential(values, 4)
