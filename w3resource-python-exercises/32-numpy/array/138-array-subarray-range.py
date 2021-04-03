import numpy as np

values = np.arange(16).reshape(4,4)
print(values)

result = values[0:2, 2:4]
print(result)
#   or
result = values[[[0,0],[1,1]], [[2,3],[2,3]]]
print(result)

