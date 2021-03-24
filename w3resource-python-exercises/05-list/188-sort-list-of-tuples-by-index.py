
def sort_list_of_tuples_by_index(values, n):
    result = sorted(values, key=lambda x: x[n-1])
    print(result)

values = [('item2', 10, 10.12), ('item3', 15, 25.1), ('item1', 11, 24.5), ('item4', 12, 22.5)]

sort_list_of_tuples_by_index(values, 1)
sort_list_of_tuples_by_index(values, 2)
sort_list_of_tuples_by_index(values, 3)

