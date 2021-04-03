import numpy as np

values = np.arange(36).reshape(6,6)
print(values)

result = values[2::2, ::2]
print(result)
#   or
result = values[[[2,2,2],[4,4,4]], [[0,2,4],[0,2,4]]]
print(result)
