import numpy as np

values = np.array([1, 3, 5, 0, -1, -7, 0, 5])
print(values)

result = np.zeros_like(values)
result[values < 0] = -1
result[values > 0] = 1
#   or
result = np.sign(values)
print(result)

