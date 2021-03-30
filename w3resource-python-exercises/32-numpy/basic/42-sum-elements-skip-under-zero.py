import numpy as np

def sum_elements_skip_under_zero(m):
    """Sum elements of a matrix, except for those with a zero in the same column in the row above"""
    result = 0
    for i in range(len(m)):
        for j in range(len(m[i])):
            if i == 0 or m[i-1, j] != 0:
                result += m[i,j]
    print(result)

m = np.array([[1, 1, 0, 2], [0, 3, 0, 3], [1, 0, 4, 4]])
sum_elements_skip_under_zero(m)

