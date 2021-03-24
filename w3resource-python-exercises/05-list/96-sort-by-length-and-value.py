
def sort_by_length_and_value(values):
    result = sorted(values, key=lambda x: (len(x), x))
    print(result)

values = [[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]
sort_by_length_and_value(values)
