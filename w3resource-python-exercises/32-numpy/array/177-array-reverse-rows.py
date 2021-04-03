import numpy as np

values = np.arange(4*5).reshape(4,5)
print(values)

result = values[::-1, :]
print(result)
#   or
result = values[::-1]
print(result)
