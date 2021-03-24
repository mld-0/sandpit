import itertools

def pack_consecutive_duplicates(values):
    result = [list(g) for k, g in itertools.groupby(values)]
    print(result)

values = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4] 
pack_consecutive_duplicates(values)
