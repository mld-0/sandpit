import numpy as np

values = np.array([1, 3, 5, 7, 0])
print(values)

result = values[1:] - values[:-1]
#   or
result = np.diff(values)
print(result)
