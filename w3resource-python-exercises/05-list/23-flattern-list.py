import itertools

def flattern_list(values):
    result_list = list(itertools.chain(*values))
    #   or
    result_list = [x for sublist in values for x in sublist]
    return result_list

def flattern_list_recursive(values):
    if values == []:
        return values
    if isinstance(values[0], list):
        return flattern_list_recursive(values[0]) + flattern_list_recursive(values[1:])
    return values[:1] + flattern_list_recursive(values[1:])

original_list = [[2,4,3],[1,5,6], [9], [7,9,0, [1, 2]]]

result = flattern_list(original_list)
print(result)

result = flattern_list_recursive(original_list)
print(result)

