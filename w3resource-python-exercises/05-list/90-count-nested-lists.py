
def count_nested_lists(values):
    result = 0
    for x in values:
        if isinstance(x, list):
            result += 1
    print(result)

values = [[1, 3], [5, 7], [9, 11], [13, 15, 17]]
count_nested_lists(values)

values = [[2, 4], [[6, 8], [4, 5, 8]], [10, 12, 14]]
count_nested_lists(values)
