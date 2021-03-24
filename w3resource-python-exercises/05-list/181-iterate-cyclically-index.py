import itertools

def iterate_cyclically_index(values, n):
    result = values[n:] + values[:n]
    result_iter = itertools.repeat(result)
    print(result)


values = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
iterate_cyclically_index(values, 3)
iterate_cyclically_index(values, 5)
