
def remove_column(values, n):
    result = [[L[i] for i in range(len(L)) if i+1 != n] for L in values]
    print(result)

values = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
remove_column(values, 1)

values = [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
remove_column(values, 3)
