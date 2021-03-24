
def combine_list_of_lists(a, b):
    result = [[i + j] for i, j in zip(a, b)]
    print(result)

a = [[1, 3], [5, 7], [9, 11]]
b = [[2, 4], [6, 8], [10, 12, 14]]
combine_list_of_lists(a, b)
