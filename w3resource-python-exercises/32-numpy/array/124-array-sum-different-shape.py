import numpy as np

#   In order to broadcast, the size of the trailing axes for both arrays in an operation must either be the same size or one of them must be one.

p = np.array([[0,0,0], [1,2,3], [4,5,6]])
q = np.array([10, 11, 12])
print(p)
print(q)

result = p + q
print(result)
