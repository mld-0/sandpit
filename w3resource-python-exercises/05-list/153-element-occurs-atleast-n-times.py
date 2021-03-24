from collections import Counter

def element_occurs_atleast_n_times(values, val, n):
    values_counter = Counter(values)
    val_count = values_counter[val]
    if (val <= n):
        print(True)
    else:
        print(False)

values = [0, 1, 3, 5, 0, 3, 4, 5, 0, 8, 0, 3, 6, 0, 3, 1, 1, 0]
element_occurs_atleast_n_times(values, 3, 4)
element_occurs_atleast_n_times(values, 0, 5)
element_occurs_atleast_n_times(values, 8, 3)
