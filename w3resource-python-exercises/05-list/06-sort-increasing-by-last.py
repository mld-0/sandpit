
def sort_increasing_last(values):
    values_sorted = sorted(values, key=lambda x: x[-1])
    print(values_sorted)

sort_increasing_last([(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)])
