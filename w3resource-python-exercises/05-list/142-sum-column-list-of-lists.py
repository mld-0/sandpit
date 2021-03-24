
def sum_column_list_of_lists(values, n):
    results = [x[i] for x in values for i in range(len(x)) if i+1 == n]
    result = sum(results)
    print(result)

values = [[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]]
sum_column_list_of_lists(values, 1)
sum_column_list_of_lists(values, 2)
sum_column_list_of_lists(values, 4)

