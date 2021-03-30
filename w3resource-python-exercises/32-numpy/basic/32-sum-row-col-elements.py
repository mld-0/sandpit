import numpy as np

x = np.array([[0,1],[2,3]])
print(x)

#   Sum all elements
x_sum = np.sum(x)
print(x_sum)

#   Sum of each column (moving along rows)
x_sum_col = np.sum(x, axis=0)
print(x_sum_col)

#   Sum of each row (moving along columns)
x_sum_row = np.sum(x, axis=1)
print(x_sum_row)

