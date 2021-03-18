
def first_missing_positive(values):
    values_sorted = sorted(values)
    values_sorted_positive = [x for x in values_sorted if x >= 0]
    for i in range(values_sorted_positive[0], values_sorted_positive[-1]+2):
        if not i in values:
            print(i)
            return

first_missing_positive([2, 3, 7, 6, 8, -1, -10, 15, 16])
first_missing_positive([1, 2, 4, -7, 6, 8, 1, -10, 15])
first_missing_positive([1, 2, 3, 4, 5, 6, 7])
first_missing_positive([-2, -3, -1, 1, 2, 3])

