import numpy as np

values = np.arange(16).reshape(4,4)
print(values)

result = values[::2, ::2]
print(result)
#   or
#   Get elements:
#       [0,0]    [0,2]
#       [2,0]    [2,2]
result = values[[[0,0],[2,2]], [[0,2],[0,2]]]
print(result)
