import numpy as np

values = np.arange(16).reshape(4,4)
print(values)

result = values[1::2, 1::2]
print(result)
#   or
rows = [[1,1], [3,3]]
cols = [[1,3], [1,3]]
result = values[rows, cols]
print(result)
