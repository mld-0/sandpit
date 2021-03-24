
def extract_column(values, n):
    result = [x[n-1] for x in values]
    print(result)

values = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
extract_column(values, 1)

values = [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
extract_column(values, 3)
