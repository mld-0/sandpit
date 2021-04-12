import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([[1, 2], [1, 2]])
print(a)
print(b)

result = a ** b
#   or
result = np.power(a, b)
print(result)

