
def remove_last_n(values, n):
    result = values[:-n]
    print(result)

values = [2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34, 2, 34, 5, 3, 5]
remove_last_n(values, 3)
remove_last_n(values, 5)
remove_last_n(values, 1)

