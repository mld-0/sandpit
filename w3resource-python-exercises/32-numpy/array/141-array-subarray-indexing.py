import numpy as np

values = np.arange(16).reshape(4,4)
print(values)

result = values[:, 1:3]
print(result)
#   or
result = values[:, [1,2]]
print(result)