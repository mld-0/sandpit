import numpy as np

values = np.arange(36).reshape(4,9)
print(values)

result = np.sum(values, axis=0)
#   or
result = values.sum(axis=0)
print(result)

