import numpy as np

values = np.array([0, 1, 6, 1, 4, 1, 2, 2, 7])
print(values)

_range = np.arange(8)
print(_range)

result = np.bincount(values)
print(result)

