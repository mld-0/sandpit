import numpy as np

a = np.array([1,2,3])
b = np.array([2,3,4])
print(a)
print(b)

result = np.column_stack((a, b))
print(result)
#   or
result = np.stack((a, b), axis=1)
print(result)
