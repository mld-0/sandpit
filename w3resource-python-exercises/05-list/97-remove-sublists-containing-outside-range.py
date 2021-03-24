
def remove_sublists_containing_outside_range(values, L, R):
    result = [x for x in values if min(x) <= R and max(x) >= L]
    print(result)

L = 13
R = 17
values = [[2], [0], [1, 2, 3], [0, 1, 2, 3, 6, 7], [9, 11], [13, 14, 15, 17]]
remove_sublists_containing_outside_range(values, L, R)

