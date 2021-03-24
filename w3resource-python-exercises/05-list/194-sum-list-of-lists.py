import itertools

def sum_list_of_lists(values):
    result = [sum(L) for L in itertools.zip_longest(*values, fillvalue=0)]
    print(result)

values = [[1, 2, 4], [2, 4, 4], [1, 2]]
sum_list_of_lists(values)

values = [[1], [2, 4, 4], [1, 2], [4]]
sum_list_of_lists(values)

