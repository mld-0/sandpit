
def matrix_dimensions(values):
    results = tuple((len(values), len(values[0])))
    print(results)

values = [[1, 2], [2, 4]]
matrix_dimensions(values)

values = [[0, 1, 2], [2, 4, 5]]
matrix_dimensions(values)

values = [[0, 1, 2], [2, 4, 5], [2, 3, 4]]
matrix_dimensions(values)

