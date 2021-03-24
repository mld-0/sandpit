
def merge_by_index(values, a, b):
    result = values[:a] + [''.join(values[a:b])] + values[b:]
    #   or
    result = values[:]
    result[a:b] = [''.join(values[a:b])]
    print(result)

values = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
merge_by_index(values, 2, 4)
merge_by_index(values, 3, 7)

