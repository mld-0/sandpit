import itertools

def list_of_lists_element_frequency(values):
    values_counter = {}
    values_flat = list(itertools.chain(*values))
    for value in values_flat:
        if value in values_counter.keys():
            values_counter[value] += 1
        else:
            values_counter[value] = 1
    print(values_counter)

values = [[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]]
list_of_lists_element_frequency(values)


