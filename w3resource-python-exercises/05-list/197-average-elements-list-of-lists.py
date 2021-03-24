import itertools
import statistics

def average_elements_list_of_lists(values, n):
    result = [statistics.mean([x for x in L if x is not None]) for L in itertools.zip_longest(*values)]
    print(result)

values = [[0, 1, 2], [2, 3, 4], [3, 4, 5, 6], [7, 8, 9, 10, 11], [12, 13, 14]]
average_elements_list_of_lists(values, 1)
