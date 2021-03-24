
def max_min_sum_sublists(values):
    values_sorted = sorted(values, key=lambda x: sum(x))
    print(values_sorted[-1])
    print(values_sorted[0])

values = [[1, 2, 3, 5], [2, 3, 5, 4], [0, 5, 4, 1], [3, 7, 2, 1], [1, 2, 1, 2]]
max_min_sum_sublists(values)
