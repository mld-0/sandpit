
def reverse_nested_lists(values):
    result = [list(reversed(x)) for x in values]
    print(result)


values = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
reverse_nested_lists(values)
