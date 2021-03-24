
def max_min_given_lists(*values):
    values_combined = [x for L in values for x in L]
    values_combined_sorted = sorted(values_combined)
    print(values_combined_sorted[-1])
    print(values_combined_sorted[0])

a = [2, 3, 5, 8, 7, 2, 3]
b = [4, 3, 9, 0, 4, 3, 9]
c = [2, 1, 5, 6, 5, 5, 4]

max_min_given_lists(a, b, c)

