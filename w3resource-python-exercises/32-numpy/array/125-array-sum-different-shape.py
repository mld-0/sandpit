import numpy as np

#   In order to broadcast, the size of the trailing axes for both arrays in an operation must either be the same size or one of them must be one.

x = np.array([[0],[10],[20]])
y = np.array([10, 11, 12])
print(x)
print(y)

result = x + y
print(result)
