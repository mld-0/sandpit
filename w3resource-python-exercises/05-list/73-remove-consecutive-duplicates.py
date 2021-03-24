import itertools

def remove_consecutive_duplicates(values):
    result = []
    for x in values:
        if len(result) == 0 or result[-1] != x:
            result.append(x)
    #   or
    result = [k for k, g in itertools.groupby(values)]
    print(result)

values = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
remove_consecutive_duplicates(values)

