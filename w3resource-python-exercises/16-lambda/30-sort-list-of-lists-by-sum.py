
sort_by_sublist_sum = lambda x: sorted(x, key=lambda a: sum(a))

values = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
print(sort_by_sublist_sum(values))

values = [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
print(sort_by_sublist_sum(values))

