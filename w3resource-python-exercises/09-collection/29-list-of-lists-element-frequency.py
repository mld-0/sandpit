from collections import Counter

def list_of_lists_element_frequency(values):
    result_counter = Counter()
    for L in values:
        result_counter.update(L)
    print(result_counter)

values = [[1, 2, 3, 2], [4, 5, 6, 2], [7, 1, 9, 5]]
list_of_lists_element_frequency(values)
        

