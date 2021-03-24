
def sort_matrix_by_row_sum(values):
    result = sorted(values, key=lambda x: sum(x))
    print(result)

values = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
sort_matrix_by_row_sum(values)

values = [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
sort_matrix_by_row_sum(values)

